---
title: Format Definition
parent: Reference
has_children: false
has_toc: false
nav_order: 3
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

## Format

Format provides styling and display options for a **cell**, but can also be applied to rows, columns, sheets and the complete workbook.

### Examples

```json
"emphasize-blue": {
    "italic": true,
    "border": "double",
    "alignH": 2,
    "backgroundColor": {
        "name": "aqua"
    }
}
```

### Implementations

- [Workbook]({{ '/reference/workbook' | relative_url }})
- [Sheet]({{ '/reference/sheet' | relative_url }})
- [Row]({{ '/reference/row' | relative_url }})
- [Column]({{ '/reference/column' | relative_url }})
- [Cell]({{ '/reference/cell' | relative_url }})


### Properties

<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
<tr>
    <th>dataType</th>
    <td>string</td>
    <td>data type of cell<br><br>possible values:<br>string<br>number<br>date<br>blank<br>timestamp<br>formula</td>
</tr>
<tr>
    <th>alignH</th>
    <td>integer</td>
    <td>Horizontal alignment of text<br><br>possible values:<br><code>0</code> general<br><code>1</code> left<br><code>2</code> center<br><code>3</code> right<br><code>4</code> full<br><code>5</code> justify<br><code>6</code> merge<br><code>7</code> distributed</td>
</tr>
<tr>
    <th>alignV</th>
    <td>integer</td>
    <td>Vertical alignment of text<br><br>possible values:<br><code>0</code> Top<br><code>1</code> Center<br><code>2</code> Bottom<br><code>3</code> Justify<br><code>4</code> Distributed</td>
</tr>
<tr>
    <th>backgroundColor</th>
    <td>object</td>
    <td rowspan=8>Contains color as Name, Ref or RGB<br><a href="/reference/color/">Color</a></td>
</tr>
<tr>
    <th>foregroundColor</th>
    <td>object</td>
</tr>
<tr>
    <th>borderColor</th>
    <td>object</td>
</tr>
<tr>
<th>borderTopColor</th>
    <td>object</td>
</tr>
<tr>
    <th>borderBottomColor</th>
    <td>object</td>
</tr>
<tr>
    <th>borderRightColor</th>
    <td>object</td>
</tr>
<tr>
    <th>borderLeftColor</th>
    <td>object</td>
</tr>
<tr>
    <th>borderDiagonalColor</th>
    <td>object</td>
</tr>
<tr>
    <th rowspan=2>border</th>
    <td>string</td>
    <td rowspan=12>Sets the border style by ID or name.<br><br>possible values:<br><code>0</code> None<br> <code>1</code> Thin<br> <code>2</code> Medium<br> <code>3</code> Dashed<br> <code>4</code> Dotted<br> <code>5</code> Thick<br> <code>6</code> Double<br> <code>7</code> Hair<br> <code>8</code> Medium dashed<br> <code>9</code> Dash dot<br> <code>10</code> Medium dash dot<br> <code>11</code> Dash Dot Dot<br> <code>12</code> Medium dash dot dot<br> <code>13</code> Slant dash dot</td>
</tr>
<tr>
    <td>integer</td>
</tr>
<tr>
    <th rowspan=2>borderTop</th>
    <td>string</td>
</tr>
<tr>
    <td>integer</td>
</tr>
<tr>
    <th rowspan=2>borderRight</th>
    <td>string</td>
</tr>
<tr>
    <td>integer</td>
</tr>
<tr>
    <th rowspan=2>borderBottom</th>
    <td>string</td>
</tr>
<tr>
    <td>integer</td>
</tr>
<tr>
    <th rowspan=2>borderLeft</th>
    <td>string</td>
</tr>
<tr>
    <td>integer</td>
</tr>
<tr>
    <th rowspan=2>borderDiagonal</th>
    <td>string</td>
</tr>
<tr>
    <td>integer</td>
</tr>
<tr>
    <th>borderDiagonalMode</th>
    <td>string</td>
    <td>Puts diagonal strokes in a cell.<br><br>possible values:<br>none<br>up<br>down<br>both</td>
</tr>
<tr>
    <th>fontName</th>
    <td>string</td>
    <td>Font face name (e.g. 'Helvetica')</td>
</tr>
<tr>
    <th>fontSize</th>
    <td>integer</td>
    <td>Font Size in pt</td>
</tr>
<tr>
    <th>fontColor</th>
    <td>object</td>
    <td>Contains color as Name, Ref or RGB<br><a href="/reference/color/">Color</a></td>
</tr>
<tr>
    <th>fontRef</th>
    <td>string</td>
    <td>Name of a Font Definition</td>
</tr>
<tr>
    <th>italic</th>
    <td>boolean</td>
    <td>Toggle for displaying text as italic.</td>
</tr>
<tr>
    <th>bold</th>
    <td>boolean</td>
    <td>Toggle bold font style</td>
</tr>
<tr>
    <th>underline</th>
    <td>string</td>
    <td>Sets the underline style of the font.<br><br>possible values:<br>single<br>double<br>acc single<br>acc double</td>
</tr>
<tr>
    <th>wrap</th>
    <td>boolean</td>
    <td>Toggle whether the cell text is wrapped.</td>
</tr>
<tr>
    <th rowspan=2>pattern</th>
    <td>integer</td><td rowspan=2>Background Pattern<br><br><code>0</code> None<br><code>1</code> Solid<br><code>2</code> 50% Gray<br><code>3</code> 75% Gray<br><code>4</code> 25% Gray<br><code>5</code> Horizontal Stripes<br><code>6</code> Vertical Stripes<br><code>7</code> Reverse Diagonal Stripes<br><code>8</code> Diagonal Stripes<br><code>9</code> Diagonal Cross Hatch<br><code>9</code> Thick Diagonal Stripe<br><code>11</code> Thin Horizontal Stripe<br><code>12</code> Thin Vertical Stripe<br><code>13</code> Thin Reverse Diagonal Stripe<br><code>14</code> Thin Diagonal Stripe<br><code>15</code> Thin Horizontal Cross Hatch<br><code>16</code> Thin Diagonal Cross Hatch<br><code>17</code> Gray 12P5<br><code>18</code> Gray 6P25</td>
</tr>
<tr>
    <td>string</td>
</tr>
<tr>
    <th>shrinkToFit</th>
    <td>boolean</td>
    <td></td>
</tr>
<tr>
    <th>formatRef</th>
    <td>string</td>
    <td>Reference to a named format.</td>
</tr>
<tr>
    <th rowspan=2>numberFormat</th>
    <td>integer</td>
    <td rowspan=2>individual format options for numbers, dates, currencies, see <a href="https://www.mbsplugins.eu/XLFormatSetNumFormat.shtml">www.mbsplugins.eu/XLFormatSetNumFormat</td>
</tr>
<tr>
    <td>string</td>
</tr>
<tr>
    <th>numberFormatCustom</th>
    <td>string</td>
    <td>custom format options for numbers, dates, currencies..., check <a href="https://www.mbsplugins.eu/XLBookAddCustomNumFormat.shtml">www.mbsplugins.eu/XLBookAddCustomNumFormat</a></td>
</tr>
</table>
