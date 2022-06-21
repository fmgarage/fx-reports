---
title: Tools for writing templates
parent: Writing templates
nav_order: 1
has_children: false
has_toc: false
---

## Tools for writing templates

Templates are written as JSON documents. The syntax, or the schema, is easy to learn. A good way to start is examining the examples (folder `examples`) from the FX_Reports folder.

### Using the Online-Editor

Our [Online-Template-Editor](https://fmgarage.github.io/fx-reports/editor/) serves as a comfortable way to create templates with a graphical interface.

> *Tip*<br>Paste one of the examples into the JSON field to the right and click "Update Form".

### Using VS Code

With **VS Code** comes the option to define a schema for certain files or directories. This means we can add our schema for template files. Either we give all our templates a unique file extension or we just assign the schema to all files with a `.json` extension in a specific folder where we save our templates.

#### Configure VS Code

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
        "url": "https://raw.githubusercontent.com/fmgarage/fx-reports/main/schema/fxrp-xl-v2-2-0.json"
    }
]
```

In the `fileMatch` array, we name the filename pattern and - when necessary - the path, where the schema should be used. The mask for the name can be choosen freely. When done, save the file.

Now, when we edit a `json` file matching that pattern, the valid keys and values are shown inside the doublequotes.

<img src="{{ site.baseurl }}/assets/images/vsc-schema-1.png" style="magin-bottom: 20px;">

