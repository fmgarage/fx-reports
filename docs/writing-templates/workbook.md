---
title: Workbook
parent: Writing templates
has_children: false
nav_order: 4
---

## Workbook

The upmost level of a template represents the Excel workbook that is supposed to be created. Here, some properties can be defined that are valid throughout the workbook. Some can only be set here, others may be overridden at lower levels. For example, you can set the column width for the whole workbook to `-1` and later, for a particular column, set a specific width of `25`.

Example for a minimal template:

```json
{
    "filename": "simple-data-export.xlsx",
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

See the complete reference: [Workbook Reference]({{ '/reference/workbook' | relative_url }})

### Definitions

If some formats will be reused throughout the workbook multiple times, possibly over multiple sheets, they can be defined at this level and then behave like a library. They can then be referenced from anywhere. Elements that can be defined include fonts, formats, pictures and colors.

```json
{
    "filename": "simple-data-export.xlsx",
    "fonts": {
        "baseFont": {
            "fontName": "Source Sans Pro",
            "fontSize": 13
        }
    }
}
```

### Settings

Settings like display, print, filters or columnWidth apply to the whole workbook, and are set at the workbook level.


```json
{
    "filename": "simple-data-export.xlsx",
    "display": {
        "hideGrid": true,
        "zoom": 150
    }
}
```

### Central Data Storage

Like formats, data can be saved in a central storage and be referenced from throughout the workbook. This has the advantage of being decoupled of the source file logic when accessing certain values.

```json
{
    "values": {
        "names": [
            ["Jim", "James"],
            ["Joe", "Jackson"],
            ["James", "Joyce"]
        ]
    }
}
```

### Sheets

A workbook consists of one or more worksheets, which again consist of columns, rows and cells. If there is only one sheet in the workbook, it can be defined at the root level and doesn't need to be in a `sheets` array.

```json
{
    "sheets": [
        {
            "name": "Sheet1",
            "display": {
                "freeze": true
            },
            "columns": [...],
            "rows": [...]
        },
        {
            "name": "Sheet2",
            "columns": [...],
            "rows": [...]
        }
    ]
}
```

