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
- `dtp kaizen capture "TEXT" [--type auto] [--status inbox]`
- `dtp kaizen update ID [--status now|waiting|blocked|parked|done]`
- `dtp kaizen status [--status STATUS] [--limit N] [--json]`
- `dtp kaizen mirror --dry-run [--include-done] [--limit N]`
- `dtp workspace report [--json]`
- `dtp workspace dashboard [--surface browser|vscode] [--out PATH]`
- `dtp web [--host 127.0.0.1] [--port 8765] [--no-open]`
- `dtp vault init [--remote PRIVATE_GIT_URL]`
- `dtp vault status`
- `dtp vault snapshot [-m MESSAGE] [--push]`

`kit`, `redact`, `practice doctor`, `kaizen`, `workspace report`, `web`, and `vault` support the Practice OS + Client Operating Kit workflow. They stay local-first and markdown-first. `dtp kaizen` is the thin continuous-improvement intake/index layer for meaningful new ideas, asks, blockers, proof candidates, repo issues, client signals, corrections, and process improvements; private/COI captures write redacted committed stubs and raw text only to ignored local `.dtp/kaizen/` state. `mirror --dry-run` emits sanitized Notion payloads, skips `done` by default, and blocks private/COI/secret/unreviewed proof rows. `dtp kit new` creates the core kit docs plus a Command Room fit assessment and proof/redaction governance starter so every pilot begins with consent, evidence, permission, and public-proof gates. `dtp workspace report` is the read-only Workspace Command Center V0 report: it reads DTP-owned manifests, evidence indexes, roadmap/backlog docs, and the command-center spec, but it does not execute repo checks, call GitHub, mutate files, install skills, publish proof, touch DSE, or build FAOS. `dtp workspace dashboard` renders that same cross-workspace state as static HTML for browser or VS Code panel surfaces without changing the source-of-truth boundary. `dtp web` is the local UI. `dtp vault` gives private engagement artifacts a separate git durability path without committing client records to the DTP code repo.

The production roadmap now adds a future hosted private DTP app. These commands remain the local fallback, verification, and import/export surface. See `docs/PRACTICE_PRODUCTION_ROADMAP.md`.
