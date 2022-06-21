---
title: Picture
parent: Reference
has_children: false
has_toc: false
nav_order: 13
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

## Picture

A Picture can be set by naming a `path` in the filesystem or `referencing` from the pictures catalog.

When adding pictures to the catalog, only `path` is available to use.

It is recommended to use width and height to adjust the size of pictures rather than scale, as results are a little more predictable. Read more: [Picture](/writing-templates/pictures)

### Examples

```json
"cells": [
    {
        "pos": [0,0],
        "picture": {
            "ref": "logo",
            "width": 227,
            "height": 60,
            "position": "move"
        }
    }
],
"pictures": {
    "logo": {"path": "desktop/examples/picture-logo/fx-reports.png"}
}
```
### Implementations

[Cell](/reference/cell)

### Properties

<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
<tr>
    <th>ref</th>
    <td>string</td>
    <td>a ref name referring to a picture defined in the pictures catalog. </td>
</tr>
<tr>
    <th>path</th>
    <td>string</td>
    <td>system path, shortcuts are supported (e.g. 'desktop/logo.jpeg') or as field reference (e.g. 'FxReports::a_container_[2]')</td>
</tr>
<tr>
    <th>width</th>
    <td>integer</td>
    <td>Width in pixels. Can be <code>-1</code> or non-defined for auto.</td>
</tr>
<tr>
    <th>height</th>
    <td>integer</td>
    <td>Height in pixels. Can be <code>-1</code> or non-defined for auto.</td>
</tr>
<tr>
    <th>scale</th>
    <td>number</td>
    <td>Not recommended to use.<br>Aspect ratio will be scaled unevenly.<br><br>Scale in percent. You can either use scale or width and height. Default ist 1.0<br><br>exclusiveMinimum:0</td>
</tr>
<tr>
    <th>x</th>
    <td>integer</td>
    <td>Relative offset from left in pixels</td>
</tr>
<tr>
    <th>y</th>
    <td>integer</td>
    <td>Relative offset from top in pixels</td>
</tr>
<tr>
    <th>pos</th>
    <td>string</td>
    <td>Determines the future scaling and positioning behaviour of the picture.<br><br>"resize" – move and size with cells<br>"move" – move but don't size with cells<br>"fix" – don't move or size with cells<br><br>possible values:<br>resize<br>move<br>fix</td>
</tr>
</table>
