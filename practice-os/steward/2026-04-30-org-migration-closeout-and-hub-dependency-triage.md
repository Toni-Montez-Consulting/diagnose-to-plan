---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Receipt: Org Migration Closeout And Hub Dependency Triage

## Session

- Date: 2026-04-30
- Active story: Close GitHub org migration, then triage Hub dependency PRs
- Steward mode: execution/postflight
- Owner: Toni Montez

## Trigger

Toni asked to finish the GitHub Enterprise organization migration closeout before moving into the visible Hub Dependabot queue. `dse-content` remains explicitly excluded because it is still in the personal/Microsoft-linked namespace and should stay COI-gated.

## Activation

| Prompt intent | Activated asset | Result |
|---|---|---|
| "Close org migration" | Roadmap Steward plus Workspace Efficiency lane | Rechecked Omnexus #559 and Hub local branch state |
| "Triage Hub dependency PRs" | Hub repo manifest/evidence index, testing ladder, delivery baseline | Started with Hub PR #59 and did not merge because the strict local audit gate is not clean |
| "Do not miss anything" | Agentic performance gap review posture | Captured blocked review, stale branch cleanup, audit nuance, and deferred unsafe PRs |

## Repos

| Repo | Action | Status |
|---|---|---|
| `fitness-app` / Omnexus | Rechecked PR #559 | Checks are green, but required review still blocks merge |
| `hub` | Cleaned stale local org-migration branch; triaged PR #59; updated PR #59 from `main` | Local `main` aligned to `origin/main`; PR #59 not merged |
| `diagnose-to-plan` | Updated source-of-truth evidence and backlog surfaces | This receipt plus Hub evidence/backlog updates |
| `dse-content` | Read-only status check only | Untouched and still excluded |

## Omnexus Closeout

- PR: `https://github.com/Toni-Montez-Consulting/Omnexus/pull/559`
- Head: `fix/org-repo-references`
- Base: `main`
- State: open
- Merge state: blocked
- Review decision: required
- Decision: do not bypass the required review gate.

Next action: Toni or another authorized reviewer approves PR #559. After it merges, fetch/prune `fitness-app`, align local `main` to `origin/main`, and delete only represented local PR branches.

## Hub Local Cleanup

- Hub PR #60 was already merged into `origin/main` via squash merge.
- Local `hub` was still on deleted branch `chore/org-repo-references`.
- Content equivalence was confirmed against `origin/main` ignoring line-ending noise.
- Local `main` was moved to `origin/main`, switched cleanly, and the stale branch was deleted.

Result: Hub local checkout is no longer stranded on a deleted org-migration branch.

## Hub PR #59 Triage

- PR: `https://github.com/Toni-Montez-Consulting/hub/pull/59`
- Branch: `dependabot/npm_and_yarn/prod-minor-patch-7dd19ef87c`
- Dependency group: Supabase, Hono, PostCSS, TypeScript ESLint, Anthropic SDK packages.
- Branch update: `gh pr update-branch 59` succeeded so the PR now includes the org-safe Hub security workflow from `main`.
- Remote status after branch update: all GitHub checks passed and merge state is clean.

Local evidence:

| Gate | Result | Notes |
|---|---|---|
| `pnpm install --frozen-lockfile` | pass | lockfile was current |
| `pnpm verify` | blocked by local noise | stopped on ignored `supabase/.temp/linked-project.json` Prettier finding, not on dependency code |
| `pnpm lint` | pass | direct local gate passed |
| `pnpm build` | pass | workspace build passed |
| `pnpm typecheck` | pass | rerun standalone after avoiding build/typecheck race |
| `pnpm test` | pass | workspace tests passed |
| `pnpm security:secrets` | pass | Gitleaks CLI scan found no leaks |
| `pnpm audit --prod --audit-level=high` | pass | matches CI security threshold |
| `pnpm audit --prod` | fail | two moderate findings remain |

Strict audit findings:

| Package path | Advisory | Current read |
|---|---|---|
| `apps/server > node-cron > uuid` | `uuid` buffer bounds advisory | requires a `node-cron` major-version review or other package resolution strategy |
| `packages/agent-runtime > @anthropic-ai/claude-agent-sdk > @anthropic-ai/sdk` | insecure default file permission advisory | direct SDK is patched, but the Claude Agent SDK still resolves a vulnerable transitive SDK version under PNPM |

Decision: do not merge PR #59 under the stricter local gate from this plan. The remote PR is green and merge-clean, but it still needs either an accepted audit threshold decision or a scoped Hub dependency-security fix.

## Other Hub Dependency PRs

| PR | Status | Decision |
|---|---|---|
| #52 dev-dependencies group | remote build-test failures | do not merge blindly |
| #54 `@vitejs/plugin-react` 6.x | remote typecheck/deps/build/Vercel failures | separate migration/debug pass |
| #55 `react-dom` and types | remote audit and Windows Node 24 failures | separate compatibility pass |
| #56 `openai` 4.x to 6.x | remote audit and Windows Node 24 failures | separate major SDK migration review |

## Blockers

- Omnexus #559 cannot close until required review is complete.
- Hub PR #59 cannot merge under strict `pnpm audit --prod` until moderate findings are resolved or policy explicitly accepts CI's high-severity threshold.
- DSE remains excluded.
- Mom nonprofit facts remain pending owner confirmation.
- FAOS remains parked.

## Follow-Ups

1. Human-review and merge Omnexus #559, then prune local Omnexus org-migration branches.
2. Decide Hub audit policy: strict zero-vulnerability `pnpm audit --prod` versus CI's `--audit-level=high`.
3. If strict audit stays required, create a Hub dependency-security story for `node-cron` v4 compatibility and PNPM override/upstream handling for `@anthropic-ai/claude-agent-sdk`.
4. Merge PR #59 only after the accepted local audit policy is clear; remote checks are already green after the branch update.
5. Leave #52/#54/#55/#56 parked until explicitly selected.
