---
title: Cell
parent: Writing templates
has_children: false
nav_order: 7
---

## Cell

A cell is the smallest element of an excel workbook. While most properties can and often will be set on higher levels like rows or columns, they can also be adjusted per cell, if necessary.

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
    },
    {
        "pos": [3,1],
        "value": 42
    }
]
```

See the complete reference: [Cell Reference](/reference/cell)

### Values

Like in rows, cell data can be pulled from Central Data Storage with the `valueRef` key, making it easy to deal with dynamic values. Alternatively the value is written directly into the cell using the `value` key.

### Pictures

Pictures can only be set in cells. They are set by either writing directly into the cell or by using a reference to the workbook pictures repository.
