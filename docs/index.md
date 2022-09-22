---
title: Home
nav_order: 1
---

## Welcome to FX Reports

**FX Reports** is a powerful extension for generating fully-featured spreadsheets in xslx format from FileMaker. It can easily be integrated into your existing solution.

### What can I achieve with it?

Exports from a FileMaker database are extremely quick to set up but also very limited – think of human readable column headers for instance. On the other end there is [LibXL](https://www.libxl.com) via the [MBS plugin](https://www.mbsplugins.eu/component_XL.shtml) where you can (and have to!) define every single detail of every cell that you want to put into your Excel file. That can be a lot of work for one output.

**FX Reports** combines both the simplicity and flexibility into a single tool. It works as a wrapper around the Excel functions of the MBS-Plugin, covering the all of the possibilities, but you can use JSON text to define the structure and content of your output file. Like Alan Kay said: *“Simple things should be simple, complex things should be possible”*.

For instance changing the column headers of a previously exported file is as easy as this:

```json
{ "rows": [
    {"values": [ "First Name", "Last Name", "Age" ]},
    {"path": "desktop/contacts.xlsx"}
]}
```

The big advantage of **FX Reports** is the way you define new export formats or edit existing ones: by just providing text - there is no need for programming.

Most of the Excel features are already supported, like

- multiple sheets
- formatting of text, numbers, dates etc.
- images

We will constantly improve the functionality of **FX Reports**, so if you have a feature request, feel free to add or comment on an issue [here](https://github.com/fmgarage/fx-reports/labels/enhancement) or start a [discussion](https://github.com/fmgarage/fx-reports/discussions).

### Support or Contact

Having trouble with implementing **FX Reports**? Not sure, if **FX Reports** matches your individual requirements? We are happy to assist, just contact us via our website, Twitter ([@fmgarage](https://twitter.com/fmgarage)) or email (support@fmgarage.com).
