# Workspace Task Ledger

This folder holds the cross-workspace operating index used by the static DTP
dashboard.

- `task-ledger.jsonl` is the reviewed durable task ledger.
- `dtp workspace recover --dry-run` writes review candidates to ignored
  `outputs/` files.
- `dtp workspace recover --apply --approved PATH` imports reviewed candidates
  into `task-ledger.jsonl`.
- `outputs/notion-workspace-cockpit.json` is the sanitized Notion mirror export.

Kaizen remains the lightweight intake stream. This ledger is the normalized
operating view after items are reviewed, deduped, and safe to show in the daily
cockpit.
