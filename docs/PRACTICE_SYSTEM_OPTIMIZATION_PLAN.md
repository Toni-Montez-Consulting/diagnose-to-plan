# Practice System Optimization Plan

Status: prioritized improvement plan derived from `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md`.

Owner: `diagnose-to-plan`

Purpose: convert system-audit findings into epics, stories, gates, owners, and sequencing without removing or demoting any existing roadmap item.

## Optimization Strategy

The strategy is not to build more surface area first. The strategy is to make every future surface more trustworthy.

Optimize in this order:

1. Make the system understandable from DTP alone.
2. Make the practice offer-led before making it platform-heavy.
3. Make the agentic performance loop catch routing, context, skill-trigger, validation, research, safety, and learning gaps.
4. Make squad ownership, source scope, business justification, approval, and handoff explicit before central boards or automation.
5. Make the next real pilot produce evidence.
6. Make public proof permissioned and receipt-backed.
7. Expand repo manifests and local pointers only when the repo lane is touched.
8. Cross-validate Hub prompts and registry before deeper runtime automation.
9. Install and smoke-test global skills only after approval.
10. Build hosted DTP only when real artifacts need persistence.
11. Add steward automation, evals, red-team, and protocols after manual loops prove useful.

## Epic A: Practice System Documentation Pack

Goal: a future agent can open DTP and understand the current system, future system, gaps, and optimization path.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| Current system architecture doc | `diagnose-to-plan` | Done when merged | `docs/PRACTICE_SYSTEM_ARCHITECTURE.md` exists and names all repos, flows, and gates | keep linked from doc map |
| Future system doc | `diagnose-to-plan` | Done when merged | `docs/PRACTICE_SYSTEM_FUTURE_STATE.md` exists with hosted/steward/research/repo-manifest diagrams | use before hosted implementation |
| Audit and gap review | `diagnose-to-plan` | Done when merged | severity-ranked findings tie to follow-up stories | revisit after Mom pilot |
| Agentic performance gap review | `diagnose-to-plan` | Done when merged | required template and doc inspect prompt routing, context, skill triggers, verification, research, safety, and learning-loop conversion | run after major agent-system misses |
| Optimization plan | `diagnose-to-plan` | Done when merged | findings convert into epics/stories/gates | keep backlog aligned |
| Practice machine operating map | `diagnose-to-plan` | Done when merged | offer-led machine map stages ideas as Now/Next/Later/Hold and points to proof, Hub, and workspace runbooks | use before broad workspace/platform prompts |
| Workspace operator runbook | `diagnose-to-plan` | Done when merged | safe command classes, repo roles, and no-touch boundaries are documented | use before cross-repo command selection |
| Offer packaging source | `diagnose-to-plan` | Done when merged | first three sellable offers are internally defined before public copy changes | use before consulting copy pass |

## Epic B: Documentation Propagation Lane

Goal: every repo eventually gets the right local pointer without duplicating DTP roadmap ownership.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| Add propagation lane to backlog | `diagnose-to-plan` | Ready | backlog tracks future local pointers by repo | update backlog now |
| Consulting local pointer | `consulting` | Later | README or docs point to DTP for practice system and proof governance | do during next proof/site pass |
| Hub local pointer | `hub` | Later | docs name Hub/DTP/consulting boundary and prompt/registry validation path | do during prompt/registry work |
| `tm-skills` alignment pointer | `tm-skills` | Later | skill trigger changes reference DTP activation map | do during install/smoke pass |
| Project repo pointers | project repos | Later | each repo has local note for its lane: proof, privacy, COI, or launch | do during repo touch passes |

Gate: no bulk repo edits. Propagate when the owning lane becomes active.

## Epic C: Private Kit Durability

Goal: private engagement work is both excluded from public git and durable enough for real operations.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| Private durability decision | `diagnose-to-plan` | Ready | decision names when to use local ignored kit, private vault, and private remote | decide before relying on private client material |
| `dtp vault` pilot | `diagnose-to-plan` private area | Ready | private remote exists and restore path is documented | use only when real private material exists |
| Private material evidence rule | `diagnose-to-plan` | Ready | public docs explain that private proof sources stay private until redacted | align with proof pilot |

