---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Opportunity Private Store Boundary Receipt - 2026-05-09

## Trigger

After merging the first-wave agent, Research Arm, Opportunity OS, and Notion
mirror package, Toni approved continuing with the next item: deciding how to
handle private Opportunity OS records before returning to client lanes.

## Decision

Create a boundary decision, not a new tool choice.

Opportunity OS should not create a raw private relationship ledger, CRM,
Notion source of truth, or Hub/Supabase schema yet. V0 should prove the manual
DTP loop first with sanitized records and human-owned next actions.

## Artifacts

- `decisions/0010-opportunity-os-private-store-boundary.md`
- `docs/OPPORTUNITY_OS_V0.md`
- `docs/DOCUMENTATION_MAP.md`
- `practice-os/templates/activation-routing-map.md`

## Locked Boundaries

- DTP owns method, templates, sanitized examples, and decisions.
- Active client truth belongs in the private `engagements` lane.
- Gmail, Calendar, and meeting notes remain source evidence until summarized.
- Notion is a sanitized mirror/cockpit only.
- Consulting does not store raw opportunity or relationship records.
- No new CRM, database, schema, automation, outreach, or public proof action was
  authorized.

## Validation

- Passed: `.\.venv\Scripts\python.exe -m dtp practice doctor`.
- Passed: `git diff --check`.
