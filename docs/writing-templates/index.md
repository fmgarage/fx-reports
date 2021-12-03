---
title: Writing templates
has_children: true
---

## Introduction to templates

Templates define the document that is supposed to be created. It describes how it looks, the data contained and where that data will appear. The template is a requirement in order to create any output with FX_Reports. Given that writing a template from scratch requires some knowledge of the syntax, modifying an existing one to match your needs is a good option for a start.

A template needs a valid **JSON schema** as a blueprint. In that schema, allowed values and structures for building a template are defined. It specifies, for example, where columns and cells can be written or which keys and values may be defined in a format. The schema for  FX Reports is defined in `https://fmgarage.com/schemas/json2excel/v2-1-0.json`.
> @todo

## Tools for writing templates

Templates are written as JSON documents. The syntax, or the schema, is easy to learn. A good way to start is examining the examples (folder `examples`) from the FX_Reports folder.

### Using the Online-Editor

Our [Online-Template-Editor](https://fmgarage.github.io/fx-reports/editor/) serves as a comfortable way to create templates with a graphical interface.

> *Tip*<br>Paste one of the examples into the JSON field to the right and click "Update Form".

### Using VSCode

With VSCode comes the option to define a schema for certain files or directories. This means we can add our json2excel schema for template files. Either we give all our templates a unique file extension or we just assign the schema to all files with a `.json` extension in a specific folder where we save our templates.

#### Configure VSCode

We need to edit the `settings.json` for that and there are 2 ways to open the file:

1. Using the mouse
- open Settings UI with <kbd>⌘ Command</kbd> + <kbd>,</kbd> / <kbd>Strg</kbd> + <kbd>,</kbd> or via app menu
- in `Extensions/JSON/JSON: Schemas` click `Edit in settings.json`
- the file opens

2. Using keyboard shortcuts
- open commands with <kbd>F1</kbd>
- search for `Open Settings (JSON)`
- the file opens

Inside the outermost curly brackets, at the last position (with a comma after the preceding entry, because now comes a new one), we add the following:

```json
"json.schemas": [
    {
        "fileMatch": [
            "examples/**/*fxrpxl.json",
            "custom/**/*fxrpxl.json"
        ],
        "url": "./schema/fxrp_excel_v2.schema.json"
    }
]
```

In the `fileMatch` array, we name the filename pattern and - when necessary - the path, where the schema should be used. The mask for the name can be choosen freely. When done, save the file.

Now, when we edit a json file matching that pattern, the valid keys and values are shown inside the doublequotes.

<img src="{{ site.baseurl }}/assets/images/vsc-schema-1.png" style="magin-bottom: 20px;">

### Test a template

(Paste the template into the editor window of FX Reports, click `Generate xlsx` and check the output.)
> @todo das ist das normale Vorgehen beim Erstellen

## Basic structure of a template

**document**

On the highest level of the JSON document is where document-specific properties belong. These are for instance filename and output directory for the Excel document and format-, display- and print options valid for the whole document.

**sheet**

Next are properties of the worksheet. These can contain format options too, as well as frozen panes or the default column definitions. Also, columns, rows and cells of that worksheet will be defined here.

**column**

Here, format- and data properties, like column width or position, are defined.
> @todo satz umstellen

**row**

Rows can be of type header, data or summary. Data can be saved as individual rows or referenced to a data source. Formats specific to the row also go here.

**cell**

For single cells it is possible to define position, size, formats and content, like data or an image for instance. That way, richly designed documents featuring headlines, description texts and logos are possible to make.

## An example template: step-by-step

```json
{
    "filename": "report.xlsx",
    "columnWidth": -1
}
```

Let's start with a new template and define the filename of the `xlsx` document as well as a default `columnWidth` of `-1`, meaning automatic width according to the content.

Now we define the data that should be in the table. From a table with many columns we want to have 3, `data_name`, `data_age` and `data_adress`, in the table and we want them to have the names `Name`, `Age`, and `Address`. So we add the node `rows` to the document and inside, add an array with 2 `row` objects. The first row should be of type `header` and be formatted as bold. The texts for the cells come as a list of `values`: "Name", "Age", "Address".

To get a bold header, we add the `format` key and `"bold": true` as its value.

