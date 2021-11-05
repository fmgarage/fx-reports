## Example: data-file

This example demonstrates how to change the header and field order from a given export. 

```json
{
	"columnWidth": -1,
	"rows": [
		{"values": [ "Title", "Firstname", "Surname", "Gender", "Language"]},
		{
			"path": "desktop/examples/data-file/data-file.xlsx",
			"fields": [ "Title", "GivenName", "Surname", "Gender", "NameSet" ]
		}
	]
}
```

#### columnWidth
Adjust column width to the cells' content using *-1* as value.

#### rows
Two rows arrays with with an offset.

#### values
Values array for the first row.

#### path
File path to the file to be modified. 

#### fields
Name of the source fields (column headers).

