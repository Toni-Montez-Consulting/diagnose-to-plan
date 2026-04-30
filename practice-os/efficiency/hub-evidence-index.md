---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: hub

## Repo

- Name: `hub`
- Branch: `main`
- Last updated: 2026-04-30
- Reviewer: Roadmap Steward expansion pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| local | 2026-04-30 | pass | cross-repo prompt lane | `hub-prompts npm test`; `hub-registry npm run validate`, `npm run validate:manifests`, `npm run validate:prompt-ids`, `npm test`; negative missing-id check failed as expected |
| CI | 2026-04-30 | pass | `ded15ad` | `ci` run `25167610722`; `security` run `25167610677`; `CodeQL` run `25167609842` |
| dependency | 2026-04-30 | pass | `8717e8e` | Hub PR #59 merged after scoped dependency-security fix `088899f`; local `pnpm install --frozen-lockfile`, `pnpm lint`, `pnpm build`, `pnpm typecheck`, `pnpm test`, `pnpm audit --prod`, and `pnpm security:secrets` passed; GitHub CI/security/CodeQL checks passed before squash merge |
| release | 2026-04-30 | manual_pending | `1215995` | Vercel/Supabase live runtime checks not run in this batch |
| support | 2026-04-30 | manual_pending | `1215995` | `/health`, `/api/intake`, `/console`, and webhook smoke need live environment |
| proof | 2026-04-30 | internal_only | current branch | runtime evidence can support proof only after DTP redaction/permission review |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| Hub owns runtime support for consulting intake and console records without becoming DTP | `docs/CONSULTING_CONSOLE_FULL_STACK.md`, CI evidence | internal_only | public-safe summary only | pending |
| Hub prompt/registry dispatch has local prompt-id cross-validation | `hub-registry/scripts/validate-prompt-ids.mjs`, local validation output | internal_only | not a public proof item | reviewed for operating use |

## Open Gaps

- Prompt id cross-validation is implemented as a local workspace gate in `hub-registry`; repo-scoped CI remains intentionally thin.
- Full portfolio manifest and prompt-id validation are local-only until CI has explicit safe access to private sibling repos.
- Dependabot PR #59 is merged; PRs #52/#54/#55/#56 remain parked and should not be merged without separate local/remote gates and migration review.
- Live runtime checks need a controlled environment, credentials, test row cleanup, and no secret/log leakage.

## Notes

Hub evidence should link to DTP proof records later, but Hub should not store DTP engagement kits or become the practice roadmap owner.
