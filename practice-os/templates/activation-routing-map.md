---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Activation Routing Map

Use this map when a prompt could route to more than one skill, template, process, or roadmap lane. Activation means "load the right context and gate the right workflow"; it does not mean autonomous repo edits, agent spawning, global installs, public proof, or hosted automation.

## Routing Rules

- Prefer the most specific asset that matches the prompt.
- Use `tm-skills` for reusable software delivery behavior after global install is approved and tools are reloaded.
- Use DTP Practice OS skills/templates for consulting practice methodology, proof, COI, redaction, command rooms, roadmap stewardship, and client operating kits.
- Use repo manifests/evidence indexes before guessing a repo's gates.
- Use `practice-os/templates/contextual-idea-intake.md` when Toni submits a new idea, design, business move, project request, development enhancement, or automation concept that should become a durable artifact.
- Use Roadmap Steward review when the prompt changes roadmap priority, status, active-next work, blockers, repo coverage, or idea capture.
- Use `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` when a prompt maps to a specific epic/story and you need the matching skill, template, agent-role suggestion, or gate.
- Use `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` when a prompt asks for squads,
  agent teams, knowledge bases, business justification, approval gates, or
  source-indexed handoffs.
- Use `docs/AUTONOMY_READINESS_LADDER_V0.md` when a prompt asks for autonomous
  agents, semi-autonomous workflows, scheduled stewards, an agent manager,
  read-only agents, draft-only agents, bounded autonomy, or whether a workflow
  can move up in authority.
- Use `docs/PRACTICE_OPERATING_REVIEW_LOOP_V0.md` when a prompt asks to review
  everything, find what is next, continue moving forward, recover after a
  disconnect, or check whether captured ideas are being revisited.
- Use `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md` when a prompt says an idea,
  collaboration pattern, research observation, messaging line, or agent
  behavior should not be forgotten and may need to mature beyond basic Kaizen
  capture.
- Use `docs/RESEARCH_ARM_SOURCE_LIST_V0.md` when a prompt asks for a recurring
  source list, current research sources, AI/news source monitoring, or source
  candidates for Research Arm.
- Use `docs/KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md` when a prompt says a
  knowledge base should be updated, refined, expanded, operationalized, or
  maintained across memory, operations, project execution, agent roles,
  messaging, or research.
- Use `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md` when a prompt asks
  for the practice operating system, strategic backlog, agent workflow,
  knowledge base, Hub/tm-skills coordination, consulting design architecture,
  vector brain, or FAOS sequencing.
- Keep all gated actions gated: global skill install, hosted DTP implementation, public proof promotion, write-enabled automation, autonomous agents, and production/client data changes.

## Prompt Activation Matrix

