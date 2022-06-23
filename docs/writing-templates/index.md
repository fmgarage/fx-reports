---
title: Writing templates
nav_order: 3
has_children: true
has_toc: false
---

## Introduction to templates

Templates define the document that is supposed to be created. It describes how it looks, the data contained and where that data will appear. The template is a requirement in order to create any output with **FX Reports**. Given that writing a template from scratch requires some knowledge of the syntax, modifying an existing one to match your needs is a good option for a start.

A template needs a valid **JSON schema** as a blueprint. In that schema, allowed values and structures for building a template are defined. It specifies, for example, where columns and cells can be written or which keys and values may be defined in a format. The schema for **FX Reports** is defined in `https://github.com/fmgarage/fx-reports/blob/main/schema/fxrp-xl-v2-2-0.json`.

#### Introduction

- [Tools for writing templates]({{ 'writing-templates/tools' | relative_url }})
- [Basic structure of a template]({{ 'writing-templates/structure' | relative_url }})
- [Example, step-by-step]({{ 'writing-templates/bystep' | relative_url }})

#### Structure

- [Workbook]({{ 'writing-templates/workbook' | relative_url }})
- [Column]({{ 'writing-templates/column' | relative_url }})
- [Row]({{ 'writing-templates/row' | relative_url }})
- [Cell]({{ 'writing-templates/cell' | relative_url }})

#### Design Definitions

- [Formats]({{ 'writing-templates/formats' | relative_url }})
- [Fonts]({{ 'writing-templates/fonts' | relative_url }})
- [Pictures]({{ 'writing-templates/pictures' | relative_url }})
- [Colors]({{ 'writing-templates/colors' | relative_url }})
