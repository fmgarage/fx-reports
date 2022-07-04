---
title: Integration
has_children: false
has_toc: false
parent: Getting Started
nav_order: 3
---

## Integrate FX Reports

This article is about how you can integrate **FX Reports** with your own application. There are 2 ways to do that.

### 1. Using the Add-on

Requires FileMaker 19 and up.

The Add-on provides the easiest way to integrate **FX Reports** into your application.
On double-clicking the `FX_Reports.fmaddon` FileMaker file will install an FX_Reports folder in the AddonModules directory.

Alternatively can copy the FX_Reports `addon` folder from the repository to `AddonModules` manually.

If FileMaker has been running while copying the Add-on, it must be restarted. Now, going into layout mode and switching to 'Add-ons' in the left sidebar, Add-ons can be added to the application with the `+` button at the bottom. Choose "FX_Reports" in the list to add the elements necessary to talk to **FX Reports**.

The add-on does not replace the FX_Reports database but merely provides a connection and simplifies the integration into an existing solution.

### 2. Manually with copy/paste

The target file, `FX_Reports.fmp12` and `FX_ReportsExample.fmp12` must be located in the same directory or on the same server.

The file `FX_ReportsExample.fmp12` serves as blueprint and holds the elements necessary for the integration.

These elements must be added to the target file in this order:

#### Custom Functions

First copy the custom functions:

`SError.catch_v7`

`SError.display_v6`

#### Table: FxReports

Now create the table occurence for `FxReports` in the target file. It must not be renamed.

#### Scripts

At last, copy the scripts from the `FxReports` folder beneath `# Connector`:

`*FxReports.excelGenerate( $filename, $location )`

`*FxReports.excelValidate()` (optional)

The file reference to `FX_Reports.fmp12` should now be present.

## Basic Usage

### Provide the source data

The source data can be written directly into the template that is used to create a report or it can be provided as an xlsx export file. This file is placed in a directory of choice, the temporary folder for example; or it can be copied into a special container field.

The source file is then referenced in the template by its path.

### Prepare the template

The templates prepared for custom exports can be stored in fields in the application, where they can be edited before specific tasks, like setting a desired target filename or the output directory.

### Generate the document with FX Reports

To generate the output:
- copy the template json to the container field `FxReports::a_container_`
- call the script `*FxReports.excelGenerate()`

The file will be generated and saved at the location specified by `location` and `filename` either by parameter or as specified in the template (or by default on the desktop with a generic filename).