| Prompt shape | Primary activation | Supporting asset | Gate |
|---|---|---|---|
| "review my changes", "review this PR", "find regressions" | `tm-skills/review-checklist` | repo-local tests and CI evidence | no merge/push unless requested |
| "make this UI feel better", "polish this dashboard", "responsive/mobile QA", "make everything custom" | `tm-skills/frontend-craft` plus Custom Interface Craft Standard | `docs/CUSTOM_INTERFACE_CRAFT_STANDARD.md`, `practice-os/templates/custom-interface-craft-brief.md`, visual QA docs | craft brief or hotfix exception before broad UI work; preserve product/design boundary |
| "add auth/schema/API/storage", "design hosted boundary", "smallest backend" | `tm-skills/backend-design` | `docs/HOSTED_DTP_PHASE_0.md` for hosted DTP | boundary accepted before implementation |
| "what tests should run", "CI failed", "verification depth" | `tm-skills/testing-ladder` | repo manifest, evidence index, verification pattern | hard gates stay hard |
| "validate branch", "what is left", "committed/pushed?", "prepare handoff" | `tm-skills/delivery-baseline` | evidence index, git status, CI status | do not commit/push unless requested |
| "where are we", "review everything", "what is next", "keep moving forward", "what has been done", "are we losing ideas", "continue from here" | Practice Operating Review Loop | `docs/PRACTICE_OPERATING_REVIEW_LOOP_V0.md`, `practice-os/templates/practice-operating-review.md`, Kaizen status, evolution status, Memory Steward, Research Steward, practice doctor | produce decisions and next actions; do not use the review loop to bypass public/client/tool/runtime/autonomy gates |
| "run a systems health review", "review this like a living system", "check the weakest system", "what system is unhealthy here?", "find the intake, memory, recovery, and immune risks" | `tm-skills/systems-health-review` | repo manifests, code, docs, prompts, logs, runbooks, workflow maps | review-first; sequence fix now vs queue; no rewrite unless structurally unsalvageable |
| "what is next on the roadmap", "keep everything aligned", "capture this idea" | Roadmap Steward review | `docs/ROADMAP_EXECUTION_BACKLOG.md` | update status only with real evidence |
| "Business Brain", "Consulting OS", "business agents", "practice comms", "diagnose prospect", "draft proposal", "operator handoff" | Business Brain source map and Practice OS command contracts | `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md`, `practice-os/commands/`, `practice-os/agents/`, `practice-os/comms/`, `practice-os/fixtures/business-brain/` | DTP is source of truth; no public proof, pricing, live integrations, or autonomous agents without gates |
| "consulting strategy", "practice thesis", "offer strategy", "pricing posture", "buyer fit", "proposal framing", "scope shape", "business plan/site" | Consulting Strategy Agent | `practice-os/agents/consulting-strategy.md`, offer/proof/pricing docs, business justification scorecard | no unsupported ROI, public proof, pricing commitment, or offer copy without review |
| "customer email", "professional email", "external communication", "client follow-up", "prospect reply", "executive update", "sendable version", "Gmail draft", "summarize this email" | External Communications Agent | `practice-os/agents/external-communications.md`, `practice-os/templates/client-reply-intake.md`, authentic voice policy, proof/redaction templates when claims are present | summarize before drafting/action; create Gmail draft when connector supports and Toni asks; never send without explicit approval |
| "Google Workspace", "Calendar", "Meet", "appointment schedule", "founder email", "LLC", "EIN", "business admin", "offer catalog", "logos as offerings", "mission/vision as offerings" | Business Admin OS and Internal Offer Repertoire Catalog | `docs/BUSINESS_ADMIN_OPERATING_SYSTEM.md`, `docs/INTERNAL_OFFER_REPERTOIRE_CATALOG.md`, `practice-os/templates/business-admin-item.md`, `practice-os/templates/calendar-policy.md`, `practice-os/templates/offer-catalog-item.md` | no filings, calendar writes, public offers, or public proof without explicit approval and proof/professional gates |
| "Apple Reminders", "iOS Reminders", "sync reminders", "I use reminders all day", "do not move to Google Tasks" | Business Admin OS Apple Reminders capture lane | `docs/BUSINESS_ADMIN_OPERATING_SYSTEM.md`, `practice-os/templates/apple-reminders-capture-pilot.md`, `practice-os/templates/connector-map.md`, Tooling Steward review | one-list pilot only; no all-reminders sync, broad third-party access, or private reminder mirror without explicit approval |
| "new idea", "design idea", "business idea", "development enhancement", "project idea", "can we add this later" | contextual idea intake | `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md`, story activation index | classify before implementation |
| "which agent/skill should this story use", "tie this to Kanban", "activate for this epic" | story activation index | `docs/ROADMAP_STORY_ACTIVATION_INDEX.md`, story activation contract | suggested agents require explicit delegation approval |
| "squad of agents", "agent squad", "Delivery Squad", "Business Justification Squad", "knowledge base", "knowledge scope", "business justification", "approval gate", "handoff receipt" | Agent Squads + Knowledge Base V0 | `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md`, squad charter, source index, business justification scorecard, approval gate, squad handoff receipt | human-led only; no install, autonomous agents, public proof, client comms, production writes, or repo mutation without gates |
| "autonomy readiness", "autonomy ladder", "autonomous agent", "semi-autonomous", "read-only agent", "draft-only agent", "bounded autonomous workflow", "scheduled steward", "what can be autonomous", "move this up the ladder" | Autonomy Readiness Ladder | `docs/AUTONOMY_READINESS_LADDER_V0.md`, `practice-os/templates/autonomy-readiness-review.md`, Agent Squads + Knowledge Base V0, FAOS orchestration roadmap | classify current/target autonomy level first; no scheduled, write-enabled, live, client-facing, public-proof, financial, legal, production, or external action without accepted readiness review |
| "don't forget this", "dont forget this", "meta-pattern", "idea evolution", "this worked well", "do this again", "collaboration pattern", "practice evolution", "make sure this becomes how we work" | Practice Evolution System V0 | `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md`, `practice-os/templates/idea-evolution-record.md`, `practice-os/templates/remaining-locks-ledger.md`, `practice-os/templates/memory-promotion-record.md` | capture broadly, promote deliberately; no autonomous self-learning, public/client changes, or playbook-memory promotion without review |
| "show captured ideas", "practice evolution dashboard", "evolution status", "what is waiting for review", "which patterns are parked", "what did we capture" | Practice Evolution status dashboard | `dtp evolution status`, `dtp evolution dashboard`, `docs/practice-evolution-dashboard.html` | visibility only; dashboard does not promote memory, sync Notion, or authorize implementation |
| "memory steward", "memory agent", "what should be remembered", "what should be promoted", "what should be parked", "review memory", "memory queue" | Memory Steward | `practice-os/agents/memory-steward.md`, `dtp memory steward`, `docs/practice-evolution-dashboard.html`, `practice-os/templates/memory-promotion-record.md` | read-only recommendations; no autonomous self-learning, Notion sync, public/client action, or playbook promotion without Toni approval |
| "messaging system", "pitch system", "how I explain what I do", "owner bottleneck language", "claims library", "metaphor library", "visual asset seeds" | Messaging Knowledge Base | `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md`, `practice-os/comms/private/messaging-knowledge-base-2026-05-10.md`, External Communications Agent, Consulting Strategy Agent | internal only until public-copy, proof, positioning, and destination gates pass |
| "recurring source list", "source list", "AI source list", "research sources", "what sources should we watch", "source candidate", "keep me current on AI news", "research decision record" | Research Arm Source List | `docs/RESEARCH_ARM_SOURCE_LIST_V0.md`, `practice-os/templates/research-decision-record.md`, `docs/RESEARCH_ARM_V0.md`, Research Steward | event-based by default; source review does not authorize public claims, client comms, repo changes, tool installs, or runtime behavior |
| "event-based workflow", "update the knowledge base", "refine the knowledge base", "expand the knowledge base", "operationalize this", "memory management pattern", "project execution pattern", "knowledge base maintenance", "KB update" | Knowledge Base Event Workflow | `docs/KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md`, `practice-os/templates/knowledge-base-event-record.md`, Practice Evolution System, Memory Steward, Research Steward | human-gated maintenance only; no autonomous self-learning, Notion source-of-truth shift, public/client action, or playbook promotion without review |
| "practice OS", "operating system backlog", "client OS pilot", "Greg first", "CCAAP next", "Cam after confirmation" | Practice OS strategic backlog and Client OS pilot wave | `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`, `docs/CLIENT_OS_PILOT_WAVE_2026-05.md`, `practice-os/templates/client-os-pilot-packet.md` | private engagement truth stays in the vault; automation is draft-only; public proof waits for gates |
| "vector brain", "semantic memory", "knowledge base V1", "persistent recall", "source packs" | Practice Knowledge Base V1 and vector brain roadmap | `docs/PRACTICE_KNOWLEDGE_BASE_V1.md`, `docs/PRACTICE_VECTOR_BRAIN_ROADMAP.md`, `practice-os/templates/memory-promotion-record.md` | markdown corpus and privacy/citation evals before retrieval implementation |
| "architecture review", "component/design-system architecture", "runtime authority", "automation authority", "cross-repo system map" | architecture review packet and automation authority matrix | `docs/PRACTICE_ARCHITECTURE_REVIEW_PACKET_2026-05.md`, `practice-os/templates/architecture-review-packet.md`, `practice-os/templates/automation-authority-matrix.md` | review-first; no new runtime, schema, global install, or write-enabled automation without separate approval |
| "software architecture agent", "system architecture", "integration design", "module boundary", "runtime boundary", "data flow", "ADR", "technical tradeoff" | Software Architecture Agent | `practice-os/agents/software-architecture.md`, architecture review packet, automation authority matrix | review-first; no new runtime, schema, framework, integration, or cross-repo orchestration without approval |
| "software engineering agent", "coding agent", "implementation agent", "code this", "build this", "fix this bug" | Software Engineering Agent plus repo-local delivery skills | `practice-os/agents/software-engineering.md`, repo `AGENTS.md`, delivery-baseline, backend-design or frontend-craft as applicable | repo-grounded only; no production writes, deploys, commits, pushes, or cross-repo churn without explicit approval |
| "product strategy agent", "product strategy", "MVP", "feature priority", "launch sequence", "adoption loop", "feedback synthesis", "what should we build" | Product Strategy Agent | `practice-os/agents/product-strategy.md`, contextual idea intake, business justification scorecard, roadmap steward review | no invented demand, validation, conversion, willingness to pay, or market proof |
| "design agent", "UX agent", "UX/design", "web experience agent", "page spine", "interface craft", "visual QA" | UX / Design Agent | `practice-os/agents/ux-design.md`, custom interface craft brief, frontend-craft, visual QA evidence | no new visual direction without accepted brief; proof/private data stays gated |
| "QA agent", "audit agent", "go/no-go", "release readiness", "acceptance check", "verify this", "risk review" | QA / Audit Agent | `practice-os/agents/qa-audit.md`, review-checklist, testing-ladder, delivery-baseline, engineering readiness receipt | do not call work done without evidence; separate automated proof from manual gates |
| "audit the agent system", "what gaps did we miss", "why did this not activate", "I caught a design hole" | Agentic Performance Gap Review | `docs/PRACTICE_SYSTEM_AGENTIC_PERFORMANCE_GAP_REVIEW.md`, Roadmap Steward review | convert misses into durable artifacts, not autonomy |
| "can this become proof", "case study", "public claim" | proof/redaction templates | evidence source, asset inventory, claim review | permission, redaction, reviewer required |
| "client uses Azure/Copilot/Microsoft", "DSE", "COI" | DTP COI screen | data classification and redaction policy; after clearance route to the relevant Azure incubator skill | pause before scoping/coding |
| "prepare this app for Azure", "Azure Container Apps plan", "Azure deployment plan" | `tm-skills/azure-prepare` | `tm-skills/azure-validate`, repo manifest, DTP client/data boundary | plan-first; no live cloud mutation without explicit approval |
| "validate this Azure deployment", "preflight Azure release", "prove Azure plan is ready" | `tm-skills/azure-validate` | `tm-skills/azure-prepare`, delivery evidence, rollback notes | validate only after a prepared plan exists; no deploy until validation is accepted |
| "deploy this Azure plan", "run Azure deployment", "ship Azure infra" | `tm-skills/azure-deploy` | `tm-skills/azure-validate`, delivery baseline, release evidence | deploy only after validation, owner approval, secrets handling, and rollback gate |
| "DevOps agent", "infrastructure agent", "CI/CD", "deployment readiness", "rollback plan", "environment inventory", "observability", "runtime proof", "cost risk" | DevOps / Infrastructure Agent | `practice-os/agents/devops-infrastructure.md`, engineering readiness receipt, connector map, delivery-baseline, Azure skills when relevant | read-only by default; no deploy, DNS, billing, secret, OAuth, database, or production config mutation without approval |
| "Azure diagnostics", "Azure cost", "Azure RBAC", "Azure resource lookup" | matching Azure incubator skill | `azure-diagnostics`, `azure-cost`, `azure-rbac`, `azure-resource-lookup` | read-only by default; do not infer live resource truth without evidence |
| "Entra app registration", "Entra agent identity", "Microsoft Foundry hosted agent" | matching Entra/Foundry incubator skill | `entra-app-registration`, `entra-agent-id`, `microsoft-foundry` | identity, tenant, credentials, eval, trace, and approval boundaries first |
| "does this need a portal", "command room", "owner dashboard" | Command Room fit assessment | Command Room spec if fit passes | checklist/no surface is allowed |
| "new client kit", "Mom nonprofit", "engagement plan" | Client Operating Kit | diagnose, plan, consent, data inventory | private engagement material stays private |
| "research this tool/protocol", "should we adopt X" | research radar or research spike | Future Intelligence layer | classify Adopt/Pilot/Watch/Reject |
| "research arm", "research agent", "research steward", "research queue", "AI research digest", "keep me current", "what changed in AI", "turn research into practice updates", "source digest", "research pattern", "pattern extraction", "business observation", "field note pattern" | Research Arm V0 and Research Steward | `docs/RESEARCH_ARM_V0.md`, `practice-os/agents/research-steward.md`, `dtp research steward`, `docs/RESEARCH_AND_OPPORTUNITY_NOTION_MIRROR_V0.md`, `practice-os/templates/research-arm-digest.md`, `practice-os/templates/research-radar-item.md`, `practice-os/templates/research-spike.md`, `practice-os/templates/research-pattern-candidate.md` | research and field notes can become pattern candidates, but cannot authorize public claims, offer changes, tool installs, repo changes, client communication, or autonomous runtime |
| "Opportunity OS", "relationship system", "warm lead", "relationship map", "referral map", "operator opportunity", "high-trust consulting growth", "consulting CRM", "private relationship ledger", "Notion mirror for opportunities", "research/opportunity Notion mirror" | Opportunity OS V0 | `docs/OPPORTUNITY_OS_V0.md`, `decisions/0010-opportunity-os-private-store-boundary.md`, `docs/RESEARCH_AND_OPPORTUNITY_NOTION_MIRROR_V0.md`, `practice-os/templates/opportunity-os-record.md` | no raw private relationship ledger in consulting repo; no automated outreach; Notion is mirror only |
| "agent failed", "lesson learned", "make this self-learning" | lesson capture and eval candidate | agent session record | human approves skill/eval updates |
| "lost connection", "stream disconnected", "reconnecting", "command timed out", "timeout", "resume from where we were", "what happened before the disconnect" | Session Rehydration Checklist plus Agentic Performance Gap Review when repeated | `practice-os/templates/session-rehydration-checklist.md`, `practice-os/templates/agentic-performance-gap-review.md` | verify live files/logs/git/processes before claiming status; capture timeout/disconnect in the ledger |
| "App Store approved", "app review", "TestFlight", "Play Console", "mobile launch journey", "store rejection" | mobile app review and launch pattern | `docs/MOBILE_APP_REVIEW_AND_LAUNCH_PATTERN.md`, `practice-os/templates/mobile-app-review-journey.md` | no credentials/private store screenshots in git; public proof stays gated |
| "FAOS", "Frontier Agentic Operating System", "agent operating system", "agent orchestration substrate", "op wrapper", "Langfuse/Mem0/Letta", "Spec-Kit Phase 0" | FAOS orchestration roadmap plus Autonomy Readiness Ladder | `practice-os/templates/faos-phase-readiness-review.md`, `docs/AUTONOMY_READINESS_LADDER_V0.md`, `practice-os/templates/autonomy-readiness-review.md`, Agentic Performance Gap Review, Roadmap Steward review | roadmap/research only unless Phase 0A and autonomy readiness reviews are accepted; do not create `faos` repo, mutate DTP/skills, or move workflows above A3 automatically |
| "red-team this AI flow", "guardrails", "prompt injection" | AI red-team plan | OWASP/NIST/OpenAI guardrail references | before public/write-enabled AI |
| "feature flag", "kill switch", "rollback plan" | feature flag/kill switch plan | release trust/supply-chain baseline | required for risky client-facing automation |
| "which repo should this touch", "all apps covered?" | repo manifest and portfolio scorecard | workspace roadmap/backlog | do not force churn into every repo |
| "install skills globally", "activate tm-skills everywhere" | `tm-skills` install dry-run first | `doctor.ps1`, `freshness-check.ps1`, `install.ps1 -WhatIf` | `install.ps1 -Apply` needs explicit approval |
| "new agent role", "create a specialized agent", "add an agent persona", "define an agent domain" | Specialized Agent Role Spec | `practice-os/templates/specialized-agent-role-spec.md`, `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md`, agent role index | role spec only first; no autonomous runtime, tool install, or public behavior change without review |
| "add more agents", "more roles", "agent org chart", "expand the agent roster" | First-Wave Role Boundary | `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` first-wave role boundary | do not add roles by default; pilot the existing role set on real work unless a repeated gap is proven |
| "pilot the roles", "test the agent roles", "run the squad on this", "use the first-wave roles" | First-Wave Agent Role Pilot | `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md`, `practice-os/steward/2026-05-09-first-wave-agent-role-pilot-consulting-site.md` | produce a role-pass receipt with sources, decisions, open questions, and approval gates; do not add autonomous runtime |
| "build an agent manager", "autonomous steward", "self-modifying skills" | Autonomy Readiness Ladder, then parked/gated automation if authority is not ready | `docs/AUTONOMY_READINESS_LADDER_V0.md`, `practice-os/templates/autonomy-readiness-review.md`, Roadmap Steward V0, Future Intelligence | classify current/target autonomy first; self-modifying skills stay blocked until evals, guardrails, human review, rollback, and explicit approval exist |

