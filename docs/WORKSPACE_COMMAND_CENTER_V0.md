---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Workspace Command Center V0

Status: implemented to the V0 read-only report boundary as `dtp workspace report`.

Purpose: define and run the first useful shape for a workspace command center after repo manifests and evidence indexes proved useful across DTP, consulting, Hub, `hub-prompts`, `hub-registry`, `tm-skills`, DeMario, FamilyTrips, engineering-playbook, and `fitness-app` / Omnexus.

## Boundary

V0 is a reporting surface, not an automation runner.

`dtp workspace report` may read DTP-owned artifacts only:

- repo manifests in `practice-os/efficiency/`
- evidence indexes in `practice-os/efficiency/`
- `docs/ROADMAP_EXECUTION_BACKLOG.md`
- `docs/WORKSPACE_COMMAND_CENTER_V0.md`
- manually recorded verification state inside DTP evidence indexes

It must not:

- execute repo-local commands
- call GitHub or live CI APIs
- mutate files
- execute repo checks
- apply fixes
- install skills
- publish proof
- change CI tokens or sibling-repo access
- touch production systems, Vercel, Supabase, Google OAuth, billing, or client data
- read or print secrets, private client records, family data, or raw logs

Future versions may add live git or CI reads only after a separate boundary decision. V0 reports live state as `not_checked_v0`.

## Inputs

| Input | Source | Notes |
|---|---|---|
| Repo coverage | canonical repo list in the CLI plus `docs/ROADMAP_EXECUTION_BACKLOG.md` | identifies owned lanes, blockers, and next actions |
| Repo manifests | `practice-os/efficiency/*-repo-manifest.md` | names owner lane, gates, sensitive data, safe commands, and next touch trigger |
| Evidence indexes | `practice-os/efficiency/*-evidence-index.md` | names latest receipt, result, open gaps, and proof state |
| Git status | not checked in V0 | live git reads stay later |
| CI status | manually recorded run ids in evidence indexes only | no live GitHub calls in V0 |
| Proof/privacy gates | proof/redaction templates and manifest notes | highlights blocked public proof, COI, and privacy risks |

## Outputs

The V0 report produces:

- repo coverage table
- suggested local gates
- manifest/evidence status
- latest recorded verification state
- open blockers
- proof/privacy/COI warnings
- manual gates
- next actions by repo
- parked automation items
- optional machine-readable JSON via `dtp workspace report --json`

## Report Shape

| Repo | Lane | Recorded state | Latest evidence | Suggested gate | Blocker | Next action |
|---|---|---|---|---|---|---|
| `diagnose-to-plan` | Practice OS | manifest/evidence ok | DTP CI or local validation from evidence index | pytest/ruff/skills/doctor | varies | current roadmap story |
| `consulting` | public proof/storefront | manifest/evidence ok | build/secret scan/proof packet from evidence index | build/secrets/route smoke | proof gates | public-safe updates only |
| `architected-strength` | personal brand OS and later assistant-pattern candidate | manifest/evidence ok | local CI and GitHub Actions from evidence index | `pnpm run ci` | assistant manifest/source/refusal gates | revisit after consulting public assistant pilot proves useful |
| `hub` | runtime/intake | manifest/evidence ok | CI/security/local verify from evidence index | pnpm verify or targeted gates | production secrets | runtime/support work |
| `hub-prompts` | prompt catalog | manifest/evidence ok | prompt validation from evidence index | npm test | eval/golden fixtures | prompt quality work |
| `hub-registry` | prompt routing registry | manifest/evidence ok | registry and prompt-id validation from evidence index | npm test locally; CI-safe validate in GitHub | sibling CI access deferred | registry validation work |
| `tm-skills` | global SDLC skills | manifest/evidence ok | doctor/freshness/install preview from evidence index | doctor/freshness/WhatIf | external smoke | skill canary/misfires |
| `engineering-playbook` | doctrine/reference | manifest/evidence ok | local ops status from evidence index | script parse/status-only/diff hygiene | roadmap ownership drift | doctrine/policy maintenance |
| `fitness-app` / Omnexus | app release and verification cockpit reference | manifest/evidence ok | Omnexus evidence index | tools doctor/matrix, CI, Verification Toolkit, release runbooks | user/billing/App Store/proof privacy | verification pattern extraction or app-release lane |
| `ccaap-site` | CCAAP launch readiness | manifest/evidence ok | CCAAP launch evidence index | pnpm lint/check/content/build, launch validation after owner inputs | PayPal/contact/DNS/assets/review/proof permissions | owner-input closure and Cloudflare preview before production |
| project repos | app-specific lane | manifest/evidence may be missing | repo-local index when touched | manifest gate | privacy/proof/launch | one scoped touch pass |

## Suggested Gates

Gate suggestions must come from manifests first, then repo-local docs. If no manifest exists, the report should say `manifest_missing` rather than guessing. If the Active Next Queue explicitly names a blocker for a missing repo, the report may carry that blocker forward so missing coverage does not appear unblocked.

Gate classes:

- hard: required before commit, merge, release, or proof promotion
- advisory: useful but not blocking
- manual: requires a person, dashboard, secret, permission, production account, or external tool reload
- parked: intentionally not active

## Safety Rules

- If a future live version reports a repo as dirty and it is not owned by the current story, report it and do not touch it.
- If a repo contains private/client/family data, summarize the risk without copying details.
- If proof is requested, require evidence, permission, redaction, reviewer, and caveat.
- If DSE/Microsoft/customer-adjacent material appears, route to COI review.
- If FAOS, MCP, tracing, memory, hooks, or agents are requested, route to the FAOS readiness gate.

## Pilot Acceptance

The V0 report is accepted when `dtp workspace report` can answer:

- Which repo owns the next story?
- Which checks should run?
- Which repos still need DTP-owned manifest/evidence coverage?
- Which verification evidence is recorded?
- Which proof/privacy/COI gates block publication?
- Which automation is parked?
- What should happen next?

The live runner stays later until the read-only report proves value and a separate boundary decision accepts any live git, CI, or command-execution behavior.
