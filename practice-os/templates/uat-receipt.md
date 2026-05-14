---
data_class: P0
confidential: false
permission_level: internal_only
review_status: template
---

# UAT Receipt

Use this receipt when a meaningful user journey, handoff, public surface,
operator surface, app release, AI-assisted workflow, or reusable pattern needs
acceptance evidence.

Do not paste raw private records, secrets, private screenshots, or client data
into this file. Use summarized fields and redacted evidence pointers.

## Metadata

- Work item:
- Repo / lane:
- Date:
- Operator:
- Reviewer:
- UAT type: public_route | client_handoff | admin_operator | app_release | ai_workflow | proof_surface | pattern_candidate | other
- Related requirements brief:
- Related decision ledger:
- Related Integrity Gate:
- Related proof / redaction / permission gate:

## Claim Under Review

- Claim:
- Claim level: local | preview | production | client_handoff | public_proof | app_release | internal_pattern
- What this UAT can prove:
- What this UAT cannot prove:

## Journey

- User / operator:
- Starting point:
- Main path:
- Expected outcome:
- Expected next action:

## Repo Gates

| Command or check | Required? | Result | Evidence or note |
|---|---|---|---|
|  | yes / no | pass / fail / skipped |  |

## Manual UAT

| Area | Result | Evidence or note |
|---|---|---|
| Core journey | pass / fail / skipped |  |
| Mobile / small screen | pass / fail / skipped |  |
| Desktop / wide screen | pass / fail / skipped |  |
| Error states | pass / fail / skipped |  |
| Empty states | pass / fail / skipped |  |
| Auth / permissions | pass / fail / skipped |  |
| Data / privacy | pass / fail / skipped |  |
| AI output review | pass / fail / skipped |  |
| Handoff clarity | pass / fail / skipped |  |

## Quality And Integrity

- Truth: Are claims accurate and limitations labeled?
- Usefulness: What does this help the user decide, do, understand, or operate?
- Restraint: What was intentionally not added?
- Durability: What proves this works beyond one happy-path demo?
- Handoff: Can the owner, client, operator, or future maintainer understand the result?
- AI usage, if relevant: What did AI draft or generate, and how was it reviewed?

## Evidence And Caveats

- Evidence pointers:
- Screenshots or logs, if redacted:
- Known limitations:
- Manual gates still open:
- Cleanup debt:
- Privacy / proof boundary:

## Decision

- Decision: pass | pass_with_caveats | hold | block
- Required before ship or handoff:
- Parked follow-up:
- Owner:
- Next review trigger:

## Public Proof Notes

This receipt is not public proof by itself. Public proof still requires source
evidence, permission, redaction, reviewer approval, and caveat.
