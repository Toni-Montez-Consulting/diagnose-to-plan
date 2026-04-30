---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: FamilyTrips

## Repo

- Name: `FamilyTrips`
- Branch: `main`
- Last updated: 2026-04-30
- Reviewer: Adjacent project privacy-first touch pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| data | 2026-04-30 | pass | current branch | `npm run validate:data`: validated 5 trip data files |
| static | 2026-04-30 | pass | current branch | `npm run lint` passed |
| unit | 2026-04-30 | pass | current branch | `npm run test`: 1 test file / 11 tests passed |
| build | 2026-04-30 | pass | current branch | `npm run build` passed with Vite production output |
| release | 2026-04-30 | manual_pending | current branch | `docs/DEPLOY_SMOKE_TEST.md` not rerun against a live deploy in this touch pass |
| privacy | 2026-04-30 | documented | current branch | `docs/PLAYBOOK.md` now points to DTP and repeats the static-bundle privacy rule |
| proof | 2026-04-30 | not_applicable | current branch | private family app; not a public proof source by default |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| FamilyTrips has a privacy-first validation lane for static trip data | `README.md`, `ARCHITECTURE.md`, `docs/PLAYBOOK.md`, local validation commands | internal_reference | public screenshots/data blocked | pending |

## Open Gaps

- No confirmed repo CI gate in this touch pass.
- Live deploy smoke was not rerun; use `docs/DEPLOY_SMOKE_TEST.md` after preview or production deploys.
- The casual privacy model is intentional but limited: unlisted routes are not authentication.
- Stronger privacy, auth, AI, or public sharing should be a separate architecture decision.

## Notes

This DTP-owned index is a planning receipt. It does not replace FamilyTrips repo-local docs, deploy smoke tests, or privacy review before sensitive data is added.
