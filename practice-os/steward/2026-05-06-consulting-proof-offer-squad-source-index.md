---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Consulting Proof / Offer Pilot Source Index

Work item: first Agent Squads + Knowledge Base V0 pilot for consulting
proof/offer movement.

Owning repo: `diagnose-to-plan`

Owning squads: Delivery Squad, Business Justification Squad

Date: 2026-05-06

Prepared by: Codex

## Source-Of-Truth Order

| Rank | Source | Path or URL | Why it is authoritative | Freshness / drift risk |
|---|---|---|---|---|
| 1 | Agent Squads V0 model | `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` | Defines V0 squad ownership, source-index discipline, gates, first pilot, and DTP ownership | New draft; revisit after first repeated receipts |
| 2 | Proof queue | `docs/PRACTICE_PROOF_QUEUE_INDEX.md` | Owns proof-candidate status before consulting copy changes | Medium; proof status can change after permission/review |
| 3 | Public proof runbook | `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md` | Defines evidence, permission, redaction, reviewer, caveat, and copy-audit path | Low; policy surface |
| 4 | Offer matrix | `docs/OFFER_TO_PROOF_MATRIX.md` | Connects proof candidates to offer posture and what cannot be claimed | Medium; offer language can evolve |
| 5 | DeMario proof packet | `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md` | Current public-safe packet with posted URLs and claim boundaries | Medium; future screenshots, testimonials, or metrics need separate review |

## Repo Sources Used

| Repo | Path | Purpose | Notes |
|---|---|---|---|
| `diagnose-to-plan` | `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` | Confirms consulting proof/offer squad pilot routing | DTP owns receipt |
| `diagnose-to-plan` | `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md` | Candidate evidence for first proof/offer pilot | Public-safe social posting only |
| `consulting` | `docs/SITE_NEXT_PASS_ROADMAP.md` | Confirms consulting proof gap is evidence/case-study maturity, not more design complexity | Use after consulting PR #7 customer-positioning merge |
| `consulting` | `docs/POSITIONING_BRIEF.md` | Confirms customer-facing offer, audience, CTA, and portfolio posture | Do not replace with internal proof language |

## Private Sources

| Source | Allowed? | Reason | Redaction / privacy note |
|---|---|---|---|
| Raw booking/admin/payment records | no | Not needed for this pilot | Blocked from public proof |
| Private screenshots/testimonials | no | Separate proof/redaction review required | Keep out of this receipt |
| Public LinkedIn/Instagram post URLs recorded in DTP packet | yes | Existing public-safe evidence record | Use only as source pointer, not expanded claim |

## External Sources

| Source | URL | Use | Dependency? |
|---|---|---|---|
| LinkedIn post URL | `https://www.linkedin.com/posts/toni-montez_vibecoding-ai-share-7457778664995434496-_YWO` | Public proof pointer already recorded in DTP packet | no |
| Instagram reel URL | `https://www.instagram.com/reel/DX_7B34AKFK/` | Public proof pointer already recorded in DTP packet | no |

## Blocked Sources

Do not use:

- private admin rows;
- student names, emails, phone numbers, lesson notes, or payment records;
- screenshots with private data;
- unsupported booking, revenue, conversion, student-count, or impact metrics;
- private Hub rows, prompts, webhook records, or console screenshots;
- any claim that implies autonomous tools built or run the business.

## Knowledge Gaps

- Exact consulting page/component target is not chosen yet.
- Public claim review has not approved exact consulting-site wording.
- Copy authenticity audit has not been run for a consulting-page proof update.

## Revisit Trigger

Reopen this source index when a proof packet moves to `approved_public_safe`,
when Toni chooses a public target page/component, when new evidence appears, or
when consulting public copy is ready to move.
