## Example: display-and-print

This example demonstrates how to freeze panes on a spreadsheet and how to hide the grid on two different sheets.

```json
{
	"filename": "display-and-print.xlsx",
	"sheets": [
		{
			"name": "Freeze Panes",
			"display": {
				"freeze": [2, 2]
			},
			"cells": [{
				"pos": [0, 0],
				"value": "Freeze panes on position 2/2"
			}]
		},
		{
			"name": "Hidden Grid",
			"display": {
				"hideGrid": true
			},
			"cells": [{
				"pos": [0, 0],
				"value": "hide grid"
			}]
		},
		{
			"name": "Zoom",
			"display": {
				"zoom": 200
			},
			"cells": [{
				"pos": [0, 0],
				"value": "zoom 200%"
			}]
		},
		{
			"name": "Print Options",
			"cells": [
				{
					"pos": [0, 0, 5],
					"value": "print options: A4 landscape"
				},
				{
					"pos": [0, 1, 5],
					"value": "rows 0 and 1 are printed on each page"
				}
			],
			"print":{
				"paperSize": "A4",
				"landscape": true,
				"repeatRows": [0,2],
				"header":{
					"right":{
						"text": "page: {page} of {total}"
					}
				},
				"footer":{
					"left":{
						"text": "{date} {time}"
					},
					"center":{
						"text": "{filepath} {filename} {sheet}",
						"bold": true
					},
					"right":{
						"text": "page: {page} of {total}"
					}
				}
			}
		}
	]
}
```

#### filename

Specify output file name. Otherwise `YYMMDD_hhmmss.xslx` will be used as default.

#### sheets

Array of sheets. This array can be used if more than one sheet is defined.

#### name

Name of each sheet.

#### display

Default Display Options like freeze, zoom, hideGrid.

#### freeze

Freeze panes at the given position as array [column, row-number] or boolean to freeze the top-row.

#### hideGrid

Hide Grid

#### cells

Array of cells.

#### pos

Set the pointer to given position.

#### value

Set the value.

#### print

Default Print Options. Can be applied to book or sheet.

#### paperSize

Paper Size setting for printing. Set paper size by name, 'default' depends on the machine the template is processed on, this could also be different on server. Use values like 'A4', 'letter', 'legal'.

#### landscape

For printing in landscape orientation.

#### repeatRows

Repeat these row(s) as header on every printed page. If a worksheet spans more than one printed page, you can label data by adding column headings that will appear on each print page.
These labels are also known as column titles. Value con be an array, wich contains the first row and the number of rows to be repeated or just the row-position as an integer. "repeatRows":0

#### header or footer

You can add header or footer at the top or bottom of every printed page. There are three sections to place the text: **left**, **center** and **right**. 

#### **left**, **center** or **right - section**

In the section your have a 'text' object and optional formatting information like 'bold', 'fontName', 'fontSize'.

In the text you can use placeholders marked with {}

##### supported placeholders:

{page} – current pagenumber
{total} – number of all pages
{date} – current date
{time} – current time
{filepath} – file path
{filename} – file name
{sheet} – sheet title

Or style tags  – for start and stop the text style

{strike} – strikethrough
{sup} – superscript
{sub} – subscript
{underline} – single underline
{underlines} – double underline
{b} – bold
{i} – italic
