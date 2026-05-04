---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Kaizen Kanban Index

This folder is the thin intake and routing layer for the consulting operating
system. It exists so new ideas, asks, blockers, repo issues, proof candidates,
client replies, corrections, and process improvements do not live only in chat
memory.

Use the CLI first:

```powershell
.\.venv\Scripts\python.exe -m dtp kaizen capture "Capture the new request here"
.\.venv\Scripts\python.exe -m dtp kaizen update kzn-YYYYMMDD-slug-hash --status now
.\.venv\Scripts\python.exe -m dtp kaizen status --limit 5
.\.venv\Scripts\python.exe -m dtp kaizen mirror --dry-run --limit 100
```

## Files

- `intake.jsonl`: append-friendly machine-readable records. Each line is one
  stable Kaizen record with ID, type, sensitivity, owning repo, status, DTP
  source path, Notion target, and next action.
- `.dtp/kaizen/private-intake.jsonl`: ignored local-only raw private capture
  storage. The committed index must contain only redacted private/COI stubs.

## Rules

- DTP is the source of truth.
- Notion is a sanitized cockpit and inbox mirror.
- Captures stay lightweight until steward review promotes them to a backlog
  story, steward receipt, proof packet, decision record, engagement kit,
  research item, or parked item.
- Private client material, COI-sensitive work, secrets, raw transcripts,
  financial details, and unreviewed proof stay out of Notion payloads.
- Private/COI captures must never write raw text to the committed index.
