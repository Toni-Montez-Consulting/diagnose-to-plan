# Roadmap Execution Backlog

Status: canonical Kanban-style execution view for the practice roadmap.

This backlog turns the master roadmap into epics and stories. The roadmap remains the source of strategic priority; this file answers what is ready, active, gated, parked, or next for implementation.

Workspace source repo for this backlog: `Projects/diagnose-to-plan`.

## Kanban Rules

Statuses:

- `Done`: implemented to the intended boundary and verified.
- `Review`: artifact exists and needs human acceptance before implementation.
- `Ready`: scoped enough for a future implementation session.
- `Active next`: the next implementation candidate.
- `Blocked`: cannot proceed until a named condition is resolved.
- `Later`: valuable, but intentionally deferred.
- `Parked`: explicitly out of near-term scope.

Story rules:

- Every story must name the owning repo.
- Every story must name the gate that makes it Done.
- Docs/templates/design-boundary work counts as implementation when the roadmap calls for a design or governance artifact.
- Hosted app, agent automation, public proof, and cross-repo command runners require accepted boundary docs before code.
- Project repos stay separate. A story can touch a repo only when its lane is ready.
- Roadmap Steward review is a standing preflight/postflight for major roadmap sessions; it keeps ideas, gates, blockers, and repo coverage out of chat memory.
- Activation routing is the standing prompt-to-process map; it tells future agents which skill, template, gate, or roadmap lane to use without creating autonomy.
- Story activation is the standing story-to-skill/template/agent-role map; `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` ties each epic/story family to the right assets and gates.
- Agentic performance gap review is the standing audit for whether prompts routed correctly, context was sufficient, skills triggered correctly, verification/research/safety gates happened, and misses became durable learning.
- The Practice System Documentation Pack is the standing architecture/audit/optimization layer. Use it to understand the current system, target state, highest-risk gaps, and next optimization stories before creating more platform surface.
- Notion Mirror is a mobile capture and daily-cockpit layer. Use `docs/NOTION_MIRROR_V0.md` before connecting Notion MCP, creating Notion databases, or mirroring roadmap/proof/repo-health records. Notion may capture ideas, but DTP remains the source of truth after steward triage.
- Recurring client cadence uses `docs/RECURRING_CLIENT_CADENCE_OPERATING_PATTERN.md` and `practice-os/templates/recurring-engagement-cadence.md` before Notion or chat memory becomes the operating surface for live meetings.
- Client reply intake uses `docs/CLIENT_REPLY_INTAKE_OPERATING_PATTERN.md` and `practice-os/templates/client-reply-intake.md` before Gmail replies, meeting notes, owner updates, or casual owner-approved facts change DTP state, Notion status, calendar invites, build work, or proof posture.
- Practice memory control uses `docs/PRACTICE_MEMORY_CONTROL_PLANE.md` and `practice-os/templates/memory-control-checkpoint.md` when ideas, connector plans, broad infrastructure choices, status sweeps, or multi-client execution could otherwise live only in chat.
- Agent memory optimization uses `docs/PRACTICE_MEMORY_OPTIMIZATION_PLAN.md`, `practice-os/templates/session-rehydration-checklist.md`, and `practice-os/templates/memory-source-index.md` before hosted storage, vector retrieval, MCP recall, or a private Business Brain assistant becomes implementation work.
- Tooling stewardship uses `docs/PRACTICE_TOOLING_STEWARD.md` and `practice-os/templates/tooling-steward-review.md` before adding, removing, piloting, expanding, or relying on plugins, MCP servers, OAuth apps, CLIs, hosted tools, or business integrations.
- FAOS orchestration is a gated future substrate lane. Use `docs/FAOS_ORCHESTRATION_ROADMAP.md` and `practice-os/templates/faos-phase-readiness-review.md` before any `faos` repo, `op` wrapper, tracing/memory substrate, Spec-Kit rollout, MCP server, subagent roster, hook, durable workflow, or business-agent automation is implemented.
- Custom Interface Craft is a hard gate for broad UI work. Use `docs/CUSTOM_INTERFACE_CRAFT_STANDARD.md` and `practice-os/templates/custom-interface-craft-brief.md` before building or substantially redesigning public sites, apps, admin portals, proof surfaces, or assistant-facing interfaces. Hotfixes may skip only with a documented exception.

## Story Activation Contract

Use `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` before starting or advancing a story when the prompt could imply a specific skill, template, agent role, proof gate, COI gate, or repo touch pass.

Use `practice-os/templates/story-activation-contract.md` when a story needs a dedicated one-off activation record.

