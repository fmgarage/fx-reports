## Example: data-blocks

This example demonstrates how to split the Source file in two parts.

```json
{
	"columnWidth": -1,
	"filename": "data-blocks.xlsx",
	"display": {
		"hideGrid": true,
		"zoom": 150
	},
```

#### columnWidth

Adjust column width to the cells' content using *-1* as value.

#### filename

Specify output file name. Otherwise *YYMMDD_hhmmss.xslx* will be used as default. 


#### display

Specify values for displayed spreadsheet


#### hideGrid

Hides the grid on the entire spreadsheet.

#### zoom

Set the zoom to 150%.



```json
	"rows": [
		{
			"values": [ "Title", "Firstname", "Surname"],
			"formatRef": "Header"
		},
		{
			"pos": [4,0],
			"values": [ "Title", "Firstname", "Surname"],
			"formatRef": "Header"
		},
		{
			"path": "desktop/examples/data-blocks/data-file.xlsx",
			"fields": [ "Title", "GivenName", "Surname"],
			"limit": 13,
			"formatRef": "Table"
		},
		{
			"pos": [4,1],
			"path": "desktop/examples/data-blocks/data-file.xlsx",
			"fields": [ "Title", "GivenName", "Surname"],
			"offset": 13,
			"formatRef": "Table"
		}		
	],
```

#### rows
Two rows arrays with with an offset.

#### values
Values array for each row.

#### formatRef
Reference to a named format . 

#### pos
Position to start. 
"pos": [4,0] sets the pointer to column 4 in the first row.

#### path
File path to the file to be modified. 

#### fields
Name of the source fields (column headers).

#### limit
Row to stop processing the source file.

#### offset
Row to start processing the source file.



```json
	"formats": {
		"Table": {
			"border": 7
		},
		"Header": {
			"formatRef": "Table",
			"bold": true,
			"backgroundColorRgb": [89, 173, 255]
		}
	}
}
```





#### formats
Named object for formats, eg "Table", "Header". They are aplied using "formatRef"


#### border
Sets the border style e.g "7" hairline 

#### bold
Make the content bold.

#### backgroundColorRgb
BackgroundColor in RGB 0-255.