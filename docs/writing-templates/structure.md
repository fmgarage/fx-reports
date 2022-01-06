---
title: Basic structure of a template
parent: Writing templates
nav_order: 2
has_children: false
has_toc: false
---

## Basic structure of a template

**document**

On the highest level of the JSON document is where document-specific properties belong. These are for instance filename and output directory for the Excel document and format-, display- and print options valid for the whole document.

**sheet**

Next are properties of the worksheet. These can contain format options too, as well as frozen panes or the default column definitions. Also, columns, rows and cells of that worksheet will be defined here.

**column**

In the column object, one may define format- and data properties, like column width or position.

**row**

Rows can be of type header, data or summary. Data can be saved as individual rows or referenced to a data source. Formats specific to the row also go here.

**cell**

For single cells it is possible to define position, size, formats and content, like data or an image for instance. That way, richly designed documents featuring headlines, description texts and logos are possible to make.

