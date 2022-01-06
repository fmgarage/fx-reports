---
title: Integration
has_children: true
parent: Getting Started
nav_order: 3
---

## Using the API

This article is about how you can integrate FX Reports with your own application. There are 2 ways to do that.

### 1. Using the add-on

Working from FileMaker 19

The Add-on provides the easiest way to integrate FX Reports into your application. To do that, copy the folder from inside the repositories `addon` directory into the FileMaker `AddonModules` folder.

Here is a uncomplicated way to find that folder: from the FileMaker settings, go to the Plug-ins tab and 'Reveal Plug-in Folder'. Relativ to the now open directory, go up 2 steps in the directory structure and into `Extensions`, where you will find `AddonModules`.

macOS:

`/Users/<User>/Library/Application Support/FileMaker/Extensions/AddonModules/`

Windows:

`C:\Users\<User>\AppData\Local\FileMaker\Extensions\AddonModules\`

If FileMaker has been running while copying the add-on, it must be restarted. Now, going into layout mode and switching to 'Add-ons' in the left sidebar, add-ons can be added to the application with the `+` button at the bottom. Choose "FX_Reports" in the list to add the elements necessary to talk to FX_Reports.

The add-on does not replace the FX_Reports database but merely provides a connection and simplifies the integration into an existing solution.

### Manually with copy/paste

The target file, `FX_Reports.fmp12` and `FX_ReportsExample.fmp12` must be located in the same directory or on the same server.

The file `FX_ReportsExample.fmp12` serves as blueprint and holds the elements necessary for the integration.

These elements must be added to the target file in this order:

#### Custom Functions

First copy the custom functions:

`SError.catch_v7`

`SError.display_v6`

#### Scripts

Now copy the scripts from the `FxReports` folder beneath `# Connector`:

`*FxReports.excelGenerate( $filename, $location )`

`*FxReports.excelValidate()` (optional)

The file reference to `FX_Reports.fmp12` should now be present.

#### Table: FxReports

At last, create the table occurence for `FxReports` in the target file. It must not be renamed.

> @todo describe

## Basic Usage

1. Provide the **source file**

    The source data usually comes as/from exports of the application where FX Reports is supposed to be used. These are placed in a directory of choice, the temporary folder for example; or they can be put in a container field.

    The path to the source file is then defined in `path` in the template.

2. Prepare the **template**

    The templates prepared for custom exports can be stored in fields in the application, where they can be edited before specific tasks, like setting a desired target filename or the output directory.

3. Generate the **document** with FX_Reports

    To generate the output
    - copy the template json to the container field `FxReports::a_container_`
    - call the script `*FxReports.excelGenerate( $filename, $location )`

    The file will be generated and saved at the location specified by `location` and `filename` (or by default on the desktop).
