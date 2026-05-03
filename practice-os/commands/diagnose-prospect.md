---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Command Contract: /diagnose-prospect

## Purpose

Produce a meeting-prep package that helps Toni enter a prospect or advisor
conversation with a clear read, strong questions, risk gates, and a next action.

## Inputs

- Prospect name.
- Existing notes, prep files, chat summaries, URLs supplied by Toni, and prior
  artifacts.
- Relevant proof/comms rules from `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md`.
- Existing COI or permission notes when available.

## Allowed Reads

- `practice-os/fixtures/business-brain/`
- `practice-os/skills/diagnose/SKILL.md`
- `practice-os/templates/diagnose-memo.md`
- `practice-os/policies/coi-screen.md`
- user-supplied local notes
- public web facts only if explicitly verified during the run

## Output

One meeting-prep artifact in the repo's current prep or fixture convention. If
the prospect is private or live, write to ignored `engagements/` or a private
vault unless Toni explicitly authorizes a reusable fixture.

## Required Sections

- What this is.
- Current read.
- What works.
- Highest-value gaps.
- Recommended conversation sequence.
- Questions to ask.
- Risks / gates.
- Proposed next action.
- Follow-up artifact to draft.
- Skill/template capture candidates.

## Guards

- Mark missing facts as `missing_context`; do not invent them.
- For Builder-path opportunities, preserve Operator-path as the flagship.
- If public web claims matter, verify them or mark them `unverified`.
- Do not include employer confidential information.
- Do not imply that case-study rights, pricing, or public naming are approved
  unless a source file says they are approved.

## Acceptance Criteria

- Output is skimmable before a meeting.
- It separates recommendations from open questions.
- It names at least one next artifact.
- It flags COI, permission, or proof gates when present.
- It produces at least one skill/template capture candidate.

## Fixtures

- Greg / TheGrantApp.io: `practice-os/fixtures/business-brain/greg-thegrantapp-diagnose-prospect.md`
- Cameron / M&A platform: `practice-os/fixtures/business-brain/cameron-mckesson-diagnose-prospect.md`
