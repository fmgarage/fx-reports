## Example: data-blocks

This example demonstrates how to distribute records over two column groups. 

```json
{
    "columnWidth": -1,
    "filename": "data-blocks.xlsx",
    "display": {
        "hideGrid": true,
        "zoom": 150
    }
}
```

![Preview](Preview.png)

#### columnWidth

Adjust column width to the cells' content using `-1` as value.

#### filename

Specify output file name. Otherwise *YYMMDD_hhmmss.xslx* will be used as default.

#### display

Specify values for displayed spreadsheet

#### hideGrid

Hides the grid on the entire spreadsheet.

#### zoom

Set the zoom to 150%.

#### rows

Two rows arrays with an offset.

```json
{
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
    ]
}
```

#### values

Values array for each row.

#### formatRef

Reference to a named format.

#### pos

Position to start.
"pos": [4,0] sets the pointer to column 4 in the first row.

#### path

File path to a source file providing data.

#### fields

Name of the source fields (column headers).

#### limit

Row to stop processing the source file.

Keep in mind, the count starts at row number 0, so limiting to 13 rows will stop at row number 12.

#### offset

Row to start processing the source file.


#### formats

Named object for formats, eg "Table", "Header". They are aplied using "formatRef"

```json
"formats": {
    "Table": {
        "border": 7
    },
    "Header": {
        "formatRef": "Table",
        "bold": true,
        "backgroundColor": {"rgb": [89, 173, 255]}
    }
}
```

#### border

Sets the border style e.g "7" – hairline

#### bold

Make the content bold.

#### backgroundColor

BackgroundColor in RGB 0-255.
