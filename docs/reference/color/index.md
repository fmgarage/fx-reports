---
title: Color
parent: Reference
has_children: false
has_toc: false
nav_order: 11
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

## Color

Colors can be applied to text, backgrounds, borders, and other elements in 3 ways: with <b>RGB</b> values, using the Excel <b>predefined</b> colors, or referencing a <b>named</b> color definition that you defined in the workbook.

### Example

```json
"backgroundColor": {
    "rgb": [160,210,255]
}
```
```json
"fontColor": {
    "name": "violet"
}
```
### Implementations

[Format]({{ '/reference/format' | relative_url }})

[Font]({{ '/reference/font' | relative_url }})

### Properties

<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
    <tr>
        <th>rgb</th>
        <td>array</td>
        <td>Color as RGB. Array of hex values. (0-255)<br><br>maxItems: 3<br>minItems: 3<br><br>ArrayItems:<br>&nbsp;&nbsp;<code>integer</code> - 0-255,<br>&nbsp;&nbsp;<code>integer</code> - 0-255,<br>&nbsp;&nbsp;<code>integer</code> - 0-255</td>
    </tr>
    <tr>
        <th>ref</th>
        <td>string</td>
        <td>Name of color definition.<br>A name referencing a color defined in the <b>colors</b> catalog of the <a href="/reference/workbook/">workbook</a>.</td>
    </tr>
    <tr>
        <th>name</th>
        <td>string</td>
        <td>An Excel-defined color name<br><br>possible values:<br>none<br>black<br>white<br>red<br>brightgreen<br>blue<br>yellow<br>pink<br>turquoise<br>darkred<br>green<br>darkblue<br>darkyellow<br>violet<br>teal<br>gray25<br>gray50<br>periwinkle cf<br>plum cf<br>ivory cf<br>lightturquoise cf<br>darkpurple cf<br>coral cf<br>oceanblue cf<br>iceblue cf<br>darkblue cl<br>pink cl<br>yellow cl<br>turquoise cl<br>violet cl<br>darkred cl<br>teal cl<br>blue cl<br>skyblue<br>lightturquoise<br>lightgreen<br>lightyellow<br>paleblue<br>rose<br>lavender<br>tan<br>lightblue<br>aqua<br>lime<br>gold<br>lightorange<br>orange<br>bluegray<br>gray40<br>darkteal<br>seagreen<br>darkgreen<br>olivegreen<br>brown<br>plum<br>indigo<br>gray80<br>default foreground<br>default background<br>tooltip<br>auto</td>
    </tr>
</table>