# Roadmap Execution Backlog

Status: canonical Kanban-style execution view for the practice roadmap.

This backlog turns the master roadmap into epics and stories. The roadmap remains the source of strategic priority; this file answers what is ready, active, gated, parked, or next for implementation.

Workspace source repo for this backlog: `Projects/diagnose-to-plan`.

## Kanban Rules

Statuses:

- `Done`: implemented to the intended boundary and verified.
- `Cancelled`: intentionally stopped or rejected, with a closure reason.
- `Superseded`: replaced by a newer plan, boundary, implementation, or story.
- `Discarded`: removed from the tracker because it has no durable value, is unsafe to carry, or has no evidence beyond an assistant suggestion.
- `Review`: artifact exists and needs human acceptance before implementation.
- `Ready`: scoped enough for a future implementation session.
- `Active next`: the next implementation candidate.
- `Blocked`: cannot proceed until a named condition is resolved.
- `Later`: valuable, but intentionally deferred.
- `Parked`: explicitly out of near-term scope.

Story rules:

- Every story must name the owning repo.
- Every story must name the gate that makes it Done.
- Completed, cancelled, superseded, and discarded work must remain visible in the Kaizen/dashboard archive, but terminal rows do not belong in the active execution lanes.
- Docs/templates/design-boundary work counts as implementation when the roadmap calls for a design or governance artifact.
- Hosted app, agent automation, public proof, and cross-repo command runners require accepted boundary docs before code.
- Project repos stay separate. A story can touch a repo only when its lane is ready.
- Roadmap Steward review is a standing preflight/postflight for major roadmap sessions; it keeps ideas, gates, blockers, and repo coverage out of chat memory.
- Activation routing is the standing prompt-to-process map; it tells future agents which skill, template, gate, or roadmap lane to use without creating autonomy.
- Story activation is the standing story-to-skill/template/agent-role map; `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` ties each epic/story family to the right assets and gates.
- Agent Squads + Knowledge Base V0 is the standing squad ownership and
  source-index discipline. Use `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` plus
  the squad templates before agent-squad, knowledge-base, business
  justification, approval-gate, public-proof, client-communication,
  production-write, or repo-mutation work continues.
- Kaizen Kanban capture is the standing intake/index layer. Use `docs/PRACTICE_KAIZEN_KANBAN_SYSTEM.md` and `dtp kaizen capture` for meaningful new ideas, asks, blockers, proof candidates, repo issues, client signals, corrections, and process improvements before promoting them into stories or artifacts.
- Practice Roadmap Horizons is the standing urgent/short/mid/long overlay. Use `docs/PRACTICE_ROADMAP_HORIZONS_2026.md` when a prompt asks for comprehensive planning, feature revisits, envisioning, or sequencing beyond the current active queue.
- Agentic performance gap review is the standing audit for whether prompts routed correctly, context was sufficient, skills triggered correctly, verification/research/safety gates happened, and misses became durable learning.
- The Practice System Documentation Pack is the standing architecture/audit/optimization layer. Use it to understand the current system, target state, highest-risk gaps, and next optimization stories before creating more platform surface.
- Notion Mirror and Command Center is a mobile capture and daily-cockpit layer. Use `docs/NOTION_MIRROR_V0.md` and `practice-os/templates/notion-cockpit-audit.md` before connecting Notion MCP, creating/updating Notion databases, rebuilding dashboard views, or mirroring roadmap/proof/repo-health records. Notion may capture ideas, but DTP remains the source of truth after steward triage.
- Recurring client cadence uses `docs/RECURRING_CLIENT_CADENCE_OPERATING_PATTERN.md` and `practice-os/templates/recurring-engagement-cadence.md` before Notion or chat memory becomes the operating surface for live meetings.
- Client reply intake uses `docs/CLIENT_REPLY_INTAKE_OPERATING_PATTERN.md` and `practice-os/templates/client-reply-intake.md` before Gmail replies, meeting notes, owner updates, or casual owner-approved facts change DTP state, Notion status, calendar invites, build work, or proof posture.
- Practice memory control uses `docs/PRACTICE_MEMORY_CONTROL_PLANE.md` and `practice-os/templates/memory-control-checkpoint.md` when ideas, connector plans, broad infrastructure choices, status sweeps, or multi-client execution could otherwise live only in chat.
- Agent memory optimization uses `docs/PRACTICE_MEMORY_OPTIMIZATION_PLAN.md`, `practice-os/templates/session-rehydration-checklist.md`, and `practice-os/templates/memory-source-index.md` before hosted storage, vector retrieval, MCP recall, or a private Business Brain assistant becomes implementation work.
- Practice intelligence control uses `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md` before broad sessions that combine client replies, Notion cockpit state, Gmail, Calendar, QuickBooks ideas, assistant planning, tools, memory, or roadmap movement. It is the first route map before building more infrastructure.
- Consulting Workspace OS, Requirements Gatherer, and Integrity Layer use `docs/CONSULTING_WORKSPACE_OS_V0.md`, `practice-os/templates/requirements-gathering-brief.md`, `practice-os/templates/requirements-decision-ledger.md`, `practice-os/policies/integrity-layer-craft-standard.md`, and `practice-os/templates/pre-ship-integrity-gate.md` before major features, hotfixes, cleanup, UI/design, backend/data, public copy, business strategy, client work, or operations work need risk-sized discovery, a build-ready brief, or a quality/handoff gate.
- UAT Kit uses `docs/UAT_KIT_V0.md` and `practice-os/templates/uat-receipt.md` when meaningful work needs acceptance evidence for user journeys, mobile/desktop states, errors, empty states, privacy/proof boundaries, AI output, handoff, caveats, or reusable pattern review.
- Business Admin OS uses `docs/BUSINESS_ADMIN_OPERATING_SYSTEM.md`, `practice-os/templates/business-admin-item.md`, `practice-os/templates/calendar-policy.md`, and `practice-os/templates/apple-reminders-capture-pilot.md` before Google Workspace, Calendar/Meet, Apple Reminders capture, LLC readiness, EIN/banking/tax, contracts, insurance, or brand/admin overhead becomes live process. The internal offer repertoire uses `docs/INTERNAL_OFFER_REPERTOIRE_CATALOG.md` and `practice-os/templates/offer-catalog-item.md` before new delivery patterns become public offers.
- Tooling stewardship uses `docs/PRACTICE_TOOLING_STEWARD.md` and `practice-os/templates/tooling-steward-review.md` before adding, removing, piloting, expanding, or relying on plugins, MCP servers, OAuth apps, CLIs, hosted tools, or business integrations.
- FAOS orchestration is a gated future substrate lane. Use `docs/FAOS_ORCHESTRATION_ROADMAP.md` and `practice-os/templates/faos-phase-readiness-review.md` before any `faos` repo, `op` wrapper, tracing/memory substrate, Spec-Kit rollout, MCP server, subagent roster, hook, durable workflow, or business-agent automation is implemented.
- Custom Interface Craft is a hard gate for broad UI work. Use `docs/CUSTOM_INTERFACE_CRAFT_STANDARD.md` and `practice-os/templates/custom-interface-craft-brief.md` before building or substantially redesigning public sites, apps, admin portals, proof surfaces, or assistant-facing interfaces. Hotfixes may skip only with a documented exception.

