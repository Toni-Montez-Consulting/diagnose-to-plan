---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Consulting Intelligence Fixture Set

Use these fixtures to test whether the Business Brain is getting sharper at
diagnosis, scoping, proof safety, follow-up quality, handoff quality, and Toni's
operator voice.

This fixture set is public-safe by design. It should point to private
engagement kits only by sanitized lane name unless a future proof review
approves more detail.

## Lanes

| Lane | Fixture role | Current proof posture |
|---|---|---|
| Cameron / SMB marketplace | diagnosis, scope shaping, COI-aware sales support | internal only |
| Greg / TheGrantApp | case-study proposal, discovery clarity, proof permission | internal only |
| CCAAP | owner-action extraction, launch blockers, family/private boundary | internal only |
| Omnexus | mobile launch evidence, verification tooling, founder/operator proof | internal only |
| DeMario | local business launch handoff and command-room reference | owner-safe only |
| DSE | internal/professional proof candidate | COI-gated |

## Eval Families

- Diagnosis quality.
- Scope shaping.
- COI and permission routing.
- Proof safety.
- Follow-up quality.
- Handoff quality.
- Operator voice.
- Anti-slop review.
- Evidence dossier depth.
- Memory correction and source promotion.

## Machine-Readable Seed

- `eval-cases.json` stores the first fixture seed for future automated evals.
- `eval-cases.md` remains the human-readable version for weekly resets.
- The first real misfire seed is evidence-dossier depth: shallow synthesis with
  too few source/memory citations should become a correction checklist, source
  sweep, and claim ledger instead of another short summary.

## Promotion Rule

When a real session exposes a good or bad answer, create a small fixture here
or in the owning prompt/skill repo. Do not copy private raw material. Use the
correction checklist and proof/redaction templates before anything public.
