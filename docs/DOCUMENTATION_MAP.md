# Documentation Map

Use this map to decide which document to update when the consulting practice changes.

## Canonical Source

`docs/PRACTICE_PRODUCTION_ROADMAP.md` is the canonical roadmap for practice production. It owns what is implemented, what remains, project sequencing, hosted DTP, Client Operating Kits, redaction, COI, proof promotion, and parked ideas.

When another repo's docs conflict with this roadmap, treat the other doc as local or historical until it is updated.

## DTP Docs

- `README.md`: one-screen current command/workflow orientation.
- `docs/01-architecture.md`: current DTP architecture and hosted-DTP direction.
- `docs/02-commands.md`: current CLI command surface only.
- `docs/03-skills.md`: current skill layout and validation boundary.
- `docs/04-multi-repo.md`: sibling repo read/write boundaries.
- `docs/PRACTICE_VERIFICATION_SPINE.md`: Sprint 1 gate matrix, evidence contract, tool phasing, and no-slop quality gate for DTP, consulting, and Hub.
- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`: cross-workspace prioritized plan across consulting, DTP, Hub, `tm-skills`, prompt/registry repos, Omnexus, DeMario, FamilyTrips, and DSE, including value checks, current agentic-AI research additions, the Future Intelligence Layer, and the Workspace Efficiency Layer.
- `docs/ROADMAP_EXECUTION_BACKLOG.md`: Kanban-style epic/story execution view for the roadmap, with status, Done gates, and next actions.
- `docs/HOSTED_DTP_PHASE_0.md`: hosted DTP schema/app-boundary design for the private single-operator foundation; read before any hosted app, schema, or migration work.
- `docs/CLIENT_COMMAND_ROOM_PATTERN.md`: reusable admin/customer portal pattern inspired by `demario-pickleball-1`; use when planning owner-facing operating rooms.
- `docs/CLI_VERIFICATION_AUTOMATION_PATTERN.md`: reusable CLI doctor/matrix/verification/evidence pattern inspired by Omnexus; use when planning infrastructure-first automation across repos.
- `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md`: implementation handoff and shipped-status note for the separate `tm-skills` SDLC skills repo. Use this when building or activating reusable coding-agent skills.
- `docs/build-spec-v2.md`: historical implementation spec for the V2 harness. Preserve for context, but prefer the current roadmap when it conflicts with implemented reality.
- `practice-os/`: reusable policies, templates, Skills, and reviewed Bottleneck Patterns. Command-room planning now starts with `practice-os/templates/client-command-room-fit-assessment.md` and, only when justified, `practice-os/templates/client-command-room-spec.md`. Future Intelligence templates are optional assets for lessons, research, scorecards, flight records, red-team plans, feature flags, and supply-chain baselines. Workspace Efficiency templates are optional assets for repo manifests, evidence indexes, decision records, command-center planning, dependency maintenance, toolchain pinning, CI cache hygiene, and project starter baselines. Proof/redaction templates are optional assets for proof packets, redaction queue items, permission review, evidence-source review, public claim review, and asset inventory.
- `practice-os/efficiency/`: first Workspace Efficiency pilot artifacts for DTP repo manifest and evidence index. These are planning receipts, not runtime configuration.
- `extracts/`: raw extraction, detector output, lessons, decisions, and synthesis. Promote only reviewed redacted material to `practice-os/patterns/`.
- `engagements/`: private client work, gitignored from the DTP code repo except for its README.

## tm-skills Docs

`tm-skills` is a separate repo, not a DTP subdirectory. DTP's `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md` preserves the implementation handoff and shipped-status notes; the `tm-skills` repo owns active skill files and install scripts.

The repo now owns:

- root `README.md`: repo purpose, install modes, and smoke tests.
- root `AGENTS.md`: instructions for editing the skills repo itself.
- `decisions/`: install-path and cross-tool design decisions.
- `instructions/global/`: global always-on coding-agent instructions.
- `skills/*/SKILL.md`: the actual reusable SDLC skills.
- `skills/*/evals/`: trigger and expected-output fixtures.
- `MISFIRES.md`: real trigger misses and fixes.
- `manifest.json`: freshness/provenance metadata for skills.
- `scripts/`: doctor, install, and freshness checks.

Do not move DTP operator Skills into `tm-skills`. DTP Skills stay focused on consulting practice work. `tm-skills` stays focused on software delivery behavior.

## Consulting Docs

The consulting repo owns the public site, launch checklist, visual design backlog, and proof surface.

- `README.md`: public site orientation, routes, environment variables, and extension notes.
- `docs/SITE_NEXT_PASS_ROADMAP.md`: short launch-oriented priority stack for `tonimontez.co`.
- `docs/PROTOTYPE_DESIGN_ROADMAP.md`: public-site design/craft backlog. It is not the master production roadmap.
- `docs/LAUNCH_CHECKLIST.md`: final public-sharing checklist.
- `docs/DEEP_CUSTOMIZATION_10_10_RESEARCH.md`: historical/customization research and craft backlog.
- `docs/BUILD_SPEC_EXTRACT_REVIEW.md`: extraction-pattern analysis that informed DTP, especially admin-surface pattern capture.

## Hub Docs

The Hub repo owns runtime support for intake, private console records, Supabase tables, webhooks, captures, runs, prompts, and Vercel deployment.

- `docs/CONSULTING_CONSOLE_FULL_STACK.md`: consulting/Hub/Supabase runtime setup.
- `docs/PLAYBOOK.md`: pointer to the external engineering playbook.
- `docs/audit-2026-04-22.md` and `docs/audits/`: historical Hub audit surfaces and backlog context.

Hub does not own DTP engagement kits, public proof pages, or the canonical practice roadmap.

## Adjacent Portfolio Docs

These repos are intentionally adjacent, not canonical owners of the current practice production roadmap.

- `engineering-playbook`: owns portfolio schemas, templates, historical decisions, secret-management references, and general operating doctrine. It should point to DTP for current practice-production sequencing.
- `hub-prompts`: owns prompt markdown consumed by Hub. It should change only when a Hub prompt, prompt schema, eval, or golden test changes.
- `hub-registry`: owns Hub automation targets. It should change only when prompt dispatch/routing targets change.

Do not update `hub-prompts` or `hub-registry` just because the roadmap changes. Updating them can imply new automation behavior, which should be a separate decision.

## Update Rules

- Practice-wide sequencing goes in DTP's `PRACTICE_PRODUCTION_ROADMAP.md`.
- Cross-workspace prioritization, missing-item sweeps, and research-driven additions go in `WORKSPACE_PORTFOLIO_ROADMAP.md`, then promoted into the narrower owning docs when implementation starts.
- Cross-repo verification, support automation, and evidence contracts go in `PRACTICE_VERIFICATION_SPINE.md` for the current sprint contract and `CLI_VERIFICATION_AUTOMATION_PATTERN.md` for the reusable long-lived pattern, then repo-specific docs when implementation starts.
- Cross-repo SDLC skill implementation goes in `TM_SKILLS_IMPLEMENTATION_ROADMAP.md` until the separate `tm-skills` repo exists, then in `tm-skills` docs.
- Public-site polish, proof layout, and visual QA go in consulting docs.
- Intake/runtime/Supabase/Vercel support goes in Hub docs.
- Private engagement material stays in DTP `engagements/` or hosted private DTP once built.
- Public proof must be redacted, permissioned, and evidence-backed before moving into consulting.
- Verification evidence templates live in `practice-os/templates/verification-evidence.md` and `practice-os/templates/verification-evidence.json`; private run artifacts should live in ignored/private evidence paths unless they are intentionally redacted.
- Future Intelligence templates are optional until repeated usage proves they should become doctor-enforced Practice OS gates.
- Workspace Efficiency templates are optional until a repo-manifest/evidence-index pilot proves they should become doctor-enforced Practice OS gates or repo-local standards.
- Hosted DTP implementation must start from `docs/HOSTED_DTP_PHASE_0.md`; do not infer schema or app boundaries from chat-only context.
- Historical docs should be labeled or cross-linked when their assumptions are superseded.
