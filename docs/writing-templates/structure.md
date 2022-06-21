---
title: Basic structure of a template
parent: Writing templates
nav_order: 2
has_children: false
has_toc: false
---

## Basic structure of a template

### workbook

The highest level of the JSON template represents the workbook. That's where workbook-specific properties belong, for instance filename and output directory for the Excel file and format-, display- and print options valid for the whole workbook.

### Definitions

For elements that will be used in multiple places in the document or that may be interchangable without the need to edit the template in all the places where they appear, you can setup a catalogue with named elements.
Those elements can then be referenced by that name throughout the template.

##### values

In values, store the data that is supposed to appear in the output document. This is an alternative to pulling the data from an export xlsx file.

##### pictures

Setup pictures by path.

##### fonts

Define [fonts]({{ site.url }}/reference/font) and styles for different requirements/occasions.

##### formats

Cell [format]({{ site.url }}/reference/format) definitions similar to fonts.

### sheet [(Reference)]({{ site.url }}/reference/sheet)

Next are properties of the worksheet. These can contain format options too, as well as frozen panes or the default column definitions. Also, columns, rows and cells of that worksheet will be defined here.

### column [(Reference)]({{ site.url }}/reference/column)

In the column object, one may define format- and data properties, like column width or position.

### row [(Reference)]({{ site.url }}/reference/row)

Rows can be of type header, data or summary. Data can be saved as individual rows or referenced to a data source. Formats specific to the row also go here.

### cell [(Reference)]({{ site.url }}/reference/cell)

For single cells it is possible to define position, size, formats and content, like data or an image for instance. That way, richly designed documents featuring headlines, description texts and logos are possible to make.
