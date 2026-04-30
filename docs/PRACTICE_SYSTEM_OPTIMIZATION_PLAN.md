# Practice System Optimization Plan

Status: prioritized improvement plan derived from `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md`.

Owner: `diagnose-to-plan`

Purpose: convert system-audit findings into epics, stories, gates, owners, and sequencing without removing or demoting any existing roadmap item.

## Optimization Strategy

The strategy is not to build more surface area first. The strategy is to make every future surface more trustworthy.

Optimize in this order:

1. Make the system understandable from DTP alone.
2. Make the agentic performance loop catch routing, context, skill-trigger, validation, research, safety, and learning gaps.
3. Make the next real pilot produce evidence.
4. Make public proof permissioned and receipt-backed.
5. Expand repo manifests and local pointers only when the repo lane is touched.
6. Cross-validate Hub prompts and registry before deeper runtime automation.
7. Install and smoke-test global skills only after approval.
8. Build hosted DTP only when real artifacts need persistence.
9. Add steward automation, evals, red-team, and protocols after manual loops prove useful.

## Epic A: Practice System Documentation Pack

Goal: a future agent can open DTP and understand the current system, future system, gaps, and optimization path.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| Current system architecture doc | `diagnose-to-plan` | Done when merged | `docs/PRACTICE_SYSTEM_ARCHITECTURE.md` exists and names all repos, flows, and gates | keep linked from doc map |
| Future system doc | `diagnose-to-plan` | Done when merged | `docs/PRACTICE_SYSTEM_FUTURE_STATE.md` exists with hosted/steward/research/repo-manifest diagrams | use before hosted implementation |
| Audit and gap review | `diagnose-to-plan` | Done when merged | severity-ranked findings tie to follow-up stories | revisit after Mom pilot |
| Agentic performance gap review | `diagnose-to-plan` | Done when merged | required template and doc inspect prompt routing, context, skill triggers, verification, research, safety, and learning-loop conversion | run after major agent-system misses |
| Optimization plan | `diagnose-to-plan` | Done when merged | findings convert into epics/stories/gates | keep backlog aligned |

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

Gate: do not require private sibling-repo access in repo-scoped CI unless explicitly configured.

## Epic F: Repo Manifest And Evidence Expansion

Goal: make future agents stop rediscovering repo purpose, gates, proof lanes, and data boundaries.

| Story | Repo | Status | Done Gate | Next Action |
|---|---|---|---|---|
| DTP manifest/evidence index | `diagnose-to-plan` | Done | pilot exists | use as shape reference |
| Consulting manifest | `consulting` | Ready | purpose, routes, gates, deploy target, proof lane, Hub boundary named | do during next consulting pass |
| Hub manifest | `hub` | Ready | runtime gates, Supabase/Vercel boundaries, prompts/runs ownership named | do during prompt/registry pass |
| `tm-skills` manifest | `tm-skills` | Ready | install gates, global skill boundaries, smoke tests named | do during install pass |
| Adjacent repo manifests | project repos | Later | each repo gets manifest when touched | use touch-pass trigger |

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
| `fitness-app` | active branch reviewed or proof request opens | extract verification lessons, do not disturb live app work |
| `demario-pickleball-1` | launch/proof permission is ready | command-room proof and launch gate pass |
| `FamilyTrips` | new feature, AI, public sharing, or maintenance request | privacy-first validation/build/test pass |
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

## Recommended Next Execution Order

1. Finish and validate this documentation pack.
2. Run the Agentic Performance Gap Review when a session exposes a missed routing, memory, verification, research, safety, or learning-loop behavior.
3. Keep the active queue centered on the Mom nonprofit private kit.
4. Use the proof/redaction templates on the first real claim.
5. Expand repo manifests to consulting, Hub, and `tm-skills` as those lanes are touched.
6. Add Hub prompt/registry cross-validation.
7. Decide whether to approve global `tm-skills` install and smoke tests.
8. Run adjacent repo touch passes only when their triggers are ready.
9. Revisit hosted DTP implementation after real pilot records exist.
10. Run FAOS Phase 0 readiness review after the current active path; do not implement the raw FAOS prompt until the corrections are accepted.

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
