## Example: format-datatypes

This is a collection of different formatting options.

```json
{
	"filename": "format-datatypes.xlsx",
	"display": {
		"hideGrid": true,
		"zoom": 150
	},
	"columnWidth": -1,
	"rows": [
		{
			"values": [ "Number", "Text", "Date", "Date2", "Currency"],
			"type": "header",
			"height": 26,
			"format": {
				"fontRef": "Standard-bold",
				"pattern": 1,
				"foregroundColorRef": "lightblue",
				"alignV": 1,
				"border": 7

			}
		},
		{
			"path": "desktop/examples/format-datatypes/data-file.xlsx",
			"fields": [ "Number", "NameSet", "Birthday", "CCExpires", "MoneyGramMTCN" ],
			"height": 26,
			"type": "data",
			"formatRef": "table"
		}
	],
	"columns": [
		{
			"type": "data",
			"dataType": "number",
			"formatRef": "table",
			"format":{
				"fontref": "Courier",
				"numberFormat": 1
			}
		},
		{
			"pos": 1,
			"type": "data",
			"formatRef": "table"
		},
		{
			"pos": 2,
			"type": "data",
			"dataType": "date",
			"formatRef": "table",
			"format":{
				"fontref": "Courier",
				"numberFormat": 14
			}
		},
		{
			"pos": 3,
			"type": "data",
			"width": 20,
			"dataType": "date",
			"formatRef": "table",
			"format":{
				"fontref": "Courier",
				"numberFormat": 15
			}
		},
		{
			"pos": 4,
			"type": "data",
			"dataType": "number",
			"formatRef": "table",
			"format":{
				"fontref": "Courier",
				"numberFormat": 44
			}
		}
	],
	"fonts": {
		"Courier": {
			"fontName": "Courier",
			"fontSize": 13
		},
		"Standard": {
			"fontName": "Calibri",
			"fontSize": 13
		},
		"Standard-bold": {
			"fontRef": "Standard",
			"bold": true			
		}
	},
	"formats": {
		"table": {
			"fontRef": "Standard",
			"alignV": 1,
			"border": 7
		}
	},
	"colors": {
		"lightblue": [160,210,255],
		"red": [255,0,0]
	}
}
```

