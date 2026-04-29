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
- Reviewer: Toni/operator review pending

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| local | 2026-04-29 | pass | current branch | `pytest`, `ruff check .`, `dtp skills --validate`, `dtp practice doctor` |
| CI | 2026-04-29 | pass | `1519ed4` | GitHub Actions DTP CI |
| release | 2026-04-29 | manual_pending | current branch | targeted redaction checks required for changed docs/templates |
| support | 2026-04-29 | not_applicable | current branch | hosted DTP not implemented |
| proof | 2026-04-29 | manual_pending | current branch | proof/redaction templates now define required review fields |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| DTP now has a private hosted-DTP Phase 0 boundary | `docs/HOSTED_DTP_PHASE_0.md` | internal_only | public-safe doc review required | pending |
| DTP now has proof/redaction queue templates | `practice-os/templates/` | internal_only | public-safe template review required | pending |

## Open Gaps

- Hosted DTP app implementation is intentionally not started.
- Proof/redaction templates need first use on Mom nonprofit or another pilot.
- Repo manifest/evidence index shape needs review before expanding to consulting, Hub, or `tm-skills`.

## Notes

This index is a pilot artifact. It does not replace GitHub Actions, local validation output, or future hosted DTP evidence records.