## Story Activation Contract

Use `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` before starting or advancing a story when the prompt could imply a specific skill, template, agent role, proof gate, COI gate, or repo touch pass.

Use `practice-os/templates/story-activation-contract.md` when a story needs a dedicated one-off activation record.

Use `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` and
`practice-os/templates/squad-handoff-receipt.md` when a story needs squad
ownership, source-indexed knowledge, business justification, approval gates, and
a handoff receipt.

Use `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md` and `practice-os/templates/contextual-idea-intake.md` before promoting a new idea, design, business move, project request, development enhancement, or automation concept into a story.

Use `dtp kaizen capture`, `dtp kaizen status`, and `dtp kaizen mirror --dry-run` as the lightweight operator loop before creating a larger intake artifact.

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
| CMS/editor-fit skill candidate | `tm-skills`, DTP | Parked | CCAAP plus at least one more project prove repeated CMS/editor decision need, trigger evals are clear, and DTP ladder remains tool-agnostic | keep as planning only in `docs/CMS_EDITOR_TOOLING_DECISION_LADDER.md`; do not create the skill yet |

## Epic 2: Practice OS And Client Command Rooms

Goal: make owner/operator command-room decisions repeatable without building portals by default.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Capture Client Command Room pattern | `diagnose-to-plan` | Done | pattern doc plus fit/spec templates exist and practice doctor passes | use on first pilot |
| First Command Room fit assessment | `diagnose-to-plan` | Done | Mom nonprofit private kit has a completed fit assessment | handoff checklist first; revisit portal only if owner workflow pain is proven |
| Owner call-to-action extraction | `diagnose-to-plan` | Done | reusable template plus Mom action packet and extraction ledger exist | use after owner calls before mutating project repos |
| Live intake to Practice OS workflow | `diagnose-to-plan` | Done | DTP operating pattern and prospect-intake triage template explain how Hub intake becomes fit, offer-route, artifact, approval-gate, and handoff decisions | use on the next real prospect intake before expanding Hub, Notion, email, or hosted DTP behavior |
| Prospect follow-up drafting kit | `diagnose-to-plan` | Done | follow-up playbook plus Diagnostic Call, paid-Blueprint, and park/decline templates exist with send, pricing, proof, calendar, and data gates intact | use only after prospect-intake triage; approved public booking link appears after intake submission; no direct event creation, pricing, or send action without Toni approval |
| Admin-surface operating-room pattern | `diagnose-to-plan` | Done | `practice-os/patterns/admin-surface-operating-room.md` promotes the public-proof-outside/protected-operations-inside/handoff-record pattern | use with fit assessment before building portals |
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
| Hosted DTP schema/app-shell implementation | `diagnose-to-plan` | Done | Phase 0 schema, RLS policies, screen contract, and app-shell scaffold exist without dashboard/client-portal scope | preserve as the data boundary |
| Hosted DTP Phase 0.2 private UI/governance | `diagnose-to-plan` | Done | Vite React private UI renders through a real entrypoint, reads/writes the core Supabase tables through Auth/RLS, keeps smoke fixtures as tagged RLS regression, has accepted real-operator/backup-export/deployment posture, and passed live smoke against the dedicated `DTP Private` Supabase project | use only with markdown fallback until one more real operating loop proves the lane |
| Import/export contract | `diagnose-to-plan` | Done | markdown/private-kit import/export contract exists with blocked export rules, tested local helpers, and a passed live Business Brain round trip exported to steward markdown | repeat on the next client reply or weekly reset before storing client-sensitive non-smoke records |
| MCP recall | `diagnose-to-plan` | Later | 2-3 real engagements make manual recall painful | keep deferred |

## Epic 5: Proof And Redaction Governance

