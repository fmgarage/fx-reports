## Example: simple-header

In this example the column headers from an existing export file wil be replaced with custom values. The first row is set manually with a *values* array. Beginning with the following one all rows of the source file specified by *path* are written to the output file. The first row of the source file is skipped by deafult as it generally contains column headers. If you need this row to be processed, add an *includeFirstRow: true* to the row object. 

You can easily improve your output file by making the header row bold, auto-adjust the column width and even rearrange or filter the input file's columns using the *fields* array.

Tip: if place a copy of the *examples* folder on your desktop all example code and snippets from this readme will run without error.



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

File path to a source file providing data.



### Extras



#### columnWidth

Adjust the column width to the cells' content using `-1` as value.

```json
{
  "columnWidth": -1,
  "rows": [{"values": [ "Gender", "Language", "Title", "GivenName", "Surname"]}]
}
```

#### format.bold

Make the column header bold.

```json
{
  "rows": [
    {
      "values": ["Gender", "Language", "Title", "GivenName", "Surname"],
      "format": { "bold": true }
    }
  ]
}
```




#### includeFirstRow

When processing a source file and the target row is on pos:1 (second row), the source's first row is omitted as it usually contains column headers. If your source file's data starts in row 0 or you want to export the original headers you have to set `includeFirstRow: true`.

```json
{
  "rows": [
    {
      "values": ["Gender", "Language", "Title", "GivenName", "Surname"]
    },
    {
      "path": "desktop/examples/simple-header/contacts.xlsx",
      "includeFirstRow": true
    }
  ]
}
```



#### fields

By specifying column headers of the source file you can rearrange and even filter columns.

```json
{
  "rows": [{
      "values": ["Lastname", "Firstname"]
    },
    {
      "path": "desktop/examples/simple-header/contacts.xlsx",
      "fields": ["Contact::b_lastname", "Contact::b_firstname"]
    }
  ]
}
```

