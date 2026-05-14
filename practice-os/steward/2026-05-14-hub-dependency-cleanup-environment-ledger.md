---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Hub Dependency Cleanup Environment Ledger - May 14, 2026

## Ledger Metadata

- Repo/lane: `hub` dependency cleanup
- Created: 2026-05-14
- Last updated: 2026-05-14
- Owner: Toni / Codex
- Reviewer: pending
- Status: current_for_dependency_cleanup

## Environment Map

| Environment | Purpose | URL/domain | Source branch/build | Owner | Last verified |
|---|---|---|---|---|---|
| Local | dependency validation, temp DB smoke, web build | local checkout only | `main` at `51e2e0c` after PR `#78` | Toni | 2026-05-14 |
| Preview | not used for this lane | none recorded | not applicable | Toni | not checked |
| Production | live Hub runtime | not checked in this lane | not applicable | Toni | not checked |

## Configuration Names

List variable names only. Secret values were not printed or changed.

| Name | Scope | Required | Owner | Verification path | Notes |
|---|---|---|---|---|---|
| `ANTHROPIC_API_KEY` | local smoke | yes for `hub doctor` | Toni | temp placeholder used for local PR `#77` smoke only | no real value recorded |
| `HUB_DB_PATH` | local smoke | yes for temp DB smoke | Toni | temp DB path used for `pnpm hub migrate` and `pnpm hub doctor` | no production DB touched |
| `HUB_SKIP_DOTENV` | local smoke | optional | Toni | set for temp smoke isolation | avoids reading local `.env` during smoke |
| `HUB_*` runtime variables | runtime | varies | Toni | `.env.example` and Hub docs only | no values changed |
| `SUPABASE_*` runtime variables | runtime | varies | Toni | Hub docs only | no values changed |

## Deploy And Rollback

- Normal deploy path: merge to Hub `main` after local and GitHub checks.
- Manual deploy path: not used.
- Rollback path: revert merge commit `95161fb` or `51e2e0c` if a concrete
  dependency regression appears.
- Known platform caveats: dependency cleanup does not equal live Vercel or
  Supabase runtime proof.
- Last deployment proof: not checked; no deployment was claimed.

## External Services

- Hosting: Hub docs reference hosted/Vercel behavior, but not verified here.
- Database: local temp DB smoke only; no Supabase mutation.
- Auth: not checked.
- Storage: not checked.
- Email: not checked.
- Payments: not applicable.
- Analytics/observability: not checked.
- Other: GitHub PR checks passed for PRs `#77` and `#78`.

## Verification

- Local gate: `pnpm verify`, `pnpm security:secrets`, targeted web build, temp
  DB smoke.
- Preview gate: skipped.
- Production gate: skipped.
- Manual gates: GitHub PR review/branch policy for Hub PRs passed by merge.
- Last known good state: Hub `main` at `51e2e0c` after PR `#78`.
- Known stale checks: live Hub health, protected console, intake rows, Supabase
  migrations, and Vercel deployment state were not refreshed.

## Boundaries

- What this ledger proves: no environment mutation was needed to close the Hub
  dependency cleanup lane.
- What this ledger does not prove: live Hub runtime, production deployment,
  Supabase table readiness, protected console behavior, or intake cleanup.
- Public/proof boundary: internal only; not public consulting proof.
- Client-data boundary: no client data, private rows, screenshots, or secrets
  were touched.
