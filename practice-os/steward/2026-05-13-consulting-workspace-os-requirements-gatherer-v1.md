---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Consulting Workspace OS, Requirements Gatherer, And Integrity Layer Receipt

## Session

- Date: 2026-05-13
- Steward: Codex
- Trigger: Toni asked to implement the DTP Workspace OS + Requirements Gatherer V1 plan, then approved adding the Integrity Layer / Craft Standard and first pre-ship gate.
- Owning repo: `diagnose-to-plan`
- Source artifact: `docs/CONSULTING_WORKSPACE_OS_V0.md`
- Kaizen record: `kzn-20260514-consulting-workspace-os-plus-requi-c4c54796`
- Integrity add-on Kaizen record:
  `kzn-20260514-add-integrity-layer-craft-standard-f3dffe29`

## Scope Implemented

- Added a DTP-owned Workspace OS plan that preserves the Consulting Workspace OS
  email idea as an internal operating system, not a new public product.
- Added Requirements Gatherer V1 as a first-class module with tiered discovery,
  question batching, escalation, output, memory, and override rules.
- Added the first requirements artifacts:
  `practice-os/templates/requirements-gathering-brief.md` and
  `practice-os/templates/requirements-decision-ledger.md`.
- Added Integrity Layer V0 as the quality standard underneath the Workspace OS:
  `practice-os/policies/integrity-layer-craft-standard.md`.
- Added the first integrity artifact:
  `practice-os/templates/pre-ship-integrity-gate.md`.
- Kept `tm-skills` as the future skill surface only after the DTP protocol is
  reviewed once.

## Boundaries Preserved

- No public consulting-site copy changed.
- No app or runtime code changed.
- No Hub intake route changed.
- No hosted DTP behavior changed.
- No global skill install or `tm-skills` file changed.
- No client communication, proof publication, calendar, billing, production, or
  database action was taken.

## Pattern Pilot

Consulting remains the first pilot. The initial pattern scan should look at:

- live `/start` funnel to Hub intake;
- post-submit Diagnostic Call path;
- noindex `/admin` command-room boundary;
- public proof posture and redaction gates;
- visual QA and live readiness receipts;
- DTP source-of-truth boundary over Hub runtime evidence;
- labeled synthetic intake cleanup debt.

## Next Actions

1. Use Requirements Gatherer on the next three meaningful requests and record
   whether the tier estimate feels right.
2. Apply the Pre-Ship Integrity Gate to meaningful public, client-facing,
   operator-facing, AI-assisted, data-sensitive, or reusable work before ship.
3. Run the consulting pilot pattern scan before adding UAT Kit or tool registry
   modules, and include Integrity Layer questions before pattern promotion.
4. After one reviewed DTP cycle, decide whether to create a `tm-skills`
   Requirements Gatherer skill with trigger evals.

## Review Trigger

- Toni says the gatherer is too heavy, too light, or still not asking enough.
- A large product, UI, backend, business, or client request enters Deep or
  Workshop discovery.
- The consulting pilot scan produces reusable pattern candidates.
