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
- Last updated: 2026-04-30
- Reviewer: accepted by steward review on 2026-04-30

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| local | 2026-04-30 | pass | current branch | `hub-prompts npm test`; `hub-registry npm run validate`, `npm run validate:manifests`, `npm run validate:prompt-ids`, `npm test`; DTP `pytest`, `ruff check .`, `dtp skills --validate`, `dtp practice doctor`, `dtp workspace report`, `dtp workspace report --json`; Workspace Command Center blocker carry-forward test/report, including Omnexus review gate, parked Hub dependency PRs, Mom owner facts, DSE no-touch, and FAOS parked |
| local | 2026-04-30 | pass | current branch | GitHub organization ownership alignment: local remotes, manifests, roadmap surfaces, and `hub-registry` targets updated for `Toni-Montez-Consulting`; `dse-content` intentionally excluded; targeted redaction and DTP validation passed |
| CI | 2026-04-29 | pass | `dd359db` | GitHub Actions DTP CI before this workspace-report batch |
| release | 2026-04-30 | pass_with_note | current branch | targeted redaction checks passed for changed docs/templates; broad `docs/` scan still has a pre-existing `docs/build-spec-v2.md` email finding |
| support | 2026-04-30 | not_applicable | current branch | hosted DTP not implemented; Workspace Command Center V0 is recorded-artifact-only |
| proof | 2026-04-30 | manual_pending | current branch | proof/redaction templates define required review fields; public proof remains blocked |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| DTP now has a private hosted-DTP Phase 0 boundary | `docs/HOSTED_DTP_PHASE_0.md` | internal_only | steward review accepted | reviewed |
| DTP now has proof/redaction queue templates | `practice-os/templates/` | internal_only | steward review accepted | reviewed |

## Open Gaps

- Hosted DTP app implementation is intentionally not started.
- Public proof still needs permission, redaction, reviewer, evidence, and caveat gates.
- Workspace Command Center V0 reports recorded artifacts only; live git/CI reads and command execution remain later. Missing repo rows may carry explicit Active Next Queue blockers without inferring gates.
- Repo manifest/evidence index shape now covers DTP, consulting, Hub, `hub-prompts`, `hub-registry`, `tm-skills`, DeMario, FamilyTrips, engineering-playbook, and `fitness-app` / Omnexus. `dse-content` remains missing until its lane is clean or explicitly selected with COI-aware scope.

## Notes

This index is a pilot artifact. It does not replace GitHub Actions, local validation output, or future hosted DTP evidence records.
