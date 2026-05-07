---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Consulting Proof / Offer Pilot Approval Gate

Work item: first Agent Squads + Knowledge Base V0 pilot for consulting
proof/offer movement.

Owning repo: `diagnose-to-plan`

Owning squad: Business Justification Squad

Gate category: public proof and consulting offer copy.

Date opened: 2026-05-06

## Approval Fields

- required_approver: Toni Montez
- approval_state: pending
- approval_scope: exact public consulting proof/offer wording, target surface,
  approved assets, and caveats
- approved_by:
- approved_at:
- evidence:
  - `practice-os/steward/2026-05-06-consulting-proof-offer-squad-source-index.md`
  - `practice-os/steward/2026-05-06-consulting-proof-offer-business-justification.md`
  - `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md`

## Stop Conditions

- Public proof: blocked until proof packet, public claim review, copy audit, and
  target surface are complete.
- Client communication: blocked unless Toni reviews the exact message.
- Production writes: not in scope.
- Repo mutation: consulting mutation is blocked until a future scoped PR uses
  approved wording/assets only.
- Pricing / public offer posture: blocked unless Toni approves the exact
  positioning change.
- Private data handling: blocked; no private admin, booking, payment, student,
  Hub, or dashboard records.
- Live integration / connector: not in scope.
- Write-enabled automation: not in scope.
- Other: no unsupported metrics, testimonials, revenue, conversion, booking, or
  autonomous-tool claims.

## Required Evidence

| Evidence | Path / URL | Required before approval? | Status |
|---|---|---|---|
| Source index | `practice-os/steward/2026-05-06-consulting-proof-offer-squad-source-index.md` | yes | complete for DTP-only pilot |
| Business justification | `practice-os/steward/2026-05-06-consulting-proof-offer-business-justification.md` | yes | complete for DTP-only pilot |
| Proof/redaction review | `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md` plus candidate packet | yes | not complete for consulting copy |
| Repo-local verification | future consulting PR checks | yes | not started |
| Owner/client permission | proof-packet-specific approval | yes | public-safe social packet exists; broader consulting use pending |

## Decision

- Decision: blocked for public copy; approved for DTP-only pilot receipt.
- Reason: the source and business case are strong enough to organize, but exact
  consulting copy has not gone through public claim review or copy audit.
- Scope allowed: DTP receipt creation, source indexing, business justification,
  and future-agent routing.
- Scope still blocked: public consulting copy, screenshots, metrics,
  testimonials, case-study claims, and offer changes.
- Revisit trigger: Toni chooses a consulting target surface and asks to promote
  a specific proof claim or asset.

## Closure

- Closed by:
- Closed at:
- Follow-up receipt:
  `practice-os/steward/2026-05-06-consulting-proof-offer-squad-handoff-receipt.md`
