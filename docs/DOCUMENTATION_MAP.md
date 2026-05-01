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
- `docs/PRACTICE_SYSTEM_ARCHITECTURE.md`: current-state master architecture for the consulting operating system, including repo ownership, prompt/story activation, intake, proof/redaction, verification, and agent/skill boundaries.
- `docs/PRACTICE_SYSTEM_FUTURE_STATE.md`: future-state architecture for hosted DTP, steward automation, supervised learning, research radar, repo manifests, command-center planning, and gated agent activation.
- `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md`: severity-ranked audit of the current practice system, including proof, private durability, hosted-DTP, prompt/registry, skill-install, documentation propagation, and adjacent-repo gaps.
- `docs/PRACTICE_SYSTEM_AGENTIC_PERFORMANCE_GAP_REVIEW.md`: recurring audit lens for agentic performance gaps: prompt routing, context quality, skill triggers, planning continuity, verification, research, safety, and learning-loop conversion.
- `docs/PRACTICE_SYSTEM_OPTIMIZATION_PLAN.md`: audit-to-execution plan that turns system findings into epics, stories, gates, owners, and sequencing.
- `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md`: normalized source map for the Business Brain / Consulting OS. It captures the rebuilt docs, Claude planning context, source-of-truth order, repo mapping decisions, business-domain scope, first fixtures, comms posture, and forbidden-until-unlocked boundaries.
- `docs/FAOS_ORCHESTRATION_ROADMAP.md`: planning integration and technical review for the Frontier Agentic Operating System build spec; read before any FAOS repo, `op` wrapper, Langfuse, Mem0/Letta, Spec-Kit, MCP, subagent, hook, durable execution, or agent-orchestration implementation.
- `docs/WORKSPACE_COMMAND_CENTER_V0.md`: read-only Workspace Command Center spec and `dtp workspace report` boundary; use before implementing any live cross-repo status surface or command runner.
- `docs/NOTION_MIRROR_V0.md`: Notion mobile mirror/capture contract; use before connecting Notion MCP, creating Notion databases, syncing roadmap items, or treating phone-captured ideas as backlog work.
- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`: cross-workspace prioritized plan across consulting, Architected Strength, DTP, Hub, `tm-skills`, prompt/registry repos, Omnexus, DeMario, CCAAP, FamilyTrips, and DSE, including value checks, current agentic-AI research additions, the Future Intelligence Layer, and the Workspace Efficiency Layer.
- `docs/CUSTOM_INTERFACE_CRAFT_STANDARD.md`: hard practice-wide rule for fully custom authored UI work across public sites, apps, admin portals, proof surfaces, and assistant-facing interfaces. Use it before broad UI implementation or reference promotion.
- `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md`: idea-to-roadmap routing contract for classifying new ideas, designs, development enhancements, project work, business moves, proof candidates, research items, and automation concepts.
- `docs/ROADMAP_EXECUTION_BACKLOG.md`: Kanban-style epic/story execution view for the roadmap, with status, Done gates, and next actions.
- `docs/ROADMAP_STORY_ACTIVATION_INDEX.md`: story-to-skill/template/agent routing index for the Kanban backlog; use it when a roadmap story needs the right activation path.
- `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md`: governed cross-site assistant pattern for public website assistants and authenticated admin/operator assistants. Read before implementing any chatbot, assistant widget, private retrieval, admin helper, or assistant gateway.
- `docs/assistant-manifests/architected-strength-public-v0.md`: first draft public assistant manifest for Architected Strength. It names the intended public source corpus, blocked sources, handoff route, refusal rules, logging/analytics boundary, and launch gate without authorizing implementation.
- `docs/HOSTED_DTP_PHASE_0.md`: hosted DTP schema/app-boundary design for the private single-operator foundation; read before any hosted app, schema, or migration work.
- `docs/CLIENT_COMMAND_ROOM_PATTERN.md`: reusable admin/customer portal pattern inspired by `demario-pickleball-1`; use when planning owner-facing operating rooms.
- `docs/CLI_VERIFICATION_AUTOMATION_PATTERN.md`: reusable CLI doctor/matrix/verification/evidence pattern inspired by Omnexus; use when planning infrastructure-first automation across repos.
- `docs/MOBILE_APP_REVIEW_AND_LAUNCH_PATTERN.md`: reusable mobile app review, approval, and first-72-hour launch pattern inspired by Omnexus App Store approval. Use before planning client-app TestFlight/App Store/Play Console review packets, rejection repair loops, approval closeouts, or mobile launch proof.
- `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md`: implementation handoff and shipped-status note for the separate `tm-skills` SDLC skills repo. Use this when building or activating reusable coding-agent skills.
- `docs/build-spec-v2.md`: historical implementation spec for the V2 harness. Preserve for context, but prefer the current roadmap when it conflicts with implemented reality.
- `practice-os/`: reusable policies, templates, Skills, and reviewed Bottleneck Patterns. Business Brain command contracts live in `practice-os/commands/`; draft-producing role specs live in `practice-os/agents/`; private-first comms drafts live in `practice-os/comms/`; reusable internal fixtures live in `practice-os/fixtures/business-brain/`. Activation routing uses `practice-os/templates/activation-routing-map.md` to map prompt shapes to the right `tm-skills` skill, DTP Practice OS skill, template, gate, roadmap lane, repo touch pass, or parked automation path. Agentic performance review uses `practice-os/templates/agentic-performance-gap-review.md` when a session exposes a possible failure in routing, context quality, skill triggers, planning continuity, verification, research, safety, or learning-loop conversion. Contextual intake uses `practice-os/templates/contextual-idea-intake.md` plus `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md` to classify new ideas and designs before they become stories or implementation. Custom UI work uses `practice-os/templates/custom-interface-craft-brief.md` plus `docs/CUSTOM_INTERFACE_CRAFT_STANDARD.md` before broad site, app, admin, proof, or assistant-facing interface work. Story activation uses `practice-os/templates/story-activation-contract.md` plus `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` to tie Kanban stories to suggested skills, templates, agent roles, and gates. Owner-call extraction uses `practice-os/templates/owner-call-to-action-extraction.md` when a client/owner conversation needs to become facts, blockers, owner actions, handoff updates, and implementation gates. Mobile app review capture uses `practice-os/templates/mobile-app-review-journey.md` when a project approaches TestFlight, App Store, Play Console, review repair, approval closeout, or first-user launch trust. FAOS phase planning uses `practice-os/templates/faos-phase-readiness-review.md` before any orchestration-substrate implementation. Command-room planning now starts with `practice-os/templates/client-command-room-fit-assessment.md` and, only when justified, `practice-os/templates/client-command-room-spec.md`. Roadmap stewardship uses `practice-os/templates/roadmap-steward-review.md` to keep active stories, repo lanes, gates, blockers, new ideas, and no-touch boundaries out of chat memory. Future Intelligence templates are optional assets for lessons, research, scorecards, flight records, red-team plans, feature flags, mobile app review journeys, and supply-chain baselines. Workspace Efficiency templates are optional assets for repo manifests, evidence indexes, decision records, command-center planning, dependency maintenance, toolchain pinning, CI cache hygiene, and project starter baselines. Proof/redaction templates are optional assets for proof packets, redaction queue items, permission review, evidence-source review, public claim review, and asset inventory.
- `practice-os/templates/notion-mirror-item.md`: optional mirror-contract template for phone-captured ideas, roadmap items, repo-health records, proof items, research radar items, meeting notes, and action items that need to move between DTP and Notion without changing source-of-truth ownership.
- `practice-os/steward/`: live activation and Roadmap Steward review receipts. These are operating receipts, not private engagement records.
- `practice-os/efficiency/`: Workspace Efficiency pilot artifacts for repo manifests and evidence indexes. DTP, consulting, Architected Strength, Hub, `hub-prompts`, `hub-registry`, `tm-skills`, DeMario, CCAAP, FamilyTrips, engineering-playbook, and `fitness-app` / Omnexus now have planning receipts here; remaining adjacent repos should be added only when their lanes are touched. These are planning receipts, not runtime configuration.
- `extracts/`: raw extraction, detector output, lessons, decisions, and synthesis. Promote only reviewed redacted material to `practice-os/patterns/`.
- `engagements/`: private client work, gitignored from the DTP code repo except for its README.

## tm-skills Docs

`tm-skills` is a separate repo, not a DTP subdirectory. DTP's `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md` preserves the implementation handoff and shipped-status notes; the `tm-skills` repo owns active skill files and install scripts.

The repo now owns:

- root `README.md`: repo purpose, install modes, and smoke tests.
- root `AGENTS.md`: instructions for editing the skills repo itself.
- `decisions/`: install-path and cross-tool design decisions.
- `docs/PRACTICE_SYSTEM_POINTER.md`: local pointer back to DTP's practice-system source of truth and activation/performance-gap contracts.
- `docs/INSTALL_SMOKE_2026-04-30.md`: V0 install evidence, Windows junction fallback note, and manual external-tool reload gates.
- `docs/EXTERNAL_TOOL_SMOKE_RUNBOOK.md`: manual Claude Code and GitHub Copilot reload/smoke instructions.
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
- `demario-pickleball-1`: owns the DeMario local-business launch track, booking/admin surface, owner tasks, owner roadmap, venue-routing rules, and Client Command Room reference implementation. DTP owns only the manifest/evidence receipt and future proof-governance routing.
- `fitness-app` / Omnexus: owns the product app, app-store docs, mobile launch evidence, verification cockpit, and post-approval operating docs. DTP owns only the manifest/evidence receipt, reusable verification pattern, mobile app review pattern, and future proof-governance routing.
- `architected-strength`: owns Toni's personal brand OS, content hub, networking engine, proof lab, and first public assistant-pattern candidate. It stays separate from consulting and should not be migrated into the consulting site.
- `ccaap-site`: owns the CCAAP off-Wix public-site implementation and Cloudflare launch path. DTP owns the private engagement kit, owner-input gates, and proof/redaction routing.

Do not update `hub-prompts` or `hub-registry` just because the roadmap changes. Updating them can imply new automation behavior, which should be a separate decision.

## Update Rules

- Practice-wide sequencing goes in DTP's `PRACTICE_PRODUCTION_ROADMAP.md`.
- Practice system architecture, future-state design, gap audits, and optimization plans go in the `docs/PRACTICE_SYSTEM_*` pack. Keep these docs synchronized with the roadmap/backlog when the operating model changes.
- Cross-workspace prioritization, missing-item sweeps, and research-driven additions go in `WORKSPACE_PORTFOLIO_ROADMAP.md`, then promoted into the narrower owning docs when implementation starts.
- Cross-repo verification, support automation, and evidence contracts go in `PRACTICE_VERIFICATION_SPINE.md` for the current sprint contract and `CLI_VERIFICATION_AUTOMATION_PATTERN.md` for the reusable long-lived pattern, then repo-specific docs when implementation starts.
- Cross-repo SDLC skill implementation goes in `TM_SKILLS_IMPLEMENTATION_ROADMAP.md` until the separate `tm-skills` repo exists, then in `tm-skills` docs.
- Public-site polish, proof layout, and visual QA go in consulting docs.
- Intake/runtime/Supabase/Vercel support goes in Hub docs.
- Private engagement material stays in DTP `engagements/` or hosted private DTP once built.
- Public proof must be redacted, permissioned, and evidence-backed before moving into consulting.
- Use `practice-os/templates/activation-routing-map.md` when skill triggers, templates, roadmap lanes, proof gates, COI gates, research/eval artifacts, or repo touch lanes need prompt-based routing.
- Use `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md` and `practice-os/commands/` when the prompt asks for Business Brain, Consulting OS, business agents, practice comms, diagnose-prospect, COI, proposal, or operator-handoff work.
- Use `practice-os/templates/agentic-performance-gap-review.md` when a prompt, session, skill change, research adoption, or roadmap move reveals a possible agentic performance gap.
- Use `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md` and `practice-os/templates/contextual-idea-intake.md` when a new idea, design, business move, development enhancement, project request, or automation concept needs classification before implementation.
- Use `docs/CUSTOM_INTERFACE_CRAFT_STANDARD.md` and `practice-os/templates/custom-interface-craft-brief.md` before broad UI work or before treating a project as a reusable interface reference.
- Use `practice-os/templates/roadmap-steward-review.md` before or after major roadmap sessions that change priority, status, repo coverage, blockers, or idea capture.
- Use `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` when a specific Kanban story needs its suggested skill/template/agent routing checked.
- Use `docs/FAOS_ORCHESTRATION_ROADMAP.md` and `practice-os/templates/faos-phase-readiness-review.md` before accepting any FAOS, `op` wrapper, Langfuse, Mem0/Letta, Spec-Kit, MCP, subagent, hook, durable execution, or agent-orchestration implementation prompt.
- Use `docs/NOTION_MIRROR_V0.md` before connecting Notion MCP, creating Notion databases, or syncing DTP roadmap/proof/repo-health records into Notion. Notion is a mobile mirror and capture surface; DTP remains source of truth.
- Use `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md` before implementing public website assistants, admin assistants, assistant manifests, private retrieval, or assistant gateway/runtime behavior.
- Use `docs/assistant-manifests/architected-strength-public-v0.md` as the first assistant-pattern candidate only after accepting the cross-site brief; implementation still needs repo-local source corpus, refusal tests, logging review, and launch gates.
- Use `docs/MOBILE_APP_REVIEW_AND_LAUNCH_PATTERN.md` and `practice-os/templates/mobile-app-review-journey.md` before turning a mobile app launch/review journey into a client handoff, proof candidate, review-response log, or reusable checklist.
- Verification evidence templates live in `practice-os/templates/verification-evidence.md` and `practice-os/templates/verification-evidence.json`; private run artifacts should live in ignored/private evidence paths unless they are intentionally redacted.
- Future Intelligence templates are optional until repeated usage proves they should become doctor-enforced Practice OS gates.
- Workspace Efficiency templates are optional until a repo-manifest/evidence-index pilot proves they should become doctor-enforced Practice OS gates or repo-local standards.
- Hosted DTP implementation must start from `docs/HOSTED_DTP_PHASE_0.md`; do not infer schema or app boundaries from chat-only context.
- Secondary repo-local documentation should propagate later through repo touch passes. Do not bulk-update consulting, Hub, `tm-skills`, Omnexus, DeMario, FamilyTrips, DSE, engineering-playbook, `hub-prompts`, or `hub-registry` just because the DTP master system docs changed.
- Historical docs should be labeled or cross-linked when their assumptions are superseded.