Use `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md` and `practice-os/templates/contextual-idea-intake.md` before promoting a new idea, design, business move, project request, development enhancement, or automation concept into a story.

Agent roles in the activation index are recommendations, not permission. Subagents, autonomous managers, global installs, hosted implementation, public proof, and write-enabled automation still require their explicit gates.

## Epic 1: Reusable Agent SDLC Layer

Goal: make every future coding session safer and more consistent.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Create `tm-skills` repo and Phase 1 skills | `tm-skills` | Done | repo pushed, doctor/freshness/install dry-run pass, CI green | global install is applied; external smoke remains manual |
| Add `tm-skills` thin CI | `tm-skills` | Done | GitHub Actions green | keep workflow thin |
| Global install apply | `tm-skills` | Done | `install.ps1 -Apply` succeeds without `-Force` and post-install doctor passes | record smoke status |
| Tool reload smoke test | `tm-skills` plus tools | Later | Codex/Claude/Copilot discover skills after reload | Codex discovery verified; Claude Code and GitHub Copilot reloads remain manual/back-burner |
| Project-pinned canary | `tm-skills` plus one repo | Later | one low-risk repo confirms no duplicate-skill confusion | choose after global install works |
| Stack overlays | `tm-skills` | Later | base skills prove useful across real work | design overlays only after canary |

## Epic 2: Practice OS And Client Command Rooms

Goal: make owner/operator command-room decisions repeatable without building portals by default.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Capture Client Command Room pattern | `diagnose-to-plan` | Done | pattern doc plus fit/spec templates exist and practice doctor passes | use on first pilot |
| First Command Room fit assessment | `diagnose-to-plan` | Done | Mom nonprofit private kit has a completed fit assessment | handoff checklist first; revisit portal only if owner workflow pain is proven |
| Owner call-to-action extraction | `diagnose-to-plan` | Done | reusable template plus Mom action packet and extraction ledger exist | use after owner calls before mutating project repos |
| Client Command Room implementation | candidate project repo | Later | fit assessment says build, owner workflow is real, support/evidence exists | keep optional |
| Command-room proof packet | `consulting` plus source repo | Later | screenshots/walkthroughs redacted and permissioned | wait for real pilot |

## Epic 3: Verification And CI Spine

Goal: make every repo's delivery state observable before dashboards or automation depend on it.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Thin CI for DTP | `diagnose-to-plan` | Done | DTP CI green | preserve local/CI parity |
| Thin CI for consulting | `consulting` | Done | build and secret scan CI green | expand route CI only when browser setup is stable |
| Thin CI for `tm-skills` | `tm-skills` | Done | doctor/freshness/install preview CI green | keep workflow thin; external smoke remains manual |
| Hub workflow review | `hub` | Done | existing CI/security reviewed with no churn | v0.4 hardening later |
| `hub-prompts` full local prompt gate in CI | `hub-prompts` | Done | `npm test` CI green | add eval fixtures later |
| `hub-registry` CI-safe validation | `hub-registry` | Done | `npm run validate` CI green | local `npm test` stays sibling-manifest gate |
| Prompt id cross-validation | `hub-prompts`, `hub-registry` | Done | local `npm test` confirms registry references resolve to sibling prompt ids | keep repo-scoped CI thin until private sibling access is approved |
| Shared reusable workflows | core repos | Later | at least three repos repeat the same stable workflow | do not abstract early |

## Epic 4: Hosted DTP Phase 0

Goal: define and later build the private app foundation for engagements, artifacts, evidence, redaction, proof, and decisions.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Phase 0 schema/app-boundary design | `diagnose-to-plan` | Done | `docs/HOSTED_DTP_PHASE_0.md` accepted | use as implementation boundary later |
| Boundary decision record | `diagnose-to-plan` | Done | `decisions/0004-hosted-dtp-private-practice-os-boundary.md` accepted | preserve boundary |
| Hosted DTP schema/app-shell implementation | `diagnose-to-plan` | Ready | private auth/RLS/storage shell reads real records, no dashboard theater | implement only after Mom pilot/proof workflow gives real records |
| Import/export contract | `diagnose-to-plan` | Ready | local markdown kits can round-trip with hosted records | implement with app shell |
| MCP recall | `diagnose-to-plan` | Later | 2-3 real engagements make manual recall painful | keep deferred |

## Epic 5: Proof And Redaction Governance