Gate: no private client content committed to public DTP repo.

## Epic D: Mom Nonprofit Pilot And Proof Spine

Goal: use one real pilot to prove the Practice OS loop end to end.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| Fill Mom private kit | `diagnose-to-plan` ignored `engagements/` | Review | real context, consent, data inventory, diagnose, plan, and metrics exist privately | public-source refresh done; collect owner facts next |
| Complete command-room fit assessment | `diagnose-to-plan` ignored `engagements/` | Done | portal vs checklist vs no private surface decision is evidence-backed | handoff checklist first; no portal unless owner workflow proves need |
| First proof candidate | `diagnose-to-plan` plus `consulting` later | Done | one claim has evidence, caveat, permission, redaction, and reviewer state | internal candidate exists; do not publish until approved |
| Handoff/runbook | pilot repo | Ready | owner-safe launch/handoff checklist exists | after build scope is known |

Gate: proof does not move to consulting until permission/redaction/reviewer gates pass.

## Epic E: Hub Prompt And Registry Cross-Validation

Goal: reduce drift between prompt definitions, registry targets, and Hub runtime expectations.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| Prompt id inventory | `hub-prompts` | Ready | all prompt ids are machine-readable and validated | run current prompt validation first |
| Registry reference inventory | `hub-registry` | Ready | registry targets list prompt references clearly | run registry validation first |
| Cross-validation plan | `hub-prompts`, `hub-registry`, `hub` | Ready | CI-safe and local-private validation modes are documented | implement after Mom pilot or when Hub resumes |
| Runtime expectation check | `hub` | Later | Hub docs and runtime agree on prompt source and deployment path | do before deeper Hub automation |
| Runtime current-state map | `hub` | Done when merged | Hub surfaces are classified as live-hosted, local-only, legacy-proxy, planned, or retired | update whenever routing/runtime ownership changes |

Gate: do not require private sibling-repo access in repo-scoped CI unless explicitly configured.

## Epic F: Repo Manifest And Evidence Expansion

Goal: make future agents stop rediscovering repo purpose, gates, proof lanes, and data boundaries.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| DTP manifest/evidence index | `diagnose-to-plan` | Done | pilot exists | use as shape reference |
| Consulting manifest | `consulting` | Done | purpose, routes, gates, deploy target, proof lane, Hub boundary named | keep current during consulting work |
| Hub manifest | `hub` | Done | runtime gates, Supabase/Vercel boundaries, prompts/runs ownership named | keep current during prompt/registry work |
| `tm-skills` manifest | `tm-skills` | Done | install gates, global skill boundaries, smoke tests named | keep current during skill smoke/canary work |
| `hub-prompts` manifest/evidence index | `hub-prompts` | Done | prompt catalogue ownership, prompt validation gates, eval lane, and Hub runtime boundary named | add eval/golden fixtures only after real prompt misfires or high-value workflows justify them |
| `hub-registry` manifest/evidence index | `hub-registry` | Done | target/routing ownership, local registry gates, prompt-id cross-validation, and deferred sibling CI access named | keep repo-scoped CI thin unless local-first validation becomes a bottleneck |
| DeMario manifest/evidence index | `demario-pickleball-1` | Done | launch gates, command-room role, proof blockers, and local/CI evidence named | use for future command-room proof pass |
| FamilyTrips manifest/evidence index | `FamilyTrips` | Done | privacy model, local gates, deploy smoke, and no-auth/no-AI boundary named | use before future FamilyTrips feature or sharing work |
| Omnexus manifest/evidence index | `fitness-app` | Done | verification cockpit reference, release evidence, proof gates, and app-data boundaries named without mutating app code | use as reference pattern and proof input only after gates |
| Workspace Command Center V0 spec | `diagnose-to-plan` | Done | read-only inputs, outputs, safety boundaries, and pilot acceptance named | pair with `dtp workspace report` |
| Workspace Command Center V0 read-only report | `diagnose-to-plan` | Done | `dtp workspace report` outputs text/JSON from DTP-owned manifests, evidence indexes, backlog, and command-center docs without repo commands or GitHub calls | use for steward preflight; live runner remains later |
| Remaining adjacent repo manifests | project repos | Later | each repo gets manifest when touched | use touch-pass trigger |

