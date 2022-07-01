---
title: Formats
parent: Writing templates
has_children: false
nav_order: 8
---
## Formats

Formats are visual properties that alter the appearance of a cell or the cells content.

### Example

```json
{
    "cells": [{
        "pos": [0,0, 6],
        "height": 50,
        "value": "Headline - courier, color: 'indigo', 20pt, center",
        "format": {
            "fontName": "Courier",
            "fontSize": 20,
            "bold": true,
            "fontColor": {"name": "indigo"},
            "alignV": 1,
            "alignH": 2,
            "wrap": true
        }
    }],
    "rows": [{
        "pos":3,
        "values": [ "Title", "Firstname", "Lastname", "Birthday"],
        "format": {
            "backgroundColor": {"rgb": [180, 230, 255]},
            "border": 1
        }
    }]
 }
```

### Scope

When applied to a row, column, sheet or a workbook, that format is applied to all cells that belong to that element.

### Definitions

When a particular format is used in multiple parts of a workbook, instead of adding duplicate properties to all these elements, it can be defined at a central location and then be referenced from where it is used. That minimizes the effort to implement and update formats.

The central location is the `formats` objects on the top level of the template. Formats defined here get a unique name that can be used to reference them where they are needed.

(example)

See the complete reference: [Format Reference]({{ 'reference/format' | relative_url }})
