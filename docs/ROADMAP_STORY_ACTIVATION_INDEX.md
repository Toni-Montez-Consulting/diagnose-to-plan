# Roadmap Story Activation Index

Status: canonical story-to-skill/agent routing index for `docs/ROADMAP_EXECUTION_BACKLOG.md`.

This index answers: when a roadmap/Kanban story becomes relevant, which skill,
template, process, gate, or agent role should activate?

It is intentionally not an autonomous agent manager. It gives the Roadmap
Steward a routing map. Actual agent spawning, repo mutation, public proof,
hosted implementation, and global skill installation still require the existing
human gates.

## Rules

- Use `practice-os/templates/activation-routing-map.md` first when prompt intent is ambiguous.
- Use `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md` and `practice-os/templates/contextual-idea-intake.md` when Toni submits a new idea, design, development enhancement, business move, project request, or automation concept.
- Use `practice-os/templates/roadmap-steward-review.md` before or after major roadmap sessions.
- Use `practice-os/templates/story-activation-contract.md` when a story needs a one-off activation record.
- Use `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` when a story needs Delivery Squad / Business Justification Squad ownership, source-indexed knowledge, approval gates, or a squad handoff receipt.
- Skills auto-trigger only after the relevant skill layer is installed and available in the tool. Until then, this index is the human/agent routing contract.
- Suggested agent roles are recommendations, not permission. Subagents are only used when Toni explicitly asks for agent/delegation/parallel work.
- Every activation must preserve repo boundaries, proof/redaction gates, COI/privacy gates, and no-touch boundaries.

## Agent Role Vocabulary

| Role | Meaning | Gate |
|---|---|---|
| `local-codex` | Current session executes the work directly | normal repo gates |
| `explorer` | Read-only codebase question, independent of the immediate critical path | explicit agent/delegation request |
| `worker` | Bounded implementation slice with clear ownership and disjoint write scope | explicit agent/delegation request |
| `reviewer` | Review/QA pass after implementation | explicit agent/delegation request or external review workflow |
| `parked-autonomy` | Future steward/agent manager or write-enabled automation | evals, guardrails, hosted queue, and human approval first |

## Squad Vocabulary

| Squad | Meaning | Gate |
|---|---|---|
| Delivery Squad | Repo/codebase management, architecture review, implementation scope, tests, verification, and handoff | repo-local gates, approval for mutation/production writes |
| Business Justification Squad | Buyer/operator problem, workflow fit, value, proof posture, client/operator usefulness, and approval posture | business justification scorecard and approval gate for public/client/value claims |

## Epic Activation Map