Goal: make public proof evidence-backed, permissioned, caveated, and reviewable.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Proof/redaction templates | `diagnose-to-plan` | Done | proof packet, redaction item, permission, evidence, public claim, and asset templates exist | use on first pilot |
| First proof/redaction pilot | `diagnose-to-plan` plus pilot repo | Done | one real project uses proof packet and redaction queue before public proof | internal Mom candidate exists; public proof stays blocked until permission, redaction, reviewer, evidence, and caveat pass |
| Practice proof queue index | `diagnose-to-plan` | Done | `docs/PRACTICE_PROOF_QUEUE_INDEX.md` maps CCAAP, Omnexus, DeMario, Hub/intake, Architected Strength, consulting assistant, Business Brain, and DSE proof posture | review weekly and before public proof movement |
| Practice thesis and offer map | `diagnose-to-plan` | Done | `docs/PRACTICE_THESIS_AND_OFFER_MAP.md` maps the practice thesis, offer lanes, active pilots, proof posture, and next offer decisions | use before public consulting copy changes or pilot proof framing |
| Practice public offer sequence | `diagnose-to-plan`, later `consulting` | Done | `docs/PRACTICE_PUBLIC_OFFER_SEQUENCE.md` chooses broad front door plus Blueprint/Fast Track/Implementation buying path for the next public positioning pass | use before editing public offer hierarchy |
| Builder-led offer model | `diagnose-to-plan`, later `consulting` | Done | `docs/PRACTICE_BUILDER_LED_OFFER_MODEL.md` captures builder-who-consults positioning, pricing posture, Blueprint deliverables, client fit, proof tiers, and collaboration memory | use before pricing, proposal, SOW, or public-offer changes |
| Offer-to-proof matrix | `diagnose-to-plan` | Done | `docs/OFFER_TO_PROOF_MATRIX.md` maps the three V0 offers to existing proof, missing proof, eligibility, and blocked claims | use before consulting offer-copy refresh |
| Live intake receipt packet | `diagnose-to-plan`, later `consulting` and `hub` | Done | `practice-os/templates/live-intake-receipt.md` records approved live intake smoke, Hub row verification, cleanup, and proof boundary | use only when live intake check is approved |
| Consulting proof backlog | `consulting` | Ready | proof candidates mapped to real source material and redaction state | start after first pilot |
| Omnexus proof candidates | `fitness-app` | Later | claim is permissioned, redacted, reviewed, caveated, and backed by evidence | PR #553 is merged and extracted as an internal reference; do not publish proof without proof packet gates |
| Omnexus App Store approval proof candidate | `fitness-app`, `diagnose-to-plan`, later `consulting` | Later | approval/public-install/first-user-trust claims are separated, permissioned, redacted, reviewed, caveated, and backed by evidence | use the mobile app review pattern internally; public proof waits for proof packet gates |
| DeMario launch-feedback social/proof packet | `demario-pickleball-1`, `diagnose-to-plan`, later social channels | Done | text-only/channel-copy packet is permissioned, caveated, public-safe, posted from Toni-owned channels, and exact public URLs are recorded | keep private screenshots, testimonials, metrics, admin rows, payment proof, and booking data gated unless separately reviewed |
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
| No-server workspace dashboard panel | `diagnose-to-plan`, VS Code workspace | Done | `docs/WORKSPACE_DASHBOARD_READONLY.md` defines a generated dashboard from DTP-owned report, Kaizen, proof, and sweep-ledger artifacts; `tools/vscode-dtp-dashboard` opens it in VS Code without a server, watcher, live command runner, or third-party board source of truth | generate only from read-only DTP artifacts; keep panel cache in ignored `outputs/workspace-dashboard.html` |
| Workspace cockpit redesign and deterministic task recovery | `diagnose-to-plan` | Done | `practice-os/workspace/task-ledger.jsonl`, `dtp workspace recover --dry-run`, `dtp workspace validate-dashboard`, sanitized Notion export, task-ledger parser, Item Register, Recovery Inbox, cockpit tabs/search, and dashboard tests exist without raw transcript copying or live repo/cloud calls | use recovery dry-run, the Recovery Inbox, validation report, and reviewed `--apply` imports when older completed, active, blocked, cancelled, superseded, or unreviewed candidates feel missing |
| Codex chat recovery closeout | `diagnose-to-plan` | Done | `docs/CODEX_CHAT_AND_IMPLEMENTATION_RECOVERY_AUDIT_2026-05-05.md` is committed, DTP docs map the recovery reports, and `prompts/recovery-closeout.spec.md` stores the reusable prompt patterns | use the focused audit as closeout evidence; treat the broad audit as source evidence only |
| Workspace docs and Codex chat sweep archive | `diagnose-to-plan`, all workspace repos | Done | `docs/WORKSPACE_DOCS_AND_CHAT_SWEEP_LEDGER_2026-05-05.md`, terminal Kaizen rows, and generated dashboard Closed Work/Sweep Coverage views exist for the 13-repo workspace and Codex session inventory without copying raw transcripts or private/COI material | use the sweep ledger before broad workspace status claims; keep closed work visible but outside active lanes |
| Reusable recovery prompt/spec pack | `diagnose-to-plan` | Done | `prompts/recovery-closeout.spec.md` captures roadmap synthesis, prompt-to-implementation audit, buildspec review, repo audit, handoff, and assistant QA prompt shapes | keep in DTP unless a future Hub runtime prompt needs to move to `hub-prompts` |
| DSE workspace coverage | `diagnose-to-plan`, `dse-content` | Done | DTP manifest/evidence row exists while preserving COI and proof gates | live DSE validation remains required before implementation or proof |
| GitHub Enterprise org alignment | non-DSE portfolio repos | Done | local remotes, repo manifests, current docs, and `hub-registry` targets use `Toni-Montez-Consulting`; `dse-content` remains personal/Microsoft-linked and COI-gated | keep future repo references on the org namespace; do not move DSE without explicit COI-aware scope |
| GitHub Enterprise org migration closeout | Omnexus, Hub, DTP | Done | Omnexus PR #559 is merged after required review, local protected-repo PR branches are pruned safely, and DTP closeout receipt reflects final state | Closed on 2026-04-30; keep future repo references on the org namespace |
| Hub Dependabot triage V0 | `hub` | Done | selected dependency PRs pass accepted remote gates before merge | PRs #74, #75, and #76 merged on 2026-05-11 after CI/security checks passed; keep blocked PRs #77 and #78 parked for targeted Hub-local fixes |
| Hub blocked dependency fix pass | `hub` | Blocked | failing dependency PRs are reproduced locally, fixed or superseded, and pass CI/security before merge | PR #77 fails build-test after `@hono/zod-openapi` 1.4.0; PR #78 fails typecheck/build-test after Tailwind 4.3.0; do not merge without a dedicated Hub pass |
| Notion Mirror V0 spec | `diagnose-to-plan` | Done | Notion mirror contract, mirror item template, steward receipt, and roadmap pointers exist without moving source-of-truth ownership | use Notion as mirror/inbox; keep DTP authoritative |
| Notion Command Center V1 ergonomics | `diagnose-to-plan`, Notion | Done | existing `DTP Practice OS Command Center` is audited, tightened in place, linked to DTP source paths, and verified with one sanitized DTP steward receipt mirror without private data | use in the next Business Brain reset before adding automation |
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
| First agent flight record | `diagnose-to-plan` | Done | `practice-os/steward/2026-05-14-workspace-os-uat-rollout-agent-flight-record.md` captures the Workspace OS/UAT rollout, touched repos, PRs, verification, failures, lessons, follow-ups, and eval candidates | use `practice-os/templates/agent-session-record.md` on the next complex implementation |
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
| Omnexus release/live-proof closeout | `fitness-app`, App Store Connect | Waiting | monthly/annual subscriptions are operator-reported `Approved`, the app now works with subscriptions, and the product/subscription blocker is closed | verify the selected App Store Connect candidate build/version is `1.0.1`, then complete final smoke, provider/data, observability, first-availability, and non-sensitive release-proof notes without changing IAP products or code |
| DeMario launch/social proof prep | `demario-pickleball-1`, `diagnose-to-plan` | Done | social/proof packet is permissioned, caveated, public-safe, posted without exposing private admin/booking/payment details, and exact post URLs are recorded | keep private admin, booking, payment, student, testimonial, screenshot, and metric material gated unless separately reviewed |
| Consulting public-site fix/readiness pass | `consulting` | Done | PR #3 records green local gates, green CI, live route smoke, Hub-first intake proof, and remaining manual gates without broad redesign | preserve the receipt; synthetic live intake is verified, cleanup remains structural because Hub has no intake archive/delete endpoint, and human desktop/mobile taste review remains |
| Architected Strength finish/fix public-signal pass | `architected-strength` | Done | PR #3 merged the P0/P1 public-signal pass with homepage clarity, proof posture, collaboration-route polish, route copy/layout finish, claim-hygiene review, visual QA, and full repo gates | keep assistant-pattern work, publishing, Azure deploy, Notion writes, consulting copy, and public proof expansion gated until separately reopened |
| DeMario launch/proof pass | `demario-pickleball-1` | Later | manual launch/venue/permission gates complete | broader proof packet remains owner-safe until permission, review, and redaction complete |
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

