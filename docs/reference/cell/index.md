---
title: Cell
parent: Reference
has_children: false
has_toc: false
nav_order: 9
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

## Cell

Define the content, look, dimensions and place of a single cell. Must be placed with <b>cell.pos</b>.

### Examples

```json
{
    "pos": [0,0,5,2],
    "picture": {
        "ref": "logo",
        "width": 227,
        "height": 60,
        "position": "move"
    }
}
```
*Example:* Cell spanning 5 columns and 2 rows on top of sheet with picture as content.

```json
{
    "pos": [3,1],
    "format": {
        "borderColor": "blue"
    },
    "value": 42
}
```
*Example:* Cell in third column, second row with blue border and integer value.

### Implementations

The `cell` element can be used in the following components:

- [Sheet]({{ '/reference/sheet' | relative_url }})
- [Workbook]({{ '/reference/workbook' | relative_url }})

### Properties

<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
    <tr>
        <th>height</th>
        <td>integer</td>
        <td>Height of the cell in pixel.</td>
    </tr>
    <tr>
        <th>width</th>
        <td>integer</td>
        <td>Width of the cell in pixel.</td>
    </tr>
    <tr>
        <th>pos</th>
        <td>array</td>
        <td>An array of <b>integers</b> describing the cell positioning.<br><br>default length: 1 <br>maxItems: 4 <br>minItems: 2<br><br>Array Items:<br>&nbsp;&nbsp;<code>cellPosX</code> - Horizontal position by columns. (<b>Required</b>)<br>&nbsp;&nbsp;<code>cellPosY</code> - Vertical position by rows (<b>Required</b>)<br>&nbsp;&nbsp;<code>cellPosLengthX</code> - Horizontal length by columns<br>&nbsp;&nbsp;<code>cellPosLengthY</code> - Vertical length by rows<br><br><code>cellPosX</code> minimum: 0<br><code>cellPosY</code> minimum: 0</td>
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
        <th rowspan=3>value</th>
        <td>string</td>
        <td rowspan=3>Set cell value.</td>
    </tr>
    <tr>
        <td>integer</td>
    </tr>
    <tr>
        <td>boolean</td>
    </tr>
    <tr>
        <th>valueRef</th>
        <td>string</td>
        <td>Reference to central value storage.</td>
    </tr>
    <tr>
        <th rowspan=2>case</th>
        <td>object</td>
        <td rowspan=2>Conditional Properties<br><a href="/reference/case/">Case</a></td>
    </tr>
    <tr>
        <td>array</td>
    </tr>
    <tr>
        <th>picture</th>
        <td>object</td>
        <td>A picture as content of a cell<br><a href="/reference/picture/">Picture</a></td>
    </tr>
</table>