| Epic | Story family | Primary activation | Suggested agent role | Required gates |
|---|---|---|---|---|
| Reusable Agent SDLC Layer | `tm-skills` creation, CI, install, canary, overlays | `tm-skills` repo docs, install dry-run, `testing-ladder`, `delivery-baseline` | `local-codex`; `reviewer` only after install/canary work | no `install.ps1 -Apply` without explicit approval; doctor/freshness/install dry-run; CI green |
| Practice OS And Client Command Rooms | pattern capture, fit assessment, command-room implementation, proof packet | Command Room fit/spec templates, Roadmap Steward, proof/redaction templates | `local-codex`; `explorer` for candidate repo discovery only if asked | fit assessment before portal UI; proof permission/redaction before screenshots or claims |
| Verification And CI Spine | thin CI, prompt/registry validation, reusable workflows | `testing-ladder`, `delivery-baseline`, repo manifest, evidence index, verification pattern | `local-codex`; `worker` only for disjoint CI slices if asked | run local gate before CI; hard gates stay hard; no shared workflow abstraction before repetition |
| Hosted DTP Phase 0 | schema/app boundary, app shell, import/export, MCP recall | `backend-design`, hosted DTP design doc, boundary decision, steward review | `local-codex`; `worker` only after implementation is explicitly approved | design accepted; hosted implementation requires separate request; no dashboard theater |
| Proof And Redaction Governance | proof templates, first proof pilot, consulting/Omnexus/DeMario/DSE proof lanes | proof packet, redaction queue, permission checklist, evidence checklist, public claim review | `local-codex`; `reviewer` for proof review only if asked | evidence, caveat, permission, redaction, reviewer before public proof |
| Workspace Efficiency Layer | repo manifests, evidence indexes, command-center spec/report, affected checks, dependency policy | repo manifest, evidence index, decision record, workspace command-center spec, `dtp workspace report` | `local-codex`; `explorer` for repo-specific discovery only if asked | do not mutate sibling repos without lane readiness; no live git/CI reads or command runner until the V0 report proves useful |
| Roadmap Steward Loop | steward template, activation map, steward command, hosted queue, agent manager | activation map, steward review, story activation contract | `local-codex`; `parked-autonomy` for future manager | no autonomous edits/status changes; manual loop proves value first |
| Business Brain / Consulting OS | prospect diagnosis, COI, proposals, comms, operator handoff, source-module templates, business role specs | Business Brain source map, Practice OS command contracts, Thought Inbox, Input Studio, Context Pack, Opportunity Score, Exception Register, Value Ledger, Memory Review Queue, diagnose/COI/proposal/handoff skills, comms kit | `local-codex`; `parked-autonomy` for future business agents | DTP remains source of truth; no autonomous agents, public claims, pricing, employer endorsement, or live integrations without review |
| Agent Squads + Knowledge Base V0 | Delivery Squad, Business Justification Squad, source-indexed knowledge, scorecards, approval gates, handoff receipts, future central squad board | Agent Squads source map, squad charter, source index, business justification scorecard, approval gate, squad handoff receipt | `local-codex`; `parked-autonomy` for central board/hosted records | human-led only; no install/dependency; public proof, client comms, production writes, and repo mutation require approval gates |
| Practice OS Strategic Backlog And Client OS Pilot Wave | Greg, CCAAP, Cam pilot order; markdown-first KB V1; consulting audit; Hub/tm-skills readiness; vector/FAOS gates | strategic backlog, Client OS pilot wave, Client OS pilot packet, Knowledge Base V1, architecture review packet, automation authority matrix | `local-codex`; `parked-autonomy` for vector/FAOS/hosted records | draft-only automation; private engagement truth stays private; public proof, sends, scheduling, hosted memory, and write-enabled automation remain gated |
| Future Intelligence Layer | flight records, research radar, mobile app review journeys, eval garden, red-team lab | lesson capture, mobile app review journey, research radar, agent session record, red-team plan | `local-codex`; `reviewer` for red-team only if asked | human-approved learning; evals before autonomy; primary sources and repo evidence for research/launch learning |
| First Client Operating Kit Pilot | Mom kit, fit assessment, proof/redaction, handoff/runbook, public proof | Client Operating Kit, Command Room fit, proof/redaction templates, handoff/runbook | `local-codex`; `explorer` only for public/source discovery if asked | private kit stays private; consent/COI first; public proof blocked until review |
| Adjacent Project Touch Lanes | Omnexus, DeMario, FamilyTrips, DSE, engineering-playbook | repo manifest, portfolio scorecard, proof/COI/privacy lane, repo-specific gates | `local-codex`; `explorer` for scoped repo discovery only if asked | do not disturb active branches; touch only when trigger is ready |
| FAOS Agentic Orchestration Substrate | FAOS spec review, Phase 0 readiness, `op` wrapper, traces, memory, MCP, subagents, hooks, evals, durable workflows | FAOS orchestration roadmap, FAOS phase readiness review, Agentic Performance Gap Review, Roadmap Steward | `local-codex`; `parked-autonomy` for future orchestration | readiness review before implementation; no raw Phase 0 prompt execution; no trace/memory capture before redaction policy |
| Custom Interface Craft Standard | broad UI work, frontend craft, reference promotion, repo-local design pointers | custom interface craft standard, custom craft brief, `tm-skills/frontend-craft`, reference maturity gate | `local-codex`; `reviewer` only if asked for visual/design review | craft brief or hotfix exception before broad UI work; unfinished references stay north-star candidates until promoted |

## Current Active Story Activation

