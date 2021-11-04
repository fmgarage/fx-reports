## Example: simple-header

Replace the column headers in an existing export file with custom values. 

```json
{
	"rows": [
		{"values": [ "Gender", "Language", "Title", "GivenName", "Surname"]},
		{"path": "desktop/examples/simple-header/contacts.xlsx"}
	]
}
```



#### rows

Rows array.



#### values

Values array for the first row.



#### path

File path to the file to be modified. 



### Extras



#### columnWidth

Adjust column width to the cells' content using *-1* as value.



#### format.bold

Make the column header bold.



#### includeFirstRow

When processing a source file and the target row is on pos:1 (second row), the source's first row is omitted as it usually contains column headers. If your source file's data starts in row 0 or you want to export the original headers you have to set includeFirstRow: true.

```json
{
	"columnWidth": -1,
	"rows": [{
			"values": ["Gender", "Language", "Title", "GivenName", "Surname"],
			"format": {
				"bold": true
			}
		},
		{
			"path": "desktop/examples/simple-header/contacts.xlsx",
			"includeFirstRow": true
		}
	]
}
```

