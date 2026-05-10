# Documentation Map

Use this map to decide which document to update when the consulting practice changes.

## Canonical Source

`docs/PRACTICE_PRODUCTION_ROADMAP.md` is the canonical roadmap for practice production. It owns what is implemented, what remains, project sequencing, hosted DTP, Client Operating Kits, redaction, COI, proof promotion, and parked ideas.

When another repo's docs conflict with this roadmap, treat the other doc as local or historical until it is updated.

For broad workspace, business-machine, offer, proof, Hub, DTP, prompt/skill, or adjacent-project planning, read `docs/PRACTICE_MACHINE_OPERATING_MAP.md` before choosing an implementation lane. It preserves valuable ideas by staging them as `Now`, `Next`, `Later`, or `Hold` instead of deleting them or activating everything at once.

## DTP Docs

- `README.md`: one-screen current command/workflow orientation.
- `docs/01-architecture.md`: current DTP architecture and hosted-DTP direction.
- `docs/02-commands.md`: current CLI command surface only.
- `docs/03-skills.md`: current skill layout and validation boundary.
- `docs/04-multi-repo.md`: sibling repo read/write boundaries.
- `decisions/`: ADR-lite decision records for DTP. Use this directory when prompts ask for ADRs unless a future accepted repo-structure decision moves ADRs.
- `docs/adr/README.md`: pointer explaining that DTP's active ADR convention is `decisions/`, preventing duplicate ADR systems.
- `decisions/0009-workspace-control-plane-boundaries.md`: accepted boundary decision for DTP as practice source of truth, `engagements` as private client truth, Hub as runtime support, consulting as cleared-proof surface, assistant gates, and parked write-enabled cross-repo runners.
- `decisions/0010-opportunity-os-private-store-boundary.md`: accepted boundary
  decision for Opportunity OS private storage. Use it before creating raw
  opportunity records, a CRM, a Notion source-of-truth database, Hub/Supabase
  tables, or a private relationship ledger.
