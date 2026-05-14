---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Hub Dependency Cleanup Platform Preview Receipt - May 14, 2026

## Receipt Metadata

- Receipt id: `hub-dependency-cleanup-2026-05-14`
- Created: 2026-05-14
- Repo/lane: `hub` dependency cleanup
- Owner: Toni / Codex
- Reviewer: pending
- Claim level: local + CI
- Status: pass_with_caveats

## Change

- What changed: resolved and merged the two active Hub dependency cleanup PRs.
- Why it changed: Hub dependency CI was blocked by stale/conflicting Dependabot
  branches, which needed to be closed before reopening runtime cleanup work.
- User/operator journey: future Hub runtime work starts from a green dependency
  baseline instead of inheriting lockfile and migration failures.
- Non-goals: no Hub runtime features, no consulting public copy, no production
  Hub writes, no Supabase migration, no Vercel dashboard change, no `tm-skills`
  mutation.
- No-touch areas: private runtime data, live intake rows, production credentials,
  Vercel/Supabase dashboards, client proof, Greg soft-launch evidence.

## PRs Closed

| PR | Result | Merge commit | Notes |
|---|---|---|---|
| `#77` `@hono/zod-openapi` 0.18.4 to 1.4.0 | merged | `95161fb7929f96918270d697a42bf7d9c4d3a559` | repaired Zod compatibility by aligning direct Zod dependencies with Zod 4 and updating Zod 4 `z.record` call sites |
| `#78` `tailwindcss` 3.4.19 to 4.3.0 | merged | `51e2e0c3706c5e47bd984a4ec79ef792dc87fc05` | completed Tailwind 4 migration with `@tailwindcss/postcss`, `@import "tailwindcss"`, `@config`, and `@source` |

## Environment

- Local URL or command: no local server required.
- Preview URL: not used.
- Production URL: not checked.
- Deployment id or commit: Hub `main` at `51e2e0c3706c5e47bd984a4ec79ef792dc87fc05`.
- Environment variables checked by name only: no environment values were changed.
- Secret values printed: no.

## Evidence

- Build/test/lint commands:
  - `pnpm verify` passed for PR `#77`.
  - `pnpm security:secrets` passed for PR `#77`.
  - temp DB smoke passed for PR `#77` with `pnpm hub migrate` and
    `pnpm hub doctor`.
  - `pnpm --filter @hub/web build` passed for PR `#78`.
  - `pnpm --filter @hub/web typecheck` passed for PR `#78`.
  - `pnpm --filter @hub/web test` passed for PR `#78`.
  - `pnpm verify` passed for PR `#78`.
  - `pnpm security:secrets` passed for PR `#78`.
  - `git diff --check` passed for PR `#78`.
- Route/API checks: none; this was not runtime proof.
- Browser/device checks: none.
- Screenshots or recordings: none.
- Logs inspected: GitHub PR checks and local command output.
- Data writes or migrations: temp local DB smoke only for PR `#77`; no
  production data writes.
- Skipped checks and reason: live Hub, Vercel, Supabase, intake, and console
  checks were skipped because dependency cleanup did not mutate runtime state.

## Tailwind 4 Specific Proof

PR `#78` was treated as a migration, not a routine patch. The first passing web
build produced an undersized CSS bundle because Tailwind was not loading the
existing JS config and source graph. The repair explicitly loaded both:

- `@config "../tailwind.config.js";`
- `@source ".";`

The generated CSS was checked for app utilities including `bg-neutral-900`,
`text-neutral-400`, `max-w-5xl`, responsive `sm:` rules, and `.console-page`.

## Integrity Check

- Truth: this proves the dependency cleanup lane is green on local gates and
  GitHub CI; it does not prove live Hub runtime behavior.
- Usefulness: it removes the dependency/lockfile blocker before archive/delete
  cleanup or runtime evidence work resumes.
- Restraint: runtime cleanup, live tests, and public proof were deliberately
  deferred.
- Durability: both PRs are merged to `main`, GitHub checks passed, and stale
  remote refs were pruned locally.
- Handoff: future agents should start Hub runtime cleanup from `main` and avoid
  reopening PR `#68`, `#77`, or `#78` as active work.

## Decision

- Decision: dependency cleanup lane is closed.
- Caveats:
  - GitHub reported existing default-branch Dependabot vulnerabilities after
    push; those are outside the two closed PRs and should be assessed as a
    separate security/dependency lane.
  - Live Hub runtime was not verified in this receipt.
  - Omnexus PR `#566` remains review-required and could not be merged without
    review or admin override.
- Rollback path: revert the merge commits on `main` if either dependency bump
  causes a concrete regression; do not hand-edit lockfile state without rerunning
  `pnpm install`.
- Next action: choose either Hub runtime archive/delete cleanup or Omnexus data
  boundary proof once the relevant review gate is clear.
- Follow-up owner: Toni / next agent.
