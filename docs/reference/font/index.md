---
title: Font Definition
parent: Reference
has_children: false
has_toc: false
nav_order: 2
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

## Font

Definition of a font. Define the font face, the size, color and styles. It is possible to refer to a defined font from the catalog and add further properties or override existing ones.

### Examples

```json
"font1":{
    "fontName": "Source Sans Pro",
    "fontSize": 13,
    "fontColor": {
        "rgb": [255,140,0]
    }
}
```

### Implementations

[Workbook](/reference/workbook)

[Format](/reference/format)

### Properties

<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
    <tr>
        <th>fontName</th>
        <td>string</td>
        <td>Font face name (e.g. 'Helvetica')</td>
    </tr>
    <tr>
        <th>fontRef</th>
        <td>string</td>
        <td>Name of a Font Definition</td>
    </tr>
    <tr>
        <th>bold</th>
        <td>boolean</td>
        <td>Toggle bold font style</td>
    </tr>
    <tr>
        <th>italic</th>
        <td>boolean</td>
        <td>Toggle italic font style</td>
    </tr>
    <tr>
        <th>underline</th>
        <td>integer</td>
        <td>Toggle underline style of the font.<br><code>0</code> no underline<br><code>1</code> single<br><code>2</code> double<br><code>33</code> acc single<br><code>34</code> acc double</td>
    </tr>
    <tr>
        <th>fontColor</th>
        <td>object</td>
        <td>Contains color as Name, Ref or RGB<br><a href="/reference/color/">Color</a></td>
    </tr>
    <tr>
        <th>fontSize</th>
        <td>integer</td>
        <td>Font Size in pt</td>
    </tr>
</table>
