---
title: Case
parent: Reference
has_children: false
has_toc: false
nav_order: 10
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


## Case

Define a format or content that is inserted into a cell based on a condition. The condition is evaluated against the content of the cell.

When multiple conditionals shall be applied, they must be items in an array.

### Example

```json
"case": [
    {
        "if": {
            "value": {
            "greaterThan": 10
            }
        },
        "then": {
            "formatRef": "light-green"
        }
    },
    {
        "if": {...},
        "then": {...},
        "else": {...}
    }
]
```

### Implementations

[Cell]({{ '/reference/cell' | relative_url }})

[Column]({{ '/reference/column' | relative_url }})

### Properties

<table>
    <tr>
        <th>name</th>
        <th>type</th>
        <th>description</th>
    </tr>
    <tr id="if">
        <th>if</th>
        <td>object</td>
        <td>The condition definition object.</td>
    </tr>
    <tr>
        <th>if.value</th>
        <td>object</td>
        <td>Object holding a condition rule.<br><br><b>Attention: only one property allowed!</b></td>
    </tr>
    <tr>
        <th>if.value.beginsWith</th>
        <td>string</td>
        <td>Check if value has substring at the start.</td>
    </tr>
    <tr>
        <th>if.value.contains</th>
        <td>string</td>
        <td>Check if value has substring anywhere.</td>
    </tr>
    <tr>
        <th>if.value.containsAll</th>
        <td>array</td>
        <td>Check if all of multiple substrings exist in value.<br><br>Array items:<br>&nbsp;&nbsp;substring <code>string</code></td>
    </tr>
    <tr>
        <th>if.value.containsAny</th>
        <td>array</td>
        <td>Check if any of multiple substrings exists in value.<br><br>Array Items:<br>&nbsp;&nbsp;substring <code>string</code></td>
    </tr>
    <tr>
        <th>if.value.endsWith</th>
        <td>string</td>
        <td>Check if value has substring at the end.</td>
    </tr>
    <tr>
        <th rowspan="2">if.value.equalTo</th>
        <td>number</td>
        <td>Compare numbers.</td>
    </tr>
    <tr>
        <td>string</td>
        <td>Compare strings. Case-insensitive when comparing strings.</td>
    </tr>
    <tr>
        <th>if.value.greaterThan</th>
        <td>number</td>
        <td>Check if value is greater than number.</td>
    </tr>
    <tr>
        <th>if.value.greaterThanOrEqualTo</th>
        <td>number</td>
        <td>Check if value is greater or equal than number.</td>
    </tr>
    <tr>
        <th>if.value.lessThan</th>
        <td>number</td>
        <td>Check if value is lower than number.</td>
    </tr>
    <tr>
        <th>if.value.lessThanOrEqualTo</th>
        <td>number</td>
        <td>Check if value is lower than or equal to number.</td>
    </tr>
    <tr>
        <th>then</th>
        <td>object</td>
        <td>When the condition evaluates true, the object defined here is applied to/inserted into the cell.</td>
    </tr>
    <tr>
        <th>then.formatRef</th>
        <td>object</td>
        <td>A named format is applied to the cell.<br><br><a href="/reference/format/">FormatRef link</a></td>
    </tr>
    <tr>
        <th>then.picture</th>
        <td>object</td>
        <td>A named format is applied to the cell.<br><br><a href="/reference/picture/">Picture link</a></td>
    </tr>
    <tr>
        <th rowspan="3">then.value</th>
        <td>string</td>
        <td>Insert a string value into cell.</td>
    </tr>
    <tr>
        <td>number</td>
        <td>Insert a numeric value into cell.</td>
    </tr>
    <tr>
        <td>null</td>
        <td>Insert nothing/null value into cell.</td>
    </tr>
    <tr>
        <th>else</th>
        <td>object</td>
        <td>When the condition evaluates false, the object defined here is applied to/inserted into the cell.</td>
    </tr>
        <tr>
        <th>else.formatRef</th>
        <td>object</td>
        <td>A named format is applied to the cell.<br><br><a href="/reference/link/">FormatRef link</a></td>
    </tr>
    <tr>
        <th>else.picture</th>
        <td>object</td>
        <td>A named format is applied to the cell.<br><br><a href="/reference/picture/">Picture link</a></td>
    </tr>
    <tr id="else.value">
        <th rowspan="3">else.value</th>
        <td>string</td>
        <td>Insert a string value into cell.</td>
    </tr>
    <tr>
        <td>number</td>
        <td>Insert a numeric value into cell.</td>
    </tr>
    <tr>
        <td>null</td>
        <td>Insert nothing/null value into cell.</td>
    </tr>
</table>

### Example

```json
"case": [
    {
        "if": {
            "value": {
                "endsWith": "€"
            }
        },
        "then": {
            "formatRef": "euro-blue"
        }
    },
    {
        "if": {
            "value": {
                "equalTo": 0
            }
        },
        "then": {
            "value": "",
            "picture": {
                "ref": "zero.png"
            }
        },
        "else": {
            "format": {
                "border": "none"
            }
        }
    },
    {
        "if": {
            "value": {
                "greaterThanOrEqualTo": 5000
            }
        },
        "then": {
            "format": {
                "borderColor": "Green"
            }
        }
    }
]
```
