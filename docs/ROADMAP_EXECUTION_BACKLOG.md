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
- FAOS orchestration is a gated future substrate lane. Use `docs/FAOS_ORCHESTRATION_ROADMAP.md` and `practice-os/templates/faos-phase-readiness-review.md` before any `faos` repo, `op` wrapper, tracing/memory substrate, Spec-Kit rollout, MCP server, subagent roster, hook, durable workflow, or business-agent automation is implemented.

## Story Activation Contract

Use `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` before starting or advancing a story when the prompt could imply a specific skill, template, agent role, proof gate, COI gate, or repo touch pass.

Use `practice-os/templates/story-activation-contract.md` when a story needs a dedicated one-off activation record.

Use `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md` and `practice-os/templates/contextual-idea-intake.md` before promoting a new idea, design, business move, project request, development enhancement, or automation concept into a story.

Agent roles in the activation index are recommendations, not permission. Subagents, autonomous managers, global installs, hosted implementation, public proof, and write-enabled automation still require their explicit gates.

## Epic 1: Reusable Agent SDLC Layer

Goal: make every future coding session safer and more consistent.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Create `tm-skills` repo and Phase 1 skills | `tm-skills` | Done | repo pushed, doctor/freshness/install dry-run pass, CI green | install only after explicit approval |
| Add `tm-skills` thin CI | `tm-skills` | Done | GitHub Actions green | keep workflow thin |
| Global install apply | `tm-skills` | Done | `install.ps1 -Apply` succeeds without `-Force` and post-install doctor passes | record smoke status |
| Tool reload smoke test | `tm-skills` plus tools | Review | Codex/Claude/Copilot discover skills after reload | Codex discovery verified; Claude Code and GitHub Copilot reloads remain manual |
| Project-pinned canary | `tm-skills` plus one repo | Later | one low-risk repo confirms no duplicate-skill confusion | choose after global install works |
| Stack overlays | `tm-skills` | Later | base skills prove useful across real work | design overlays only after canary |

## Epic 2: Practice OS And Client Command Rooms

Goal: make owner/operator command-room decisions repeatable without building portals by default.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Capture Client Command Room pattern | `diagnose-to-plan` | Done | pattern doc plus fit/spec templates exist and practice doctor passes | use on first pilot |
| First Command Room fit assessment | `diagnose-to-plan` | Done | Mom nonprofit private kit has a completed fit assessment | handoff checklist first; revisit portal only if owner workflow pain is proven |
| Client Command Room implementation | candidate project repo | Later | fit assessment says build, owner workflow is real, support/evidence exists | keep optional |
| Command-room proof packet | `consulting` plus source repo | Later | screenshots/walkthroughs redacted and permissioned | wait for real pilot |

## Epic 3: Verification And CI Spine

Goal: make every repo's delivery state observable before dashboards or automation depend on it.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Thin CI for DTP | `diagnose-to-plan` | Done | DTP CI green | preserve local/CI parity |
| Thin CI for consulting | `consulting` | Done | build and secret scan CI green | expand route CI only when browser setup is stable |
| Thin CI for `tm-skills` | `tm-skills` | Done | doctor/freshness/install preview CI green | keep global install gated |
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
| Omnexus proof candidates | `fitness-app` | Later | PR/work is human-reviewed and proof is permissioned/redacted | do not disturb active app work |
| DeMario proof packet | `demario-pickleball-1` | Later | launch gates and permission are complete | keep owner-safe |
| DSE internal proof lane | `dse-content` | Later | COI, permission, and redaction review complete | internal/professional only |

## Epic 6: Workspace Efficiency Layer