Gate: manifests are advisory until proven useful in at least two repos.

## Epic G: `tm-skills` Activation Completion

Goal: make reusable SDLC skills actually available to future sessions.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| Review dry-run output | `tm-skills` | Done | Toni approves global skill links/files | preserve evidence in smoke note |
| Run install apply | `tm-skills` | Done | `install.ps1 -Apply` succeeds without `-Force` | keep force gated |
| Reload tools | Codex/Claude/Copilot | Review | tools see expected skills | external reloads remain manual |
| Smoke-test discovery | `tm-skills` plus tools | Review | trigger prompts activate correct skills | record misfires |
| Choose canary | one repo | Later | no duplicate trigger confusion | pick low-risk repo |

Gate: no global install without explicit approval.

## Epic H: Hosted DTP Implementation Readiness

Goal: build the private hosted app only when it has real records and a clear boundary.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| Readiness review | `diagnose-to-plan` | Ready | pilot produced records that match Phase 0 model | run after Mom/proof pilot |
| Schema implementation | `diagnose-to-plan` | Ready, gated | migrations/RLS match accepted model | separate implementation request |
| Private app shell | `diagnose-to-plan` | Ready, gated | auth, engagement list, artifact/evidence/redaction/proof placeholders connect to real model | no dashboards without artifacts |
| Import/export | `diagnose-to-plan` | Ready, gated | local markdown kits round-trip with hosted records | build with app shell |

Gate: hosted implementation waits for separate approval and real records.

## Epic I: Future Intelligence And Guardrail Maturity

Goal: make the practice learn from work without letting automation outrun governance.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| First agent flight record | `diagnose-to-plan` | Ready | one complex session records goal, files, commands, failures, lessons, eval candidates | use next suitable session |
| Agentic performance gap review V0 | `diagnose-to-plan` | Done when merged | review doc exists, template is required, activation map routes performance-gap prompts | use after major roadmap/agent sessions |
| First research radar item | `diagnose-to-plan` | Ready | item classified Adopt/Pilot/Watch/Reject with source and next review | use when research changes roadmap |
| Eval garden seed | DTP, `tm-skills`, `hub-prompts` | Later | real misfires become fixtures | wait for evidence |
| Red-team pilot | Hub or hosted DTP | Later | guardrail/red-team plan exists before public AI/write-enabled workflow | before autonomy |
| Supply-chain baseline | higher-risk repos | Later | SBOM/scanner/release evidence added where risk justifies it | start with Omnexus/Hub/hosted DTP/consulting intake |

Gate: intelligence assets propose changes; humans approve adoption.

## Epic J: Adjacent Repo Touch Passes

Goal: every workspace repo benefits eventually without unnecessary churn.

| Repo | Trigger | First Touch |
|---|---|---|
| `fitness-app` | PR #553 merged; future proof or release-support request opens | manifest/evidence index exists; verification lessons extracted without disturbing live app work |
| `demario-pickleball-1` | launch/proof permission is ready | manifest/evidence index exists; next pass is command-room proof and launch gate pass |
| `FamilyTrips` | new feature, AI, public sharing, or maintenance request | manifest/evidence index exists; next pass should update privacy review and gates |
| `dse-content` | proof or Microsoft-adjacent reuse request | COI-aware proof review |
| `engineering-playbook` | doctrine or template change | pointer audit to DTP source of truth |
| `hub-prompts` | prompt/schema/eval change | validation and prompt id alignment |
| `hub-registry` | routing/target change | registry validation and cross-reference check |

