### Example: format-borders

This example shows how to format borders.

Borders are a `"format"` property:

```json
"format": {
	"border": "medium",
	"borderColor": {"rgb": [0,50,50]}
}
```

#### border

`"border"` means all borders of a cell. Assigned with the style `"medium"`.

#### borderColor

`"borderColor"` can be a RGB-Color

#### other border types

You can address a border directly:

* borderBottom
* borderLeft
* borderRight
* borderTop

and also the Border Color:

* borderBottomColor
* borderLeftColor
* borderRightColor
* borderTopColor

Additionally you can define a cell diagonal

* borderDiagonal

#### borderDiagonalMode

Besides the style and the color, you need to determine the mode for the diagonal with `borderDiagonalMode`.

Possible values are `"none"`, `"up"`, `"down"` or `"both"`.

```json
"format": {
	"borderDiagonal": "dashed",
	"borderDiagonalColor": {"name": "red"},
	"borderDiagonalMode": "hair"
}
```

Note that the same line style looks thicker on the diagonals than on the borders.
