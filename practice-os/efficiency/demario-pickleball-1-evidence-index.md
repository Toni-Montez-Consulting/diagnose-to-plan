---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: demario-pickleball-1

## Repo

- Name: `demario-pickleball-1`
- Branch: `master`
- Last updated: 2026-04-30
- Reviewer: Adjacent project touch pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| local | 2026-04-30 | pass | `bcd23a2` | `npm run ci`: typecheck pass, lint pass, Vitest 15 files / 55 tests pass, `next build` pass |
| local hygiene | 2026-04-30 | noted | `bcd23a2` | `next build` regenerated `next-env.d.ts` from `.next/dev/types/routes.d.ts` to `.next/types/routes.d.ts`; change was restored to keep the repo clean |
| CI | 2026-04-29 | pass | `bcd23a2` | GitHub Actions CI run `25125162032` passed |
| E2E | 2026-04-29 | pass_in_ci | `bcd23a2` | CI installs Chromium and runs `npm run test:e2e`; local E2E not rerun in this touch pass |
| release | 2026-04-30 | manual_pending | `bcd23a2` | `docs/RELEASE_CHECKLIST.md` still contains Supabase, Google OAuth, live booking QA, monitoring, and business gates |
| proof | 2026-04-30 | blocked | current branch | public proof needs owner permission, source evidence, redaction, reviewer approval, launch context, and caveats |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| DeMario has a working owner command room with bookings, tasks, owner roadmap, and launch handoff docs | `/admin`, `/admin/tasks`, `/admin/roadmap`, `docs/ADMIN_HANDOFF.md`, `docs/MARIO_ACTION_PLAN.md` | pending Mario approval | pending screenshot/data redaction | pending |
| The launch flow routes students by venue/platform rules instead of forcing every booking through the site | `docs/VENUE_RULES.md`, booking workflow, booking API guardrails, release checklist | internal_reference | public-safe summary possible; screenshots need review | pending |
| The repo has strong local and CI gates for controlled launch confidence | `npm run ci`, GitHub Actions CI run `25125162032` | internal_reference | public-safe after no private logs/screenshots | pending |
| Review/testimonial trust claims need source-backed proof before broad promotion | `docs/LAUNCH_OUTSTANDING.md` | missing source confirmation | pending | pending |

## Open Gaps

- Manual launch gates remain outside code: Supabase SQL application, admin/MFA verification, Google Calendar OAuth, live booking QA, and owner handoff.
- Review/testimonial proof needs source confirmation before broad public promotion or consulting proof reuse.
- Sentry remains recommended post-launch ops unless Mario/Tonio decide it becomes mandatory.
- Node 24 runner/toolchain migration is already deferred on the developer roadmap.
- `next-env.d.ts` can dirty the worktree when Next switches typed-route references between dev and production build output; fix or document this if it keeps disrupting future agent gates.

## Notes

This DTP-owned index is a planning receipt. It does not replace DeMario's repo-local release checklist, launch outstanding notes, owner handoff, GitHub Actions logs, or future DTP proof packet.
