---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Opportunity Notion Mirror Design Receipt - 2026-05-09

## Trigger

Toni approved the order: first package the DTP branch, then define the Notion
mirror shape for the Research Arm and Opportunity OS before deciding any future
private storage layer.

## Decision

DTP remains the source of truth. Notion can become a sanitized mirror/cockpit
for research and opportunity review, but it is not the private relationship
ledger, CRM replacement, autonomous outreach system, or public-proof source.

## Artifacts

- `docs/RESEARCH_AND_OPPORTUNITY_NOTION_MIRROR_V0.md`
- `docs/NOTION_MIRROR_V0.md`
- `docs/DOCUMENTATION_MAP.md`
- `practice-os/templates/activation-routing-map.md`

## Locked Boundaries

- No live Notion writes happened in this pass.
- No Gmail, calendar, client communication, or public proof action happened.
- No raw client replies, transcripts, contact details, or sensitive relationship
  notes belong in the Notion mirror.
- Seed rows are sanitized examples only until Toni approves a live Notion pass.
- Any future private store decision must be made after the manual DTP + Notion
  loop proves which fields matter.

## Validation

- Passed: `.\.venv\Scripts\python.exe -m dtp practice doctor`.
- Passed: `git diff --check`.