Goal: make public proof evidence-backed, permissioned, caveated, and reviewable.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Proof/redaction templates | `diagnose-to-plan` | Done | proof packet, redaction item, permission, evidence, public claim, and asset templates exist | use on first pilot |
| First proof/redaction pilot | `diagnose-to-plan` plus pilot repo | Done | one real project uses proof packet and redaction queue before public proof | internal Mom candidate exists; public proof stays blocked until permission, redaction, reviewer, evidence, and caveat pass |
| Consulting proof backlog | `consulting` | Ready | proof candidates mapped to real source material and redaction state | start after first pilot |
| Omnexus proof candidates | `fitness-app` | Later | claim is permissioned, redacted, reviewed, caveated, and backed by evidence | PR #553 is merged and extracted as an internal reference; do not publish proof without proof packet gates |
| Omnexus App Store approval proof candidate | `fitness-app`, `diagnose-to-plan`, later `consulting` | Later | approval/public-install/first-user-trust claims are separated, permissioned, redacted, reviewed, caveated, and backed by evidence | use the mobile app review pattern internally; public proof waits for proof packet gates |
| DeMario proof packet | `demario-pickleball-1` | Later | launch gates and permission are complete | keep owner-safe |
| DSE internal proof lane | `dse-content` | Later | COI, permission, and redaction review complete | internal/professional only |

## Epic 6: Workspace Efficiency Layer

Goal: reduce rediscovery, setup drift, CI waste, and handoff friction.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| DTP repo manifest/evidence-index pilot | `diagnose-to-plan` | Done | pilot shape accepted as useful | core manifests plus prompt/registry, DeMario, FamilyTrips, engineering-playbook, and Omnexus adjacent passes now exist |
| Consulting repo manifest | `consulting` | Done | manifest names gates, deploy target, proof lane, and data boundaries | keep current during consulting proof/intake work |
| Hub repo manifest | `hub` | Done | manifest names runtime gates, Supabase/Vercel boundaries, and prompt/run ownership | keep current during Hub runtime and prompt/registry work |
| `hub-prompts` repo manifest/evidence index | `diagnose-to-plan`, `hub-prompts` | Done | manifest and evidence index capture prompt catalogue ownership, prompt validation gates, eval lane, and Hub runtime boundary without mutating prompt content | add eval/golden fixtures only when real prompt misfires or high-value workflows justify them |
| `hub-registry` repo manifest/evidence index | `diagnose-to-plan`, `hub-registry` | Done | manifest and evidence index capture target/routing ownership, local registry gates, prompt-id cross-validation, and deferred sibling CI access without mutating targets | keep repo-scoped CI thin; decide sibling CI access only if local-first validation becomes a bottleneck |
| `tm-skills` repo manifest | `tm-skills` | Done | manifest names install gates and global-skill boundaries | keep current during skill smoke/canary work |
| DeMario repo manifest/evidence index | `diagnose-to-plan`, `demario-pickleball-1` | Done | manifest and evidence index capture launch gates, proof blockers, command-room role, and local/CI evidence without mutating app code | use for future command-room proof pass |
| FamilyTrips repo manifest/evidence index | `diagnose-to-plan`, `FamilyTrips` | Done | manifest and evidence index capture privacy model, local/CI gates, release smoke, and no-auth/no-AI boundary | use before future FamilyTrips feature, AI, or public-sharing work |
| Engineering playbook repo manifest/evidence index | `diagnose-to-plan`, `engineering-playbook` | Done | manifest and evidence index capture doctrine/reference boundary, local evidence gates, and DTP source-of-truth pointer | revisit only when general doctrine or portfolio policy changes |
| Omnexus repo manifest/evidence index | `diagnose-to-plan`, `fitness-app` | Done | manifest and evidence index capture verification cockpit reference, release evidence, proof gates, and app-data boundaries without mutating app code | use as reference pattern; no public proof without permission/redaction/reviewer/caveat |
| CCAAP site repo manifest/evidence index | `diagnose-to-plan`, `ccaap-site` | Done | manifest and evidence index capture the private off-Wix prototype boundary, launch gates, Cloudflare target, and proof/privacy blockers | keep CCAAP visible in workspace reporting; production waits on PayPal, contact routing, DNS, authentic assets, owner review, and proof permission |
| Workspace Command Center spec | `diagnose-to-plan` | Done | `docs/WORKSPACE_COMMAND_CENTER_V0.md` defines read-only inputs, outputs, gates, and safety boundaries | no command runner yet |
| Workspace Command Center V0 read-only report | `diagnose-to-plan` | Done | `dtp workspace report` outputs text/JSON from DTP-owned manifests, evidence indexes, backlog, and command-center docs without executing repo commands or calling GitHub; missing repo rows can carry explicit Active Next Queue blockers | use for steward preflight; live git/CI reads remain later |
| GitHub Enterprise org alignment | non-DSE portfolio repos | Done | local remotes, repo manifests, current docs, and `hub-registry` targets use `Toni-Montez-Consulting`; `dse-content` remains personal/Microsoft-linked and COI-gated | keep future repo references on the org namespace; do not move DSE without explicit COI-aware scope |
| GitHub Enterprise org migration closeout | Omnexus, Hub, DTP | Done | Omnexus PR #559 is merged after required review, local protected-repo PR branches are pruned safely, and DTP closeout receipt reflects final state | Closed on 2026-04-30; keep future repo references on the org namespace |
| Hub Dependabot triage V0 | `hub` | Done | selected dependency PRs pass accepted local and remote gates before merge | PR #59 merged after strict audit fix; PR #55 merged after React 19 peer alignment; #54/#56/#61 remain parked for separate review |
| Notion Mirror V0 spec | `diagnose-to-plan` | Done | Notion mirror contract, mirror item template, steward receipt, and roadmap pointers exist without moving source-of-truth ownership | use Notion as mirror/inbox; keep DTP authoritative |
| Notion MCP/manual mirror setup | `diagnose-to-plan`, Notion | Done | Notion smoke page, V0 databases, safe seed records, and phone-friendly views exist; no private data is mirrored without gates | use manually from the phone; future sync starts with DTP dry-run export and steward review |
| Workspace Command Center live status/runner | `diagnose-to-plan` | Later | separate boundary decision accepts live git/CI reads or command execution without weakening repo-local gates | do not implement from the V0 report |
| Affected-only verification | DTP/Hub first | Later | hard gates are reliably encoded per repo | keep advisory until proven |
| Dependency maintenance policy | each repo | Later | grouping/schedule/approval rules accepted | do not enable bots broadly yet |