Gate: each touch pass names one repo, one lane, and one Done gate.

## Epic K: FAOS Orchestration Substrate Readiness

Goal: absorb the FAOS build spec into the practice system as a technically sound, gated orchestration substrate instead of a parallel platform.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| FAOS roadmap integration | `diagnose-to-plan` | Review | roadmap doc, backlog epic, activation row, steward receipt, and future-state pointer exist | accept as roadmap-only capture |
| Phase 0 readiness review | `diagnose-to-plan` | Ready | readiness template resolves Langfuse topology, `uv` flow, memory isolation, DTP tracing conflict, trace redaction, Spec-Kit CLI syntax, and COI ownership | run after current pilot/proof/smoke/Hub-validation priorities |
| FAOS implementation prompt rewrite | future `faos` repo | Later | raw Phase 0 prompt is corrected into an executable spec with impossible/conflicting gates removed | only after readiness review |
| FAOS substrate implementation | future `faos` repo plus DTP adapter stories | Later | corrected foundation passes tests, ADRs, redaction, and accepted tracing/memory gates | no repo creation yet |

Gate: FAOS work may plan and review now, but implementation is parked until the readiness review is accepted.

## Epic L: Agent Squads + Knowledge Base V0

Goal: make human-led squads useful immediately while preserving DTP ownership,
source-indexed knowledge, business justification, and explicit approval gates.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| Squad source map | `diagnose-to-plan` | Done when merged | `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` defines V0 boundaries, squads, knowledge scope, gates, first pilot, and future persistence | use before squad/KB work |
| Squad templates | `diagnose-to-plan` | Done when merged | charter, source index, scorecard, approval gate, and handoff receipt templates exist | pilot on consulting proof/offer lane |
| Consulting pointer | `consulting` | Done when merged | consulting docs route agents back to DTP without duplicating source-of-truth ownership | keep lightweight |
| Consulting proof/offer pilot | `diagnose-to-plan`, `consulting` | Ready | one proof/offer work item uses source index, scorecard, approval gate, and receipt | run before public proof/offer movement |
| Hosted squad persistence | hosted DTP | Later | repeated markdown receipts prove the record shapes | preserve markdown fallback |

Gate: squads organize work; they do not authorize autonomous agents, public proof,
client communication, production writes, or repo mutation.

## Recommended Next Execution Order

1. Use `docs/PRACTICE_MACHINE_OPERATING_MAP.md` before broad workspace, offer, platform, Hub, proof, or adjacent-project planning.
2. Run one real client loop through `client-reply-intake` and `recurring-engagement-cadence`.
3. Use `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` on the next consulting proof/offer move so the first squad receipt is real.
4. Fill the private kit with real context, decisions, source material, and one internal proof candidate.
5. Use `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md` on the first real claim.
6. Use `docs/OFFER_LED_PRACTICE_PACKAGING.md` for the consulting public-copy pass after proof classification.
7. Keep repo manifests current for DTP, consulting, Hub, `hub-prompts`, `hub-registry`, `tm-skills`, DeMario, FamilyTrips, engineering-playbook, and `fitness-app` / Omnexus as those lanes are touched.
8. Keep Hub prompt/registry cross-validation local-first unless private sibling-repo CI access becomes worth the cost.
9. Keep external `tm-skills` Claude Code/GitHub Copilot smoke tests manual until they can be observed.
10. Revisit public assistant manifests only after proof/source/refusal gates pass.
11. Revisit hosted DTP implementation after real pilot records exist.
12. Run FAOS Phase 0 readiness review after the current active path; do not implement the raw FAOS prompt until the corrections are accepted.

## Optimization Done Gate

The optimization path is working when a future agent can answer all of these from DTP without chat memory:

- what is next
- which repo owns it
- which gates must pass
- which skill or template should activate
- what proof can or cannot be public
- what private data must not be touched
- what should be parked
- what should become an eval, lesson, decision, or research item
