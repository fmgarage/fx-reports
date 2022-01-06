---
title: Example, step-by-step
parent: Writing templates
nav_order: 1
has_children: false
---

## An example template: step-by-step

```json
{
    "filename": "report.xlsx",
    "columnWidth": -1
}
```

Let's start with a new template and define the filename of the `xlsx` document as well as a default `columnWidth` of `-1`, meaning automatic width according to the content.

Now we define the data that should be in the table. Let's use a file with many columns from our examples: `desktop/examples/data-file/data-file.xlsx`. From that file we want to have 3 columns, `Surname`, `Centimeters` and `StreetAddress`, in the table and we want them to have the names `Name`, `Size`, and `Address`. So we add the node `rows` to the document and inside, add an array with 2 `row` objects. The first row should be of type `header` and be formatted as bold. The texts for the cells come as a list of `values`: "Name", "Size", "Address".

To get a bold header, we add the `format` key and `"bold": true` as its value.

In the second object we pull the data from the 3 determined columns out of the export file `data-file.xlsx`, which is located in the examples directory on the desktop. To do that, we write the path to the source file in `path` and list the columns we want in `fields`.

>*INFO*<br>Choosing columns with `fields` only works with properly named column headers. If no header is present, it may be worthwhile to make one and put proper names on the columns.

Since the source data spans multiple rows, multiple rows will also be created in the output by this `row` object.

Our `rows` object should look like this:

```json
    "rows": [
        {
            "type": "header",
            "values": ["Name", "Size", "Address"],
            "format": {"bold": true}
        },
        {
            "path": "desktop/examples/data-file/data-file.xlsx",
            "fields": ["Surname", "Centimeters", "StreetAddress"]
        }
    ]
```

Next up, we define the type of those 3 columns. They shall contain data and the second column only holds numbers. The datatype in the other two columns shall be text. To do that, we add a new key (or node) `columns`. Inside this node, in a sorted array, we add `column` objects that describe the columns from left to right.


```json
    "columns": [
        {"type": "data", "dataType": "text"},
        {"type": "data", "dataType": "number"},
        {"type": "data", "dataType": "text"}
    ]
```

If we do not define the datatype, it will be the same as in the source.

Let's say we are okay with the text fields being a Standard dataType like in the source file we and only need to set the number type. We only have 1 `column` object left to write, but it references a column in the middle of the document. To clarify which column is meant, we add a property that says at which position the dataType should be applied:

```json
    "columns": [{"type": "data", "dataType": "number", "pos": 2}]
```

So this is how our template should look at this point:

```json
{
    "filename": "report.xlsx",
    "columnWidth": -1,
    "rows": [
        {
            "type": "header",
            "values": ["Name", "Size", "Address"],
            "format": {"bold": true}
        },
        {
            "path": "desktop/examples/data-file/data-file.xlsx",
            "fields": ["Surname", "Centimeters", "StreetAddress"]
        }
    ],
    "columns": [{"type": "data", "dataType": "number", "pos": 1}]
}
```

Let's hit that `Generate xlsx` button to see the result of our little tutorial!

What have we accomplished to this point? We...
- pulled selected columns from a full export to a new excel document
- set custom headers for these columns
- set the dataType of a column with numbers accordingly