## Epic 7: Roadmap Steward Loop

Goal: make roadmap execution reliable without relying on Toni's memory or a fully autonomous manager.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Roadmap Steward V0 template and lane | `diagnose-to-plan` | Done | steward template exists, practice doctor enforces it, roadmap/backlog explain the loop | use as standing preflight/postflight |
| AI Activation Map V0 | `diagnose-to-plan` | Done | activation map exists, practice doctor enforces it, and docs explain prompt routing | use with Roadmap Steward reviews |
| First live Roadmap Steward review | `diagnose-to-plan` | Done | one review records current next story, repo lane, gates, blockers, uncaptured ideas, and no-touch boundaries | repeat before Mom nonprofit private kit |
| `dtp steward review` command | `diagnose-to-plan` | Later | command reads workspace/backlog docs and reports coverage or drift without mutating repos | implement only after manual template proves useful |
| Hosted steward queue | hosted DTP | Later | accepted hosted DTP can track steward review items, blockers, and follow-ups | wait for hosted DTP Phase 0 implementation |
| Agent-assisted roadmap manager | DTP/Hub future | Parked | evals, guardrails, proof gates, and human approval exist | no autonomous edits or status changes |

## Epic 8: Future Intelligence Layer

Goal: turn delivery, failures, research, and agent sessions into supervised learning.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Future Intelligence templates | `diagnose-to-plan` | Done | lesson, research, scorecard, flight recorder, red-team, feature flag, and supply-chain templates exist | use opportunistically |
| Agentic Performance Gap Review V0 | `diagnose-to-plan` | Done | performance-gap doc exists, template is required by practice doctor, activation map routes gap prompts | use after major agent-system misses |
| First agent flight record | `diagnose-to-plan` | Ready | one major session leaves a reusable receipt | capture on next complex implementation |
| Omnexus App Store approval learning | `diagnose-to-plan`, `fitness-app` reference | Done | mobile app review/launch pattern, journey template, lesson record, steward receipt, and evidence-index update exist without mutating Omnexus | use on future mobile client builds; keep public proof gated |
| Research Radar first item | `diagnose-to-plan` | Ready | one item classified Adopt/Pilot/Watch/Reject with source and next action | use when research changes roadmap |
| Eval garden | `hub-prompts`, `tm-skills`, DTP | Later | real misfires become fixtures | wait for misfire history |
| Red-team lab | Hub/DTP future agent workflows | Later | adversarial tests exist before write-enabled automation | keep before autonomy |

## Epic 9: First Client Operating Kit Pilot

