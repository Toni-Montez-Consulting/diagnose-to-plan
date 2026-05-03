---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Receipt: Hub PR #55 React Dependency Triage

## Session

- Date: 2026-04-30
- Active story: Hub PR #55 dependency triage
- Steward mode: execution/postflight
- Owner: Toni Montez

## Trigger

Toni selected Hub PR #55 as the next dependency-health item after Omnexus org migration closed, Hub PR #59 merged, and Mom/CCAAP remained parked until owner-confirmed facts exist.

## Activation

| Prompt intent | Activated asset | Result |
|---|---|---|
| "Hub PR #55 dependency triage" | Hub repo manifest, Delivery Baseline, Testing Ladder | Checked out the PR, ran local gates, fixed the compatibility gap, watched remote checks, merged after green |
| "Do not touch Mom/DSE/FAOS" | Roadmap Steward no-touch boundary | No CCAAP private-kit updates, no DSE work, no FAOS implementation |
| "Keep PR #56 parked" | Dependency maintenance policy | Treated OpenAI 6.x as a separate major SDK migration review |

## Repo Actions

| Repo | Action | Status |
|---|---|---|
| `hub` | Triaged Dependabot PR #55 | Merged after local and remote gates passed |
| `diagnose-to-plan` | Updated steward, evidence, and roadmap records | This receipt plus Hub evidence/backlog updates |
| `dse-content` | No action | Remains excluded/COI-gated |
| `engagements/mom-nonprofit` | No action | Owner facts still pending |

## Hub PR #55 Result

- PR: `https://github.com/Toni-Montez-Consulting/hub/pull/55`
- Original branch: `dependabot/npm_and_yarn/multi-2a6546692b`
- Dependency intent: bump `react-dom` and `@types/react-dom`.
- Corrective commit: `ec41263`
- Merge commit: `ff7f1e4`
- Merged: 2026-04-30

Finding: the Dependabot branch originally upgraded `react-dom` and `@types/react-dom` to the React 19 line while leaving `react` and `@types/react` on React 18. That created a peer dependency mismatch that local build/test gates did not catch by themselves.

Resolution: aligned `@hub/web` to a coherent React 19 set:

- `react@^19.2.5`
- `react-dom@^19.2.5`
- `@types/react@^19.2.14`
- `@types/react-dom@^19.2.3`

## Verification

Local Hub gates passed before merge:

| Gate | Result |
|---|---|
| `pnpm install --frozen-lockfile --strict-peer-dependencies` | pass |
| `pnpm lint` | pass |
| `pnpm build` | pass |
| `pnpm typecheck` | pass |
| `pnpm test` | pass |
| `pnpm audit --prod` | pass |
| `pnpm security:secrets` | pass |

Remote Hub checks passed before merge:

| Check | Result |
|---|---|
| `lint` | pass |
| `typecheck` | pass |
| `build-test (ubuntu-24.04, 22)` | pass |
| `build-test (ubuntu-24.04, 24)` | pass |
| `build-test (windows-latest, 22)` | pass |
| `build-test (windows-latest, 24)` | pass |
| `smoke-cli` | pass |
| `deps-audit` | pass |
| `secrets-scan` | pass |
| `CodeQL` actions and JavaScript/TypeScript analyses | pass |

Post-merge cleanup:

- `hub/main` fast-forwarded to `origin/main`.
- The local PR branch was content-equivalent to `main` after squash merge and then deleted.
- Existing unrelated local Hub branches and stash entries were left untouched.

## Remaining Hub Queue

| PR | Status | Decision |
|---|---|---|
| #54 `@vitejs/plugin-react` 6.x | parked | debug separately because prior checks were failing |
| #56 `openai` 4.x to 6.x | parked | separate major SDK migration review |
| #61 dependency update | parked | debug separately because prior checks were failing |

Older PR #52 is no longer part of the active visible Hub PR queue.

## Blockers

- Mom/CCAAP owner facts and permission decisions remain pending.
- DSE remains excluded unless explicitly reopened with COI-aware scope.
- FAOS remains parked until readiness review is accepted.
- Cross-repo CI token/sibling-repo access remains deferred.

## Follow-Ups

1. Treat Hub PR #56 as the next dependency candidate only if Toni selects an OpenAI 6.x migration pass.
2. Do not merge PR #54 or #61 without a focused failing-check/debug pass.
3. Resume Mom/CCAAP only after owner-confirmed facts, recording/transcript handling, and permission decisions exist.
