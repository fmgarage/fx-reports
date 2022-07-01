---
title: Colors
parent: Writing templates
has_children: false
nav_order: 11
---

## Colors

Different elements, like column headers in the workbook can be highlighted with colors. Color is part of [Formats](/writing-templates/formats). A color can be set as an RGB value or a colorname defined by Excel can be used.

See the complete reference: [Color Reference]({{ '/reference/color' | relative_url }})

### Examples

```json
"rows": [{
    "values": [ "Title", "Firstname", "Lastname", "Birthday"],
    "format": {
        "fontSize": 13,
        "bold": true,
        "fontColor":{"name": "plum"}
        "backgroundColor": {"rgb": [180, 230, 255]}
	}
}]
```

### Definitions

If a color is used in several formats, it can be defined at a central location and then be referenced from
where it is used. That minimizes the effort to implement and update.