Goal: run one real engagement through the Practice OS before building more platform surface.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Mom nonprofit kit creation | `diagnose-to-plan` private `engagements/` | Done | kit created with COI, consent, diagnose, plan, and metrics placeholders | owner direction and off-Wix preference captured; finish PayPal/contact/domain/photos/review gates |
| Command Room fit assessment | `diagnose-to-plan` | Done | assessment decides portal vs checklist vs no private surface | handoff checklist first; no UI unless owner workflow proves portal need |
| Proof/redaction use | `diagnose-to-plan` | Done | proof packet and redaction queue item created for one claim candidate | keep internal until reviewed |
| Handoff/runbook | `diagnose-to-plan` plus project repo | Ready | owner-safe handoff exists | after build scope is known |
| Public proof promotion | `consulting` | Blocked | permission, redaction, reviewer, evidence, and caveat all approved | no auto-publish |

## Epic 10: Adjacent Project Touch Lanes

Goal: ensure every workspace repo benefits without unnecessary churn.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Omnexus verification cockpit review | `fitness-app` | Done | merged PR #553 reviewed read-only, reusable lessons extracted into DTP receipts and pattern docs | keep as reference; do not mutate app code unless lane is reopened |
| Omnexus App Store review-to-launch extraction | `diagnose-to-plan`, `fitness-app` reference | Done | DTP captures the App Store approval journey as a mobile app review/launch pattern, template, lesson, steward receipt, and evidence-index update | use for future client mobile app builds; public proof remains gated |
| DeMario launch/proof pass | `demario-pickleball-1` | Later | manual launch/venue/permission gates complete | manifest/evidence index exists; owner-safe proof only |
| FamilyTrips privacy maintenance pass | `FamilyTrips` | Done | data validation/build/test and privacy notes complete | manifest/evidence index exists; revisit before new features, AI, or public sharing |
| DSE COI-aware proof pass | `dse-content` | Later | COI screen and live branch verification complete | internal/professional only |
| Engineering playbook pointer audit | `engineering-playbook` | Done | doctrine points to DTP without duplicating roadmap ownership | DTP-owned manifest/evidence index exists; revisit only for reusable doctrine or policy drift |

## Epic 11: Practice System Documentation And Audit

Goal: document, scrutinize, and optimize the whole consulting operating system without duplicating roadmap ownership across repos.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Current architecture master doc | `diagnose-to-plan` | Done | `docs/PRACTICE_SYSTEM_ARCHITECTURE.md` names repos, flows, gates, and boundaries | keep synced with roadmap changes |
| Future-state master doc | `diagnose-to-plan` | Done | `docs/PRACTICE_SYSTEM_FUTURE_STATE.md` defines hosted DTP, steward, self-learning, research, manifest, and agent target state | read before future platform work |
| System audit and gap review | `diagnose-to-plan` | Done | severity-ranked findings map to follow-up stories | revisit after Mom pilot |
| Agentic performance gap review | `diagnose-to-plan` | Done | required review catches prompt routing, context, skill-trigger, verification, research, safety, and learning-loop gaps | run when a miss is caught |
| Optimization plan | `diagnose-to-plan` | Done | findings convert to epics/stories/gates/owners/sequencing | use to choose next refinements |
| Documentation propagation lane | all workspace repos | Ready | each repo gets a lightweight pointer or local doc when its lane is touched | do not bulk-edit repos now |

## Epic 12: FAOS Agentic Orchestration Substrate

