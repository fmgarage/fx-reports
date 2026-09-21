# FX Reports template reference (condensed)

Authoritative source is `schema.json` (v2.2.1). Where the public docs and the schema disagree, the schema wins, because the engine validates every template against it before processing.

## Contents
1. Workbook (root)
2. Sheet
3. Row
4. Column
5. Cell
6. Format
7. Font
8. Color
9. Picture
10. Case (conditional)
11. Print, header/footer
12. Number formats
13. Known doc/schema mismatches

All positions are **0-based**. Every object is closed (`additionalProperties: false`): an unknown or misspelled key is a schema error, not silently ignored.

---

## 1. Workbook (root)

| key | type | notes |
|---|---|---|
| `schemaVersion` | string | minimum schema version, e.g. `"2.2"` |
| `filename` | string | output name; default is a timestamp name |
| `location` | string | folder (e.g. `desktop/exports`) or container field reference (`FxReports::a_container_[2]`); if set nowhere: `desktop/FX Reports output` |
| `formats` `fonts` `colors` `pictures` | object | named catalogs, referenced via `formatRef`, `fontRef`, `{"ref":…}`, `picture.ref` |
| `values` | object | central value storage: name → array of rows, or name → scalar |
| `formatRef` / `format` | | workbook default format |
| `display` | object | `hideGrid` bool, `zoom` 25–400, `freeze` `true` or `[col,row]` |
| `print` | object | see §11 |
| `columnWidth` | int | default width in characters, `-1` = auto |
| `filters` | object | `{"autofilter": true}` (lower-case `f`) |
| `columns` `rows` `cells` `name` | | content of a single sheet, placed directly at root |
| `sheets` | array | use instead of root-level content when there is more than one sheet |
| `columnSeparator` `rowSeparator` | string | for text sources, defaults `;` and `¶` |
| `split` | | deprecated → `display.freeze` |

