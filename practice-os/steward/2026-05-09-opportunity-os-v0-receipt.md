---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
---

# Opportunity OS V0 Receipt - 2026-05-09

## Trigger

Toni clarified that the relationship system should eventually be mirrored in
Notion and have durable source material in consulting and DTP markdown, with a
more robust persistence layer later.

## Decision

Create Opportunity OS V0 as a method and data-boundary spec now, but do not
create real private relationship records yet.

## Boundary

Accepted:

- DTP owns the method, score model, template, and steward receipts.
- Consulting can hold public-safe pointers and future launcher language.
- Notion can mirror sanitized cockpit fields.
- A future private store can persist real relationship/opportunity records when
  justified.

Rejected:

- Notion as source of truth.
- The public/deploy-adjacent consulting repo as raw relationship database.
- Automated outreach, lead scoring, or follow-up.

## Artifacts Added

- `docs/OPPORTUNITY_OS_V0.md`
- `practice-os/templates/opportunity-os-record.md`

## Next Pilot

Create 3-5 sanitized test records with generic labels before entering real
names. Use those to test whether the fields, scoring, and capacity guard work.

## Validation

Pending after implementation:

- `dtp practice doctor`
- `git diff --check`
