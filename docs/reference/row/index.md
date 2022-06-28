---
title: Row
parent: Reference
has_children: false
has_toc: false
nav_order: 8
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

## Row

The row object describes one or many rows on a sheet. A row is added after the previous one if not defined otherwise using 'pos'.

### Examples

```json
"rows": [
    {
        "values": [ "Title", "Firstname", "Lastname", "Email"],
        "format": {
            "fontRef": "Standard-bold",
            "backgroundColor": {"rgb": [160,210,255]}
        }
    },
    {
        "path": "tmp/export.xlsx",
        "fields": ["Title", "First Name", "Last Name", "Email Addresses::Address"],
        "type": "data"
    }
]
```

### Implementations

[Workbook]({{ '/reference/workbook' | relative_url }})

[Sheet]({{ '/reference/sheet' | relative_url }})

### Properties

<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
    <tr>
        <th>contentType</th>
        <td>string</td>
        <td>Content Type in Source File or Field<br><br>possible values:<br>json<br>csv<br>tab</td>
    </tr>
    <tr>
        <th>fields</th>
        <td>array</td>
        <td>Filter Data Source by Column Names.<br>Determines which fields from the source shall be in the target file. References the header names.<br><br>Array Items:<br>&nbsp;&nbsp;string<br><br>minItems: 1</td>
    </tr>
    <tr>
        <th>includeFirstRow</th>
        <td>boolean</td>
        <td>Import first row from source.<br><br>When processing a source file and the target row is on pos:1 (second row), the source's first row is omitted as it usually contains column headers. If your source file's data starts in row 0 or you want to export the original headers you have to set <code>includeFirstRow: true</code>.<br><br>default: <code>false</code></td>
    </tr>
    <tr>
        <th>limit</th>
        <td>integer</td>
        <td>Limit number of rows processed from source.</td>
    </tr>
    <tr>
        <th>offset</th>
        <td>integer</td>
        <td>Row to start processing the source file.</td>
    </tr>
    <tr>
        <th>path</th>
        <td>string</td>
        <td>File path to a source file providing data.</td>
    </tr>
    <tr>
        <th>type</th>
        <td>string</td>
        <td>Rows can be of type <b>header</b>, <b>data</b> or <b>summary</b>. Choosing one applies specific formattings.<br><br>possible values:<br>header<br>data<br>summary</td>
    </tr>
    <tr>
        <th>widths</th>
        <td>array</td>
        <td>Specify Columns Widths, use -1 for 'auto'. The unit is character. To specify the width for all columns, set Default Column Width in sheet or workbook. Width items per column, from left to right.<br><br>Array Items:<br>&nbsp;&nbsp;<b>width</b> - integer</td>
    </tr>
    <tr>
        <th>formatRef</th>
        <td>string</td>
        <td>Reference to a named format.</td>
    </tr>
    <tr>
        <th>format</th>
        <td>object</td>
        <td>Format Options<br><a href="/reference/format/">Format</a></td>
    </tr>
    <tr>
        <th>height</th>
        <td>integer</td>
        <td>Set the row height in points.</td>
    </tr>
    <tr>
        <th rowspan=2>pos</th>
        <td>integer </td>
        <td>Position of row.<br>Starting row position. First row is pos 0.<br><br>minimum:0</td>
    </tr>
    <tr>
        <td>array</td>
        <td>Array containing start and length of row. First row is pos 0.<br><br>Array Items:<br>&nbsp;&nbsp;<code>start</code> integer minimum:0<br>&nbsp;&nbsp;<code>length</code> integer minimum:0</td>
    </tr>
    <tr>
        <th>values</th>
        <td>array</td>
        <td>Values array for each row.<br><br>minItems:1<br><br>Standard Value Data Types OR<br>Array of Standard Value Data Types<br><br>Array Items:<br>&nbsp;&nbsp;string OR<br>&nbsp;&nbsp;integer OR<br>&nbsp;&nbsp;boolean OR<br>&nbsp;&nbsp;Array[string OR integer OR boolean]</td>
    </tr>
    <tr>
        <th>valuesRef</th>
        <td>string</td>
        <td>Reference to central value storage.</td>
    </tr>
</table>