---
title: Sheet
parent: Reference
has_children: false
has_toc: false
nav_order: 6
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

## Sheet

The Sheet object holds a lot of settings and values. It contains the data in form of rows, columns and/or cells and many format and display options.

Content and Structure of an Excel Sheet. 'Columns', 'Rows' and 'Cells' will be processed in this very order.

### Examples

```json
"sheet": {
    "name": "Example-1",
    "rows": [
        {
            "values": [ "Title", "Firstname", "Surname"]
        },
        {
            "path": "desktop/examples/data-blocks/data-file.xlsx",
            "fields": [ "Title", "GivenName", "Surname"]
        }
    ],
    "display": {
        "hideGrid": true
    }
}
```

### Implementations

[Workbook]({{ '/reference/workbook' | relative_url }})

### Properties

<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
<tr>
    <th>columnWidth</th>
    <td>integer</td>
    <td>Set default Column Width for the sheet.<br><br>Set auto width to match the cells' content: <code>-1</code><br><br>Unit: character<br>minimum:-1</td>
</tr>
<tr>
    <th>defaultColumn</th>
    <td>object</td>
    <td></td>
</tr>
<tr>
    <th>defaultColumn.minWidth</th>
    <td>integer</td>
    <td>Default column minimum width.<br>Unit: character</td>
</tr>
<tr>
    <th>defaultColumn.maxWidth</th>
    <td>integer</td>
    <td>Default column maximium width.<br>Unit: character</td>
</tr>
<tr>
    <th>filters</th>
    <td>object</td>
    <td>Sets sheet filters</td>
</tr>
<tr>
    <th>filters.autoFilter</th>
    <td>boolean</td>
    <td>Sets columns auto filter for sheet, based on contents of the columns</td>
</tr>
<tr>
    <th>name</th>
    <td>string</td>
    <td>Optional sheet name. default: "Sheet1"</td>
</tr>
<tr>
    <th>columns</th>
    <td>array</td>
    <td>Array of Columns<br>minItems:1<br><br>ArrayItems<br>&nbsp;&nbsp;<a href="/reference/column/">Column</a></td>
</tr>
<tr>
    <th>rows</th>
    <td>array</td>
    <td>Array of Rows, starting from top if not specified by Position.<br>Data Rows are repeated regarding to their input.<br><br>ArrayItems<br>&nbsp;&nbsp;<a href="/reference/row/">Row</a></td>
</tr>
<tr>
    <th>cells</th>
    <td>array</td>
    <td>Array of Cells.<br><br>ArrayItems<br>&nbsp;&nbsp;<a href="/reference/cell/">Cell</a></td>
</tr>
<tr>
    <th>display</th>
    <td>object</td>
    <td>Set display options</td>
</tr>
<tr>
    <th>display.hideGrid</th>
    <td>boolean</td>
    <td>Hides the grid on the entire spreadsheet.</td>
</tr>
<tr>
    <th>display.zoom</th>
    <td>integer</td>
    <td>Set the zoom to a value between 25 and 400 percent.</td>
</tr>
<tr><th rowspan=2>display.freeze</th>
    <td>boolean</td>
    <td>Freeze panes at column 0 : row 1</td>
</tr>
<tr>
    <td>array</td>
    <td>Freeze at custom position<br><br>ArrayItems:<br>&nbsp;&nbsp;<b>column</b> integer - default: 0<br>&nbsp;&nbsp;<b>row</b> integer - default: 1</td>
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
</table>