Path shortcuts: `desktop`, `documents`, `tmp` (`tmp` resolves to FileMaker's `Get ( TemporaryPath )`).
`filename` and `location` can be overridden per call by the parameters of the connector script.

## 2. Sheet

`name`, `formatRef`, `format`, `display`, `print`, `columnWidth`, `columns`, `rows`, `cells`, `filters`, `note`, plus `defaultColumn: {width, minWidth, maxWidth}` (characters; only available on a sheet, not at root).

Processing order inside a sheet is **columns → rows → cells**. Cells are written last, so they overwrite whatever rows put there.

## 3. Row

A row object produces one row, or many when its source has many records. Without `pos` it is placed after the previous one.

| key | notes |
|---|---|
| `values` | `["a","b"]` = one row, `[["a","b"],["c","d"]]` = many rows. Items: string, number, boolean, null. Objects are not allowed here (only in the central storage, see `valuesRef`). Dates as ISO strings `YYYY-MM-DD`, timestamps `YYYY-MM-DD hh:mm:ss`. |
| `valuesRef` | name in root `values`. Pattern `^[a-zA-Z0-9/]+$` — so value-storage names must be alphanumeric (no `-` or `_`). The referenced entry is an array of rows; each row is an array (positional) or an object (keyed). For objects the keys of the first item are the header names; `fields` in the row object maps them to columns (left to right). Without `fields`, all keys of the first item are output in stored order (alphabetical after FileMaker JSON functions) — so always set it. Unknown names raise `FieldNotFound`. |
| `path` | source file path or container field reference |
| `contentType` | `json` \| `csv` \| `tab` for non-xlsx sources |
| `fields` | select and order source columns by their header names (file sources) or object keys (`valuesRef` to an array of objects) |
| `includeFirstRow` | The engine assumes every source file has a header row and skips it. Omit the key (= false) in the normal case; it is implied when the source row is written to sheet row 0 without `offset`; set `true` to output the source's first row (keep its headers, or header-less source). |
| `limit` `offset` | slice of source rows |
| `pos` | integer = row index, or `[colOffset, row]` |
| `type` | `header` \| `data` \| `summary` |
| `dataType` | see Column |
| `formatRef` `format` | applied to every cell of the row(s) |
| `height` | points |
| `widths` | per-column widths in characters, `-1` auto |

Side-by-side blocks: two header rows (`pos` omitted and `pos:[4,0]`), then two source rows with `limit: n` and `pos:[4,1], offset: n`. See `examples/data-blocks.fxrpxl.json`.

## 4. Column

`columns` is an array. Without `pos`, entries apply left to right starting at column 0. Use `pos` to target a specific column (integer) or a range (`[start, length]`, `-1` = auto).

| key | notes |
|---|---|
| `dataType` | `text` `number` `date` `timestamp` `blank` `formula`. If omitted, the source type is kept. |
| `type` | which rows the column settings apply to: `header` \| `data` (default) \| `summary` |
| `width` | characters, `-1` auto |
| `formatRef` `format` | |
| `case` | conditional, see §10 |

Setting `dataType: "number"` matters for anything Excel should sum or sort numerically — FileMaker exports frequently deliver numbers as text.

## 5. Cell

`pos` is required: `[col, row]` or `[col, row, colSpan, rowSpan]` (spans merge cells).
Other keys: `value`, `valueRef` (scalar from root `values`), `dataType`, `formatRef`, `format`, `height`, `width`, `picture`, `case`, `note`.

Typical use: title block, logo, merged headline, totals label. Remember to start the data rows below with `rows[0].pos`.

## 6. Format

Usable inline as `format` or named in root `formats`. A format can extend another via its own `formatRef`; inline `format` next to a `formatRef` overrides single properties.

- Font: `fontRef`, `fontName`, `fontSize`, `fontColor`, `bold`, `italic`, `underline` (integer: 0 none, 1 single, 2 double, 33/34 accounting)
- Alignment: `alignH` 0 general, 1 left, 2 center, 3 right, 4 fill, 5 justify, 6 merge, 7 distributed · `alignV` 0 top, 1 center, 2 bottom, 3 justify, 4 distributed · `wrap`, `shrinkToFit`
- Numbers: `numberFormat` (integer id, §12) or `numberFormatCustom` (Excel format string)
- Borders: `border` (all four) or `borderTop|Right|Bottom|Left`, plus `…Color`. Style by id 0–13 or name: none, thin, medium, dashed, dotted, thick, double, hair, medium dashed, dash dot, medium dash dot, dash dot dot, medium dash dot dot, slant dash dot. Diagonal: `borderDiagonal`, `borderDiagonalMode` (`none|up|down|both`), `borderDiagonalColor`.
- Fill: `backgroundColor`, `foregroundColor`, `pattern` (0–18 or name, 1 = `solid`)
- `dataType`, `hide`, `note`
- Not implemented in the engine: `lock`, `indent`, `rotate` — do not offer them.

## 7. Font (catalog entry)

`fontName`, `fontSize`, `fontColor`, `bold`, `italic`, `underline`, `fontRef` (extend another font), `note`. The font must be installed on the machine that generates the file (mind server-side generation).

## 8. Color

Exactly one of: `{"rgb":[r,g,b]}`, `{"name":"lightblue"}` (Excel palette names, see schema enum), `{"ref":"myColor"}`.
Catalog entries in root `colors` may only use `name` or `rgb`. A `ref` must be at least 2 characters.

## 9. Picture

Only inside a cell (or a `case` result). One of `ref` (catalog), `path`, `base64`. Options: `width`, `height` (pixels, `-1` auto), `x`, `y` (pixel offset), `position` (`resize` | `move` | `fix`), `scale` (0–1, not recommended).
Catalog: `"pictures": {"logo": {"path": "desktop/logo.png"}}` or `{"base64": "…"}`.
Sizing is approximate in Excel and differs slightly across OS/Excel versions; tell the user to expect one or two adjustment rounds.

## 10. Case (conditional)

On a column or a cell. One object, or an array of objects for several independent rules.

```json
"case": {
  "if":   {"value": {"lessThan": 0}},
  "then": {"formatRef": "negative"},
  "else": {"formatRef": "table"}
}
```

`if.value` holds exactly **one** operator: `equalTo` (string, case-insensitive, or number), `beginsWith`, `endsWith`, `contains` (string), `containsAny`, `containsAll` (array of strings), `greaterThan`, `greaterThanOrEqualTo`, `lessThan`, `lessThanOrEqualTo` (number).
`then` / `else` accept cell properties except `pos` and `case`: `value` (use `null` or `""` to blank the cell), `formatRef`, `format`, `picture`, `dataType`, `valueRef`, `height`, `width`.
There is no AND across operators; ranges need two rules, and the result is evaluated at generation time — this is not Excel's live conditional formatting.

## 11. Print

`paperSize` (name such as `"A4"`, `"LETTER"`, or id 0–41), `landscape`, `fit: [pagesWide, pagesTall]`, `repeatRows` (row index or `[start, count]`), `withGrid`, `marginTop|Right|Bottom|Left` (inches), `header`, `footer`.

Header/footer: `margin` (inches) and sections `left`, `center`, `right`. A section is `{"text": …}` plus **either** `fontRef` **or** inline `fontName`/`fontSize`/`bold`/`italic` — not both.
Placeholders: `{page} {total} {date} {time} {filepath} {filename} {sheet} {picture}`. Toggle tags: `{b} {i} {underline} {underlines} {strike} {sup} {sub}`.

## 12. Number formats

`numberFormat` takes the LibXL built-in id (0–49). Common ones:

| id | format | id | format |
|---|---|---|---|
| 0 | General | 14 | short date (system locale) |
| 1 | `0` | 15 | `d-mmm-yy` |
| 2 | `0.00` | 20 | `h:mm` |
| 3 | `#,##0` | 21 | `h:mm:ss` |
| 4 | `#,##0.00` | 22 | `m/d/yy h:mm` |
| 9 | `0%` | 44 | accounting with currency, 2 decimals |
| 10 | `0.00%` | 49 | `@` (text) |

Full list: https://www.mbsplugins.eu/XLFormatSetNumFormat.shtml
For anything locale-specific use `numberFormatCustom`, e.g. `"DD.MM.YYYY"`, `"#,##0.00 €"`, `"0.0 \"kg\""`. Format strings use Excel's invariant syntax (`.` decimal, `,` thousands); Excel localises the display.

## 13. Known doc/schema mismatches

| topic | docs say | schema says (use this) |
|---|---|---|
| picture positioning key | `pos` | `position` |
| `underline` | string (`single`…) | integer 0/1/2/33/34 |
| `numberFormat` | string or integer | integer only (since 2.2.1) |
| `filters.autoFilter` | camelCase | `autofilter` |
| row `pos` array | `[start, length]` | `[colOffset, row]` |
| row `"format": "bold"` | shown in an example | `format` must be an object: `{"bold": true}` |
| `fontNmae` in fonts example | typo | `fontName` |
