---
title: Document
parent: Writing templates
has_children: false
---

## Document/Workbook

The upmost level of a template represents the Excel document that is supposed to be created. Here, some properties can be defined that are valid throughout the document. Some can only be set here, others may be overridden at lower levels. For example, you can set the column width for the whole document to `-1` and later, for a particular column, set a specific width of `25`.

Example for a minimal template:

```json
{
    "filename": "simple-data-export.xlsx",
    "name": "sheet1",
    "columnWidth": -1,
    "rows": [
        {
            "values": ["Last Name", "First Name", "Gender"]
        },
        {
            "values": ["Waldherr", "Nils", "m"]
        }
    ]
}
```
> @todo name ist ein sheet value, könnte hier verwirren?

### filename

Filename of the excel file to be created. If not set, the default will be `[date]+[time].xlsx`.

### location

> @todo Wenn field: nur Container? FxReports::a_tmp_[1] sieht aus wie Wiederholfeld?

Where the export file should be saved. Can be a path in the filesystem or a (container)field in a FileMaker table. If not set, the default will be the folder `fx_reports` on the desktop.

### name

Name of the worksheet. Default: sheet[n]

### columns

List of columns.
See [Column]({{ site.baseurl }}{% link writing-templates/column.md %})

### rows
List of rows.
See [Row]({{ site.baseurl }}{% link writing-templates/row.md %})


### cells
List of cells.
See [Cell]({{ site.baseurl }}{% link writing-templates/cell.md %})


### display

**hideGrid**: boolean value

show or hide grid

**zoom**: integer between 25 and 400

Zoom view

```json
"display": {
    "hideGrid": true,
    "zoom": 150
}
```

### format


### columnWidth

-1: auto

### print