Goal: capture and eventually implement the Frontier Agentic Operating System ideas as a gated orchestration substrate, without replacing DTP, `tm-skills`, Hub, consulting, or repo-local gates.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| FAOS spec technical review and planning integration | `diagnose-to-plan` | Review | `docs/FAOS_ORCHESTRATION_ROADMAP.md`, activation map, backlog, and master roadmap pointers exist | accept as roadmap-only capture |
| FAOS Phase 0 readiness review | `diagnose-to-plan` | Ready | readiness template resolves technical corrections, repo boundary, trace redaction, storage isolation, `uv` package flow, DTP adapter conflict, and COI ownership | run only after current pilot/proof/smoke priorities |
| FAOS Phase 0 foundation implementation | future `faos` repo plus DTP adapters | Later | corrected compose/services, `op` CLI, memory surface, tracing, tests, and ADRs pass accepted Phase 0 gates | do not create repo or services until readiness accepted |
| Spec-Kit project flow pilot | `diagnose-to-plan`, `tm-skills`, then selected repo | Later | one real work item proves Spec-Kit improves planning over existing DTP Work Item Spec | verify CLI syntax and avoid token-heavy ceremony |
| Code agent stack: subagents, hooks, commands | future `faos`, `tm-skills`, DTP | Later | review/test/eval/trace roles have fixtures and path-scoped hooks | no autonomous write behavior before evals and gates |
| Inspect AI eval harness | future `faos`, `tm-skills`, Hub prompts, DTP | Later | real misfires become portable eval fixtures | seed after enough trace/misfire evidence exists |
| Supervised reflection with DSPy/GEPA | future `faos`, `tm-skills`, DTP | Later | reflection proposes changes into human review queue only | requires traces, evals, and no self-modifying skills |
| Durable execution with DBOS/Inngest | future `faos`, hosted DTP/Hub if needed | Later | one real workflow needs crash/sleep survival or multi-day state | simple Postgres state first |
| Cross-project skill propagation | future `faos`, `tm-skills`, project repos | Later | project-local skill promotion has evals, ADR, and human approval | keep globals tight |
| Business agent stack and prediction calibration | future `faos`, DTP/Hub/consulting | Later | business-agent actions are draft/review only and produce scoreable predictions | no auto-send or public/client action |
| Cloud migration | future `faos` | Later | local stack hits explicit pain threshold | local-first until pain forces cloud |

## Epic 13: Cross-Site Assistant Experience

Goal: give the right workspace websites a useful public assistant and, where justified, a private/admin assistant without mixing public content, private records, client data, or unsupported claims.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Cross-site assistant architecture brief | `diagnose-to-plan` | Review | `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md` defines shared gateway direction, per-site manifests, public/admin boundaries, refusal rules, logging/analytics expectations, and rollout order | accept or revise brief and the consulting manifest before any assistant code |
| Consulting public assistant pilot manifest | `diagnose-to-plan`, later `consulting` and Hub/future runtime | Review | `docs/assistant-manifests/consulting-public-v0.md` names approved public route sources, blocked sources, handoff path, refusal policy, logging/analytics plan, and launch gate | accept/revise manifest, then extract repo-local source corpus and tests before any widget/runtime implementation |
| Architected Strength assistant-pattern candidate | `architected-strength`, future runtime owner | Later | `docs/assistant-manifests/architected-strength-public-v0.md` names intended public source corpus, blocked sources, handoff path, refusal policy, logging/analytics plan, and launch gate | revisit after consulting public assistant pilot proves useful |
| DeMario admin assistant pilot | `demario-pickleball-1`, Hub/future runtime | Later | protected admin assistant is read-only first and never sends texts, mutates bookings, changes payments, or cancels lessons without explicit confirmation | wait for owner/admin habits and proof boundaries to stabilize |
| CCAAP assistant lane | `ccaap-site`, future runtime | Later | public assistant only after launch inputs, preview, owner review, contact routing, assets, and privacy/proof decisions are stable | do not implement during current CCAAP launch gate |

## Epic 14: Custom Interface Craft Standard

Goal: make every broad UI surface fully custom and authored while preventing unfinished references from becoming accidental templates.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Practice-wide custom interface standard | `diagnose-to-plan` | Done | standard doc, required template, roadmap pointers, doctor enforcement, and tests exist | use on future broad UI work |
| `frontend-craft` behavior update | `tm-skills` | Done | skill/eval encode custom authored design as the default without weakening practical UI checks | use after tool reload; external smoke remains manual |
| Reference promotion gate | `diagnose-to-plan`, candidate repos | Ready | candidate project has production-level gates, Toni acceptance, clean boundaries, and a DTP note naming reusable lessons | evaluate Architected Strength and consulting only after production-level passes |
| Repo-local custom craft pointers | touched project repos | Later | each repo has local pointer/brief when its lane is active | do not bulk-edit inactive repos |

## Epic 15: Business Brain / Consulting OS

