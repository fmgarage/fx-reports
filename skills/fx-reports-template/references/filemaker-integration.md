# FileMaker integration

How a template gets from a FileMaker solution into FX Reports. Read this when the user wants to wire a template into their own file, fill it with found-set data, or asks "how do I call this".

## Prerequisites (one-time)

- `FX_Reports.fmp12` next to the user's file (same folder or same server). It must not be renamed.
- MBS Plugin ≥ 11 and LibXL ≥ 4.0 in the FileMaker plug-in folder. Both run in demo mode for evaluation; hosting on FileMaker Server needs licenses.
- Connector in the user's file, either via the add-on (`FX_Reports.fmaddon`, FileMaker 19+) or copied manually from `FX_ReportsExample.fmp12` in this order: custom functions `SError.catch_v7`, `SError.display_v6` → table occurrence `FxReports` (exact name) → scripts from the `# CONNECTOR` folder: `*FxReports.excelGenerate( $filename, $location )` and optionally `*FxReports.excelValidate()`.

Do not re-explain this unless the user asks; most users of this skill already have it running.

## The call

1. Put the template text into the container field `FxReports::a_container_`.
2. Perform script `*FxReports.excelGenerate( $filename, $location )`.
3. Check for errors with `SError.catch_v7 ( "" )`; show them with `SError.display_v6 ( "" )`.

`filename` and `location` can live in the template **or** be passed as parameters of the connector script; parameters override the template. Rule of thumb: static values belong in the template; if the path is part of the calling solution's logic (per user, per record, temp folder then e-mail…), pass it as parameter and keep the template free of it. Without either, the file goes to `desktop/FX Reports output` under a timestamp name.

The script parameter is a JSON object, e.g. `JSONSetElement ( "{}" ; [ "filename" ; $name ; JSONString ] ; [ "location" ; $folder ; JSONString ] )`; both keys are optional.

Sketch (adapt names, keep the user's own scripting conventions):

```
Set Variable [ $template ; Value: <template JSON, see below> ]
Set Field [ FxReports::a_container_ ; $template ]
Perform Script [ "*FxReports.excelGenerate( $filename, $location )" ; Parameter: $param ]
If [ SError.catch_v7 ( "" ) ]
    Exit Script [ Text Result: SError.display_v6 ( "" ) ]
End If
```

## Getting data into the template

Three options, pick by data volume and by where formatting decisions live.

### A. Export file as source (large found sets)

Export the found set as xlsx to the temp folder, then reference it by `path`. FileMaker's export is fast, and the template only reshapes and styles it.

```
Set Variable [ $path ; Value: Get ( TemporaryPath ) & "export.xlsx" ]
Export Records [ With dialog: Off ; "$path" ]
```

Template side: a header row with friendly names, then
`{"path": "tmp/export.xlsx", "fields": ["Contact::b_lastname", …]}`.
The `tmp` shortcut resolves to `Get ( TemporaryPath )`, so the export above and the template path meet in the same folder. The export's header row is skipped automatically.
`fields` uses the header names of the export file — for FileMaker exports these are the field names, fully qualified for related fields (`Email Addresses::Address`).

### B. Central value storage (small to medium, calculated data)

Keep the template static (stored in a field or a text object) and inject only the data:

```
JSONSetElement ( $template ;
    [ "values.rows" ; $rowsArray ; JSONArray ] ;
    [ "values.reportDate" ; Get ( CurrentDate ) ; JSONString ] ;
    [ "filename" ; "invoices-" & Year ( Get ( CurrentDate ) ) & ".xlsx" ; JSONString ]
)
```

with `{"valuesRef": "rows"}` in a row and `{"valueRef": "reportDate"}` in a cell. Storage names must be alphanumeric (`valuesRef` pattern). Build `$rowsArray` with a loop over the found set, `ExecuteSQL` plus conversion, or a `While()`. Rows can be **arrays** (positional, compact) or **objects** (keyed):

```json
"rows":   [ {"values": ["Customer", "No.", "Amount"]},
            {"valuesRef": "invoices", "fields": ["customer", "no", "amount"]} ],
"values": { "invoices": [ {"no": "R-1001", "customer": "ACME", "amount": 1200.5} ] }
```

With objects, `fields` decides which keys appear and in which order, so columns can be added, dropped or reordered in the template without touching the FileMaker side. The engine reads the available keys from the first object only — keep the keys identical across all objects — and `fields` assigns them to columns. Without `fields` all keys are output in stored order — alphabetical once FileMaker's JSON functions have touched the payload — so always set `fields` with object rows. A name in `fields` that is missing in the first object stops generation with a `FieldNotFound` error.

This separation (template = layout, `values` = data) is the recommended default: the same template can be validated once and reused.

### C. Inline `values` in rows

Fine for fixed content (headers, labels, a handful of rows). Not meant as the data channel for real reports.

## Things to get right

- **Numbers**: pass them as JSON numbers (`JSONNumber`), not strings, and set `dataType: "number"` on the column, otherwise Excel will not sum them.
- **Dates**: set `dataType: "date"` (or `timestamp`) on the column plus a `numberFormat` / `numberFormatCustom`. In `values`, pass dates as ISO strings `YYYY-MM-DD` and timestamps as `YYYY-MM-DD hh:mm:ss` (space-separated). Text in the FileMaker file's own date format is also accepted, but it is locale-dependent, so prefer ISO. With an xlsx export as source, dates arrive as real dates.
- **Paths**: shortcuts `desktop/…`, `documents/…`, `tmp/…` work for sources, pictures and `location`. A container field reference (`FxReports::a_container_[2]`) also works as source, picture path or target location.
- **Server-side** (PSOS/schedule): paths resolve on the server, so use `tmp` or a container field rather than `desktop`; fonts and default paper size come from the server machine.
- **Validate first**: `*FxReports.excelValidate()` checks a template against the schema inside FileMaker — useful while the user iterates without Claude.
