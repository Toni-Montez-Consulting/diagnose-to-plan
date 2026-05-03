---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Command Contract: /draft-proposal

## Purpose

Draft a one-page proposal based on a diagnosed prospect, selected engagement
shape, and any COI/proof constraints.

## Inputs

- Prospect brief.
- Selected offer shape: Audit, Operating System, AI Assistant, Launch Sprint,
  case-study engagement, advisor-only, or parked.
- COI screen status.
- Case-study rights preference when applicable.
- Pricing source if Toni has approved one.

## Allowed Reads

- Prospect brief.
- `practice-os/skills/proposal-draft/SKILL.md`
- `practice-os/templates/case-study-capture.md`
- `practice-os/policies/coi-screen.md`
- Existing proposal fixtures.

## Output

One proposal draft in the current proposal/pipeline location. If the prospect is
live/private, write to ignored `engagements/` or private vault; if it is a
reusable fixture, write under `practice-os/fixtures/business-brain/`.

## Required Sections

- Situation.
- Recommended scope.
- Deliverables.
- Out of scope.
- Timeline.
- Success criteria.
- Access needed.
- Terms to decide.
- Case-study / naming rights if applicable.
- Next step.

## Guards

- Do not quote price unless pricing source or user approval exists.
- Do not promise outcomes without data.
- Do not include public case-study rights without explicit approval language.
- Keep Builder-path exceptions scoped; do not turn them into the flagship.
- Use operator voice, not generic AI consulting copy.

## Acceptance Criteria

- Proposal can be lightly edited and sent within 48 hours.
- It names what Toni will not do.
- It includes handoff/proof expectations where relevant.
- It does not overclaim technical validation, revenue impact, or public rights.

## Fixtures

- Greg case-study proposal:
  `practice-os/fixtures/business-brain/greg-thegrantapp-case-study-proposal.md`