- `docs/source/practice_os_build_spec_v0_1.md`: additive source spec for the Practice OS capture -> learn loop and MVP modules. Preserve it; convert it into integration docs/templates/backlog items instead of editing it directly.
- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md`: additive company thesis and implementation-layer source material. Preserve its strategic language and use it as source for positioning, offer design, client discovery, and internal product development.
- `database/schema/practice_os_schema_v0_1.sql`: additive starter schema source for future Practice OS records. Do not run it as a migration until it is reconciled with Hosted DTP Phase 0.
- `docs/PRACTICE_VERIFICATION_SPINE.md`: Sprint 1 gate matrix, evidence contract, tool phasing, and no-slop quality gate for DTP, consulting, and Hub.
- `docs/PRACTICE_ROADMAP_HORIZONS_2026.md`: urgent/short/mid/long horizon overlay for the practice roadmap. Use it to decide what should happen now, what should be improved next, and which future capabilities remain gated.
- `docs/PRACTICE_MACHINE_OPERATING_MAP.md`: offer-led compression map for the whole practice machine. Use it before broad cross-repo plans, business-system changes, proof strategy, Hub expansion, hosted DTP decisions, or public-offer changes.
- `docs/PRACTICE_KAIZEN_KANBAN_SYSTEM.md`: DTP-first continuous-improvement intake/index loop. Use it before trusting chat memory with new ideas, asks, blockers, proof candidates, repo issues, client signals, corrections, process improvements, completed work, cancelled work, superseded work, or discarded assistant suggestions.
- `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md`: human-gated evolution spine for turning raw ideas, collaboration patterns, research observations, messaging language, and client lessons into reviewed memory, pattern candidates, playbook rules, or parked/superseded records. Use it when an idea should not be captured once and forgotten.
- `docs/WORKSPACE_OPERATOR_RUNBOOK.md`: safe cross-repo operator runbook. It names command classes, repo roles, verification paths, package managers, deploy ownership, and no-touch boundaries without authorizing a live command runner.
- `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md`: public proof movement path. It reuses the existing proof/redaction templates and blocks public claims until evidence, permission, redaction, reviewer, and caveat gates pass.
- `docs/PRACTICE_PROOF_QUEUE_INDEX.md`: active proof-candidate queue across CCAAP, Omnexus, DeMario, Hub/intake, Architected Strength, consulting assistant, Business Brain, and DSE. Use it before deciding what proof can move next.
- `docs/PRACTICE_THESIS_AND_OFFER_MAP.md`: internal one-page practice thesis
  and offer map. Use it before deciding which client/operator loop proves which
  offer lane or before translating offer language into `consulting`.
- `docs/PRACTICE_PUBLIC_OFFER_SEQUENCE.md`: internal sequencing decision for
  future public consulting copy. Use it to keep the broad front door,
  Blueprint/Fast Track buying path, builder-led identity, and proof gates
  aligned before public site changes.
- `docs/PRACTICE_BUILDER_LED_OFFER_MODEL.md`: current builder-led consulting
  business model, including client fit, pricing posture, Blueprint deliverable
  standard, Fast Track split, proof hierarchy, and collaboration memory.
- `docs/PRACTICE_HOMEPAGE_START_AND_BLUEPRINT_COPY_LOCK.md`: locked internal
  source for the next consulting homepage, `/start`, proof-card, and Blueprint
  copy pass. Use before implementing public offer copy.
- `practice-os/templates/business-systems-blueprint.md`: reusable paid
  Blueprint template and source for a future public-safe sample artifact.
- `practice-os/templates/remaining-locks-ledger.md`: collaboration pattern for
  carrying unresolved strategy, offer, proof, positioning, and product-shaping
  decisions across turns before durable capture.
- `practice-os/templates/idea-evolution-record.md`: review template for maturing
  Kaizen captures into working memory, decision memory, pattern candidates,
  pattern memory, playbook memory, or explicit parked/superseded outcomes.
- `practice-os/templates/research-pattern-candidate.md`: Research Arm companion
  template for converting research signals, field notes, and business
  observations into reusable consulting pattern candidates.
- `practice-os/comms/private/messaging-knowledge-base-2026-05-10.md`: internal
  messaging knowledge base for owner-bottleneck language, short pitch variants,
  claims/metaphor candidates, and visual seeds before any public-copy gate.
- `practice-os/fixtures/consulting-intelligence/northline-performance-studio-blueprint-sample.md`:
  public-safe fictional Blueprint sample for a wellness/performance practice.
- `docs/OFFER_LED_PRACTICE_PACKAGING.md`: internal offer-packaging source for the first sellable practice offers. Use it before changing `consulting` public copy around offers.
- `docs/OFFER_TO_PROOF_MATRIX.md`: maps the three V0 offers to existing proof, missing proof, public-copy eligibility, and claims that are not allowed yet.
- `docs/BUSINESS_ADMIN_OPERATING_SYSTEM.md`: DTP-first operating lane for Toni's own Google Workspace, Calendar/Meet, Apple Reminders capture, LLC readiness, EIN/banking/tax/contract/insurance prompts, brand assets, admin cadence, and sanitized Notion mirror state.
- `docs/INTERNAL_OFFER_REPERTOIRE_CATALOG.md`: private repertoire catalog for reusable services and delivery patterns discovered through Toni's own operations and client work. Use before turning logos, mission/vision work, Apple Reminders capture bridges, admin systems, command rooms, intake systems, launch hardening, or follow-up queues into public offers.
- `docs/PRACTICE_SYSTEM_ARCHITECTURE.md`: current-state master architecture for the consulting operating system, including repo ownership, prompt/story activation, intake, proof/redaction, verification, and agent/skill boundaries.
- `docs/PRACTICE_SYSTEM_FUTURE_STATE.md`: future-state architecture for hosted DTP, steward automation, supervised learning, research radar, repo manifests, command-center planning, and gated agent activation.
- `docs/RESEARCH_ARM_V0.md`: manual-first research and intelligence loop for
  turning AI/software/workflow signals into digests, classifications,
  recommendations, and approval-gated practice updates. Use it before building
  always-on research agents, scheduled digests, or research-to-roadmap
  automation.
- `docs/OPPORTUNITY_OS_V0.md`: relationship-led consulting growth system for
  warm opportunities, referral paths, fit scoring, capacity protection, and
  sanitized Notion mirror fields. Use it before creating any private
  relationship ledger, CRM replacement, or automated outreach flow.
- `docs/RESEARCH_AND_OPPORTUNITY_NOTION_MIRROR_V0.md`: detailed Notion mirror
  design for Research Arm signals and sanitized Opportunity OS state. Use it
  before creating Notion databases, views, seed rows, or sync behavior for
  research/opportunity review. DTP remains source of truth and Notion remains a
  mirror/cockpit.
- `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md`: severity-ranked audit of the current practice system, including proof, private durability, hosted-DTP, prompt/registry, skill-install, documentation propagation, and adjacent-repo gaps.
- `docs/PRACTICE_SYSTEM_AGENTIC_PERFORMANCE_GAP_REVIEW.md`: recurring audit lens for agentic performance gaps: prompt routing, context quality, skill triggers, planning continuity, verification, research, safety, and learning-loop conversion.
- `docs/PRACTICE_SYSTEM_OPTIMIZATION_PLAN.md`: audit-to-execution plan that turns system findings into epics, stories, gates, owners, and sequencing.
- `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md`: DTP-owned operating model for
  human-led Delivery and Business Justification squads, source-indexed
  knowledge scope, business justification scorecards, approval gates, handoff
  receipts, consulting proof/offer pilot routing, specialized first-wave role
  specs, and future hosted DTP squad records. External Squad/SuperClaude-style
  frameworks stay inspiration-only.
- `practice-os/steward/2026-05-09-first-wave-agent-role-pilot-consulting-site.md`:
  first public-safe pilot receipt for applying the first-wave specialized roles
  to the consulting site, `/start`, `/blueprint`, and builder-led offer posture.
  Use it before adding more roles or building autonomous orchestration.
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`: current strategic
  backlog for proving the Practice OS through real client/operator loops before
  hosted, vector, or FAOS implementation work.