| Active story | Trigger examples | Activation | Agent role | Done gate |
|---|---|---|---|---|
| Fill Mom nonprofit private kit | "use my mom's website", "scope nonprofit rebuild", "fill the Mom kit" | Client Operating Kit, public-source inventory, consent, diagnose, plan, metrics | `local-codex` | private kit updated, redaction check passes, no private data committed |
| Extract owner call actions | "give my mom action items", "turn the call into next steps", "extract the process from the notes" | Owner call-to-action extraction template, owner action packet, facts intake, handoff checklist | `local-codex` | action packet and extraction ledger updated; implementation waits on owner-approved values |
| Complete Command Room fit assessment | "does Mom need a portal", "owner dashboard", "command room" | Command Room fit assessment, no-portal/checklist decision path | `local-codex` | real owner workflow facts decide portal vs checklist vs defer |
| First proof/redaction packet | "can this become proof", "case study", "baseline screenshots" | proof packet, asset inventory, evidence checklist, redaction queue, permission checklist | `local-codex`; `reviewer` only if asked | evidence, caveat, permission, redaction, reviewer before public proof |
| Expand repo manifests | "make every repo covered", "what does this repo own", "which gates run" | repo manifest, evidence index, portfolio scorecard | `local-codex`; `explorer` only if asked | manifest names purpose, gates, proof/privacy lane, deploy/data boundaries |
| Capture mobile app review/launch journey | "App Store approved", "app review", "TestFlight", "Play Console", "mobile launch", "store rejection" | Mobile App Review And Launch pattern, mobile app review journey template, lesson capture, proof/redaction templates if proof is requested | `local-codex`; `reviewer` only if proof review is explicitly requested | launch pattern/template/lesson updated; no credentials or private store screenshots committed; public proof remains gated |
| Hub prompt/registry validation | "Hub prompts", "registry cross-validation", "prompt ids" | `testing-ladder`, Hub prompt/registry validation story | `local-codex`; `worker` only if asked and write scopes are split | local gates pass in both repos; CI-safe path does not require private siblings unless configured |
| Custom interface craft gate | "everything should be custom", "make this less generic", "design it like the consulting process", "custom site/app/admin UI" | Custom Interface Craft Standard, custom craft brief, `tm-skills/frontend-craft`, reference maturity model | `local-codex`; `reviewer` only if asked | brief exists or hotfix exception recorded; reference maturity named; visual/mobile checks pass |
| First Business Brain artifact pass | "Greg prep", "Cameron COI", "Mom/Mario handoff", "diagnose prospect", "draft proposal", "practice comms" | Business Brain source map, command contracts, fixtures, diagnose/COI/proposal/handoff skills, comms kit | `local-codex` | artifacts generated from fixtures, reviewed by Toni before use, lessons captured, no public comms or contracts without human review |
| Consulting proof/offer squad pilot | "run this through squads", "does this proof/offer make business sense", "what squad owns this", "source-index the consulting proof lane" | Agent Squads + Knowledge Base V0, source index, business justification scorecard, approval gate, squad handoff receipt, proof/offer docs | `local-codex` | DTP owns receipt; consulting remains pointer/public surface; no private data or public proof without gates |
| May 2026 Client OS pilot wave | "Greg first", "CCAAP second", "Cam after confirmation", "run the Client OS pilot", "prepare the client operating loop" | Practice OS strategic backlog, Client OS pilot wave, Client OS pilot packet, private engagement kit, Agent Squads V0 if proof/offer/client-comms changes | `local-codex` | private packet and receipt exist; public DTP only summarizes lane/status/gates; automation stays draft-only |
| Knowledge Base V1 and vector brain gate | "build the knowledge base", "vector brain", "semantic recall", "source packs", "agent memory" | Knowledge Base V1, vector brain roadmap, memory promotion record, memory source index | `local-codex`; `parked-autonomy` for retrieval/runtime | markdown corpus and privacy/citation/refusal evals before retrieval implementation |
| Practice architecture and automation authority review | "architecture review", "automation authority", "component/design-system architecture", "Hub/tm-skills readiness" | architecture review packet, automation authority matrix, systems-health-review, repo-local readiness docs | `local-codex` | review packet exists before runtime/schema/global-install/write-enabled automation |
| First Practice OS template pilot | "use the source material", "run the weekly reset", "capture this idea", "score this opportunity", "what did we learn" | Thought Inbox, Input Studio, Context Pack, Opportunity Score, Exception Register, Value Ledger, Memory Review Queue, reprioritization log | `local-codex` | one real cycle records useful output and friction without making templates doctor-required or adding app behavior |

