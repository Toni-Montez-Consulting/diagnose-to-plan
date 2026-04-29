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
- `dtp web [--host 127.0.0.1] [--port 8765] [--no-open]`
- `dtp vault init [--remote PRIVATE_GIT_URL]`
- `dtp vault status`
- `dtp vault snapshot [-m MESSAGE] [--push]`

`kit`, `redact`, `practice doctor`, `web`, and `vault` support the Practice OS + Client Operating Kit workflow. They stay local-first and markdown-first. `dtp web` is the local UI. `dtp vault` gives private engagement artifacts a separate git durability path without committing client records to the DTP code repo.
