---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Workspace Command Center V0

Status: spec-only, read-only, not implemented.

Purpose: define the first useful shape for a workspace command center after repo manifests and evidence indexes proved useful across DTP, consulting, Hub, `tm-skills`, DeMario, FamilyTrips, and engineering-playbook.

## Boundary

V0 is a reporting surface, not an automation runner.

It may read:

- repo manifests in `practice-os/efficiency/`
- evidence indexes in `practice-os/efficiency/`
- DTP roadmap/backlog docs
- local `git status` summaries
- CI status links or manually recorded run ids
- repo-local docs that are named by manifests

It must not:

- mutate files
- execute repo checks
- apply fixes
- install skills
- publish proof
- change CI tokens or sibling-repo access
- touch production systems, Vercel, Supabase, Google OAuth, billing, or client data
- read or print secrets, private client records, family data, or raw logs

## Inputs

| Input | Source | Notes |
|---|---|---|
| Repo coverage | `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`, `docs/ROADMAP_EXECUTION_BACKLOG.md` | identifies owned lanes, blockers, and next actions |
| Repo manifests | `practice-os/efficiency/*-repo-manifest.md` | names owner lane, gates, sensitive data, safe commands, and next touch trigger |
| Evidence indexes | `practice-os/efficiency/*-evidence-index.md` | names latest receipt, result, open gaps, and proof state |
| Git status | read-only local status command | identifies dirty/clean and branch drift; does not fix |
| CI status | GitHub Actions links or run ids | read-only summary only |
| Proof/privacy gates | proof/redaction templates and manifest notes | highlights blocked public proof, COI, and privacy risks |

## Outputs

The V0 report should produce:

- repo health table
- changed repos
- suggested local gates
- stale evidence warnings
- open blockers
- proof/privacy/COI warnings
- manual gates
- next actions by repo
- parked automation items

## Report Shape

| Repo | Lane | State | Latest evidence | Suggested gate | Blocker | Next action |
|---|---|---|---|---|---|---|
| `diagnose-to-plan` | Practice OS | clean/dirty | DTP CI or local validation | pytest/ruff/skills/doctor | varies | current roadmap story |
| `consulting` | public proof/storefront | clean/dirty | build/secret scan/proof packet | build/secrets/route smoke | proof gates | public-safe updates only |
| `hub` | runtime/intake | clean/dirty | CI/security/local verify | pnpm verify or targeted gates | production secrets | runtime/support work |
| `tm-skills` | global SDLC skills | clean/dirty | doctor/freshness/install preview | doctor/freshness/WhatIf | external smoke | skill canary/misfires |
| `engineering-playbook` | doctrine/reference | clean/dirty | local ops status | script parse/status-only/diff hygiene | roadmap ownership drift | doctrine/policy maintenance |
| project repos | app-specific lane | clean/dirty | repo-local index | manifest gate | privacy/proof/launch | one scoped touch pass |

## Suggested Gates

Gate suggestions must come from manifests first, then repo-local docs. If no manifest exists, the report should say `manifest_missing` rather than guessing.

Gate classes:

- hard: required before commit, merge, release, or proof promotion
- advisory: useful but not blocking
- manual: requires a person, dashboard, secret, permission, production account, or external tool reload
- parked: intentionally not active

## Safety Rules

- If a repo is dirty and not owned by the current story, report it and do not touch it.
- If a repo contains private/client/family data, summarize the risk without copying details.
- If proof is requested, require evidence, permission, redaction, reviewer, and caveat.
- If DSE/Microsoft/customer-adjacent material appears, route to COI review.
- If FAOS, MCP, tracing, memory, hooks, or agents are requested, route to the FAOS readiness gate.

## Pilot Acceptance

The V0 spec is accepted when a future manual or CLI report can answer:

- Which repos changed?
- Which repo owns the next story?
- Which checks should run?
- Which evidence is stale?
- Which proof/privacy/COI gates block publication?
- Which automation is parked?
- What should happen next?

Implementation stays later until at least one more adjacent repo touch pass confirms this report shape reduces rediscovery.
