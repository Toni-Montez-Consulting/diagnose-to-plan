---
data_class: P1
confidential: false
permission_level: internal_only
review_status: template
---

# AI Operating Loop Readiness Review

Use this template when a client, internal lane, or project asks for AI,
automation, agents, governance, model orchestration, human-in-the-loop review,
or infrastructure around AI-enabled work.

This is a manual review. It does not approve public copy, compliance claims,
runtime implementation, connectors, autonomous agents, Hub changes, FAOS work,
or live system mutation.

## Review Metadata

- Review id:
- Created:
- Business / lane:
- Owner:
- Reviewer:
- Related source docs:
- Related engagement kit:
- Current autonomy level:
- Target autonomy level:
- Status: draft | reviewed | parked | promoted | rejected

## Business Outcome

- What outcome should improve:
- Who benefits:
- How the business knows it worked:
- What decision this review should make:

## Model / Tool Role

- Model, tool, agent, or automation being considered:
- What it should do:
- What it should not do:
- Current alternative without AI:
- Why AI/tooling is useful here:

## Source And Data Boundary

| Source or data type | Allowed? | Owner | Sensitivity | Handling rule |
|---|---|---|---|---|
|  | yes / no / maybe |  | public / internal / private / regulated |  |

Blocked sources:

- TBD

## Human Review Point

- What output or action needs human review:
- Who reviews it:
- What reviewer checks:
- What can proceed without review:
- What must stop until review:

## Validation / Proof Step

- What must be validated:
- Evidence source:
- Acceptance signal:
- Rejection signal:
- How false positives, bad answers, or weak outputs are caught:

## Escalation And Fallback

- When to escalate:
- Escalation owner:
- Manual fallback:
- Rollback or undo path:
- Incident / error note location:

## Failure Modes

| Failure mode | Risk | Detection | Mitigation |
|---|---|---|---|
| Wrong answer |  |  |  |
| Sensitive data exposure |  |  |  |
| Over-automation |  |  |  |
| Unclear owner |  |  |  |
| Cost or runtime surprise |  |  |  |
| Client/customer confusion |  |  |  |

## Owner Handoff

- Source of truth after handoff:
- Owner maintenance rhythm:
- Review cadence:
- What Toni supports:
- What the client / owner must own:
- Training or runbook needed:

## Safe First Action

- Recommended first artifact or workflow:
- Why it is safe:
- What it proves:
- What it does not prove:
- Next review trigger:

## Gates And No-Touch Boundaries

- [ ] No public proof or public copy without proof/redaction gates.
- [ ] No legal, compliance, privacy, security, medical, financial, or regulated
      assurance without qualified review.
- [ ] No client/customer communication without human approval.
- [ ] No live connector, OAuth, billing, database, DNS, production, ad account,
      App Store, or cloud mutation without explicit approval.
- [ ] No autonomous authority increase without Autonomy Readiness review.
- [ ] No Microsoft confidential, customer-sensitive, credential, or private
      day-job material.

## Decision Summary

- Recommended state: manual only | readiness review | draft-only workflow |
  supervised local execution | parked | rejected
- Recommended next artifact:
- Required reviewer:
- Approved scope:
- Open questions:
