---
title: Column
parent: Reference
has_toc: false
nav_order: 7
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

## Column

Column object describing one or many columns.

### Example

```json
"columns": [
    {
        "pos": 2,
        "dataType": "number",
        "type": "data",
        "format": {
            "border": "medium",
	        "borderColor": {
                "rgb": [0,50,50]
            }
        },
        "case": {
            "if": {
                "value": { "lessThan": 0 }
            },
            "then": {
                "formatRef": "Basic-red"
            }
        },
        "width": -1
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
        <th rowspan="2">pos</th>
        <td>integer</td>
        <td>Set the starting position of the column as integer. <code>-1</code> for auto.<br><br>mininum: <code>-1</code><br> default: <code>-1</code></td>
    </tr>
    <tr>
        <td>array</td>
        <td>In addition to the starting position also set the length. <code>-1</code> for auto. <br><br>Array Items:<br>&nbsp; &nbsp;<code>integer</code> - starting position<br>&nbsp; &nbsp;<code>integer</code>  - length<br><br>starting position:<br>mininum: <code>-1</code><br> default: <code>-1</code><br><br>length:<br>mininum: <code>-1</code><br> default: <code>-1</code></td>
    </tr>
    <tr>
        <th rowspan="2">dataType</th>
        <td rowspan="2">string</td>
        <td>Determine the type of data for the cells.</td>
    </tr>
    <tr>
        <td><br><br>possible values: <code>text</code>, <code>number</code>, <code>date</code>, <code>timestamp</code></td>
    </tr>
    <tr>
        <th>type</th>
        <td>string</td>
        <td>If dataType is set, this says where the format is applied.<br><br>possible values: <code>header</code>, <code>data</code>, <code>summary</code></td>
    </tr>
    <tr>
        <th>format</th>
        <td>object</td>
        <td>Format Options to apply to a column.<br><a href="/reference/format/">Format</a></td>
    </tr>
        <tr>
        <th>formatRef</th>
        <td>string</td>
        <td>Reference to a named format. Format references are defined in <a href="/reference/workbook/#formats">Formats</a></td>
    </tr>
    <tr>
        <th rowspan="2">case</th>
        <td>object</td>
        <td>Define a format or content that is inserted based on one condition.<br><br><a href="/reference/case/">Condition Object</a></td>
    </tr>
    <tr>
        <td>array</td>
        <td>Define a format or content that is inserted based on multiple conditions.<br><br>Array Items [<a href="/reference/case/">Condition Object</a>]</td>
    </tr>
    <tr>
        <th>width</th>
        <td>integer</td>
        <td>Set default Column Width for (all Sheets)<br>
            Auto adjust column width to the cells' content using <code>-1</code> as value.<br><br>
            minimum: <code>-1</code>
        </td>
    </tr>
</table>
