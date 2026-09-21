#!/usr/bin/env python3
"""Validate an FX Reports template (JSON) against the bundled schema.

Usage:  python3 validate.py <template.json> [--schema <schema.json>]

Beyond the JSON schema this also checks things the schema cannot express:
  - formatRef / fontRef / color ref / picture ref / valuesRef / valueRef
    point to an existing catalog entry
  - root-level sheet content mixed with a "sheets" array
  - a few known pitfalls (warnings)

Exit code 0 = valid (warnings possible), 1 = errors, 2 = usage/setup problem.
Requires: pip install jsonschema
"""
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Missing dependency. Run: pip install jsonschema", file=sys.stderr)
    sys.exit(2)

DEFAULT_SCHEMA = Path(__file__).resolve().parent.parent / "references" / "schema.json"
COLOR_KEYS = {
    "fontColor", "backgroundColor", "foregroundColor", "borderColor",
    "borderTopColor", "borderRightColor", "borderBottomColor",
    "borderLeftColor", "borderDiagonalColor",
}


def path_str(parts):
    out = ""
    for p in parts:
        out += f"[{p}]" if isinstance(p, int) else f"/{p}"
    return out or "/"


def best_message(err):
    """For anyOf/oneOf errors, surface the most specific underlying cause."""
    if err.context:
        deepest = max(err.context, key=lambda e: len(e.absolute_path))
        return f"{err.message[:120]}  ->  {path_str(deepest.absolute_path)}: {deepest.message[:160]}"
    return err.message[:240]


def walk(node, path, visit):
    if isinstance(node, dict):
        for k, v in node.items():
            visit(k, v, path + [k])
            walk(v, path + [k], visit)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, path + [i], visit)


def semantic_checks(tpl):
    errors, warnings = [], []
    formats = tpl.get("formats", {}) or {}
    fonts = tpl.get("fonts", {}) or {}
    colors = tpl.get("colors", {}) or {}
    pictures = tpl.get("pictures", {}) or {}
    values = tpl.get("values", {}) or {}

    def visit(key, val, path):
        # skip the central value storage: it is user data, not template syntax
        if path and path[0] == "values" and len(path) > 1:
            return
        where = path_str(path)
        if key == "formatRef" and isinstance(val, str) and val not in formats:
            errors.append(f"{where}: formatRef '{val}' is not defined in /formats")
        elif key == "fontRef" and isinstance(val, str) and val not in fonts:
            errors.append(f"{where}: fontRef '{val}' is not defined in /fonts")
        elif key in COLOR_KEYS and isinstance(val, dict) and "ref" in val:
            if val["ref"] not in colors:
                errors.append(f"{where}: color ref '{val['ref']}' is not defined in /colors")
        elif key == "picture" and isinstance(val, dict) and "ref" in val:
            if val["ref"] not in pictures:
                errors.append(f"{where}: picture ref '{val['ref']}' is not defined in /pictures")
        elif key == "valuesRef" and isinstance(val, str):
            if val.split("/")[0] not in values:
                errors.append(f"{where}: valuesRef '{val}' is not defined in /values")
            elif not isinstance(values.get(val, []), list):
                errors.append(f"{where}: valuesRef '{val}' must point to an array of rows")
            else:
                data = values.get(val) or []
                if data and isinstance(data[0], dict):
                    row = tpl
                    for p in path[:-1]:
                        row = row[p]
                    keys = list(data[0].keys())
                    if "fields" not in row:
                        warnings.append(
                            f"{path_str(path[:-1])}: object rows without 'fields' - all keys of the first object are output in stored "
                            "(usually alphabetical) order; add 'fields'")
                    else:
                        for f in row["fields"]:
                            if f not in keys:
                                errors.append(f"{path_str(path[:-1])}/fields: '{f}' is not a key of the first object in /values/{val}")
                    for i, item in enumerate(data):
                        if isinstance(item, dict) and set(item.keys()) != set(keys):
                            warnings.append(f"/values/{val}[{i}]: keys differ from first object - only the first object's keys are read")
                            break
        elif key == "valueRef" and isinstance(val, str):
            if val.split("/")[0] not in values:
                errors.append(f"{where}: valueRef '{val}' is not defined in /values")
        elif key == "split":
            warnings.append(f"{where}: 'split' is deprecated, use display.freeze")

    walk(tpl, [], visit)

    if "sheets" in tpl:
        mixed = [k for k in ("rows", "columns", "cells", "name") if k in tpl]
        if mixed:
            warnings.append(
                f"/: root-level {mixed} used together with 'sheets' - put sheet content "
                "either at the root (single sheet) or inside 'sheets', not both")
        names = [s.get("name") for s in tpl["sheets"] if isinstance(s, dict) and s.get("name")]
        dup = {n for n in names if names.count(n) > 1}
        if dup:
            errors.append(f"/sheets: duplicate sheet names {sorted(dup)}")
        for n in names:
            if len(n) > 31 or any(c in n for c in r"[]:*?/\\"):
                errors.append(f"/sheets: sheet name '{n}' violates Excel rules (max 31 chars, none of []:*?/\\)")

    for group, catalog in (("formats", formats), ("fonts", fonts)):
        ref_key = "formatRef" if group == "formats" else "fontRef"
        for name in catalog:
            seen, cur = set(), name
            while isinstance(catalog.get(cur), dict) and ref_key in catalog[cur]:
                if cur in seen:
                    errors.append(f"/{group}/{name}: circular {ref_key} chain")
                    break
                seen.add(cur)
                cur = catalog[cur][ref_key]
    return errors, warnings


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(2)
    schema_path = DEFAULT_SCHEMA
    if "--schema" in args:
        i = args.index("--schema")
        schema_path = Path(args[i + 1])
        del args[i:i + 2]
    tpl_path = Path(args[0])

    try:
        tpl = json.loads(tpl_path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as e:
        print(f"ERROR  not valid JSON: {e}")
        sys.exit(1)
    schema = json.loads(schema_path.read_text(encoding="utf-8-sig"))

    validator = jsonschema.Draft7Validator(schema)
    errors = [f"{path_str(e.absolute_path)}: {best_message(e)}"
              for e in sorted(validator.iter_errors(tpl), key=lambda e: list(map(str, e.absolute_path)))]
    sem_errors, warnings = semantic_checks(tpl) if isinstance(tpl, dict) else ([], [])
    errors += sem_errors

    for w in warnings:
        print(f"WARN   {w}")
    for e in errors:
        print(f"ERROR  {e}")
    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
        sys.exit(1)
    print(f"OK     {tpl_path.name} is valid ({len(warnings)} warning(s))")


if __name__ == "__main__":
    main()