- `practice-os/steward/2026-05-07-workflow-spine-p0-implementation-plan.md`:
  current P0 implementation receipt for the Workflow Spine. Use it before
  changing lifecycle labels, `tm-skills` readiness, Workflow Spine templates,
  Greg spine records, or Cam spine records.
- `docs/CLIENT_OS_PILOT_WAVE_2026-05.md`: sanitized May 2026 pilot sequence for
  Greg, CCAAP, and Cam. Private working truth stays in the nested engagement
  vault.
- `docs/PRACTICE_KNOWLEDGE_BASE_V1.md`: markdown-first knowledge-base design
  for source-indexed records, metadata, validation risks, hosted-DTP scale path,
  and future retrieval readiness.
- `docs/PRACTICE_VECTOR_BRAIN_ROADMAP.md`: gated vector-memory path from
  markdown corpus to sanitized local retrieval, hosted/RLS retrieval, and
  agent-integrated retrieval.
- `docs/PRACTICE_ARCHITECTURE_REVIEW_PACKET_2026-05.md`: architecture and
  systems-health packet for repo ownership, runtime authority, proof movement,
  skill portability, and next-sequence review.
- `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md`: normalized source map for the Business Brain / Consulting OS. It captures the rebuilt docs, Claude planning context, source-of-truth order, repo mapping decisions, business-domain scope, first fixtures, comms posture, and forbidden-until-unlocked boundaries.
- `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md`: V0 operating layer for broad-session rehydration, input routing, client waiting states, Notion cockpit fields, tool stewardship, assistant gates, QuickBooks boundaries, and memory promotion. Use it before expanding infrastructure or returning to multi-client work.
- `docs/PRACTICE_MEMORY_CONTROL_PLANE.md`: Priority 1 operating layer for keeping ideas, replies, meetings, blockers, proof gates, connector plans, and session receipts out of chat-only memory. Use before expanding Notion, QuickBooks, hosted DTP, or agent automation.
- `docs/PRACTICE_MEMORY_OPTIMIZATION_PLAN.md`: retrieval and persistence ladder for making Codex rehydration reliable before adding hosted storage, vector retrieval, MCP recall, or a private Business Brain assistant.
- `docs/PRACTICE_TOOLING_STEWARD.md`: connector/plugin/tool evaluation pattern. Use before adding, removing, piloting, or expanding access for plugins, MCP servers, OAuth apps, CLIs, hosted tools, or business integrations.
- `docs/integration/source_index.md`: source-material inventory for the Practice OS thesis/spec/schema files and external DOCX duplicate.
- `docs/integration/integration_map.md`: map from new source concepts to existing DTP architecture, current support, gaps, and additive-first implementation sequence.
- `docs/integration/concept_registry.md`: named concept registry preserving the thesis language, memory levels, Input Studio, opportunity scoring, anti-slop review, value ledger, and related ideas.
- `docs/integration/conflict_register.md`: additive source-material conflict register. Use when new thesis/spec/schema material conflicts with, is absent from, or needs mapping against current DTP architecture.
- `docs/integration/reprioritization_log.md`: deliberate priority-change log. Use after new source documents, implementation slices, major exceptions, client feedback, constraints, strategy changes, or architecture decisions.
- `docs/integration/schema_reconciliation_v0.md`: planning-only reconciliation between the Practice OS starter SQL schema and Hosted DTP Phase 0. Use before any schema design, migration, hosted app shell, or database implementation work.
- `docs/FAOS_ORCHESTRATION_ROADMAP.md`: planning integration and technical review for the Frontier Agentic Operating System build spec; read before any FAOS repo, `op` wrapper, Langfuse, Mem0/Letta, Spec-Kit, MCP, subagent, hook, durable execution, or agent-orchestration implementation.
- `docs/WORKSPACE_COMMAND_CENTER_V0.md`: read-only Workspace Command Center spec and `dtp workspace report` boundary; use before implementing any live cross-repo status surface or command runner.
- `docs/WORKSPACE_DASHBOARD_READONLY.md`: static daily cockpit, Item Register, Recovery Inbox, validation report, and local VS Code panel spec generated from the workspace task ledger plus DTP-owned report, Kaizen, proof, backlog, repo-local boards, and sweep-ledger artifacts, preserving the no-live-runner boundary.
- `docs/workspace-dashboard.html`: generated browser dashboard for Toni's current, closed, and unreviewed recovery-candidate view. Regenerate with `dtp workspace dashboard`; it reads the workspace task ledger, workspace report, Kaizen queue, roadmap backlog, proof queue, sweep ledger, and unreviewed recovery pointers without live repo/cloud calls.
- `practice-os/workspace/task-ledger.jsonl`: reviewed normalized cross-workspace operating index for active, blocked, waiting, parked, completed, cancelled, superseded, and discarded work. Update it through `dtp workspace recover --apply --approved PATH` after reviewing dry-run candidates, or `dtp workspace task add` for an already-reviewed source-backed row.
- `outputs/workspace-dashboard-validation.json` / `outputs/workspace-dashboard-validation.md`: ignored validation artifacts from `dtp workspace validate-dashboard`; use these to reconcile reviewed dashboard rows, Recovery Inbox candidates, missing source refs, duplicate merges, redaction posture, and count mismatches.
- `docs/WORKSPACE_DOCS_AND_CHAT_SWEEP_LEDGER_2026-05-05.md`: evidence-first closeout ledger for the final workspace docs and Codex chat sweep. Use it before claiming the dashboard/kanban/roadmap tracker has every meaningful built, active, blocked, parked, completed, cancelled, superseded, or discarded item from the 13-repo workspace.
- `tools/vscode-dtp-dashboard/`: local no-server VS Code panel for the cross-workspace planning dashboard. It opens/refreshed DTP-owned dashboard HTML only; it is not a new roadmap source of truth.
- `docs/WORKSPACE_ROADMAP_AND_PLANNING_REPORT_2026-05-05.md`: internal Workspace Control Plane report for every consulting workspace repo except `dse-content`, including `architected-strength` and the private `engagements` lane. Use it before broad cross-repo roadmap status, planning-system, stale-doc triage, allowed-lane decisions, or repo-stability claims.
- `docs/CODEX_CHAT_AND_IMPLEMENTATION_RECOVERY_AUDIT_2026-05-05.md`: focused prompt-to-implementation audit. Use it for closeout routing when a recovered chat idea must be committed, promoted, backlogged, saved as a prompt/spec, parked, or archived.
- `docs/NOTION_MIRROR_V0.md`: Notion mobile mirror/capture and Command Center contract; use before connecting Notion MCP, creating/updating Notion databases, rebuilding cockpit views, syncing roadmap items, or treating phone-captured ideas as backlog work.
- `docs/RECURRING_CLIENT_CADENCE_OPERATING_PATTERN.md`: live-client cadence loop for prep, meeting, extraction, decision, action, and sanitized Notion mirror work across Cam, Greg, CCAAP, and Toni's weekly Business Brain reset.
- `docs/CLIENT_REPLY_INTAKE_OPERATING_PATTERN.md`: reply-to-state loop for Gmail replies, meeting notes, owner updates, and casual owner-approved facts. Use it before client replies turn into build work, calendar invites, Notion status, or proof movement.
- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`: cross-workspace prioritized plan across consulting, Architected Strength, DTP, Hub, `tm-skills`, prompt/registry repos, Omnexus, DeMario, CCAAP, FamilyTrips, and DSE, including value checks, current agentic-AI research additions, the Future Intelligence Layer, and the Workspace Efficiency Layer.
- `docs/CUSTOM_INTERFACE_CRAFT_STANDARD.md`: hard practice-wide rule for fully custom authored UI work across public sites, apps, admin portals, proof surfaces, and assistant-facing interfaces. Use it before broad UI implementation or reference promotion.
- `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md`: idea-to-roadmap routing contract for classifying new ideas, designs, development enhancements, project work, business moves, proof candidates, research items, and automation concepts.
- `docs/ROADMAP_EXECUTION_BACKLOG.md`: Kanban-style epic/story execution view for the roadmap, with status, Done gates, and next actions.
- `docs/ROADMAP_SYNTHESIS_GATE_LEDGER.md`: gate ledger for blocked/speculative synthesis candidates, including CCAAP public proof, Hub PR #68, Azure readiness extraction, Hosted DTP promotion, manual availability, Architected Strength assistant pattern, and FAOS revisit.
- `docs/ROADMAP_STORY_ACTIVATION_INDEX.md`: story-to-skill/template/agent routing index for the Kanban backlog; use it when a roadmap story needs the right activation path.
- `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md`: governed cross-site assistant pattern for public website assistants and authenticated admin/operator assistants. Read before implementing any chatbot, assistant widget, private retrieval, admin helper, or assistant gateway.
- `docs/assistant-manifests/consulting-public-v0.md`: first public assistant pilot manifest for the consulting site. It names approved public route sources, blocked private sources, handoff route, refusal rules, logging/analytics boundary, and launch gate without authorizing implementation.
- `docs/assistant-manifests/architected-strength-public-v0.md`: later public assistant manifest candidate for Architected Strength. It names the intended public source corpus, blocked sources, handoff route, refusal rules, logging/analytics boundary, and launch gate without authorizing implementation.
- `docs/HOSTED_DTP_PHASE_0.md`: hosted DTP schema/app-boundary design for the private single-operator foundation; read before any hosted app, schema, or migration work.
- `docs/CLIENT_COMMAND_ROOM_PATTERN.md`: reusable admin/customer portal pattern inspired by `demario-pickleball-1`; use when planning owner-facing operating rooms.
- `docs/CLI_VERIFICATION_AUTOMATION_PATTERN.md`: reusable CLI doctor/matrix/verification/evidence pattern inspired by Omnexus; use when planning infrastructure-first automation across repos.
- `docs/MOBILE_APP_REVIEW_AND_LAUNCH_PATTERN.md`: reusable mobile app review, approval, and first-72-hour launch pattern inspired by Omnexus App Store approval. Use before planning client-app TestFlight/App Store/Play Console review packets, rejection repair loops, approval closeouts, or mobile launch proof.
- `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md`: implementation handoff and shipped-status note for the separate `tm-skills` SDLC skills repo. Use this when building or activating reusable coding-agent skills.
- `docs/TM_SKILLS_READINESS_SCORECARD.md`: DTP-owned readiness scorecard for
  `tm-skills` phase-1, incubator, parked, candidate, and high-risk skill use.
  Use it before treating `tm-skills` as part of the squad workflow.
- `prompts/recovery-closeout.spec.md`: reusable prompt/spec pack for roadmap synthesis, prompt-to-implementation audits, buildspec reviews, repo audits, handoffs, and public assistant QA gates.
- `docs/build-spec-v2.md`: historical implementation spec for the V2 harness. Preserve for context, but prefer the current roadmap when it conflicts with implemented reality.
- `practice-os/`: reusable policies, templates, Skills, and reviewed Bottleneck Patterns. Business Brain command contracts live in `practice-os/commands/`; draft-producing role specs live in `practice-os/agents/`, including the first-wave role set for consulting strategy, external communications, product strategy, UX/design, software architecture, software engineering, DevOps/infrastructure, QA/audit, controller, COO, and general counsel; private-first comms drafts live in `practice-os/comms/`; reusable internal fixtures live in `practice-os/fixtures/business-brain/`. Workspace operating rows live in `practice-os/workspace/task-ledger.jsonl`; use `dtp workspace recover --dry-run` and reviewed `--apply` imports instead of copying chat transcripts into tracked docs. Kaizen intake lives in `practice-os/kaizen/intake.jsonl` and should receive meaningful new ideas, asks, blockers, proof candidates, repo issues, client signals, corrections, and process improvements before promotion. Activation routing uses `practice-os/templates/activation-routing-map.md` to map prompt shapes to the right `tm-skills` skill, DTP Practice OS skill, template, gate, roadmap lane, repo touch pass, or parked automation path. Agent Squads + Knowledge Base V0 uses `practice-os/templates/agent-squad-charter.md`, `knowledge-scope-source-index.md`, `business-justification-scorecard.md`, `approval-gate.md`, `squad-handoff-receipt.md`, and `specialized-agent-role-spec.md` to make squad ownership, source indexing, value justification, approvals, handoff, and role boundaries explicit. Client OS pilot work uses `practice-os/templates/client-os-pilot-packet.md`; architecture and automation authority work uses `architecture-review-packet.md` and `automation-authority-matrix.md`; durable learning uses `memory-promotion-record.md`. Agentic performance review uses `practice-os/templates/agentic-performance-gap-review.md` when a session exposes a possible failure in routing, context quality, skill triggers, planning continuity, verification, research, safety, or learning-loop conversion. Contextual intake uses `practice-os/templates/contextual-idea-intake.md` plus `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md` to classify new ideas and designs before they become stories or implementation. Practice OS module work can now start manually with `practice-os/templates/thought-inbox.md`, `input-studio.md`, `context-pack.md`, `opportunity-score.md`, `exception-register.md`, `value-ledger.md`, and `memory-review-queue.md`; keep these optional until real usage proves which should become gates. Memory control uses `practice-os/templates/memory-control-checkpoint.md` plus `docs/PRACTICE_MEMORY_CONTROL_PLANE.md` when a work block, idea, connector, client status sweep, or infrastructure question is too important to trust to chat memory. Tooling stewardship uses `practice-os/templates/tooling-steward-review.md` plus `docs/PRACTICE_TOOLING_STEWARD.md` before adding, removing, piloting, or expanding plugins, MCP servers, OAuth apps, CLIs, hosted tools, or business integrations. Custom UI work uses `practice-os/templates/custom-interface-craft-brief.md` plus `docs/CUSTOM_INTERFACE_CRAFT_STANDARD.md` before broad site, app, admin, proof, or assistant-facing interface work. Story activation uses `practice-os/templates/story-activation-contract.md` plus `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` to tie Kanban stories to suggested skills, templates, agent roles, and gates. Recurring client cadence uses `practice-os/templates/recurring-engagement-cadence.md` plus `docs/RECURRING_CLIENT_CADENCE_OPERATING_PATTERN.md` so recurring meetings produce prep, extraction, decisions, action updates, and sanitized Notion mirror fields. Client reply intake uses `practice-os/templates/client-reply-intake.md` plus `docs/CLIENT_REPLY_INTAKE_OPERATING_PATTERN.md` so Gmail replies, meeting notes, owner updates, and casual owner-approved facts update DTP before Notion or calendar actions. Owner-call extraction uses `practice-os/templates/owner-call-to-action-extraction.md` when a client/owner conversation needs to become facts, blockers, owner actions, handoff updates, and implementation gates. Mobile app review capture uses `practice-os/templates/mobile-app-review-journey.md` when a project approaches TestFlight, App Store, Play Console, review repair, approval closeout, or first-user launch trust. FAOS phase planning uses `practice-os/templates/faos-phase-readiness-review.md` before any orchestration-substrate implementation. Command-room planning now starts with `practice-os/templates/client-command-room-fit-assessment.md` and, only when justified, `practice-os/templates/client-command-room-spec.md`. Roadmap stewardship uses `practice-os/templates/roadmap-steward-review.md` to keep active stories, repo lanes, gates, blockers, new ideas, and no-touch boundaries out of chat memory. Future Intelligence templates are optional assets for lessons, research, scorecards, flight records, red-team plans, feature flags, mobile app review journeys, and supply-chain baselines. Workspace Efficiency templates are optional assets for repo manifests, evidence indexes, decision records, command-center planning, dependency maintenance, toolchain pinning, CI cache hygiene, and project starter baselines. Proof/redaction templates are optional assets for proof packets, redaction queue items, permission review, evidence-source review, public claim review, and asset inventory.
- `practice-os/templates/notion-mirror-item.md`: optional mirror-contract template for phone-captured ideas, roadmap items, repo-health records, proof items, research radar items, meeting notes, and action items that need to move between DTP and Notion without changing source-of-truth ownership.
- `practice-os/templates/notion-cockpit-audit.md`: required audit template for live Notion Command Center rebuilds, dashboard cleanup, database/view normalization, and safety checks before Notion status is treated as current.
- `practice-os/templates/weekly-operator-cockpit.md`: weekly allowed-lane/status-only/no-touch cockpit for choosing what gets touched, what stays waiting, and what must be finished or avoided.
- `practice-os/templates/client-roadmap-one-pager.md`: client-safe roadmap shape that translates internal control-plane state into plain current state, first priority, deliverables, non-goals, inputs, timeline, cost, handoff, and support.
- `practice-os/templates/engineering-readiness-receipt.md`: repo/project checkpoint receipt for branch, commit SHA, worktree state, commands, results, security/dependency notes, manual QA, known issues, owner decision, and next action.
- `practice-os/templates/live-intake-receipt.md`: repeatable receipt for human-approved live consulting-to-Hub intake smokes, Hub row verification, test-record cleanup, and proof boundary notes.
- `practice-os/templates/business-admin-item.md`: reusable item contract for business/admin overhead lanes.
- `practice-os/templates/calendar-policy.md`: reusable policy surface for external meeting identity, Google Meet defaults, timezone, approval, and connector gates.
- `practice-os/templates/offer-catalog-item.md`: reusable offer-candidate contract for turning real delivery patterns into internal catalog entries before public promotion.
- `practice-os/templates/session-rehydration-checklist.md`: broad-session preflight for reconstructing active source state from DTP, git, steward receipts, engagement kits, Gmail, Calendar, and Notion before acting.
- `practice-os/templates/memory-source-index.md`: durable topic map for frequently rediscovered context, naming authoritative sources, drift risks, refresh commands, and promotion rules.
- `practice-os/templates/workflow-spine.md`: active current-state template for
  client/operator workflows. Use stable `active-workflow-spine.md` files with a
  dated receipt register; switch to dated spine filenames only if receipt
  discipline fails.
- `practice-os/policies/document-lifecycle.md`: minimal lifecycle label policy
  for `current`, `active`, `needs_stale_review`, `historical_reference`, and
  `superseded` docs.
- `practice-os/steward/`: live activation and Roadmap Steward review receipts. These are operating receipts, not private engagement records.
- `practice-os/patterns/admin-surface-operating-room.md`: reusable pattern for public proof surface outside, protected operating room inside, and handoff record after shipping.
- `practice-os/fixtures/consulting-intelligence/real-reply-seed-queue.md`: waiting queue for turning future Cam, Greg, CCAAP, or weekly Business Brain replies into sanitized eval cases.
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
- `docs/PRACTICE_OS_SKILL_READINESS.md`: readiness note for the Practice OS
  skill lane, including local candidate skill folders and promotion gates.
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
- `docs/UX_DESIGN_SYSTEM_AUDIT_2026-05-07.md`: current UX/design-system audit for
  CTA clarity, visual polish, proof/case-study presentation structure,
  component health, and route/data-flow architecture.
- `docs/LAUNCH_CHECKLIST.md`: final public-sharing checklist.
- `docs/DEEP_CUSTOMIZATION_10_10_RESEARCH.md`: historical/customization research and craft backlog.
- `docs/BUILD_SPEC_EXTRACT_REVIEW.md`: extraction-pattern analysis that informed DTP, especially admin-surface pattern capture.

## Hub Docs

The Hub repo owns runtime support for intake, private console records, Supabase tables, webhooks, captures, runs, prompts, and Vercel deployment.

- `docs/CONSULTING_CONSOLE_FULL_STACK.md`: consulting/Hub/Supabase runtime setup.
- `docs/HUB_RUNTIME_CURRENT_STATE.md`: current-state classifier for Hub surfaces: `live-hosted`, `local-only`, `legacy-proxy`, `planned`, or `retired`. Read it before expanding Hub or treating Hub runtime evidence as current.
- `docs/PRACTICE_OS_RUNTIME_READINESS.md`: Hub-local readiness note for Practice
  OS runtime support, preserving Hub as intake/runtime support rather than DTP
  source truth.
- `docs/PR68_TAILWIND4_MIGRATION_PLAN.md`: targeted plan for the parked Tailwind 4 dependency PR; use before reopening or replacing Hub PR #68.
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
- `architected-strength`: owns Toni's personal brand OS, content hub, networking engine, proof lab, and later public assistant-pattern candidate. It stays separate from consulting and should not be migrated into the consulting site.
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
- Use `docs/PRACTICE_MACHINE_OPERATING_MAP.md` before broad workspace, offer-led, platform, Hub, DTP, prompt/skill, proof, or adjacent-project planning. It decides whether the work is `Now`, `Next`, `Later`, or `Hold`.
- Use `docs/PRACTICE_KAIZEN_KANBAN_SYSTEM.md` and `dtp kaizen capture` when a new idea, feature, engagement signal, ask, blocker, proof candidate, correction, repo issue, process improvement, completed task, cancelled task, superseded task, or discarded suggestion should survive beyond the current chat.
- Use `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md` and `practice-os/templates/idea-evolution-record.md` when a captured idea, collaboration meta-pattern, messaging line, or agent behavior needs a path from raw capture into reviewed memory, a reusable pattern, a template, or an explicit parked/superseded state.
- Use `docs/WORKSPACE_OPERATOR_RUNBOOK.md` before running commands or changing files across repo boundaries. It keeps `dtp workspace report` read-only and avoids accidental deploy/migration/source-of-truth drift.
- Use `dtp workspace recover --dry-run` before claiming older completed, active, blocked, parked, cancelled, or superseded work is missing from the cockpit. Review the ignored output, then import approved rows with `dtp workspace recover --apply --approved PATH`.
- Use `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md` before moving any screenshot, claim, metric, client/project artifact, internal system evidence, or proof candidate toward public consulting copy.
- Use `docs/OFFER_LED_PRACTICE_PACKAGING.md` before updating the public consulting offer narrative.
- Use `docs/BUSINESS_ADMIN_OPERATING_SYSTEM.md` when Google Workspace, Calendar/Meet, Apple Reminders capture, LLC readiness, EIN/banking/tax, contracts, insurance, brand assets, or business overhead need durable planning state.
- Use `docs/INTERNAL_OFFER_REPERTOIRE_CATALOG.md` before turning a newly delivered asset, system, logo kit, mission/vision sprint, admin room, command room, launch hardening pass, or follow-up queue into an offer candidate.
- Use `practice-os/templates/activation-routing-map.md` when skill triggers, templates, roadmap lanes, proof gates, COI gates, research/eval artifacts, or repo touch lanes need prompt-based routing.
- Use `practice-os/templates/research-pattern-candidate.md` when a research signal, field note, or business observation needs to become a reusable consulting pattern candidate instead of a one-off summary.
- Use `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md` and `practice-os/commands/` when the prompt asks for Business Brain, Consulting OS, business agents, practice comms, diagnose-prospect, COI, proposal, or operator-handoff work.
- Use `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md` at the start of broad work blocks that combine clients, repos, Notion, Gmail, Calendar, QuickBooks ideas, public assistant planning, memory, or tooling decisions. It tells future agents how to rehydrate, route inputs, choose artifacts, and avoid unsafe action.
- Use `practice-os/templates/agentic-performance-gap-review.md` when a prompt, session, skill change, research adoption, or roadmap move reveals a possible agentic performance gap.
- Use `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md` and `practice-os/templates/contextual-idea-intake.md` when a new idea, design, business move, development enhancement, project request, or automation concept needs classification before implementation.
- Use `docs/CUSTOM_INTERFACE_CRAFT_STANDARD.md` and `practice-os/templates/custom-interface-craft-brief.md` before broad UI work or before treating a project as a reusable interface reference.
- Use `practice-os/templates/roadmap-steward-review.md` before or after major roadmap sessions that change priority, status, repo coverage, blockers, or idea capture.
- Use `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` when a specific Kanban story needs its suggested skill/template/agent routing checked.
- Use `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` when a prompt asks for
  squads, agent teams, knowledge bases, business justification, approval gates,
  handoff receipts, or source-indexed squad work. Consulting may point to this
  doc, but DTP remains the source of truth.
- Use `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md` and
  `docs/CLIENT_OS_PILOT_WAVE_2026-05.md` when Toni asks to organize the
  practice OS, pick the next client/operator loop, or sequence Greg, CCAAP, Cam,
  Hub, `tm-skills`, consulting design, vector memory, or FAOS.
- Use `docs/PRACTICE_KNOWLEDGE_BASE_V1.md`,
  `docs/PRACTICE_VECTOR_BRAIN_ROADMAP.md`, and
  `practice-os/templates/memory-promotion-record.md` before adding hosted
  memory, vector retrieval, persistent brain behavior, or agent recall.
- Use `docs/PRACTICE_ARCHITECTURE_REVIEW_PACKET_2026-05.md`,
  `practice-os/templates/architecture-review-packet.md`, and
  `practice-os/templates/automation-authority-matrix.md` before expanding
  cross-repo automation authority or architecture surface.
- Use `docs/FAOS_ORCHESTRATION_ROADMAP.md` and `practice-os/templates/faos-phase-readiness-review.md` before accepting any FAOS, `op` wrapper, Langfuse, Mem0/Letta, Spec-Kit, MCP, subagent, hook, durable execution, or agent-orchestration implementation prompt.
- Use `docs/NOTION_MIRROR_V0.md` and `practice-os/templates/notion-cockpit-audit.md` before connecting Notion MCP, creating/updating Notion databases, rebuilding cockpit views, or syncing DTP roadmap/proof/repo-health records into Notion. Notion is a mobile mirror and capture surface; DTP remains source of truth.
- Use `docs/PRACTICE_MEMORY_CONTROL_PLANE.md` and `practice-os/templates/memory-control-checkpoint.md` when Toni asks whether the system can remember/handle everything, when a new connector like QuickBooks enters scope, or when multiple workstreams risk living only in chat.
- Use `docs/PRACTICE_MEMORY_OPTIMIZATION_PLAN.md`, `practice-os/templates/session-rehydration-checklist.md`, and `practice-os/templates/memory-source-index.md` when Toni asks about persistent memory, better recall, context loss, source-aware rehydration, vector storage, private retrieval, MCP recall, or whether Codex can handle the operating load.
- Use `docs/PRACTICE_TOOLING_STEWARD.md` and `practice-os/templates/tooling-steward-review.md` when Toni asks about plugins/tools, missing connectors, whether a tool is worth keeping, or whether to add/remove/park a tool.
- Use `docs/CLIENT_REPLY_INTAKE_OPERATING_PATTERN.md` before turning Gmail replies, meeting notes, owner updates, or casual owner-approved facts into DTP state, Notion cockpit changes, calendar invites, build work, or proof movement.
- Use `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md` before implementing public website assistants, admin assistants, assistant manifests, private retrieval, or assistant gateway/runtime behavior.
- Use `docs/assistant-manifests/consulting-public-v0.md` as the first public assistant pilot manifest; implementation still needs repo-local source corpus, refusal tests, logging review, and launch gates.
- Use `docs/assistant-manifests/architected-strength-public-v0.md` as a later assistant-pattern candidate only after accepting the cross-site brief; implementation still needs repo-local source corpus, refusal tests, logging review, and launch gates.
- Use `docs/MOBILE_APP_REVIEW_AND_LAUNCH_PATTERN.md` and `practice-os/templates/mobile-app-review-journey.md` before turning a mobile app launch/review journey into a client handoff, proof candidate, review-response log, or reusable checklist.
- Verification evidence templates live in `practice-os/templates/verification-evidence.md` and `practice-os/templates/verification-evidence.json`; private run artifacts should live in ignored/private evidence paths unless they are intentionally redacted.
- Future Intelligence templates are optional until repeated usage proves they should become doctor-enforced Practice OS gates.
- Workspace Efficiency templates are optional until a repo-manifest/evidence-index pilot proves they should become doctor-enforced Practice OS gates or repo-local standards.
- Hosted DTP implementation must start from `docs/HOSTED_DTP_PHASE_0.md`; do not infer schema or app boundaries from chat-only context.
- Secondary repo-local documentation should propagate later through repo touch passes. Do not bulk-update consulting, Hub, `tm-skills`, Omnexus, DeMario, FamilyTrips, DSE, engineering-playbook, `hub-prompts`, or `hub-registry` just because the DTP master system docs changed.
- Historical docs should be labeled or cross-linked when their assumptions are superseded.
