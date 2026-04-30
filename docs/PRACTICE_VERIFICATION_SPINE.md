# Practice Verification Spine

This is the Sprint 1 verification contract for the consulting practice stack.

DTP owns the contract. Each repo owns its local implementation. Evidence should be durable enough for a future hosted DTP view, client command room, release handoff, or public proof packet, but raw private data must stay out of public artifacts.

## Operating Rules

- Hard gates block completion. Advisory gates can fail only when the failure is named in the evidence artifact.
- Advisory mode must never hide a hard failure.
- Manual gates stay manual until they have a reliable command or hosted API check.
- Public proof must be backed by reviewed evidence, redaction status, permission level, and reviewer.
- No hosted dashboard, command-room widget, or client-facing proof surface should be built before the repo-local gates produce useful evidence.

## Sprint 1 Repos

| Repo | Owns | Local gate | Release/support gate | Evidence path |
|---|---|---|---|---|
| `diagnose-to-plan` | Practice OS, verification contract, redaction, COI, templates | `pytest`, `ruff check .`, `dtp skills --validate`, `dtp practice doctor` | `dtp index --all`, `dtp synthesize --no-confirm`, redaction checks when evidence moves toward proof | `artifacts/verification/dtp/` or engagement-local private evidence |
| `consulting` | Public storefront, `/start`, `/admin`, visual QA, public proof shell | `npm run build`, `npm run security:secrets`; route smoke remains advisory until browser CI is intentionally expanded | Hub intake endpoint/CORS, visual QA, public/private markup scan | `artifacts/verification/consulting/` |
| `hub` | Runtime intake, private console, Supabase/Vercel support | `pnpm verify`, `pnpm test`, `hub doctor` | health route, protected console, intake CORS, Supabase migration/status, Vercel deployment checks | `artifacts/verification/hub/` |
| `tm-skills` | Cross-repo SDLC behavior and global skill activation | `doctor.ps1`, `freshness-check.ps1`, `install.ps1 -WhatIf` | install approval, tool reloads, Codex/Claude/Copilot discovery smoke tests | `artifacts/verification/tm-skills/` or GitHub Actions logs |
| `hub-prompts` | Prompt catalogue consumed by Hub | `npm test` | prompt eval/golden checks when added | `artifacts/verification/hub-prompts/` or GitHub Actions logs |
| `hub-registry` | Hub automation target routing | `npm run validate` in CI; local `npm test` validates registry shape, sibling manifests, and prompt ids against `hub-prompts` | private sibling-repo access for CI manifest/prompt checks only if explicitly approved later | `artifacts/verification/hub-registry/` or GitHub Actions logs |

## Reference Implementation

Omnexus / `fitness-app` now has the strongest concrete version of the verification cockpit pattern.

Verified on 2026-04-29:

- PR: `https://github.com/toniomon96/Omnexus/pull/553`
- Branch: `feat/verification-toolkit-supabase-cockpit`
- State: merged on 2026-04-29, GitHub checks green
- Merge commit: `1347368a01480110e3816e2f4b067102891bde23`
- Post-merge evidence: Verification Toolkit workflow run `25137681778` passed on `main`
- Commits: `52f56097 chore: add verification toolkit cockpit`, `2ffd3088 fix: align verification gates with baseline repair`

Reusable pieces:

- shared tool registry;
- lock file for Docker images and important CLI versions;
- `tools:doctor`, `tools:matrix`, `tools:verify:local`, and release evidence commands;
- ignored `artifacts/verification/` output convention;
- Docker-backed specialty tools;
- Supabase fresh-replay contract and migration drift guard;
- split hard gates from advisory evidence;
- CI artifact upload for verification reports.

This should guide DTP, consulting, Hub, and `tm-skills`, but it should not be copied blindly. Each repo still owns its own local, release, support, manual, and proof gates.

DTP-owned extraction receipts now live in `practice-os/efficiency/fitness-app-repo-manifest.md`, `practice-os/efficiency/fitness-app-evidence-index.md`, and `practice-os/steward/2026-04-30-omnexus-verification-cockpit-extraction.md`. These are planning receipts, not Omnexus runtime configuration.

Story 3 uses the "core plus map" version of this pattern: core repos get thin CI now, adjacent project repos get an explicit benefit lane and keep their existing owner-specific gates until a real project need calls for changes.

## Tool Phasing

### Add Now

- Evidence writer/template: required for every verification lane.
- Gitleaks: hard gate for DTP, consulting, Hub, and future client-kit repos.
- Playwright + axe for consulting: advisory route smoke, mobile/desktop checks, `/admin` noindex, sitemap exclusion, form action, and accessibility evidence.
- Knip for consulting and Hub: advisory traversal-noise detection only; no blind deletion.
- Repo doctor/matrix coverage: every repo should explain its gates before hosted evidence UI exists.
- Thin GitHub Actions that run stable local gates exactly as developers run them.

### Add Soon

- Lighthouse CI as advisory performance/accessibility evidence.
- Semgrep as advisory static analysis until rules are tuned.
- Renovate or grouped Dependabot for dependency hygiene.
- Shared GitHub Actions only after local commands are stable.
- Docker-backed specialty scanners/load tools after the repo has a registry, lock file, and artifact convention.

### Table

- Dashboards that do not connect to real evidence.
- Storybook/Chromatic until reusable UI components become a managed design system.
- Percy/Applitools until visual regression pain is real.
- OpenTelemetry until hosted DTP/runtime complexity justifies it.
- k6/load tests until Hub or a client runtime has real load concerns.
- PostHog for consulting until Plausible plus intake evidence is not enough.

## Evidence Contract

Use both a human-readable markdown artifact and a machine-readable JSON artifact when a run matters.

Required fields:

- `repo`
- `branch`
- `commit`
- `run_at`
- `lane`: `local`, `release`, `support`, or `proof`
- `result`: `pass`, `fail`, `advisory_pass`, or `manual_pending`
- `commands`
- `hard_failures`
- `advisory_failures`
- `manual_gates`
- `artifacts`
- `redaction_status`
- `reviewer`
- `next_action`

## No-Slop Quality Gate

Apply this to public/proof-facing work before it moves to Done:

- The story shows real evidence instead of generic claims.
- The copy keeps operator voice and avoids generic AI consultancy language.
- Consulting work preserves the Steel Ledger visual baseline unless a design change is explicit.
- No fake dashboards, fake booking links, or fake proof.
- No public proof without redaction status, permission level, and reviewer.
- No AI feature without source material, eval path, failure behavior, and cost/ownership notes.
- Private Hub rows, service-role data, DTP kits, client notes, and raw intake content stay out of public markup.

## Definition Of Done

A Sprint 1 story is Done only when:

- the owner repo is clear;
- hard/advisory/manual gates are classified;
- the evidence path is documented;
- fresh verification was run or manual gates were recorded as pending;
- docs were updated in the owning repo;
- hard failures are fixed or the story remains open.
