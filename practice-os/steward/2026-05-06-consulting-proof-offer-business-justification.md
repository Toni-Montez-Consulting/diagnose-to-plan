---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Consulting Proof / Offer Pilot Business Justification

Work item: first Agent Squads + Knowledge Base V0 pilot for consulting
proof/offer movement.

Owning repo: `diagnose-to-plan`

Owning squad: Business Justification Squad

Buyer / operator: Toni Montez Consulting prospects, with Toni as operator.

Date: 2026-05-06

## Required Questions

| Question | Answer | Evidence |
|---|---|---|
| What business/operator problem is this solving? | Consulting now has clearer customer-facing positioning, but stronger public proof still needs a disciplined path so evidence improves trust without exposing private material or overclaiming. | `consulting/docs/SITE_NEXT_PASS_ROADMAP.md`; `docs/PRACTICE_PROOF_QUEUE_INDEX.md` |
| Why is this worth doing now? | PR #7 shipped the free-consultation positioning. The next quality gap is proof maturity, so the first squad pilot should happen before any public proof copy changes. | Live consulting deploy on 2026-05-06; `docs/OFFER_TO_PROOF_MATRIX.md` |
| What existing evidence supports it? | DeMario has a public-safe social proof packet with posted URLs and clear claim boundaries; the proof queue still blocks private screenshots, metrics, testimonials, admin rows, and payment data. | `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md`; `docs/PRACTICE_PROOF_QUEUE_INDEX.md` |
| What simpler alternative was considered? | Leave proof parked and make no public copy changes. That remains acceptable, but a DTP-only pilot creates reusable discipline without changing the public site. | This receipt; `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` |
| What workflow, revenue, trust, delivery, or maintenance value does it create? | It gives future agents a repeatable gate before consulting proof moves public, improving trust and reducing accidental private-data or unsupported-claim risk. | `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md` |
| What approval is needed before continuing? | Toni approval plus proof/redaction/reviewer/public-claim/copy-audit gates before any consulting public copy, screenshots, metrics, or testimonials change. | `practice-os/steward/2026-05-06-consulting-proof-offer-approval-gate.md` |

## Fit Scores

Use `0` to `3`.

| Dimension | Score | Evidence / note |
|---|---:|---|
| Operator pain is real | 3 | Public site needs proof maturity without private leakage. |
| Timing is justified | 3 | Customer-consultation PR is merged and live. |
| Evidence exists | 2 | Public-safe DeMario posting exists; consulting-page wording is not approved yet. |
| Simpler alternative was considered | 3 | Park/no-copy-change remains the fallback. |
| Workflow value is concrete | 3 | Adds a repeatable source-index and gate process. |
| Revenue or sales value is plausible | 2 | Stronger proof should improve buyer trust, but no conversion metric is claimed. |
| Trust / proof value is meaningful | 3 | Directly protects proof quality and public/private boundary. |
| Delivery value is meaningful | 2 | Helps future implementation scope proof changes cleanly. |
| Maintenance value is meaningful | 3 | Keeps consulting pointers light and DTP as source of truth. |
| Approval path is clear | 3 | Runbook and approval gate name the stops. |

## Recommendation

- Recommendation: proceed with DTP-only pilot; park public copy.
- Reason: the candidate is valuable enough to source-index, but not ready for
  consulting copy because exact public wording and claim review are not done.
- Minimum useful slice: keep DeMario as a proof candidate, attach this receipt
  set, and require future public claim review before consulting changes.
- What must not be claimed yet: bookings, revenue, conversion, student count,
  testimonials, private admin/payment proof, or broad autonomous AI claims.

## Approval

- required_approver: Toni Montez
- approval_state: pending
- approval_scope: any future consulting public proof or offer copy based on
  DeMario/Omnexus/GitHub evidence
- stop_conditions: public proof, screenshots, testimonials, metrics, private
  data, or public offer changes before gates pass

## Later ROI Closeout

Do not invent ROI in V0. Revisit after a public proof move has approved wording,
publication date, target page/component, and any real observed prospect signal.