## Epic 11A: Agent Squads + Knowledge Base V0

Goal: make squad ownership, knowledge scope, business justification, approval,
and handoff explicit before hosted persistence or central squad boards exist.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Agent Squads source map | `diagnose-to-plan` | Done | `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` defines V0 squads, knowledge scope, approval gates, first pilot, and future persistence boundary | use before squad/KB work |
| V0 squad templates | `diagnose-to-plan` | Done | squad charter, source index, handoff receipt, business justification scorecard, and approval gate templates exist | pilot on consulting proof/offer lane |
| Consulting local pointer | `consulting` | Done | consulting docs point future agents back to DTP instead of owning squad state | keep pointer lightweight |
| Consulting proof/offer pilot | `diagnose-to-plan`, `consulting` | Ready | one consulting proof/offer work item uses source index, scorecard, approval gate, and handoff receipt without exposing private data | run on the next proof/offer move |
| Central squad board | hosted DTP | Later | story/handoff receipts prove the interaction model is useful | do not build before repeated receipts |
| Hosted squad records | hosted DTP | Later | hosted DTP persists squad charter, source index, scorecard, approval gate, and receipt while markdown remains fallback | wait for real V0 operating loops |

## Epic 11B: Practice OS Strategic Backlog And Client OS Pilot Wave

Goal: prove the Practice OS through real draft-only client/operator loops before
adding heavier hosted, vector, or orchestration infrastructure.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Practice OS strategic backlog | `diagnose-to-plan` | Active next | `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md` captures P0/P1/P2/P3 sequence, repo roles, draft-only automation, vector path, FAOS hold, and Workflow Spine P0 order | use as the current sequence for this wave |
| Workflow Spine P0 plan | `diagnose-to-plan` | Done | steward receipt defines P0-only order: lifecycle vocabulary, `tm-skills` scorecard, Workflow Spine template, Greg record, Cam record, and obvious stale labels | use as the source receipt for future P1 dashboard/archive work |
| Minimal doc lifecycle labels | `diagnose-to-plan` | Done | `practice-os/policies/document-lifecycle.md` defines labels and `docs/WORKSPACE_COMMAND_CENTER_V0.md` is labeled as historical reference without move/delete/archive churn | keep labels DTP-first before supporting repo cleanup |
| `tm-skills` readiness scorecard | `diagnose-to-plan`, `tm-skills` | Done | `docs/TM_SKILLS_READINESS_SCORECARD.md` classifies phase-1, incubator, parked, candidate, and high-risk skills with use/blocked-use gates and activation-map status | do not promote candidates without separate review |
| Workflow Spine template | `diagnose-to-plan` | Done | `practice-os/templates/workflow-spine.md` defines required frontmatter, allowed/blocked actions, gates, source index, proof posture, dashboard mirror fields, receipt register, and closeout condition | use stable `active-workflow-spine.md` files while receipts stay accurate |
| Greg Workflow Spine record | private `engagements/greg-thegrantapp` | Done | Greg has one active Workflow Spine record for launch-readiness discovery with source files, proof gate, allowed/blocked actions, receipt register, and post-meeting update target | update after the 2026-05-08 meeting |
| Cam Workflow Spine record | private `engagements/cameron-mckesson` | Done | Cam has one active Workflow Spine record that preserves waiting-on-packet/build-readiness state and blocks premature repo/proof/production movement | update only after the item packet or Toni-confirmed state change |
| May 2026 Client OS pilot wave | private `engagements`, sanitized DTP | Active next | Greg, CCAAP, and Cam each get a packet/receipt or an explicit waiting-state record without public proof leakage | run through Workflow Spine for Greg and Cam first; keep CCAAP in existing packet lane until reopened |
| Knowledge Base V1 markdown corpus | `diagnose-to-plan` | Ready | V1 doc and templates define source-indexed records, metadata, validation risks, and hosted-DTP scale path | use the Greg/CCAAP loops to test friction before adding doctor gates |
| Architecture review packet | `diagnose-to-plan`, touched repos | Ready | architecture packet defines ownership, systems-health review, automation authority, and next sequence | use before consulting/Hub/tm-skills cleanup implementation |
| Consulting UX/design-system audit | `consulting` | Active next | repo-local audit covers CTA clarity, visual polish, proof presentation, component/design-system health, and route/data-flow architecture without public proof changes | keep proof changes blocked until DTP proof gates pass |
| Hub runtime readiness note | `hub` | Ready | Hub repo records near-term intake/runtime/console hardening without CRM, DTP cockpit, proof, or billing ownership | keep v0.4 hardening first |
| tm-skills readiness note | `tm-skills` | Ready | repo records doctor/freshness/install preview, untracked skill candidates, and manual external smoke state | do not promote candidate skills or run global install without a separate gate |
| Vector Brain path | `diagnose-to-plan` | Ready | roadmap defines markdown-first corpus, sanitized local retrieval, hosted/RLS retrieval, and agent-integrated retrieval gates | do not implement retrieval until corpus and privacy evals exist |
| FAOS post-pilot readiness | `diagnose-to-plan`, future `faos` | Later | at least two Client OS loops complete before another FAOS readiness pass | keep implementation parked |

