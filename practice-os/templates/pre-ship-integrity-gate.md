---
data_class: P0
confidential: false
permission_level: internal_only
review_status: template
---

# Pre-Ship Integrity Gate

Use this before shipping or handing off meaningful public, client-facing,
operator-facing, AI-assisted, data-sensitive, or reusable work.

This gate does not replace repo tests, UAT, security checks, proof review, or
client approval. It asks whether the work meets the Integrity Layer standard:
truth, usefulness, restraint, durability, clarity, and clean handoff.

Tiny hotfix exception: record impact, rollback, and verification only.

## Metadata

- Work item:
- Repo / lane:
- Date:
- Reviewer:
- Gate type: launch | handoff | proof | app_release | client_delivery | internal_tool | pattern_promotion | other
- Related requirements brief:
- Related decision ledger:
- Related proof / redaction / permission gate:

## Gate Decision

- Decision: pass | pass_with_caveats | hold | block
- Caveats:
- Required before ship:
- Parked after ship:
- Owner:
- Review date:

## Truth

- [ ] Claims are accurate.
- [ ] AI behavior is not overstated.
- [ ] Known limitations are documented.
- [ ] Prototype, draft, beta, or production status is labeled honestly.
- [ ] No fake ROI, fake automation, fake certainty, or unsupported guarantee is present.
- [ ] Public or client-facing wording avoids generic hype and unsupported proof.

Notes:

## Usefulness

- [ ] The core user journey solves a real problem.
- [ ] The main screen, workflow, dashboard, or document supports a real decision or action.
- [ ] Empty states and error states help the user recover or continue.
- [ ] The next action is clear after every major step.
- [ ] The feature, doc, or workflow has a reason to exist now.

Notes:

## Quality And UAT

- [ ] UAT passed for the core flow.
- [ ] Mobile or small-screen behavior was checked where relevant.
- [ ] Error states were checked where relevant.
- [ ] Auth, permission, privacy, and data boundaries were checked where relevant.
- [ ] Telemetry, logging, or evidence exists where future decisions depend on it.
- [ ] AI outputs are reviewed, constrained, or validated where relevant.
- [ ] The evidence proves more than "the demo worked once."

Notes:

## Design Integrity

- [ ] The interface is clear under stress.
- [ ] The most important action looks like the most important action.
- [ ] Visual polish clarifies the task instead of hiding weak thinking.
- [ ] The surface is specific to this business, user, or workflow.
- [ ] Generic AI/SaaS patterns are not copied without a reason.
- [ ] Nothing is manipulative, confusing, or unnecessarily clever.

Notes:

## Handoff

- [ ] Runbook, owner note, or maintainer note exists where meaningful.
- [ ] Account, billing, credential, and ownership boundaries are clear.
- [ ] Common failure modes or breakpoints are documented.
- [ ] Future maintainer context is captured.
- [ ] The client or operator is more capable after handoff, not more trapped.
- [ ] Retainer/support value is clear and optional, not dependency by design.

Notes:

## Restraint

- [ ] No unnecessary tools were added.
- [ ] No unnecessary features were added.
- [ ] Phase 2 ideas were parked instead of forced into Phase 1.
- [ ] The simplest useful version was considered.
- [ ] Buying, simplifying, or deferring was considered when custom build work was not clearly needed.
- [ ] Complexity is not hiding unclear thinking.

Notes:

## AI Usage

- [ ] AI-generated code, copy, UI, or plans were reviewed by the builder.
- [ ] AI did not replace a needed requirements, design, security, privacy, or proof decision.
- [ ] AI-generated polish was checked against the actual user, workflow, and evidence.
- [ ] Unclear processes were clarified before automation.
- [ ] Final judgment, claims, and handoff remain human-owned.

Notes:

## Reusable Pattern Integrity

Complete this section when the work may become a reusable pattern.

- [ ] Misuse risks are named.
- [ ] Dependency risk is named.
- [ ] Simpler and safer versions are named.
- [ ] Required documentation before reuse is named.
- [ ] Proof required before promotion is named.
- [ ] Do-not-use conditions are named.

Notes:

## Final Read

- Strongest reason to ship:
- Strongest reason to hold:
- What would the stronger version of Toni do here:
- Final decision:
