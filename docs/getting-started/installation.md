---
title: Installation
has_children: true
has_toc: false
parent: Getting Started
nav_order: 1
---

## Installation

### System requirements

- An Installation of FileMaker Pro / Server at Version 18 or higher
- MBS Plugin Version 10.0 or higher
- LibXL Version 4.0.1 or higher
> @todo

### Install MBS-plugin

FX_Reports needs the MBS-plugin. While testing though, no license is needed: it is possible to use the demo version with almost no restrictions. For download and license information, see [Monkeybread Software](https://www.monkeybreadsoftware.com/filemaker/buy/)

Find here the individual downloads:

|Version|Link|Pluginfile|
|-|-|-|
| macOS | https://fmgarage.com/download/plugins/mbs/mbs-mac.zip | MBS.fmplugin |
| Windows 64bit | https://fmgarage.com/download/plugins/mbs/mbs-win64.zip | MBS.fmx64 |
| Windows 32bit | https://fmgarage.com/download/plugins/mbs/mbs-win32.zip | MBS.fmx |
| Linux | https://fmgarage.com/download/plugins/mbs/mbs-linux.zip | MBS.xxx.fmx |

The plugin file must be copied into the FileMaker plugin directory. There is a matching file for every operating system.

Assuming no plugins have been installed before, the directory does not exist yet. Still, it will be created when clicking 'Reveal Plug-in Folder' in the FileMaker settings in the 'Plug-Ins' tab. You can then place the plugin file in the folder that has opened.

After restarting FileMaker, the plugin is shown in the 'Plug-Ins' tab in the settings. It is now ready to use.

### Install LibXL

Download:

|Version|Link|Pluginfile|
|-|-|-|
| macOS | https://fmgarage.com/download/plugins/libxl/libxl-mac.zip | libxl.dylib |
| Windows 64bit | https://fmgarage.com/download/plugins/libxl/libxl-win64.zip | libxl.dll |
| Windows 32bit | https://fmgarage.com/download/plugins/libxl/libxl-32.zip | libxl32.dll |
| Linux | https://fmgarage.com/download/plugins/libxl/libxl-linux.zip | libxl<area>.so |

For the creation of Excel-documents, the LibXL extension from version 4.0.1 upwards is needed. The library is controlled via the MBS-plugin.

Similar to the MBS-plugin, the LibXL file has to be copied to the Plugin directory of FileMaker.

### open FX_Reports

The file FX_Reports.fmp12 must not be renamed. You can open it locally or upload it to the server.

### Hosting with FileMaker Server

An appropriate license is necessary to host FX_Reports on FileMaker Server, it is not possible to do that with just the demo.

### Examples

If you want to try the examples, which is a good way to learn writing templates and generally just see what FX Reports can do, copy the `examples` folder from the repository to your desktop. Now copy the content of one of the json templates into the FX Reports editor window and hit the **Generate xlsx** button.

Or, in the [Online-Template-Editor](https://fmgarage.github.io/fx-reports/editor/), paste the example template into the field below the button **Update form** on the right and press that button. This gives you a simple example to play around with.