## Epic 12: FAOS Agentic Orchestration Substrate

Goal: capture and eventually implement the Frontier Agentic Operating System ideas as a gated orchestration substrate, without replacing DTP, `tm-skills`, Hub, consulting, or repo-local gates.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| FAOS spec technical review and planning integration | `diagnose-to-plan` | Done | `docs/FAOS_ORCHESTRATION_ROADMAP.md`, activation map, backlog, and master roadmap pointers exist | keep as roadmap-only capture |
| FAOS Phase 0 readiness review | `diagnose-to-plan` | Done | `practice-os/steward/2026-05-03-faos-phase-0a-readiness-review.md` checks current Langfuse, Mem0, Letta, and Spec-Kit docs, repo boundary, trace redaction, storage isolation, DTP adapter conflict, and COI ownership | implementation remains parked until Toni accepts a separate FAOS build pass |
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
| Workspace roadmap deep audit and focus queue | `diagnose-to-plan`, private `engagements` reference | Done | `practice-os/steward/2026-05-04-workspace-roadmap-deep-audit.md` and private `engagements/2026-05-04-engagement-vault-status.md` classify Now, Waiting, Parked, PR, repo, DSE, and engagement-vault state | use the audit's three-item Now queue before starting new broad workspace work |
| Private engagement-vault durability pass | private `engagements` repo | Active next | private engagement diff is reviewed, coherent client-kit state is committed in the nested vault, and a private remote decision is recorded before any push | do not public-commit client kit material; configure/push only to an approved private remote |
| Kaizen Kanban operating loop and CLI | `diagnose-to-plan`, Notion mirror | Done | DTP source doc, `practice-os/kaizen/` index, terminal archive statuses, closure metadata, `dtp kaizen capture/update/status/mirror --dry-run`, private/COI redacted committed stubs, ignored raw-private state, doctor gate, tests, and Notion write guard exist | capture meaningful new ideas/asks/state changes here before promotion; close done/cancelled/superseded/discarded rows with evidence; live Notion apply remains gated |
| Practice roadmap horizon overlay | `diagnose-to-plan` | Done | `docs/PRACTICE_ROADMAP_HORIZONS_2026.md` organizes urgent, short-term, mid-term, long-term, feature-enhancement, cadence, and do-not-build lanes without replacing the backlog | use before broad planning/envisioning sessions |
| Practice memory control plane | `diagnose-to-plan` | Done | memory control doc, checkpoint template, connector-map update, and steward receipt exist | use before more Notion/QuickBooks/hosted-DTP/agent automation work |
| Agent memory optimization plan | `diagnose-to-plan` | Done | retrieval/persistence ladder, session rehydration checklist, memory source index template, docs map, roadmap pointer, and steward receipt exist | use at the start of broad sessions before relying on chat memory or adding hosted/vector memory |
| Practice Intelligence Control Plane V0 | `diagnose-to-plan` | Done | control-plane doc, memory-source index, tooling snapshot, Notion cockpit confirmation, and steward receipt exist without hosted app, QuickBooks OAuth, assistant runtime, vector memory, or autonomy | use as broad-session preflight before client/infrastructure work |
| Consulting Workspace OS + Requirements Gatherer V1 | `diagnose-to-plan` | Done | DTP canonical plan, requirements brief template, decision ledger template, steward receipt, first lean consulting pattern candidates, roadmap pointer, and reprioritization log exist without public-site, app-code, Hub, hosted-DTP, or `tm-skills` mutation | review the four draft pattern candidates after real use, apply Requirements Gatherer on the next two meaningful requests, then decide whether to create a `tm-skills` skill |
| Integrity Layer / Craft Standard V0 | `diagnose-to-plan` | Done | DTP policy and pre-ship gate template exist, Workspace OS points to them, and no public-site, app-code, Hub, hosted-DTP, or `tm-skills` mutation occurred | apply the gate during the consulting pattern scan, UAT Kit work, and any public/client/operator-facing handoff |
| UAT Kit V0 | `diagnose-to-plan` | Done | DTP manual UAT standard, reusable UAT receipt, Workspace OS pointer, steward receipt, three consulting UAT pilots, friction review, roadmap pointer, and reprioritization log exist without public-site, app-code, Hub, hosted-DTP, browser-automation, production, private-vault, or `tm-skills` mutation | keep the base receipt canonical; use V0.1 proof-readiness, boundary-only, and operator-surface modes; wait for one more meaningful non-consulting or client-facing receipt before narrower templates or `tm-skills` behavior |
| Platform Operating Patterns V0 | `diagnose-to-plan` | Done | DTP manual plan, five reusable templates, five draft pattern candidates, Workspace OS pointer, and steward receipt exist without Greg proof movement, public copy, Hub runtime, production, hosted-DTP, app code, or `tm-skills` mutation | use Launch Momentum Receipt only after the Greg meeting if approved; test Environment Ledger/Preview Receipt on Hub or Omnexus before promotion |
| Memory Spine V1 CLI/doctor gate | `diagnose-to-plan` | Done | `dtp memory status` checks source docs/templates/receipts, practice doctor requires memory and correction templates, and broad-session correction is captured as a template | use before long-context or memory-heavy implementation sessions |
| Practice OS source material integration | `diagnose-to-plan` | Done | new thesis/spec/schema files are preserved in canonical source paths, integration map/source index/concept registry/conflict register/reprioritization log exist, ADR 0007 preserves additive integration, and source-material evidence closeout is recorded | use source docs through integration docs and templates; do not overwrite current architecture |
| Input Studio / Thought Inbox template pass | `diagnose-to-plan` | Done | manual templates exist for Thought Inbox, Input Studio, Context Pack, Opportunity Score, Exception Register, Value Ledger, and Memory Review Queue | pilot templates on the next real reply or weekly reset cycle before making them stricter gates |
| Schema reconciliation against Hosted DTP Phase 0 | `diagnose-to-plan` | Done | starter schema is mapped against Hosted DTP Phase 0 for RLS, storage pointers, import/export, redaction, proof, evidence, and permission review in `docs/integration/schema_reconciliation_v0.md` | do not run SQL as migration until a merged schema design is accepted |
| First real Practice OS template pilot | `diagnose-to-plan` private kits or steward receipts | Done | one live weekly reset/source-state cycle used the new templates and recorded friction without adding app behavior | repeat on the next substantive client reply before making templates doctor-required |
| Second-cycle client reply/template pilot | `diagnose-to-plan` private kits or steward receipts | Active next | the next Cam, Greg, CCAAP, or weekly reset update uses reply intake plus the module templates and records friction | apply when the next real reply arrives |
| Merged hosted-DTP schema design | `diagnose-to-plan` | Ready | a design doc reconciles the source schema, Hosted DTP Phase 0, RLS, storage, import/export, proof/redaction, evidence, data classification, and memory review without running migrations | start only when hosted schema work is explicitly reopened |
| Tooling Steward review loop | `diagnose-to-plan` | Done | tooling steward doc, review template, and steward receipt exist | run first monthly review after two Business Brain reset cycles or before adding a specific connector |
| CMS/editor tooling decision ladder | `diagnose-to-plan` | Done | planning doc routes Sanity/CMS/editor/page-builder decisions across repos without authorizing implementation | use before any new CMS, owner editor, page builder, `/admin`, or content-management skill work |
| Google Workspace + Business Admin operating lane | `diagnose-to-plan`, `consulting`, Notion | Done | DTP source doc, templates, steward receipt, sanitized Notion mirror plan, Apple Reminders-first lane, starter DMARC, and `/admin` launcher scope exist without filing, all-reminders sync, or private public-site data | keep DMARC in monitoring mode; tighten only after separate review |
| Apple Reminders-first task system | `diagnose-to-plan`, Notion, iOS | Done | Apple Reminders is Toni's daily action system, Google Tasks is out of scope, and any bridge starts with `Consulting` only if useful | use Apple Reminders normally; do not introduce Google Tasks |
| Founder Calendar/Meet connector and booking setup | Google Workspace, `diagnose-to-plan` | Done | Google Calendar and Gmail connectors return the founder mailbox, appointment schedules are tested, and booking/Meet/mailbox flow works | maintain booking pages and questions/reminders in Google Calendar |
| Starter DMARC policy | Google Workspace, `diagnose-to-plan` | Done | `_dmarc.tonimontez.co` TXT exists with `v=DMARC1; p=none; pct=100` | recorded in `practice-os/steward/2026-05-06-starter-dmarc-receipt.md`; keep monitoring mode until a separate review |
| Internal offer repertoire catalog | `diagnose-to-plan` | Done | private offer-candidate catalog exists with proof/repeatability/privacy/public-status gates | add the next reusable delivery pattern with `practice-os/templates/offer-catalog-item.md` |
| Business Brain weekly operating packet | `diagnose-to-plan` | Done | weekly packet template captures client next actions, proof status, blockers, value ledger, offer learning, and memory promotion | run at weekly reset and after broad business-intelligence sessions |
| First Business Brain weekly reset | `diagnose-to-plan` | Done | `practice-os/steward/2026-05-03-business-brain-weekly-reset.md` records current lanes, blockers, value ledger, proof status, offer learning, and top actions | repeat at next weekly reset or after real replies |
| Consulting intelligence fixture set | `diagnose-to-plan` | Done | public-safe eval cases exist for diagnosis, scope, proof safety, follow-up, handoff, operator voice, evidence dossier depth, and memory correction across active lanes | convert into automated evals only after more real answer examples accumulate |
| Business Brain eval garden | `diagnose-to-plan` | Seeded | `practice-os/fixtures/consulting-intelligence/eval-cases.json` seeds machine-readable cases and includes a real evidence-dossier-depth misfire | add real reply examples after the next Cam/Greg/CCAAP reply |
| Real reply eval seed queue | `diagnose-to-plan` | Done | `practice-os/fixtures/consulting-intelligence/real-reply-seed-queue.md` names the next reply patterns to convert into sanitized evals | fill only after real replies arrive |
| Authentic Voice and Anti-Slop System | `diagnose-to-plan`, `consulting` | Done | DTP owns the canonical standard, audit template, updated proof/public-claim/correction templates, anti-slop eval cases, advisory scanner, and consulting current-state copy audit | use the audit before public copy, client emails, proof packets, assistant-source updates, or broad roadmap synthesis |
| Controller close loop | `diagnose-to-plan` | Later | weekly-close command contract and fixture exist with financials unavailable when QuickBooks is absent | wait until the first weekly close is needed |
| QuickBooks read-only connector readiness | `diagnose-to-plan`, future hosted DTP/Hub | Blocked | Intuit app/OAuth path, source-of-truth rules, credential storage, allowed entities/reports, and no-write boundary are accepted | use manual exports or mark financials unavailable until Toni approves connector setup |
| Business Admin OS public-offer timing | `diagnose-to-plan`, later `consulting` | Review | Business Admin OS components are split between internal operating infrastructure, backlog items, and proof-gated offer candidates | Toni decides when any component becomes public offer language |
| AI Gateway Cost Control Pack discovery | `diagnose-to-plan`, later `tm-skills` or Hub | Parked | audience, proof, product boundary, and Azure skill foundation are accepted | keep parked; do not treat as an offer or implementation task yet |

