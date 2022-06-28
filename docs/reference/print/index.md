---
title: Print Options
parent: Reference
has_children: false
has_toc: false
nav_order: 1
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

## Print

This is the place to set options for a print output. Options can be set at the workbook level - setting default values for all sheets, and also at every sheet to set specific settings.

### Examples

```json
"print":{
    "paperSize": 0,
    "fit": [2,4],
    "header":{
        "right":{
            "text": "page: {page} of {total}"
        }
    },
    "footer":{
        "left":{
            "text": "{date} {time}"
        },
        "center":{
            "text": "{filepath} {filename} {sheet}",
            "bold": true
        }
    }
}
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
    <th>fit</th>
    <td>array</td>
    <td>Fit sheet to page(s) in width and height when printed. [ pages width, pages height ]<br>When a sheet is too big for the targeted paper size, print it over multiple pages.<br><br>Array Items:<br>&nbsp;&nbsp;<b>width</b> integer, minimum: 0<br>&nbsp;&nbsp;<b>length</b> integer, minimun: 0</td>
</tr>
<tr>
    <th>landscape</th>
    <td>boolean</td>
    <td>Toggle for document landscape orientation.</td>
</tr>
<tr>
    <th>withGrid</th>
    <td>boolean</td>
    <td>Include cell grid when printing.</td>
</tr>
<tr>
    <th>header</th>
    <td>object</td>
    <td>Set up a header.<br><a href="/reference/print/#header-and-footer">Header and Footer</a></td>
</tr>
<tr>
    <th>footer</th>
    <td>object</td>
    <td>Set up a footer.<br><a href="/reference/print/#header-and-footer">Header and Footer</a></td>
</tr>

<tr><th rowspan=2>repeatRows</th>
    <td>integer</td>
    <td>Repeat these row(s) as header after each pagebreak.<br>Repeat single row.<br>minimum:0</td>
</tr>
<tr>
    <td>array</td>
    <td>Set first row (starting with 0) and count of rows to repeat.<br><br>Array Items:<br>&nbsp;&nbsp;<b>start</b> integer<br>&nbsp;&nbsp;<b>length</b> integer</td>
</tr>
<tr>
    <th rowspan=2>paperSize</th>
    <td>string</td>
    <td rowspan=2>Set paper size <b>by Name</b> or <b>as Integer</b>. 'Default' depends on the machine the template is processed on, this could also be different on server.<br>https://www.mbsplugins.eu/XLSheetGetPaper.shtml<br><br><code>0</code> DEFAULT<br><code>1</code> LETTER<br><code>2</code> LETTERSMALL<br><code>3</code> TABLOID<br><code>4</code> LEDGER<br><code>5</code> LEGAL<br><code>6</code> STATEMENT<br><code>7</code> EXECUTIVE<br><code>8</code> A3<br><code>9</code> A4<br><code>10</code> A4SMALL<br><code>11</code> A5<br><code>12</code> B4<br><code>13</code> B5<br><code>14</code> FOLIO<br><code>15</code> QUATRO<br><code>16</code> 10x14<br><code>17</code> 10x17<br><code>18</code> NOTE<br><code>19</code> ENVELOPE_9<br><code>20</code> ENVELOPE_10<br><code>21</code> ENVELOPE_11<br><code>22</code> ENVELOPE_12<br><code>23</code> ENVELOPE_14<br><code>24</code> C_SIZE<br><code>25</code> D_SIZE<br><code>26</code> E_SIZE<br><code>27</code> ENVELOPE_DL<br><code>28</code> ENVELOPE_C5<br><code>29</code> ENVELOPE_C3<br><code>30</code> ENVELOPE_C4<br><code>31</code> ENVELOPE_C6<br><code>32</code> ENVELOPE_C65<br><code>33</code> ENVELOPE_B4<br><code>34</code> ENVELOPE_B5<br><code>35</code> ENVELOPE_B6<br><code>36</code> ENVELOPE<br><code>37</code> ENVELOPE_MONARCH<br><code>38</code> US_ENVELOPE<br><code>39</code> FANFOLD<br><code>40</code> GERMAN_STD_FANFOLD<br><code>41</code> GERMAN_LEGAL_FANFOLD<br></td>
</tr>
<tr>
    <td>integer</td>
</tr>

</table>

#### Header and Footer
<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
<tr>
<th>margin</th>
    <td>number</td>
<td>Margin from header or footer cell to the outer bounds of paper. The unit is inches.<br>minimum:0</td>
</tr>
<tr>
    <th>left</th>
    <td>object</td>
    <td><a href="/reference/print/#section">Section</a></td>
</tr>
<tr>
    <th>center</th>
    <td>object</td>
    <td><a href="/reference/print/#section">Section</a></td>
</tr>
<tr>
    <th>right</th>
    <td>object</td>
    <td><a href="/reference/print/#section">Section</a></td>
</tr>

</table>

#### Section

<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
<tr>
    <th>text</th>
    <td>string</td>
    <td>Text for header section. Combinable with placeholders:<br><br>{page}<br>{total}<br>{date}<br>{time}<br>{picture}<br>{filepath}<br>{filename}<br>{sheet}<br>format tags (start/stop):<br><br>{strike}<br>{sup}<br>{sub}<br>{underline}<br>{underlines}<br>{b}<br>{i}</td>
</tr>
</table>

Font for Section can be referenced or defined:

#### Section Font Reference

<table>

<tr>
    <th>fontRef</th>
    <td>string</td>
    <td>Name of a Font Definition</td>
</tr>

</table>

#### Section Font Definition

<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
<tr>
    <th>fontName</th>
    <td>string</td>
    <td>Name of a Font face (e.g. 'Helvetica')</td>
</tr>
<tr>
    <th>fontSize</th>
    <td>integer</td>
    <td>Font Size in point</td>
</tr>
<tr>
    <th>bold</th>
    <td>boolean</td>
    <td>Font Style bold</td>
</tr>
<tr>
    <th>italic</th>
    <td>boolean</td>
    <td>Font Style italic</td>
</tr>

</table>