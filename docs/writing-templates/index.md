---
title: Writing templates
nav_order: 30
has_children: true
---

## Introduction to templates

Templates define the document that is supposed to be created. It describes how it looks, the data contained and where that data will appear. The template is a requirement in order to create any output with FX_Reports. Given that writing a template from scratch requires some knowledge of the syntax, modifying an existing one to match your needs is a good option for a start.

A template needs a valid **JSON schema** as a blueprint. In that schema, allowed values and structures for building a template are defined. It specifies, for example, where columns and cells can be written or which keys and values may be defined in a format. The schema for  FX Reports is defined in `https://fmgarage.com/schemas/json2excel/v2-1-0.json`.
> @todo

## Tools for writing templates

Templates are written as JSON documents. The syntax, or the schema, is easy to learn. A good way to start is examining the examples (folder `examples`) from the FX_Reports folder.