## Idea-To-Story Activation

Use this when the prompt is not yet a backlog story but should be captured.

| Idea shape | First activation | Then attach to | Typical next artifact |
|---|---|---|---|
| Development enhancement | contextual idea intake, repo manifest, `testing-ladder` or `delivery-baseline` | Verification/CI, Workspace Efficiency, or repo-specific lane | work item spec or implementation plan |
| Development implementation | contextual idea intake, story activation index, repo-local gates | owning repo story or new backlog candidate | direct implementation if scoped; otherwise work item spec |
| Product/design | contextual idea intake, Custom Interface Craft Standard, `frontend-craft`, Command Room fit if owner-facing | project lane, Client Command Room lane, or Custom Interface Craft Standard | custom craft brief, design spec, visual QA checklist, or implementation |
| Project/client work | contextual idea intake, Client Operating Kit, COI/consent | Client Operating Kit pilot or adjacent project lane | private kit, handoff, proof packet |
| Business/offer | contextual idea intake, Practice Production Roadmap | consulting/proof/business-ops lane | decision record or roadmap story |
| Agent squad / knowledge base | contextual idea intake, activation map, Agent Squads + Knowledge Base V0 | Agent Squads + Knowledge Base V0 lane | squad charter, source index, scorecard, approval gate, or handoff receipt |
| Client OS pilot | Client OS pilot wave, client reply/cadence operating pattern, private kit | Practice OS Strategic Backlog And Client OS Pilot Wave | private packet, receipt, next-action packet, sanitized status |
| Vector/persistent memory | Knowledge Base V1, Vector Brain roadmap, memory promotion record | Practice OS Strategic Backlog And Client OS Pilot Wave or Future Intelligence Layer | source corpus review, eval seed, retrieval gate |
| Proof/case study | contextual idea intake, proof/redaction templates | Proof And Redaction Governance | proof packet, asset inventory, claim review |
| Research/tooling | contextual idea intake, research radar/spike | Future Intelligence Layer | Adopt/Pilot/Watch/Reject item |
| Mobile app review/launch learning | mobile app review and launch pattern, lesson capture | Future Intelligence Layer and Adjacent Project Touch Lanes | mobile app review journey, approval closeout, rejection repair log, client launch packet |
| Agent/automation | contextual idea intake, activation map, red-team/eval path | Roadmap Steward, Future Intelligence, or `tm-skills` | skill update, eval, guardrail plan, parked automation |
| Agent operating system / FAOS substrate | activation map, FAOS orchestration roadmap, FAOS phase readiness review | FAOS Agentic Orchestration Substrate | readiness review, corrected build prompt, ADR, or parked implementation |

## Story-Level Update Contract

When a backlog story changes status, also check whether one of these needs an update:

- this activation index;
- `practice-os/templates/activation-routing-map.md`;
- `practice-os/templates/roadmap-steward-review.md`;
- `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` and the squad templates;
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`, Client OS pilot wave,
  Knowledge Base V1, vector brain, or architecture review docs;
- repo manifest or evidence index;
- proof/redaction template;
- custom interface craft standard or custom craft brief;
- `tm-skills` trigger description or eval;
- FAOS orchestration roadmap or readiness review when agent substrate prompts change;
- research radar item;
- lesson/eval/agent-session record.

## No-Touch Defaults

- Do not globally install `tm-skills` unless explicitly approved.
- Do not spawn agents unless Toni explicitly asks for agents, delegation, or parallel agent work.
- Do not treat squads as autonomous agents. Squads are ownership, knowledge, justification, approval, and handoff contracts until a separate hosted/agent implementation is accepted.
- Do not start hosted DTP app implementation from a routing/steward prompt alone.
- Do not implement the raw FAOS Phase 0 prompt or create a `faos` repo before the FAOS readiness review is accepted.
- Do not publish or prepare public proof without permission/redaction/reviewer gates.
- Do not mutate `fitness-app`/Omnexus unless its app lane is intentionally reopened.
- Do not fold Hub, consulting, DTP, and project repos into one ownership surface.