Goal: make DTP the durable operating system for business practice, not only
software delivery.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Business Brain source map | `diagnose-to-plan` | Done | `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md` captures source docs, Claude context, repo mapping, source-of-truth order, proof/comms gates, and forbidden-until-unlocked boundaries | keep updated when Business Brain scope changes |
| Command contracts and first fixtures | `diagnose-to-plan` | Done | `/diagnose-prospect`, `/coi-screen`, `/draft-proposal`, and `/comms-kit` contracts exist with Greg, Cameron, and Mom/Mario fixtures | convert into CLI/eval support only after manual use proves shape |
| Business agent role specs | `diagnose-to-plan` | Done | Controller, General Counsel, and COO specs exist as draft-producing operating modes with escalation rules | keep non-autonomous until evals and write gates exist |
| Private communications kit | `diagnose-to-plan` | Done | pitch kit, explainer, infographic brief, three diagrams, master deck, internal email, LinkedIn drafts, and X thread exist with public review gates | revise after first live conversations |
| First live artifact run | `diagnose-to-plan` | Done | Greg/Cameron/Mom-Mario artifacts were converted into Cam and Greg send-ready packets, CCAAP waiting state, sanitized Notion mirrors, and a steward receipt | use client replies to update private kits first, then seed evals from the observed workflow |
| Client reply intake loop | `diagnose-to-plan` | Done | reply intake pattern/template exist, practice doctor enforces the template, and the first Cam reply is captured without advancing blocked work | use on every Cam/Greg/CCAAP reply before Notion or calendar changes |
| Practice memory control plane | `diagnose-to-plan` | Done | memory control doc, checkpoint template, connector-map update, and steward receipt exist | use before more Notion/QuickBooks/hosted-DTP/agent automation work |
| Agent memory optimization plan | `diagnose-to-plan` | Done | retrieval/persistence ladder, session rehydration checklist, memory source index template, docs map, roadmap pointer, and steward receipt exist | use at the start of broad sessions before relying on chat memory or adding hosted/vector memory |
| Practice OS source material integration | `diagnose-to-plan` | Done | new thesis/spec/schema files are preserved in canonical source paths, integration map/source index/concept registry/conflict register/reprioritization log exist, ADR 0007 preserves additive integration, and source-material evidence closeout is recorded | use source docs through integration docs and templates; do not overwrite current architecture |
| Input Studio / Thought Inbox template pass | `diagnose-to-plan` | Done | manual templates exist for Thought Inbox, Input Studio, Context Pack, Opportunity Score, Exception Register, Value Ledger, and Memory Review Queue | pilot templates on the next real reply or weekly reset cycle before making them stricter gates |
| Schema reconciliation against Hosted DTP Phase 0 | `diagnose-to-plan` | Done | starter schema is mapped against Hosted DTP Phase 0 for RLS, storage pointers, import/export, redaction, proof, evidence, and permission review in `docs/integration/schema_reconciliation_v0.md` | do not run SQL as migration until a merged schema design is accepted |
| First real Practice OS template pilot | `diagnose-to-plan` private kits or steward receipts | Active next | one live Cam, Greg, CCAAP, or weekly reset cycle uses the new templates and records friction without adding app behavior | apply to the next substantive reply or weekly reset |
| Merged hosted-DTP schema design | `diagnose-to-plan` | Ready | a design doc reconciles the source schema, Hosted DTP Phase 0, RLS, storage, import/export, proof/redaction, evidence, data classification, and memory review without running migrations | start only when hosted schema work is explicitly reopened |
| Tooling Steward review loop | `diagnose-to-plan` | Done | tooling steward doc, review template, and steward receipt exist | run first monthly review after two Business Brain reset cycles or before adding a specific connector |
| Business Brain eval garden | `diagnose-to-plan` | Ready | eval garden is ready to seed from fixtures, client replies, and send-confirmation examples for diagnose-prospect, COI, proposal, handoff, and comms anti-slop checks | seed after Cam/Greg replies or send confirmation |
| Controller close loop | `diagnose-to-plan` | Later | weekly-close command contract and fixture exist with financials unavailable when QuickBooks is absent | wait until the first weekly close is needed |
| QuickBooks read-only connector readiness | `diagnose-to-plan`, future hosted DTP/Hub | Blocked | Intuit app/OAuth path, source-of-truth rules, credential storage, allowed entities/reports, and no-write boundary are accepted | use manual exports or mark financials unavailable until Toni approves connector setup |

## Current Active Next Queue

Standing preflight/postflight: use `practice-os/templates/activation-routing-map.md`, `practice-os/templates/agentic-performance-gap-review.md`, and `practice-os/templates/roadmap-steward-review.md` for major roadmap sessions so the right skill/template/process is selected, agentic performance gaps are caught, and new ideas, blockers, repo lanes, gates, and no-touch boundaries are captured before memory drift.

