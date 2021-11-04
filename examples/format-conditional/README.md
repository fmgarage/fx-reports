## Example: format-conditional

```json
{
	"filename": "format-conditional.xlsx",
	"display": {
		"hideGrid": true,
		"zoom": 150
	},
	"columnWidth": -1,
	"rows": [
		{
			"type": "header",
			"values": [ "equalTo 10", "greaterThan 10", "greaterThanOrEqualTo 10",  "lessThan 10", "lessThanOrEqualTo 10", "beginsWith \"G\"/endsWith \")\"", "contains \"p\"", "containsAny [\"0\",\"1\"]", "containsAll [\"0\",\"1\"]" ],
			"format": {
				"bold": true,
				"backgroundColorRef": "Lightblue",
				"border": 7

			}
		},
		{
			"path": "desktop/examples/format-conditional/data-file.xlsx",
			"fields": [ "Number", "Number", "Number", "Number", "Number", "NameSet", "CountryFull", "StreetAddress", "StreetAddress" ],
			"formatRef": "Table"
		}
	],
	"columns": [
		{
			"type": "data",
			"dataType": "number",
			"case": {
				"if": {
					"value": { "equalTo": 10 }
				},
				"then": {
					"formatRef": "Table-red"
				}
			}
		},
		{
			"type": "data",
			"dataType": "number",
			"case": {
				"if": {
					"value": { "greaterThan": 10 }
				},
				"then": {
					"formatRef": "Table-red"
				}
			}
		},
		{
			"type": "data",
			"dataType": "number",
			"case": {
				"if": {
					"value": { "greaterThanOrEqualTo": 10 }
				},
				"then": {
					"formatRef": "Table-red"
				}
			}
		},
		{
			"type": "data",
			"dataType": "number",
			"case": {
				"if": {
					"value": { "lessThan": 10 }
				},
				"then": {
					"formatRef": "Table-red"
				}
			}
		},
		{
			"type": "data",
			"dataType": "number",
			"case": {
				"if": {
					"value": { "lessThanOrEqualTo": 10 }
				},
				"then": {
					"formatRef": "Table-red"
				}
			}
		},
		{
			"type": "data",
			"case": [
				{
					"if": {
						"value": { "beginsWith": "G" }
					},
					"then": {
						"formatRef": "Table-red"
					}
				},
				{
					"if": {
						"value": { "endsWith": ")" }
					},
					"then": {
						"formatRef": "Table-blue"					}
				}
			]
		},
		{
			"type": "data",
			"case": {
				"if": {
					"value": { "contains": "p" }
				},
				"then": {
					"formatRef": "Table-red"
				}
			}
		},
		{
			"type": "data",
			"case": {
				"if": {
					"value": { "containsAny": ["0","1"] }
				},
				"then": {
					"formatRef": "Table-red"
				}
			}
		},
		{
			"type": "data",
			"case": {
				"if": {
					"value": { "containsAll": ["0","1"] }
				},
				"then": {
					"formatRef": "Table-red"
				}
			}
		}
	],
	"formats": {
		"Table": {
			"border": 7
		},
		"Table-blue": {
			"formatRef": "Table",
			"fontColorRef": "Blue"
		},
		"Table-red": {
			"formatRef": "Table",
			"fontColorRef": "Red"
		}
	},
	"colors": {
		"Lightblue": [160,210,255],
		"Blue": [0,80,170],
		"Red": [255,0,0]
	}
}
```



### Properties

#### filename

Specify output file name. Otherwise *YYMMDD_hhmmss.xslx* will be used as default. 



#### equals

case-insensitive



#### contains