Goal: reduce rediscovery, setup drift, CI waste, and handoff friction.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| DTP repo manifest/evidence-index pilot | `diagnose-to-plan` | Done | pilot shape accepted as useful | core manifests plus DeMario and FamilyTrips adjacent passes now exist |
| Consulting repo manifest | `consulting` | Done | manifest names gates, deploy target, proof lane, and data boundaries | keep current during consulting proof/intake work |
| Hub repo manifest | `hub` | Done | manifest names runtime gates, Supabase/Vercel boundaries, and prompt/run ownership | keep current during Hub runtime and prompt/registry work |
| `tm-skills` repo manifest | `tm-skills` | Done | manifest names install gates and global-skill boundaries | keep current during skill smoke/canary work |
| DeMario repo manifest/evidence index | `diagnose-to-plan`, `demario-pickleball-1` | Done | manifest and evidence index capture launch gates, proof blockers, command-room role, and local/CI evidence without mutating app code | use for future command-room proof pass |
| FamilyTrips repo manifest/evidence index | `diagnose-to-plan`, `FamilyTrips` | Done | manifest and evidence index capture privacy model, local gates, release smoke, and no-auth/no-AI boundary | use before future FamilyTrips feature, AI, or public-sharing work |
| Workspace Command Center spec | `diagnose-to-plan` | Done | `docs/WORKSPACE_COMMAND_CENTER_V0.md` defines read-only inputs, outputs, gates, and safety boundaries | no command runner yet |
| Workspace Command Center implementation | `diagnose-to-plan` | Later | read-only report proves value and no mutation boundary remains intact | implement only after another touch pass confirms the report shape |
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
| Research Radar first item | `diagnose-to-plan` | Ready | one item classified Adopt/Pilot/Watch/Reject with source and next action | use when research changes roadmap |
| Eval garden | `hub-prompts`, `tm-skills`, DTP | Later | real misfires become fixtures | wait for misfire history |
| Red-team lab | Hub/DTP future agent workflows | Later | adversarial tests exist before write-enabled automation | keep before autonomy |

## Epic 9: First Client Operating Kit Pilot

Goal: run one real engagement through the Practice OS before building more platform surface.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Mom nonprofit kit creation | `diagnose-to-plan` private `engagements/` | Done | kit created with COI, consent, diagnose, plan, and metrics placeholders | public-source refresh complete; collect owner facts next |
| Command Room fit assessment | `diagnose-to-plan` | Done | assessment decides portal vs checklist vs no private surface | handoff checklist first; no UI unless owner workflow proves portal need |
| Proof/redaction use | `diagnose-to-plan` | Done | proof packet and redaction queue item created for one claim candidate | keep internal until reviewed |
| Handoff/runbook | `diagnose-to-plan` plus project repo | Ready | owner-safe handoff exists | after build scope is known |
| Public proof promotion | `consulting` | Blocked | permission, redaction, reviewer, evidence, and caveat all approved | no auto-publish |

## Epic 10: Adjacent Project Touch Lanes

Goal: ensure every workspace repo benefits without unnecessary churn.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Omnexus verification cockpit review | `fitness-app` | Later | active PR/branch human-reviewed, reusable lessons extracted | do not mutate until reopened |
| DeMario launch/proof pass | `demario-pickleball-1` | Later | manual launch/venue/permission gates complete | manifest/evidence index exists; owner-safe proof only |
| FamilyTrips privacy maintenance pass | `FamilyTrips` | Done | data validation/build/test and privacy notes complete | manifest/evidence index exists; revisit before new features, AI, or public sharing |
| DSE COI-aware proof pass | `dse-content` | Later | COI screen and live branch verification complete | internal/professional only |
| Engineering playbook pointer audit | `engineering-playbook` | Later | doctrine points to DTP without duplicating roadmap ownership | after DTP contracts settle |

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

## Current Active Next Queue

Standing preflight/postflight: use `practice-os/templates/activation-routing-map.md`, `practice-os/templates/agentic-performance-gap-review.md`, and `practice-os/templates/roadmap-steward-review.md` for major roadmap sessions so the right skill/template/process is selected, agentic performance gaps are caught, and new ideas, blockers, repo lanes, gates, and no-touch boundaries are captured before memory drift.

1. Collect Mom nonprofit owner-confirmed facts: site owner, backup owner, meeting source of truth, form/payment routing, update workflow, proof reviewer, and screenshot permissions.
2. Decide the Mom site execution path after owner facts: Wix cleanup, rebuild, or migration.
3. Capture owner-approved baseline/after-state evidence for the first proof candidate and run redaction/permission review.
4. Finish `tm-skills` discovery smoke testing in Claude Code and GitHub Copilot; links are healthy and Codex discovery is verified, but external reload checks remain manual.
5. Keep Hub prompt/registry cross-validation local-first; decide private sibling-repo CI access only if it becomes worth the operational cost.
6. Keep repo manifests current as lanes are touched; DTP, consulting, Hub, `tm-skills`, DeMario, and FamilyTrips now have DTP-owned manifests/evidence indexes.
7. Run FAOS Phase 0 readiness review only after the current pilot/proof/smoke/Hub-validation path; do not build FAOS from the raw Phase 0 prompt yet.

## Answer To The Kanban Question

Yes, the roadmap should be planned in epic/story fashion. Not every item is ready for implementation today, and that is intentional. The execution model is:

- Strategic roadmap: what matters and why.
- Execution backlog: epics, stories, statuses, Done gates, and next actions.
- Implementation plans: created only when a story moves to `Active next`.
- Code/docs/templates: built only when the story's gate and repo boundary are clear.