## Current Active Next Queue

Standing preflight/postflight: use `practice-os/templates/activation-routing-map.md`, `practice-os/templates/agentic-performance-gap-review.md`, and `practice-os/templates/roadmap-steward-review.md` for major roadmap sessions so the right skill/template/process is selected, agentic performance gaps are caught, and new ideas, blockers, repo lanes, gates, and no-touch boundaries are captured before memory drift.

Kaizen preflight: run `dtp kaizen status --limit 5` at the start of broad work. When Toni adds a meaningful idea, ask, blocker, proof candidate, repo issue, client signal, correction, or process improvement, run `dtp kaizen capture "..."` before deciding whether it deserves a larger artifact. Use `dtp kaizen update ID --status ... --next-action ...` to move the item instead of hand-editing JSONL.

Current focus overlay: use `practice-os/steward/2026-05-04-workspace-roadmap-deep-audit.md` plus `docs/PRACTICE_PROOF_QUEUE_INDEX.md`, `docs/OFFER_TO_PROOF_MATRIX.md`, and `docs/ROADMAP_SYNTHESIS_GATE_LEDGER.md` as the current focus map. Keep active work to private engagement-vault durability, the human-gated client/proof loop, consulting share-readiness/proof maturity, and source-backed assistant QA. Treat DSE as a separate sensitive lane.

