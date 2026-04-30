---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: Engineering Playbook

## Repo

- Name: `engineering-playbook`
- Branch: `main`
- Last updated: 2026-04-30
- Reviewer: Adjacent reference/doctrine touch pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| pointer | 2026-04-30 | implemented | current branch | `.repo.yml` and `README.md` point to the DTP source-of-truth decision without moving roadmap ownership |
| policy | 2026-04-30 | implemented | current branch | `scripts/consulting-ops-check.ps1` treats FamilyTrips `CI` on `main` as a required workflow now that FamilyTrips CI exists |
| parse | 2026-04-30 | pass | current branch | PowerShell parse check for `scripts/consulting-ops-check.ps1` and `scripts/portfolio-ops-check.ps1` passed |
| local status | 2026-04-30 | pass_with_advisory | current branch | `.\scripts\portfolio-ops-check.ps1 -StatusOnly`: 29 green, 9 yellow, 0 red |
| diff hygiene | 2026-04-30 | pass | current branch | `git diff --check` passed |
| CI | 2026-04-30 | not_applicable | current branch | no engineering-playbook workflow exists by design |
| proof | 2026-04-30 | not_applicable | current branch | internal doctrine/reference repo; not a public proof source by default |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| Engineering Playbook is aligned as doctrine/reference while DTP owns current practice execution | `README.md`, `.repo.yml`, `decisions/2026-04-29-practice-roadmap-source-of-truth.md`, DTP roadmap docs | internal_reference | public proof blocked | pending |

## Open Gaps

- No repo-local GitHub workflow exists today; local checks remain the evidence for this doctrine repo.
- Portfolio ops status surfaced expected advisory context: this repo is dirty during the in-progress edit, `dse-content` is on an unrelated feature branch, hub-registry validation was skipped by `-StatusOnly`, engineering-playbook has no workflow by design, and optional/manual portfolio checks remain advisory.
- Secret inventory and 1Password checks stay value-free and should be run when env templates or vault metadata change, not for every roadmap-only touch.
- DTP remains the current practice source of truth; engineering-playbook should not grow a competing roadmap.

## Notes

This DTP-owned index is a planning receipt. It does not replace engineering-playbook's repo-local README, schemas, decision records, or secret-management guidance.
