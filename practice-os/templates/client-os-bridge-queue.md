---
data_class: P0
confidential: false
permission_level: internal_only
review_status: template
---

# Client OS Bridge Queue

Use private client-specific copies to prepare dry-run action rows for connector
surfaces. This template does not authorize live sends, scheduling, publishing,
syncing, or production writes.

## Queue Metadata

- Client/lane:
- Engagement:
- Meeting date:
- Automation authority: draft_only
- Mode: dry_run_only
- External writes: blocked

## Bridge Queue

| Surface | Candidate action | Payload summary | Reviewer | Permission gate | Risk | Status |
|---|---|---|---|---|---|---|
| Gmail |  |  |  |  |  | pending |
| Calendar |  |  |  |  |  | pending |
| Hub |  |  |  |  |  | pending |
| Notion |  |  |  |  |  | pending |

## Export Rules

- `dtp practice client-os bridge-export` is dry-run only.
- Do not send, schedule, publish, sync, or mutate external systems.
- Rows without reviewer, clear permission gate, and low-risk payload stay blocked.
- Public proof, private records, credentials, and raw transcripts are blocked.
