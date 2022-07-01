---
title: Pictures
parent: Writing templates
has_children: false
nav_order: 10
---

## Pictures

Pictures are imported by entering a path to the image in the filesystem.

### Issues

Positioning and sizing is a bit of a trial and error process. This unfortunately is a characteristic of Excel and cannot be overridden with FX Reports.

The developer of LibXL recommends using width/height in pixel over scale.

When changing the width and height of a picture and preserving the aspect ratio, the result can still be a little off. This can be controlled by reading the scale values of that picture in Excel.
You will have to adjust the width/height values until the desired result is achieved.

This behaviour also seems to be inconsistent across operating systems and Excel versions.

See the complete reference: [Picture Reference]({{ '/reference/picture' | relative_url }})