## Classification Labels

Use these labels in Roadmap Steward reviews and handoffs:

- `global_sdlc_skill`
- `dtp_practice_skill`
- `business_brain`
- `practice_operating_review_loop`
- `consulting_strategy_agent`
- `external_communications_agent`
- `product_strategy_agent`
- `software_architecture_agent`
- `software_engineering_agent`
- `devops_infrastructure_agent`
- `ux_design_agent`
- `qa_audit_agent`
- `agent_squad_v0`
- `autonomy_readiness_ladder`
- `autonomy_readiness_review`
- `bounded_autonomy_candidate`
- `client_os_pilot`
- `knowledge_scope`
- `knowledge_base_v1`
- `vector_brain_gate`
- `architecture_review_packet`
- `automation_authority_matrix`
- `business_justification_gate`
- `approval_gate`
- `contextual_idea_intake`
- `custom_interface_craft`
- `practice_evolution_system`
- `messaging_knowledge_base`
- `research_pattern_candidate`
- `research_decision_record`
- `research_source_list`
- `research_steward`
- `knowledge_base_event_workflow`
- `practice_os_template`
- `roadmap_backlog_story`
- `proof_redaction_gate`
- `coi_privacy_gate`
- `research_eval_lesson`
- `repo_touch_pass`
- `azure_infra_incubator`
- `entra_identity_incubator`
- `foundry_agent_incubator`
- `faos_orchestration_spike`
- `parked_gated_automation`

