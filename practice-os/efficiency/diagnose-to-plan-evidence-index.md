---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: diagnose-to-plan

## Repo

- Name: `diagnose-to-plan`
- Branch: `v2/harness`
- Last updated: 2026-04-29
- Reviewer: accepted by steward review on 2026-04-29

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| local | 2026-04-29 | pass | `9ca0848` | `pytest`, `ruff check .`, `dtp skills --validate`, `dtp practice doctor` |
| CI | 2026-04-29 | pass | `9ca0848` | GitHub Actions DTP CI |
| release | 2026-04-29 | pass | `9ca0848` | targeted redaction checks passed for changed docs/templates |
| support | 2026-04-29 | not_applicable | current branch | hosted DTP not implemented |
| proof | 2026-04-29 | manual_pending | current branch | proof/redaction templates now define required review fields |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| DTP now has a private hosted-DTP Phase 0 boundary | `docs/HOSTED_DTP_PHASE_0.md` | internal_only | steward review accepted | reviewed |
| DTP now has proof/redaction queue templates | `practice-os/templates/` | internal_only | steward review accepted | reviewed |

## Open Gaps

- Hosted DTP app implementation is intentionally not started.
- Proof/redaction templates need first live use on Mom nonprofit or another pilot.
- Repo manifest/evidence index shape is accepted for the next expansion to consulting, Hub, and `tm-skills`.

## Notes

This index is a pilot artifact. It does not replace GitHub Actions, local validation output, or future hosted DTP evidence records.
