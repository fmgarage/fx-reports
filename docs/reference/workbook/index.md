---
title: Workbook
parent: Reference
has_children: false
has_toc: false
nav_order: 5
---

<style>

table {
    border-collapse: collapse;
}

.table-wrapper {
    border-radius: 2px;
    box-shadow: none;
}

th {
    text-align: start;
}

th, td {
    vertical-align: baseline;
    min-width: 120px;
    border: 2px solid #eeebee;
}

@media (min-width: 31.25rem) { th, td { font-size: 14px !important; } }

th:first-of-type, td:first-of-type { border-left: 2px solid #eeebee; }

tbody tr:last-of-type th, tbody tr:last-of-type td { border-bottom: 2px solid #eeebee; }
/* tbody tr:last-of-type td { padding-bottom: 0.75rem; } */
code {font-size: 0.83em;}

</style>

## Workbook

Represents the Excel workbook, a file containing one or more sheets. Also holds format and style related definitions as well as picture and value catalogs.

### Examples

```json
{
    "filename": "daily.xlsx",
    "columnWidth": -1,
    "formats": {
        "emphasize-blue": {
            "italic": true,
            "border": "double",
            "alignH": 2,
            "backgroundColor": {
                "name": "aqua"
            }
        }
    },
    "pictures": {
        "path": "/usr/local/share/excel/pictures",
        },
    "values": {
        "numberToday": 8,
        "partnerData": [
            ["ARE", 50, "UK"],
            ["KLF", 89, "NVL"],
            ["OPE", 46, "FRA"]
        ]
    },
    "sheets": [
        {...},
        {...},
        {...}
    ]
}
```

### Properties

<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
<tr>
    <th>colors</th>
    <td>object</td>
    <td>Can be defined by <b>colorName</b> or <b>colorRgb</b>.<br><a href="/reference/color/">Color</a></td>
</tr>
<tr>
    <th>fonts</th>
    <td>object</td>
    <td>Add Font definitions by specifying a unique Name<br><a href="/reference/font/">Font</a></td>
</tr>
<tr>
    <th>formats</th>
    <td>object</td>
    <td>Add named formats that can be referenced with "formatRef"in columns, rows and cells.</td>
</tr>
<tr>
    <th>pictures</th>
    <td>object</td>
    <td>picture name as ref and path as field reference or file path<br>add picture to catalog by path or as base64</td>
</tr>
<tr>
    <th>pictures.path</th>
    <td>string</td>
    <td>system path, shortcuts are supported (e.g. 'desktop/logo.jpeg')</td>
</tr>
<tr>
    <th>filename</th>
    <td>string</td>
    <td>Specify output file name. Otherwise <code>YYMMDD_hhmmss.xslx</code> will be used as default.</td>
</tr>
<tr>
    <th>location</th>
    <td>string</td>
    <td>folder path ('desktop/exports') or field reference (e.g. FxReports::a_container_[2])<br>default: desktop/fx-exports</td>
</tr>
<tr>
    <th>sheets</th>
    <td>array</td>
    <td>Array of sheets. This array can be used if more than one sheet is defined.<br><a href="/reference/sheet/">Sheet</a></td>
</tr>
<tr>
    <th>columns</th>
    <td>array</td>
    <td>Array of Columns<br>minItems:1<br><a href="/reference/column/">Column</a></td>
</tr>
<tr>
    <th>rows</th>
    <td>array</td>
    <td>Array of Rows, starting from top if not specified by Position.<br>Data Rows are repeated regarding to their input.<br><a href="/reference/row/">Row</a></td>
</tr>
<tr>
    <th>cells</th>
    <td>array</td>
    <td>Array of Cells.<br><a href="/reference/cell/">Cell</a></td>
</tr>
<tr>
    <th>columnWidth</th>
    <td>integer</td>
    <td>Set default Column Width for (all Sheets)<br><br>Adjust column width to the cells' content using `-1` as value.<br>minimum:-1</td>
</tr>
<tr>
    <th>display</th>
    <td>object</td>
    <td>Specify values for displayed spreadsheet.<br><a href="/reference/sheet/">Sheet</a>.<b>display</b></td>
</tr>
<tr>
    <th>print</th>
    <td>object</td>
    <td>Option defining the print settings.<br><a href="/reference/print/">Print</a></td>
</tr>
<tr>
    <th>format</th>
    <td>object</td>
    <td>Format Options<br><a href="/reference/format/">Format</a></td>
</tr>
<tr>
    <th>formatRef</th>
    <td>string</td>
    <td>Reference to a named format.</td>
</tr>
<tr>
    <th>split</th>
    <td>boolean OR array</td>
    <td>deprecated - use display.freeze<br><a href="/reference/sheet/">Sheet</a></td>
</tr>
<tr>
    <th>filters</th>
    <td>object</td>
    <td>Sets sheet filter</td>
</tr>
<tr>
    <th>filters.autoFilter</th>
    <td>boolean</td>
    <td>Sets sheet auto filter</td>
</tr>
<tr>
    <th>values</th>
    <td>object</td>
    <td>Values that can be referenced in the template.</td>
</tr>
<tr>
    <th rowspan=5>values.<i>scalar</i></th>
    <td>string</td><td rowspan=5>Data for cells.</td>
</tr>
<tr>
    <td>integer</td>
</tr>
<tr>
    <td>number</td>
</tr>
<tr>
    <td>boolean</td>
</tr>
<tr>
    <td>null</td>
</tr>
<tr>
    <th>values<i>.array</i></th>
    <td>array</td>
    <td>Data for Rows<br><br>can contain:<br>Object(s)<br>Array(s) of Object(s)</td>
</tr>
</table>