Recovery closeout overlay: use `docs/CODEX_CHAT_AND_IMPLEMENTATION_RECOVERY_AUDIT_2026-05-05.md` only as closeout evidence. Recovered items must land in exactly one posture before implementation: commit, finish then commit, promote into canonical DTP docs, add to backlog, save as reusable prompt/spec, park in future phase, archive/discard, or wait for Toni decision.

Workspace docs/chat sweep overlay: use `docs/WORKSPACE_DOCS_AND_CHAT_SWEEP_LEDGER_2026-05-05.md` before broad claims that the dashboard/kanban/roadmap tracker is complete. The sweep ledger is the evidence-first index for the 13-repo workspace, Codex session inventory, terminal archive rows, and private/COI-gated exclusions.

Workspace cockpit/recovery overlay: use `practice-os/workspace/task-ledger.jsonl`, `dtp workspace recover --dry-run`, `dtp workspace dashboard`, and `dtp workspace validate-dashboard` before claiming older active, completed, cancelled, superseded, or unreviewed recovery work is missing from the daily view. Kaizen remains intake; the workspace task ledger is the reviewed operating index; Recovery Inbox accounts for detected but not-yet-reviewed candidates.

Horizon overlay: use `docs/PRACTICE_ROADMAP_HORIZONS_2026.md` for urgent/short/mid/long planning, feature revisits, cadence, and gated future capabilities. It does not replace this backlog; it explains sequencing across time horizons.

2026-05-07 Practice OS strategic backlog overlay: use `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`, `practice-os/steward/2026-05-07-workflow-spine-p0-implementation-plan.md`, `docs/CLIENT_OS_PILOT_WAVE_2026-05.md`, `docs/PRACTICE_KNOWLEDGE_BASE_V1.md`, `docs/PRACTICE_VECTOR_BRAIN_ROADMAP.md`, and `docs/PRACTICE_ARCHITECTURE_REVIEW_PACKET_2026-05.md` for the current wave. The immediate P0 implementation order is minimal lifecycle vocabulary, `tm-skills` readiness scorecard, Workflow Spine template, Greg spine record, Cam spine record, and obvious stale labels. Automation is draft-only. Consulting gets an audit now; public proof waits for DTP gates. Hub and `tm-skills` get readiness notes, not authority expansion. FAOS and vector implementation stay gated until real loops prove the shapes.

2026-05-05 operator reprioritization, refreshed 2026-05-11: DeMario launch-feedback social/proof prep is posted from Toni-owned LinkedIn and Instagram channels, exact public post URLs are recorded, and private screenshots/testimonials/metrics remain gated. Consulting public-site readiness is recorded and merged in PR #3; the approved Diagnostic Call booking URL is live post-submit; the 2026-05-11 browser intake smoke reached Hub and was verified through the protected dashboard by summarized fields only, with cleanup still structural because no intake archive/delete endpoint exists. Starter DMARC is added and verified in monitoring mode. Hub PRs #74, #75, and #76 merged after green checks; PRs #77 and #78 remain blocked by failing build/typecheck gates. Architected Strength PR #2 merged the repo-local boundary/roadmap note. Greg Part 1 closeout is ready and the next useful gate is Greg response or Part 2 using the UX Trust Review Notes. Omnexus PR #562 is merged, app version `1.0.1` was approved, and monthly/annual subscriptions are operator-reported `Approved`; approved subscriptions do not need app-version attachment. The remaining manual queue is Omnexus candidate build/version proof for `1.0.1`, consulting human taste review, Cam packet wait, Greg response/Part 2, and CCAAP owner-input gates. Treat Omnexus subscription work as App Store Connect/manual proof first until exact rejection details prove code changes are needed. Treat future Architected Strength P0/P1 site work as a separate focused branch, not assistant-pattern work.

