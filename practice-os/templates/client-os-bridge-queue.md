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

| Surface | Candidate action | Payload summary | Deliverable/attachment path | Draft/external id | Reviewer | Permission gate | Risk | Status |
|---|---|---|---|---|---|---|---|---|
| Gmail |  |  |  |  | Toni | draft creation allowed when recipient/source are safe; send requires explicit approval |  | pending |
| Calendar |  |  |  |  |  | confirmed time, attendees, and title required |  | pending |
| Hub |  |  |  |  |  | live mutation blocked unless separately approved |  | pending |
| Notion |  |  |  |  |  | sanitized cockpit mirror only |  | pending |

## Export Rules

- `dtp practice client-os bridge-export` is dry-run only.
- Do not send, schedule, publish, sync, or mutate external systems.
- Create Gmail drafts for client/prospect/professional email drafting when the
  connector supports it, the recipient is known, and the attachment/source is
  safe, unless Toni explicitly says to hold.
- Gmail rows that reference a packet, checklist, recap, action plan, prototype,
  or readiness review must include the attachment/source path and draft id after
  creation.
- Rows without reviewer, clear permission gate, and low-risk payload stay blocked.
- Public proof, private records, credentials, and raw transcripts are blocked.
