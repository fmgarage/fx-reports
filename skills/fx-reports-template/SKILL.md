---
name: fx-reports-template
description: Write, extend, debug and validate JSON templates for FX Reports (fmgarage), the FileMaker module that generates formatted Excel/xlsx files from a JSON definition via MBS Plugin and LibXL. Use this skill whenever the user mentions FX Reports, FX_Reports, fxrpxl, an "xlsx/Excel template" or "Excel export/report" in a FileMaker context, the FxReports table or *FxReports.excelGenerate script, or pastes JSON containing keys like rows/columns/cells with formatRef, valuesRef or fields+path — even if they only ask "how do I make this column bold/red/a number" or "why does my template fail validation". Also use it for wiring such a template into a FileMaker script.
---

# FX Reports templates

FX Reports turns a JSON template into an xlsx file. The template describes the workbook declaratively: where data comes from, which columns appear under which headers, and how everything is formatted. The user never scripts Excel; they hand a template to one FileMaker script.

The engine validates each template against a strict JSON schema before doing anything, and rejects it on the first unknown key. So the job here is less "be creative with JSON" and more "produce something that is provably valid and does what the user pictured". That is why this skill ships the schema and a validator — use them.

## Workflow

1. **Understand the report.** You need: the columns (and their source field names), where the data comes from (exported xlsx file, data injected into `values`, or inline), number/date columns, and any layout wishes (title, logo, colours, conditional highlights, print setup, multiple sheets). Ask only for what is missing and actually changes the template; assume sensible defaults for the rest and say which ones you chose.
2. **Start from the closest example** in `references/examples/` rather than from a blank page — they are known to run. Pick by need:
   - rename/reorder/filter columns of an export → `simple-header-extra`, `data-file`
   - data passed in from FileMaker → `data-reference` (preferred), `simple-data-array`
   - fonts, named formats, colours → `format-basic`; borders → `format-borders`
   - number, date, currency columns → `format-datatypes`
   - conditional formatting → `format-conditional`, `format-conditional-data-array`
   - logo, icons, title block → `picture-logo`
   - freeze, zoom, print, header/footer, several sheets → `display-and-print`
   - records in side-by-side blocks → `data-blocks`
3. **Look up anything you are not sure about** in `references/reference.md` (condensed, with a table of contents) or directly in `references/schema.json`. Do not guess key names: every object is closed, and the public docs contain a few keys that the schema rejects (listed in reference.md §13).
4. **Validate before you show it.** Write the template to a file and run
   `python3 scripts/validate.py <file>` (needs `pip install jsonschema`).
   It checks the schema plus what the schema cannot: that every `formatRef`, `fontRef`, colour `ref`, picture `ref`, `valuesRef` and `valueRef` resolves. Fix and re-run until it prints `OK`. If you cannot execute code in this environment, walk through the checklist below by hand and tell the user to run *Validate Template* in FX Reports.
5. **Deliver** the template as a `.fxrpxl.json` file (or a code block if the user works in chat), followed by a short note: assumptions made, what the user must adapt (paths, field names), and anything that needs a test run in FX Reports because it cannot be verified from here — picture sizes, fonts, date input.

If the user also wants the FileMaker side (script call, filling `values`, export-then-generate), read `references/filemaker-integration.md`.

## Core rules

These cover most real templates; details are in reference.md.

