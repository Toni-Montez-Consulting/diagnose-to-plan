---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: fitness-app / Omnexus

## Repo

- Name: `fitness-app` / Omnexus
- Branch: `main`
- Last updated: 2026-05-01
- Reviewer: Omnexus App Store approval learning pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| local | 2026-04-30 | not_rerun | `ea6c1dca` | DTP extraction used read-only inspection; prior PR evidence recorded `npm run lint`, `npm run typecheck`, `npm run build`, `npm run db:schema:contract:local`, `npx supabase db lint --local`, and `npm run tools:verify:local` as passed |
| CI | 2026-04-29 | pass | `1347368a` | PR #553 merged after CI checks including Supabase Migration Drift, Preview/Production Verification Gate, Lint, Typecheck, Unit Tests, Quality Gate, Secret Scanning, Semgrep, Accessibility, Production Audit Gate, Dependency Review, Vercel |
| release | 2026-04-29 | pass | `ea6c1dca` | Workflow-dispatched Verification Toolkit run `25137681778` passed on `main` after the cockpit work was merged |
| support | 2026-04-30 | manual_pending | `ea6c1dca` | Scheduled Health Report runs are currently skipped; live support review was not part of this extraction pass |
| proof | 2026-04-30 | internal_only | `1347368a` | Verification cockpit is a reference implementation; public proof requires permission, redaction, reviewer, evidence source, and caveat |
| org-migration | 2026-04-30 | pass | `974f1cca` | PR #559 merged org-reference and secret-scan workflow updates; local `main` aligned to `origin/main`; represented org-migration branches deleted |
| app-store approval learning | 2026-05-01 | internal_reference | current working docs | Toni reported App Review approval; Omnexus repo now contains approval closeout, master journey, and post-approval audit docs; DTP captured a mobile app review-to-launch pattern without mutating Omnexus |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| Omnexus has a production verification cockpit that produces release evidence and separates hard gates from advisory evidence | PR #553, `.github/workflows/verification-toolkit.yml`, `scripts/ops/toolkit-registry.js`, `scripts/ops/toolkit-runner.js`, `scripts/ops/toolkit-lock.json`, `docs/engineering/production-verification-cli-stack.md`, `artifacts/verification/` convention | internal_reference | public proof pending | pending |
| Supabase fresh-replay and migration-drift checks caught and guarded a baseline migration repair | PR #553, `scripts/ci/check-migration-drift.js`, `supabase/migrations/001_full_schema.sql`, `supabase/migrations/021_schema_contract_repair.sql` | internal_reference | public proof pending | pending |
| Omnexus App Store approval journey shows a reusable mobile app review-to-launch operating pattern | `docs/HOW_OMNEXUS_WORKS.md`, `docs/store-metadata/app-store-approval-closeout-2026-05-01.md`, `docs/audit/post-approval-zero-defect-audit-2026-05-01.md`, DTP `docs/MOBILE_APP_REVIEW_AND_LAUNCH_PATTERN.md` | internal_reference | public proof pending | pending |

## Open Gaps

- Public consulting proof is blocked until a proof packet names the claim, permission, redaction status, reviewer, after-state evidence, and caveat.
- This extraction did not rerun Omnexus local gates; it used read-only repo/GitHub evidence to avoid disturbing the app repo.
- External App Store/TestFlight and production-data checks remain manual, repo-owned gates.
- Public App Store install proof and first-72-hour launch trust checks remain manual after public listing availability; do not treat App Review approval as business traction proof by itself.
- DSE remains a separate COI-aware lane and was intentionally not touched.
- GitHub Enterprise org-migration closeout is complete for Omnexus as of PR #559; future Omnexus work should start from `main`.
- Omnexus repo currently has active post-approval documentation/audit changes; DTP pattern extraction should stay read-only unless the Omnexus lane is explicitly reopened.

## Notes

This DTP-owned index is a planning receipt. It does not replace Omnexus repo-local CI, release evidence, app-store runbooks, or production verification artifacts.
