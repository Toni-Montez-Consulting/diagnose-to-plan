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
- Last updated: 2026-05-03
- Reviewer: Omnexus App Store closeout evidence pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| billing support alert | 2026-05-03 | active_manual_gate | local runbook update pending | Gmail alert reported Stripe disabled a live webhook endpoint shown as the root domain; live smoke confirmed `https://omnexus.fit/api/health` returns 200, `GET /api/webhook-stripe` returns 405, and unsigned `POST /api/webhook-stripe` returns 400 signature failure; likely next fix is Stripe Dashboard endpoint update/re-enable/replay, not app-route code |
| live proof checklist | 2026-05-01 | pass_with_manual_gates | `deceade8` | `docs/ops/post-approval-live-proof-checklist.md` added and linked from README, Launch Guide, ops docs, post-approval audit, and post-App-Store roadmap; Security Ops run `25198820007`, Build iOS run `25198820004`, and Semgrep run `25198820015` passed; manual proof capture starts on or after 2026-05-02 |
| local | 2026-05-01 | pass | `65d9ea44` | `npm run typecheck`; `npx vitest run api/export-data.test.ts api/delete-account.test.ts`; `npm run ios:submission-lint:strict`; `npm run verify:local`; `npm run security:secrets`; `git diff --check` |
| CI | 2026-05-01 | pass | `65d9ea44` | GitHub Actions CI run `25198605657` passed after push to `main`; conditional branch/preview/dev jobs were skipped by workflow rules, not failures |
| native | 2026-05-01 | pass_with_advisory | `65d9ea44` | Build iOS run `25198605656` passed, exported/signed the IPA, uploaded artifacts, and uploaded to TestFlight; advisory remains for Node 20 action deprecation before the 2026 runner transition |
| security | 2026-05-01 | pass | `65d9ea44` | Security Ops run `25198605663` passed Production Audit Gate; local `npm run security:secrets` scanned with no leaks found |
| semgrep | 2026-05-01 | pass | `65d9ea44` | Semgrep run `25198605662` completed successfully on `main` |
| approval closeout | 2026-05-01 | pass_with_manual_gates | `65d9ea44` | Omnexus App Store approval closeout docs, zero-defect audit docs, and export-data parity fix were committed and pushed to `Toni-Montez-Consulting/Omnexus`; public App Store install, first-device smoke, provider, support, analytics, and billing proof remain manual on or after 2026-05-02 |
| local | 2026-04-30 | not_rerun | `ea6c1dca` | DTP extraction used read-only inspection; prior PR evidence recorded `npm run lint`, `npm run typecheck`, `npm run build`, `npm run db:schema:contract:local`, `npx supabase db lint --local`, and `npm run tools:verify:local` as passed |
| CI | 2026-04-29 | pass | `1347368a` | PR #553 merged after CI checks including Supabase Migration Drift, Preview/Production Verification Gate, Lint, Typecheck, Unit Tests, Quality Gate, Secret Scanning, Semgrep, Accessibility, Production Audit Gate, Dependency Review, Vercel |
| release | 2026-04-29 | pass | `ea6c1dca` | Workflow-dispatched Verification Toolkit run `25137681778` passed on `main` after the cockpit work was merged |
| support | 2026-04-30 | manual_pending | `ea6c1dca` | Scheduled Health Report runs are currently skipped; live support review was not part of this extraction pass |
| proof | 2026-04-30 | internal_only | `1347368a` | Verification cockpit is a reference implementation; public proof requires permission, redaction, reviewer, evidence source, and caveat |
| org-migration | 2026-04-30 | pass | `974f1cca` | PR #559 merged org-reference and secret-scan workflow updates; local `main` aligned to `origin/main`; represented org-migration branches deleted |
| app-store approval learning | 2026-05-01 | pass_with_manual_gates | `65d9ea44` | Toni reported App Review approval; Omnexus repo now contains approval closeout, master journey, post-approval audit docs, and export-data coverage alignment; DTP captured a mobile app review-to-launch pattern while preserving public proof gates |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| Omnexus has a production verification cockpit that produces release evidence and separates hard gates from advisory evidence | PR #553, `.github/workflows/verification-toolkit.yml`, `scripts/ops/toolkit-registry.js`, `scripts/ops/toolkit-runner.js`, `scripts/ops/toolkit-lock.json`, `docs/engineering/production-verification-cli-stack.md`, `artifacts/verification/` convention | internal_reference | public proof pending | pending |
| Supabase fresh-replay and migration-drift checks caught and guarded a baseline migration repair | PR #553, `scripts/ci/check-migration-drift.js`, `supabase/migrations/001_full_schema.sql`, `supabase/migrations/021_schema_contract_repair.sql` | internal_reference | public proof pending | pending |
| Omnexus App Store approval journey shows a reusable mobile app review-to-launch operating pattern | commit `65d9ea44`, `docs/HOW_OMNEXUS_WORKS.md`, `docs/store-metadata/app-store-approval-closeout-2026-05-01.md`, `docs/audit/post-approval-zero-defect-audit-2026-05-01.md`, DTP `docs/MOBILE_APP_REVIEW_AND_LAUNCH_PATTERN.md` | internal_reference | public proof pending | pending |

## Open Gaps

- Public consulting proof is blocked until a proof packet names the claim, permission, redaction status, reviewer, after-state evidence, and caveat.
- Public App Store install proof and first-72-hour launch trust checks remain manual after public listing availability on or after 2026-05-02; do not treat App Review approval as business traction proof by itself.
- External App Store, real-device, provider, support, analytics, billing, and production-data checks remain manual, repo-owned gates.
- Stripe disabled a live webhook endpoint shown as the root domain on 2026-05-02; the repo-documented route is reachable at `/api/webhook-stripe`, so Stripe Dashboard endpoint correction, re-enable, event replay, and affected-subscription verification remain manual support gates.
- GitHub reported an existing Dependabot alert backlog after the push; triage belongs to the Omnexus security backlog and is not a CCAAP launch blocker.
- DSE remains a separate COI-aware lane and was intentionally not touched.
- GitHub Enterprise org-migration closeout is complete for Omnexus as of PR #559; future Omnexus work should start from `main`.
- Omnexus closeout changes were committed and pushed at `65d9ea44`; future Omnexus work should start from clean `main` after checking live git state.

## Notes

This DTP-owned index is a planning receipt. It does not replace Omnexus repo-local CI, release evidence, app-store runbooks, or production verification artifacts.
