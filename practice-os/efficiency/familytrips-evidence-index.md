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
| CI | 2026-04-30 | pass_with_advisory | `fd983c8` | GitHub Actions CI run `25158714066`; advisory: Node 20 JavaScript action runtime deprecation for `actions/checkout@v4` and `actions/setup-node@v4` |
| release | 2026-04-30 | manual_pending | current branch | `docs/DEPLOY_SMOKE_TEST.md` not rerun against a live deploy in this touch pass |
| privacy | 2026-04-30 | documented | current branch | `docs/PLAYBOOK.md` now points to DTP and repeats the static-bundle privacy rule |
| proof | 2026-04-30 | not_applicable | current branch | private family app; not a public proof source by default |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| FamilyTrips has a privacy-first validation lane for static trip data | `README.md`, `ARCHITECTURE.md`, `docs/PLAYBOOK.md`, local validation commands | internal_reference | public screenshots/data blocked | pending |

## Open Gaps

- CI now exists and passed; GitHub emitted an advisory Node 20 JavaScript action runtime deprecation warning for `actions/checkout@v4` and `actions/setup-node@v4`.
- Live deploy smoke was not rerun; use `docs/DEPLOY_SMOKE_TEST.md` after preview or production deploys.
- The casual privacy model is intentional but limited: unlisted routes are not authentication.
- Stronger privacy, auth, AI, or public sharing should be a separate architecture decision.

## Notes

This DTP-owned index is a planning receipt. It does not replace FamilyTrips repo-local docs, deploy smoke tests, or privacy review before sensitive data is added.