- **Structure.** Root = workbook. One sheet: put `columns`, `rows`, `cells` directly at the root. Several sheets: use `sheets: [...]` and keep sheet content out of the root. Catalogs (`formats`, `fonts`, `colors`, `pictures`, `values`) always live at the root.
- **Everything is 0-based.** Column `pos: 1` is column B. Cell `pos` is `[col, row, colSpan?, rowSpan?]`; row `pos` is a row index or `[colOffset, row]`.
- **Processing order is columns → rows → cells**, and rows stack top-down unless `pos` says otherwise. If cells form a title block in rows 0–3, give the first row object `"pos": 4`.
- **Header + data is two row objects:** one with `values: [...]` for the captions, one for the data (`path`+`fields`, or `valuesRef`, or nested `values`). `fields` selects and orders source columns by their header name in the source file; for FileMaker exports that is the field name, fully qualified for related fields.
- **Source files are expected to have a header row, and the engine skips it by default.** So with your own caption row, simply omit `includeFirstRow`. One exception: a source row that lands on sheet row 0 (no caption row above, no `offset`) outputs the source's first row automatically. Set `"includeFirstRow": true` only when the source's header row should appear in the output, or when the source has no header row at all (otherwise its first record is lost).
- **Object rows behave like a source file.** When `valuesRef` points to an array of objects, the keys of the *first* object act as the source's header names, and `fields` selects and orders them — exactly as with `path`. Always give such a row a `fields` array: without it the engine outputs all keys of the first object in their stored order, which after FileMaker's JSON functions is alphabetical. A `fields` entry that is not a key of the first object aborts generation (`FieldNotFound`). Make sure every object carries the same keys (`null` instead of leaving one out).
- **Column types.** Give numeric columns `dataType: "number"` and date columns `dataType: "date"` plus a `numberFormat` or `numberFormatCustom`; otherwise values may arrive as text and Excel will not sum or sort them properly. Dates passed in via `values` should be ISO strings (`"2026-01-31"`), timestamps `"2026-01-31 14:30:00"` (space, not `T`).
- **Name what repeats.** Put shared styling into `formats`/`fonts`/`colors` and reference it; use inline `format` for one-off tweaks on top of a `formatRef`. A format can extend another via `formatRef`, a font via `fontRef`. This keeps templates short and lets users restyle in one place.
- **Colours** are objects with exactly one of `rgb`, `name`, `ref` — never a bare string or hex value.
- **Conditionals** (`case`) sit on a column or cell, test the cell's own value with exactly one operator, and are applied once at generation time. They are not live Excel conditional formatting and cannot compare against other cells.
- **Pictures** only go into cells. Prefer `width`/`height` over `scale`, and warn that sizing needs a test run.
- **`columnWidth: -1`** (auto) is the friendly default; override single columns with `width`.
- Keep `filename` ending in `.xlsx`, and keep data out of the template when it changes per run — inject it into `values` instead.

## Manual checklist (when the validator cannot run)

- Valid JSON: no trailing commas, no comments (use `note` / `$comment` keys for remarks).
- Only keys that exist in the schema for that object; spelling and case exact (`autofilter`, `position`, `fontName`).
- `underline`, `alignH`, `alignV`, `numberFormat` are integers; `format` is always an object.
- Every reference resolves to a catalog entry with identical spelling.
- `if.value` has exactly one operator; numeric operators get numbers, not strings.
- `valuesRef` names are alphanumeric.
- A header/footer section uses `fontRef` or inline font keys, not both.

## Debugging an existing template

Run the validator first; it names the JSON path and the most specific cause. Typical culprits: a key copied from the docs that the schema rejects (reference.md §13), a format given as string, a dangling `formatRef`, a colour as string, root-level rows next to `sheets`. When the template is valid but the output looks wrong, think in processing order — a cell overwriting a row, a missing row `pos` after a title block, `includeFirstRow: true` duplicating the header (or its absence swallowing the first record of a header-less source), a column `pos` off by one.

## Honesty about limits

You cannot run FX Reports, so you cannot see the resulting xlsx. Schema validity is verifiable; visual results (picture size, fonts present on the machine, auto widths, page breaks) are not. Say so briefly instead of promising a pixel-perfect result. If the user asks for something the schema does not offer — formulas across sheets, charts, live conditional formatting, data validation, cell locking — say that it is not supported rather than inventing keys; `lock`, `indent` and `rotate` exist in the schema but are marked not implemented.
