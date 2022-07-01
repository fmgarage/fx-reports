---
title: Fonts
parent: Writing templates
has_children: false
nav_order: 9
---
## Fonts

Font options are part of [Formats](/writing-templates/formats), but can also be set in a dedicated object for convenience reasons.


### Example

```json
{
    "cells": [{
        "pos": [0,0,8],
        "height": 70,
        "value": "Headline - Arial, color: 'seagreen', 30pt, wraped",
        "format": {
            "fontRef": "Headline",
            "alignV": 2,
            "alignH": 1,
            "wrap": true
        }
    }],
    "fonts": {
        "Headline": {
            "fontSize": 30,
            "fontNmae": "Arial", 
            "bold": true,
            "fontColor": {"name": "seagreen"}
        }
    }
}
```

You can set a **font face** by name, given that this font is installed and available from the operating system.
Furthermore, you can set **size** and **color**, and the styles **bold**, **italic** and **underline**.

See the [Font Reference]({{ '/reference/font' | relative_url }}) for an example and syntax.
