# Commands

Current command surface:

- `dtp draft INPUT_PATH`
- `dtp skills --validate`
- `dtp note "TEXT"`
- `dtp story TITLE`
- `dtp mentor WHAT`
- `dtp index [REPO|--all]`
- `dtp detect REPO --signal SIGNAL`
- `dtp lesson REPO --pattern PATTERN [--from PATH]`
- `dtp recall QUERY [--type pattern|lesson|decision|synthesis]`
- `dtp synthesize [--no-confirm]`
- `dtp kit new CLIENT --project SLUG --kind audit|launch|operating-system|assistant`
- `dtp kit status [CLIENT]`
- `dtp redact check PATH --profile practice|client|case-study`
- `dtp practice doctor`

`kit`, `redact`, and `practice doctor` support the Practice OS + Client Operating Kit workflow. They stay local-first and markdown-only: no backend, no CRM, no cockpit app.
