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
- Last updated: 2026-05-11
- Reviewer: Live funnel closeout and dependency triage pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| local | 2026-05-03 | pass | current branch | `.prettierignore` now excludes `supabase/.temp/`; `pnpm verify` passed end to end: Prettier check, ESLint, build, typecheck, and tests |
| dependency | 2026-05-11 | pass | `d8478c6` | Hub PRs #74, #75, and #76 merged after remote CI/security checks passed; local `hub/main` fast-forwarded cleanly to `origin/main` |
| support | 2026-05-11 | passed_with_notes | live production | Browser consulting intake smoke created synthetic row `DTP live intake smoke 20260511T131132Z`; protected Hub dashboard verified row suffix `165e0a8e`, source `tonimontez.co`, triage version `practice-start-v1`, and status `new` by summarized fields only |
| support | 2026-05-06 | passed_with_notes | live production | Synthetic consulting intake POST returned `ok: true`; Hub dashboard verified the matching intake row by summarized fields. Receipt: `practice-os/steward/2026-05-06-consulting-live-intake-receipt.md` |
| local | 2026-04-30 | pass | cross-repo prompt lane | `hub-prompts npm test`; `hub-registry npm run validate`, `npm run validate:manifests`, `npm run validate:prompt-ids`, `npm test`; negative missing-id check failed as expected |
| CI | 2026-04-30 | pass | `ded15ad` | `ci` run `25167610722`; `security` run `25167610677`; `CodeQL` run `25167609842` |
| dependency | 2026-04-30 | pass | `8717e8e` | Hub PR #59 merged after scoped dependency-security fix `088899f`; local `pnpm install --frozen-lockfile`, `pnpm lint`, `pnpm build`, `pnpm typecheck`, `pnpm test`, `pnpm audit --prod`, and `pnpm security:secrets` passed; GitHub CI/security/CodeQL checks passed before squash merge |
| dependency | 2026-04-30 | pass | `ff7f1e4` | Hub PR #55 merged after corrective React 19 peer alignment commit `ec41263`; local install with strict peers, lint, build, typecheck, tests, strict production audit, and secret scan passed; GitHub CI/security/CodeQL checks passed before squash merge |
| release | 2026-04-30 | manual_pending | `1215995` | Vercel/Supabase live runtime checks not run in this batch |
| support | 2026-04-30 | manual_pending | `1215995` | `/health`, `/api/intake`, `/console`, and webhook smoke need live environment |
| proof | 2026-04-30 | internal_only | current branch | runtime evidence can support proof only after DTP redaction/permission review |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| Hub owns runtime support for consulting intake and console records without becoming DTP | `docs/CONSULTING_CONSOLE_FULL_STACK.md`, CI evidence, `practice-os/steward/2026-05-06-consulting-live-intake-receipt.md` | internal_only | public-safe summary only; no private row screenshots | Toni |
| Hub prompt/registry dispatch has local prompt-id cross-validation | `hub-registry/scripts/validate-prompt-ids.mjs`, local validation output | internal_only | not a public proof item | reviewed for operating use |

## Open Gaps

- Prompt id cross-validation is implemented as a local workspace gate in `hub-registry`; repo-scoped CI remains intentionally thin.
- Full portfolio manifest and prompt-id validation are local-only until CI has explicit safe access to private sibling repos.
- Dependabot PRs #59, #55, #74, #75, and #76 are merged. Current blocked PRs are #77 (`@hono/zod-openapi` 1.4.0, build-test failures) and #78 (Tailwind 4.3.0, typecheck/build-test failures). Do not merge either without a targeted Hub-local fix pass.
- Live consulting intake smoke has a controlled receipt. Cleanup remains
  structural because Hub does not expose an intake archive/delete endpoint; the
  synthetic row is clearly labeled test data and no raw private row data is
  copied into DTP.

## Notes

Hub evidence should link to DTP proof records later, but Hub should not store DTP engagement kits or become the practice roadmap owner.
