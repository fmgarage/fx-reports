## Example: display-and-print

This example demonstrates how to split the spreadsheat and how hide the grid on two different sheets. 

```json
{
	"filename": "display-and-print.xlsx",
	"sheets": [{
			"name": "Split",
			"split": [2, 2],
			"cells": [{
				"pos": [0, 0],
				"value": "Split on position 2/2"
			}]
		},
		{
			"name": "Hidden Grid",
			"display": {
				"hideGrid": true
			},
			"cells": [{
				"pos": [0, 0],
				"value": "hide grid"
			}]
		}
	]
}
```



#### filename

Specify output file name. Otherwise *YYMMDD_hhmmss.xslx* will be used as default. 

#### sheets

Array of sheets.

#### name
Name of each sheet.

#### split

Split the sheet at the givven position.

#### cells

Array of cells.

#### pos

Set the pointer to given position.

#### value

Set the value.