1. Use the Practice Intelligence Control Plane as the first broad-session preflight: rehydrate from DTP/git/Gmail/Calendar/Notion, route inputs to the correct artifact, and block unsafe actions before expanding infrastructure.
2. Use the Practice Memory Control Plane before expanding infrastructure: capture new ideas, connector plans, client states, decisions, and blockers into DTP first; use Notion only as cockpit/inbox.
3. Use the Agent Memory Optimization Plan for broad sessions: rehydrate from source-aware DTP/git/Gmail/Calendar/Notion checks before acting, and graduate to hosted/vector memory only after the persistence ladder gates are met.
4. Use the Practice OS source material through `docs/integration/source_index.md`, `docs/integration/integration_map.md`, `docs/integration/concept_registry.md`, the module templates, and `docs/integration/schema_reconciliation_v0.md`; preserve source nuance and prefer templates/docs before code.
5. Run the second-cycle client reply/template pilot on the next real Cam, Greg, or CCAAP reply; the first weekly Business Brain reset is complete and should be repeated weekly.
6. Use the Tooling Steward before adding or relying on more plugins/connectors; score usefulness, data risk, source-of-truth fit, maintenance burden, and verification before adding, removing, piloting, or parking tools. For Sanity, CMS, owner-editor, content-management, or page-builder ideas, use the CMS/editor decision ladder first and keep implementation on the backburner unless a repo lane explicitly opens it.
6A. Use Platform Operating Patterns V0 before turning platform inspiration into repo work: preview receipts for readiness claims, environment ledgers for hosted/runtime state, data boundary ledgers for Supabase/Postgres/auth/storage, client handoff console specs for owner-facing surfaces, and launch momentum receipts after real launch signal. Greg's soft-launch evidence stays held until after the next meeting.
7. Preserve the completed Google Workspace starter-auth posture: DKIM is present in DNS, starter DMARC is live in monitoring mode, connector identity, booking pages, Meet links, founder mailbox testing, and Apple Reminders-first task direction are complete. Tighten DMARC only after a separate review.
8. Run the recurring client and reply intake loop: Cam weekly after time confirmation, Greg biweekly only if discovery confirms it, CCAAP monthly formal owner check-in, and Toni's weekly Business Brain reset. Update DTP private kits first, then mirror only sanitized status into Notion.
9. Wait for Leah plus Tony's CCAAP review response after the owner packet/prototype link sent on 2026-05-01 and clarification sent on 2026-05-02; collect exact PayPal donate/membership links, contact routing and spam preference, meeting label/destination, domain/DNS access, authentic photos/resources, review notes, and proof decision.
10. Continue the CCAAP off-Wix custom rebuild path only after owner-approved values arrive; production DNS waits for `pnpm validate:launch`.
11. Apply the Custom Interface Craft Standard before broad UI work, and apply the Integrity Layer when the work needs truthfulness, usefulness, restraint, durability, handoff, or AI-output judgment before ship. Consulting now carries the official 2026-05-04 Toni Montez slogan/logo kit and its 2026-05-06 readiness receipt. Architected Strength has the P0/P1 public-signal finish/fix lane recorded in its repo-local board. They remain north-star candidates, not completed templates, until future implementation passes clear reference promotion gates.
12. Use the Notion Mirror and Command Center phone inbox and daily views for capture/review; run the Notion cockpit audit and Roadmap Steward triage before promoting any Notion item into DTP source-of-truth artifacts.
13. Keep QuickBooks as a gated read-only financial connector candidate; no OAuth, token storage, imports, webhooks, or write behavior until the connector boundary is accepted.
14. Keep Architected Strength as its own personal-brand OS. PR #1 and PR #2 are merged into the org-owned private repo; run the actual public-signal finish pass on a fresh branch, and keep assistant-pattern work later until the consulting public assistant pilot proves the pattern.
15. Keep the cross-site assistant lane at architecture/manifest/QA level until the consulting public manifest, approved source corpus, refusal policy, no-widget QA checklist, logging/analytics plan, and human handoff are accepted.
16. Use Hosted DTP Phase 0.2 in one more real operating loop with markdown fallback before storing client-sensitive non-smoke records as normal workflow. The real-operator, smoke-fixture, backup/export, and local-private deployment posture is accepted; do not reuse Omnexus, Consulting, FamilyTrips, or Mario Supabase projects for the DTP brain.
17. Keep the Omnexus Stripe webhook-disabled alert parked per Toni until the support lane is reopened. When reopened, the live app route is reachable at `/api/webhook-stripe`, so the gate is Stripe Dashboard endpoint correction, re-enable, failed-event replay, and affected-subscription verification. Treat the Omnexus App Store approval journey as the first mobile app review-to-launch learning pattern, but do not publish Omnexus proof until proof gates pass.
18. Treat Omnexus as subscription-fixed and release-proof gated: monthly/annual subscriptions are operator-reported `Approved`, the app now works with subscriptions, and no developer release or IAP code change is authorized until App Store Connect confirms the selected candidate build/version is `1.0.1` and normal final smoke, provider/data, observability, first-availability, and non-sensitive release-proof notes are complete or Apple returns exact rejection/status evidence requiring a fix.
19. Capture owner-approved CCAAP baseline/after-state evidence for the first proof candidate and run redaction/permission review. Track proof posture in `docs/PRACTICE_PROOF_QUEUE_INDEX.md` before any consulting public proof movement.
20. Keep Claude Code and GitHub Copilot `tm-skills` discovery smoke testing on the manual back burner; runbook exists, links are healthy, and Codex discovery is verified, but external reload checks remain manual and non-blocking.
21. Keep Hub dependency PRs #77 and #78 parked until a targeted Hub-local fix pass reproduces and resolves the failing gates. PRs #74, #75, and #76 are merged; old PR #68 is superseded as a visible blocker by the current Tailwind PR #78.
22. Keep Hub prompt/registry cross-validation local-first; decide private sibling-repo CI access only if it becomes worth the operational cost.
23. Use `dtp workspace report` as a read-only steward preflight when checking repo coverage, recorded evidence, suggested gates, blockers, and missing manifest/evidence coverage; missing repo rows may carry explicit Active Next Queue blockers without guessing gates. Generate any workspace dashboard only from `dtp workspace report --json` and the `docs/WORKSPACE_DASHBOARD_READONLY.md` boundary.
24. Keep repo manifests current as lanes are touched; DTP, consulting, Architected Strength, Hub, `hub-prompts`, `hub-registry`, `tm-skills`, DeMario, CCAAP, FamilyTrips, engineering-playbook, `dse-content`, and `fitness-app` / Omnexus now have DTP-owned manifests/evidence indexes.
25. Keep DSE proof/reuse blocked until it is explicitly selected with COI-aware scope, live repo verification, permission, redaction, reviewer, evidence, and caveat gates. Live audit on 2026-05-04 found `dse-content/dev` ahead 4 with dirty Azure readiness work and 64 open PRs, so DSE cleanup needs its own sensitive triage pass.
26. Keep FAOS implementation parked after the 2026-05-03 readiness review; next FAOS action is a separate local command/version verification pass, not repo/service creation.

Closed on 2026-04-30: GitHub Enterprise org-migration closeout for Omnexus PR #559. The PR merged, local `fitness-app/main` was aligned to `origin/main`, and represented local org-migration branches were deleted.

## Answer To The Kanban Question

Yes, the roadmap should be planned in epic/story fashion. Not every item is ready for implementation today, and that is intentional. The execution model is:

- Strategic roadmap: what matters and why.
- Execution backlog: epics, stories, statuses, Done gates, and next actions.
- Implementation plans: created only when a story moves to `Active next`.
- Code/docs/templates: built only when the story's gate and repo boundary are clear.
