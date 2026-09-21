# Claude Skills for FX Reports

[Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) teach Claude how to do a specific job. The skills in this folder make Claude a competent author of **FX Reports** templates: it knows the schema, starts from working examples, and validates every template before handing it to you.

| Skill | What it does |
|---|---|
| [`fx-reports-template`](fx-reports-template/) | Write, extend, debug and validate FX Reports templates (JSON), including the FileMaker side: script call, passing data via `values`, export-then-generate. |

A skill is just a folder with a `SKILL.md` plus reference files and scripts. Nothing is installed on your machine apart from that folder; have a look inside before you use it.

> Claude cannot run FX Reports. It can prove that a template is valid against the schema, but how the xlsx *looks* (picture sizes, fonts, page breaks) still needs a test run in FileMaker.


## Install in Claude (claude.ai, desktop and mobile apps)

Requires *Code execution and file creation* to be enabled (Settings → Capabilities). On Team and Enterprise plans an owner may have to allow skills for the organization first.

1. Get the skill as a zip file: download this repository (Code → Download ZIP) and zip the folder `skills/fx-reports-template`, or on the command line:
   ```
   git clone https://github.com/fmgarage/fx-reports.git
   cd fx-reports/skills
   zip -r fx-reports-template.zip fx-reports-template
   ```
   The zip must contain the folder `fx-reports-template` with `SKILL.md` directly inside it.
2. In Claude open **Customize → Skills**, click **+**, choose to upload a skill and select the zip.
3. Make sure the skill is switched on in the list.

To update, upload the new zip again and replace the existing skill.

See also: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).


## Install in Claude Code

Claude Code reads skills from the file system – no upload needed.

**Personal** (available in all your projects):

```
git clone https://github.com/fmgarage/fx-reports.git
mkdir -p ~/.claude/skills
cp -r fx-reports/skills/fx-reports-template ~/.claude/skills/
```

**Per project** (commit it, and everyone working in that repository gets it):

```
mkdir -p .claude/skills
cp -r /path/to/fx-reports/skills/fx-reports-template .claude/skills/
```

If you keep a clone of this repository around, a symlink instead of `cp -r` lets updates flow through with `git pull`:

```
ln -s "$(pwd)/fx-reports/skills/fx-reports-template" ~/.claude/skills/fx-reports-template
```

Start a new Claude Code session afterwards. The validator needs Python 3 and one package:

```
pip install jsonschema
```

See also: [Extend Claude with skills](https://code.claude.com/docs/en/skills).


## Using it

There is nothing to call. Claude picks the skill up by itself when you talk about FX Reports templates, for example:

- *"I export my contacts to tmp/contacts.xlsx with the fields … Build an FX Reports template with proper headers, revenue as a number with two decimals, a frozen bold header row and A4 landscape."*
- *"I want to pass the invoice rows from a FileMaker script as JSON instead of exporting a file. Show me the template and the script call."*
- *"Why does FX Reports reject this template?"* followed by your JSON.

In Claude Code you can also run the validator yourself:

```
python3 ~/.claude/skills/fx-reports-template/scripts/validate.py my-template.fxrpxl.json
```

It checks the template against the JSON schema and, beyond that, whether every `formatRef`, `fontRef`, color, picture and `valuesRef` points to something that exists.


## Feedback

Found a template that validates but fails in FX Reports, or advice from the skill that turned out wrong? Please open an [issue](https://github.com/fmgarage/fx-reports/issues).
