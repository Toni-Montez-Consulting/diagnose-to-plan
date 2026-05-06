---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Approval Gate

Use this whenever a squad-run story could continue into public proof, client
communication, production writes, repo mutation, pricing/offer changes, private
data handling, live integrations, or write-enabled automation.

## Gate Metadata

- Work item:
- Owning repo:
- Owning squad:
- Gate category:
- Date opened:

## Approval Fields

- required_approver:
- approval_state: not_required / pending / approved / rejected / blocked
- approval_scope:
- approved_by:
- approved_at:
- evidence:

## Stop Conditions

Set explicit stop conditions before work continues.

- Public proof:
- Client communication:
- Production writes:
- Repo mutation:
- Pricing / public offer posture:
- Private data handling:
- Live integration / connector:
- Write-enabled automation:
- Other:

## Required Evidence

| Evidence | Path / URL | Required before approval? | Status |
|---|---|---|---|
| Source index |  | yes/no |  |
| Business justification |  | yes/no |  |
| Proof/redaction review |  | yes/no |  |
| Repo-local verification |  | yes/no |  |
| Owner/client permission |  | yes/no |  |

## Decision

- Decision: approved / rejected / blocked / not required
- Reason:
- Scope allowed:
- Scope still blocked:
- Revisit trigger:

## Closure

- Closed by:
- Closed at:
- Follow-up receipt:
