---
title: Row
parent: Writing templates
has_children: false
nav_order: 6
---

## Row

A row can contain data, or it is a header row or a summary.

If a row is supposed to contain data, there are multiple ways to supply them:

- directly in `values` as an array or object
- as a reference to an external file by setting `path`
- as a reference to the `values` data storage of the workbook using `valuesRef`

If the source provides multiple rows of data, multiple rows will be created from that `row` object. When a row supposed to be a header row, `"type": "header"` must be set.


```json
"rows": [
    {
        "type": "header",
        "values": [ "Title", "Firstname", "Surname" ],
        "format": "bold"
    },
    {
        "path": "desktop/examples/data-blocks/data-file.xlsx",
        "fields": [ "Title", "GivenName", "Surname" ]
    }
]
```

See the complete reference: [Row Reference](/reference/row)

### Data Sources

##### 1. As array in place

`values`

A value or a list of values, that will be written into the row. A list can contain lists of values in itself, thus filling multiple rows with values.

```json
"values": [
    ["Smith", "John", "m" ],
    ["Jonson", "James", "m" ],
    ["Maxwell", "Mary", "f" ]
]
```

##### 2. Referencing data from Central Data Storage

`valuesRef`

Apart from using the `values` key and writing the data into the rows directly, there is another way of providing data. With `valuesRef`, you can reference values that are defined in the `values` property of the workbook (Central Data Storage). It is like defining variables and using them in multiple places in the template. That is especially useful with recurring values.

Another advantage to the `values` variant is that it enables the user to write templates that are reusable when the data comes in identical structure. By replacing the `values` property of the workbook, these new values will be used in those places where `valueRef` is used to pull the content of cells from there.

```json
"values": {
    "valueR1": [
        {
            "p1": "stringdata",
            "p2": 12345
        }
    ]
}

```
*definition in data storage*

```json
"rows": [
    {
        "valuesRef": "valueR1"
    }
]
```
*referencing in rows*

##### 3. Referencing an external file

`path`

With defining the path to a source excel file located in the filesystem (or in a container field), the data will appear in the output document. Possible shortcuts to common locations are: "desktop", "tmp" and "documents".

`includeFirstRow`:

Controls wether the first row from the source file appears in the target document. Set to `false` if the source contains a header row that should not appear in the resulting document.

`fields`:

Filters fields from the source that shall be in the target file. References the header names.

```json
"rows": [
    {
        "values": ["Header_1", "Header_5", "Header_6"]
    },
    {
        "path": "tmp/data-file.xlsx",
        "fields": ["field_1", "field_5", "field_6"],
        "includeFirstRow": false
    }
]
```

`limit`, `offset`:

Sometimes it is better to present data different as in vertical columns.
By chunking data into blocks and distributing it horizontically, this data can be arranged more clearly.
This can be achieved by utilizing the `pos` property combined with `limit` and `offset`.

With `pos` you can set where a set of columns is placed on the sheet.

With `limit` you set the number of rows on that position and with `offset` you set at which position in the source file to begin or continue.

```json
"rows": [
    {
        "values": ["Header_1", "Header_5", "Header_6"]
    },
    {
        "values": ["Header_1", "Header_5", "Header_6"],
        "pos": [4,0]
    },
    {
        "path": "tmp/data-file.xlsx",
        "fields": ["field_1", "field_5", "field_6"],
        "includeFirstRow": false,
        "limit": 20,
    },
    {
        "path": "tmp/data-file.xlsx",
        "fields": ["field_1", "field_5", "field_6"],
        "includeFirstRow": false,
        "pos": [4,1],
        "limit": 20,
        "offset": 20
    }
]
```

