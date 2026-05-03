---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Command Contract: /coi-screen

## Purpose

Create or update a structured conflict/compliance screen before a prospect moves
from conversation into contracting, active client work, or public proof.

## Inputs

- Prospect name and company context.
- Prospect-disclosed facts from notes, prep, or meeting artifacts.
- Current compliance source of truth: `practice-os/policies/coi-screen.md`.
- Existing COI screens if present.

## Allowed Reads

- Prospect prep artifacts.
- `practice-os/policies/coi-screen.md`
- `practice-os/skills/coi-screen/SKILL.md`
- Existing COI fixtures or private engagement screens.

## Output

One COI screen artifact in the repo's legal/compliance location or private
engagement kit. Reusable fixtures may live under
`practice-os/fixtures/business-brain/` if they contain no confidential material.

## Required Sections

- Prospect.
- Date.
- Source facts.
- Known unknowns.
- Risk checks.
- Decision: `pass`, `pass_with_conditions`, `pending_human_review`,
  `refer_out`, or `block`.
- Contracting gate.
- Follow-up questions.

## Guards

- If facts are missing, use `pending_human_review`; do not infer.
- If the screen is missing or unresolved, `/install-os` and active-client
  creation must refuse.
- Do not store internal Microsoft customer lists, partner context, roadmaps,
  code, policies, or deal context.
- Do not treat public company affiliation alone as permission to proceed.
- This is issue spotting, not legal advice.

## Acceptance Criteria

- Contracting status is unambiguous.
- Missing facts are named plainly.
- The screen can be reviewed by Toni without hunting through chat history.
- The output avoids confidential employer data.

## Fixtures

- Cameron / Deloitte side-project scenario:
  `practice-os/fixtures/business-brain/cameron-mckesson-coi-screen.md`