## Update Rules

- When a `tm-skills` trigger description, trigger eval, or expected behavior changes, update this map or record why no map update is needed.
- When a DTP Practice OS template becomes required by `dtp practice doctor`, add it to this map if a future prompt should route to it.
- When a recurring source, source list, or research-decision workflow changes,
  update `docs/RESEARCH_ARM_SOURCE_LIST_V0.md` and this map.
- When a knowledge-base maintenance event changes a default workflow, source of
  truth, or approval path, update `docs/KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md`
  and leave a steward receipt.
- When a workflow is proposed for read-only, draft-only, supervised, scheduled,
  live, or autonomous authority, update or reference
  `docs/AUTONOMY_READINESS_LADDER_V0.md` and leave an autonomy readiness review
  before authority expands.
- When a review uncovers stale captures, unresolved steward recommendations,
  missing decisions, or unclear next actions, use
  `docs/PRACTICE_OPERATING_REVIEW_LOOP_V0.md` and leave a
  `practice-operating-review` receipt if priorities or gates changed.
- When a new repo lane is added to the workspace roadmap, add or update the relevant routing row.
- When a new idea introduces a new roadmap lane, business direction, design pattern, agent behavior, or recurring trigger, capture it through contextual idea intake before promoting it.
- When a backlog story changes status or ownership, check whether `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` needs a matching activation update.
- When a prompt repeatedly misroutes, capture the miss in a lesson, eval, `tm-skills/MISFIRES.md`, or Roadmap Steward review.
- When Toni identifies a missing agent behavior, process gap, or repeated planning miss, run the Agentic Performance Gap Review and decide whether the fix is a template, eval, skill update, research item, backlog story, decision record, or parked automation.

## Safety Notes

Do not include secrets, private client details, raw intake, Microsoft confidential material, unredacted logs, or unsupported public proof claims.
