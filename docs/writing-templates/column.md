---
title: Column
parent: Writing templates
has_children: false
nav_order: 5
---

## Column

In a `column` object, properties like width, position and format are set. Further, the data type can be defined. 

```json
{
    "type": "data",
    "pos": 3,
    "width": -1,
    "dataType": "number",
    "format": {
        "bold": true
    }
}
```

See the complete reference: [Column Reference](/reference/column)

### Data Types

The `dataType` key is used to define the type of data that a column holds. The possible types are `text`, `number`, `date`, `timestamp`,`blank`, `formula`. When setting the data type, it will be applied to the data cells by default. If necessary, this can be changed with the `type` key. The options here are `header`, `data` and `summary`.
