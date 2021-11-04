## Example: picture-logo

This example demonstrates how to place images in cells, as a logo on top or as icons in the datarows.

```json
	"cells": [
		{
			"pos": [0,0],
			"picture": {
				"ref": "logo",
				"width": 227,
				"height": 60,
				"position": "resize"
			}
		}
	],
    "pictures": {
		"logo": "desktop/examples/picture-logo/fx-reports.png",
		"suitcase": "desktop/examples/picture-logo/suitcase.png"
	}
```


#### picture

Place an image in the cell defined in `pos`. `ref` points to the file reference.
`width`, `height` and `position` define the dimensions and scaling behaviour.



#### pictures

Set a reference for each used image and a link to the file. use the reference throughout the template to place the image.


