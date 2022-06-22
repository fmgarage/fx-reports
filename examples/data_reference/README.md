## Example: data-reference

This example shows another way to provide datavalues that can be referenced in the template. By adding your json data-array with a name (here 'myContacts') to *values*, it will be accessible throughout the template when using the `valuesRef` key (or `valueRef` in a cell) .

```json
{
	"filename": "data-reference.xlsx",
	"columnWidth": -1,
	"rows": [
		{
			"values": ["Last Name", "First Name", "Gender"]
		},
		{
			"valuesRef": "myContacts"
		}
	],
	"values": {
		"myContacts": [
			["Waldherr", "Nils", "m"],
			["Smith", "John", "m" ],
			["Jonson", "James", "m" ],
			["Maxwell", "Mary", "f" ],
			["McNeil", "Leila", "f" ],
			["Smithers", "Jim", "m" ]
		]
	}
}
```

#### filename

Specify output file name. Otherwise *YYMMDD_hhmmss.xslx* will be used as default.

#### columnWidth

Adjust column width to the cells' content using *-1* as value.

#### rows

Rows array.

#### rows.values

Array of values. Each item of the array corresponds to a column value in the row.

#### rows.valuesRef

Reference to the central value storage.

#### values

Central value storage for values that can be referenced by name in the template.
