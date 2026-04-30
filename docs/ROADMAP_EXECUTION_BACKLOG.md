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

## Current Active Next Queue

Standing preflight/postflight: use `practice-os/templates/activation-routing-map.md`, `practice-os/templates/agentic-performance-gap-review.md`, and `practice-os/templates/roadmap-steward-review.md` for major roadmap sessions so the right skill/template/process is selected, agentic performance gaps are caught, and new ideas, blockers, repo lanes, gates, and no-touch boundaries are captured before memory drift.

1. Use the Notion Mirror V0 phone inbox and daily views for capture/review; run Roadmap Steward triage before promoting any Notion item into DTP source-of-truth artifacts.
2. Keep Hub dependency PRs #54/#56/#61 parked until one is explicitly selected with a migration/security plan; PRs #59 and #55 are merged and no longer block the queue. Older PR #52 is no longer in the active visible queue.
3. Complete remaining CCAAP inputs: exact PayPal donate/membership links, contact routing, domain/DNS access, authentic photos/resources, owner review, and proof permissions.
4. Continue the CCAAP off-Wix custom rebuild path; keep exact launch scope gated by owner review, PayPal links, contact routing, domain/DNS, and authentic assets.
5. Capture owner-approved baseline/after-state evidence for the first proof candidate and run redaction/permission review.
6. Keep Claude Code and GitHub Copilot `tm-skills` discovery smoke testing on the manual back burner; runbook exists, links are healthy, and Codex discovery is verified, but external reload checks remain manual and non-blocking.
7. Keep Hub prompt/registry cross-validation local-first; decide private sibling-repo CI access only if it becomes worth the operational cost.
8. Use `dtp workspace report` as a read-only steward preflight when checking repo coverage, recorded evidence, suggested gates, blockers, and missing manifest/evidence coverage; missing repo rows may carry explicit Active Next Queue blockers without guessing gates.
9. Keep repo manifests current as lanes are touched; DTP, consulting, Hub, `hub-prompts`, `hub-registry`, `tm-skills`, DeMario, FamilyTrips, engineering-playbook, `fitness-app` / Omnexus, and `ccaap-site` now have DTP-owned manifests/evidence indexes.
10. Keep DSE blocked until its active branch is clean or explicitly selected with COI-aware scope.
11. Run FAOS Phase 0 readiness review only after the current pilot/proof/smoke/Hub-validation path; do not build FAOS from the raw Phase 0 prompt yet.

Closed on 2026-04-30: GitHub Enterprise org-migration closeout for Omnexus PR #559. The PR merged, local `fitness-app/main` was aligned to `origin/main`, and represented local org-migration branches were deleted.

## Answer To The Kanban Question

Yes, the roadmap should be planned in epic/story fashion. Not every item is ready for implementation today, and that is intentional. The execution model is:

- Strategic roadmap: what matters and why.
- Execution backlog: epics, stories, statuses, Done gates, and next actions.
- Implementation plans: created only when a story moves to `Active next`.
- Code/docs/templates: built only when the story's gate and repo boundary are clear.
