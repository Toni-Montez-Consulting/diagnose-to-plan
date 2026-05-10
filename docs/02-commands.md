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
- `dtp kaizen update ID [--status now|waiting|blocked|parked|done|cancelled|superseded|discarded]`
- `dtp kaizen status [--status STATUS] [--limit N] [--json]`
- `dtp kaizen mirror --dry-run [--include-done] [--limit N]`
- `dtp evolution new "TITLE" [--kind idea|research-pattern] [--state STATE]`
- `dtp evolution status`
- `dtp evolution dashboard [--out PATH]`
- `dtp memory status`
- `dtp memory steward [--limit N]`
- `dtp workspace report [--json]`
- `dtp workspace dashboard [--surface browser|vscode] [--out PATH]`
- `dtp workspace validate-dashboard`
- `dtp workspace recover --dry-run`
- `dtp workspace recover --apply --approved PATH`
- `dtp workspace task add --title TITLE --repo REPO --status STATUS --priority P1 --next-action TEXT --source-ref REF --sensitivity internal-only --confidence high`
- `dtp web [--host 127.0.0.1] [--port 8765] [--no-open]`
- `dtp vault init [--remote PRIVATE_GIT_URL]`
- `dtp vault status`
- `dtp vault snapshot [-m MESSAGE] [--push]`

`kit`, `redact`, `practice doctor`, `kaizen`, `evolution`, `memory`, `workspace report`, `workspace dashboard`, `workspace recover`, `workspace task`, `web`, and `vault` support the Practice OS + Client Operating Kit workflow. They stay local-first and markdown-first. `dtp kaizen` is the thin continuous-improvement intake/index layer for meaningful new ideas, asks, blockers, proof candidates, repo issues, client signals, corrections, and process improvements; private/COI captures write redacted committed stubs and raw text only to ignored local `.dtp/kaizen/` state. `mirror --dry-run` emits sanitized Notion payloads, skips terminal rows by default, and blocks private/COI/secret/unreviewed proof rows. `dtp evolution new` turns reviewed or intentionally captured ideas, meta-patterns, messaging lines, and research observations into reviewable markdown records; `dtp evolution dashboard` renders the internal Practice Evolution status dashboard from those records without promoting memory, syncing Notion, touching clients, or changing public copy. `dtp memory steward` is the first active Memory Steward surface: it reads evolution records, research candidates, and open/parked Kaizen rows and emits read-only recommendations without promoting memory or writing external systems. `dtp kit new` creates the core kit docs plus a Command Room fit assessment and proof/redaction governance starter so every pilot begins with consent, evidence, permission, and public-proof gates. `dtp workspace report` is the read-only Workspace Command Center V0 report: it reads DTP-owned manifests, evidence indexes, roadmap/backlog docs, and the command-center spec, but it does not execute repo checks, call GitHub, mutate files, install skills, publish proof, touch DSE, or build FAOS. `dtp workspace dashboard` renders the task-ledger-first daily cockpit, Item Register, Archive, and Recovery Inbox as static HTML for browser or VS Code panel surfaces and writes a sanitized Notion mirror export under ignored `outputs/`. `dtp workspace validate-dashboard` writes an ignored count/source/redaction validation report. `dtp workspace recover --dry-run` scans structured DTP docs, roadmap rows, proof rows, repo-local boards, Codex session-index metadata, and memory registry pointers into ignored review artifacts; `--apply --approved PATH` imports reviewed candidates into `practice-os/workspace/task-ledger.jsonl`. `dtp workspace task add` appends a reviewed row directly to the task ledger when a candidate is already evidence-backed. `dtp web` is the local UI. `dtp vault` gives private engagement artifacts a separate git durability path without committing client records to the DTP code repo.

The production roadmap now adds a future hosted private DTP app. These commands remain the local fallback, verification, and import/export surface. See `docs/PRACTICE_PRODUCTION_ROADMAP.md`.