1. Use the Practice Memory Control Plane before expanding infrastructure: capture new ideas, connector plans, client states, decisions, and blockers into DTP first; use Notion only as cockpit/inbox.
2. Use the Agent Memory Optimization Plan for broad sessions: rehydrate from source-aware DTP/git/Gmail/Calendar/Notion checks before acting, and graduate to hosted/vector memory only after the persistence ladder gates are met.
3. Use the Practice OS source material through `docs/integration/source_index.md`, `docs/integration/integration_map.md`, `docs/integration/concept_registry.md`, the new module templates, and `docs/integration/schema_reconciliation_v0.md`; preserve source nuance and prefer templates/docs before code.
4. Pilot the new Thought Inbox, Input Studio, Context Pack, Opportunity Score, Exception Register, Value Ledger, and Memory Review Queue templates on the next real Cam, Greg, CCAAP, or weekly Business Brain reset cycle; keep hosted app/schema implementation separate.
5. Use the Tooling Steward before adding or relying on more plugins/connectors; score usefulness, data risk, source-of-truth fit, maintenance burden, and verification before adding, removing, piloting, or parking tools.
6. Run the recurring client and reply intake loop: Cam weekly after time confirmation, Greg biweekly only if discovery confirms it, CCAAP monthly formal owner check-in, and Toni's weekly Business Brain reset. Update DTP private kits first, then mirror only sanitized status into Notion.
7. Wait for Leah plus Dad's CCAAP review response after the owner packet/prototype link sent on 2026-05-01; collect exact PayPal donate/membership links, contact routing and spam preference, meeting label/destination, domain/DNS access, authentic photos/resources, review notes, and proof decision.
8. Continue the CCAAP off-Wix custom rebuild path only after owner-approved values arrive; production DNS waits for `pnpm validate:launch`.
9. Apply the Custom Interface Craft Standard before broad UI work. Architected Strength and consulting are in-progress north-star candidates, not completed templates, until reference promotion gates pass.
10. Use the Notion Mirror V0 phone inbox and daily views for capture/review; run Roadmap Steward triage before promoting any Notion item into DTP source-of-truth artifacts.
11. Keep QuickBooks as a gated read-only financial connector candidate; no OAuth, token storage, imports, webhooks, or write behavior until the connector boundary is accepted.
12. Keep Architected Strength as its own personal-brand OS. PR #1 is merged into the org-owned private repo; use it as a later assistant-pattern candidate after the consulting public assistant pilot proves the pattern.
13. Keep the cross-site assistant lane at architecture/manifest level until the consulting public manifest, approved source corpus, refusal policy, logging/analytics plan, and human handoff are accepted.
14. Treat the Omnexus App Store approval journey as the first mobile app review-to-launch learning pattern; use `docs/MOBILE_APP_REVIEW_AND_LAUNCH_PATTERN.md` for future client app builds, but do not publish Omnexus proof until proof gates pass.
15. Capture owner-approved CCAAP baseline/after-state evidence for the first proof candidate and run redaction/permission review.
16. Keep Claude Code and GitHub Copilot `tm-skills` discovery smoke testing on the manual back burner; runbook exists, links are healthy, and Codex discovery is verified, but external reload checks remain manual and non-blocking.
17. Keep Hub dependency PRs #54/#56/#61 parked until one is explicitly selected with a migration/security plan; PRs #59 and #55 are merged and no longer block the queue. Older PR #52 is no longer in the active visible queue.
18. Keep Hub prompt/registry cross-validation local-first; decide private sibling-repo CI access only if it becomes worth the operational cost.
19. Use `dtp workspace report` as a read-only steward preflight when checking repo coverage, recorded evidence, suggested gates, blockers, and missing manifest/evidence coverage; missing repo rows may carry explicit Active Next Queue blockers without guessing gates.
17. Keep repo manifests current as lanes are touched; DTP, consulting, Architected Strength, Hub, `hub-prompts`, `hub-registry`, `tm-skills`, DeMario, CCAAP, FamilyTrips, engineering-playbook, and `fitness-app` / Omnexus now have DTP-owned manifests/evidence indexes.
18. Keep DSE blocked until its active branch is clean or explicitly selected with COI-aware scope.
19. Run FAOS Phase 0 readiness review only after the current pilot/proof/smoke/Hub-validation path; do not build FAOS from the raw Phase 0 prompt yet.

Closed on 2026-04-30: GitHub Enterprise org-migration closeout for Omnexus PR #559. The PR merged, local `fitness-app/main` was aligned to `origin/main`, and represented local org-migration branches were deleted.

## Answer To The Kanban Question

Yes, the roadmap should be planned in epic/story fashion. Not every item is ready for implementation today, and that is intentional. The execution model is:

- Strategic roadmap: what matters and why.
- Execution backlog: epics, stories, statuses, Done gates, and next actions.
- Implementation plans: created only when a story moves to `Active next`.
- Code/docs/templates: built only when the story's gate and repo boundary are clear.
