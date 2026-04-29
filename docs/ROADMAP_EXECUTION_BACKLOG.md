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

## Epic 1: Reusable Agent SDLC Layer

Goal: make every future coding session safer and more consistent.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Create `tm-skills` repo and Phase 1 skills | `tm-skills` | Done | repo pushed, doctor/freshness/install dry-run pass, CI green | install only after explicit approval |
| Add `tm-skills` thin CI | `tm-skills` | Done | GitHub Actions green | keep workflow thin |
| Global install and tool reload smoke test | `tm-skills` | Blocked | Codex/Claude/Copilot discover skills after approved install | wait for explicit install approval |
| Project-pinned canary | `tm-skills` plus one repo | Later | one low-risk repo confirms no duplicate-skill confusion | choose after global install works |
| Stack overlays | `tm-skills` | Later | base skills prove useful across real work | design overlays only after canary |

## Epic 2: Practice OS And Client Command Rooms

Goal: make owner/operator command-room decisions repeatable without building portals by default.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Capture Client Command Room pattern | `diagnose-to-plan` | Done | pattern doc plus fit/spec templates exist and practice doctor passes | use on first pilot |
| First Command Room fit assessment | `diagnose-to-plan` | Active next | Mom nonprofit or another pilot has a completed fit assessment | run before any portal UI |
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
| Prompt id cross-validation | `hub-prompts`, `hub-registry` | Ready | registry references resolve to prompt ids without requiring private sibling access in repo-scoped CI | implement after Mom pilot or if Hub work resumes |
| Shared reusable workflows | core repos | Later | at least three repos repeat the same stable workflow | do not abstract early |

## Epic 4: Hosted DTP Phase 0

Goal: define and later build the private app foundation for engagements, artifacts, evidence, redaction, proof, and decisions.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Phase 0 schema/app-boundary design | `diagnose-to-plan` | Review | `docs/HOSTED_DTP_PHASE_0.md` accepted | human review/acceptance |
| Boundary decision record | `diagnose-to-plan` | Review | `decisions/0004-hosted-dtp-private-practice-os-boundary.md` accepted | review with Phase 0 doc |
| Hosted DTP schema/app-shell implementation | `diagnose-to-plan` | Blocked | private auth/RLS/storage shell reads real records, no dashboard theater | wait for design acceptance |
| Import/export contract | `diagnose-to-plan` | Ready | local markdown kits can round-trip with hosted records | implement with app shell |
| MCP recall | `diagnose-to-plan` | Later | 2-3 real engagements make manual recall painful | keep deferred |

## Epic 5: Proof And Redaction Governance

Goal: make public proof evidence-backed, permissioned, caveated, and reviewable.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Proof/redaction templates | `diagnose-to-plan` | Done | proof packet, redaction item, permission, evidence, public claim, and asset templates exist | use on first pilot |
| First proof/redaction pilot | `diagnose-to-plan` plus pilot repo | Active next | one real project uses proof packet and redaction queue before public proof | use Mom nonprofit first if ready |
| Consulting proof backlog | `consulting` | Ready | proof candidates mapped to real source material and redaction state | start after first pilot |
| Omnexus proof candidates | `fitness-app` | Later | PR/work is human-reviewed and proof is permissioned/redacted | do not disturb active app work |
| DeMario proof packet | `demario-pickleball-1` | Later | launch gates and permission are complete | keep owner-safe |
| DSE internal proof lane | `dse-content` | Later | COI, permission, and redaction review complete | internal/professional only |

## Epic 6: Workspace Efficiency Layer

Goal: reduce rediscovery, setup drift, CI waste, and handoff friction.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| DTP repo manifest/evidence-index pilot | `diagnose-to-plan` | Review | pilot shape accepted as useful | review after current docs settle |
| Consulting repo manifest | `consulting` | Ready | manifest names gates, deploy target, proof lane, and data boundaries | create after DTP pilot accepted |
| Hub repo manifest | `hub` | Ready | manifest names runtime gates, Supabase/Vercel boundaries, and prompt/run ownership | create after DTP pilot accepted |
| `tm-skills` repo manifest | `tm-skills` | Ready | manifest names install gates and global-skill boundaries | create after DTP pilot accepted |
| Workspace Command Center spec | `diagnose-to-plan` | Later | manifests/evidence indexes prove useful in at least two repos | no command runner yet |
| Affected-only verification | DTP/Hub first | Later | hard gates are reliably encoded per repo | keep advisory until proven |
| Dependency maintenance policy | each repo | Later | grouping/schedule/approval rules accepted | do not enable bots broadly yet |

## Epic 7: Future Intelligence Layer

Goal: turn delivery, failures, research, and agent sessions into supervised learning.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Future Intelligence templates | `diagnose-to-plan` | Done | lesson, research, scorecard, flight recorder, red-team, feature flag, and supply-chain templates exist | use opportunistically |
| First agent flight record | `diagnose-to-plan` | Ready | one major session leaves a reusable receipt | capture on next complex implementation |
| Research Radar first item | `diagnose-to-plan` | Ready | one item classified Adopt/Pilot/Watch/Reject with source and next action | use when research changes roadmap |
| Eval garden | `hub-prompts`, `tm-skills`, DTP | Later | real misfires become fixtures | wait for misfire history |
| Red-team lab | Hub/DTP future agent workflows | Later | adversarial tests exist before write-enabled automation | keep before autonomy |

## Epic 8: First Client Operating Kit Pilot

Goal: run one real engagement through the Practice OS before building more platform surface.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Mom nonprofit kit creation | `diagnose-to-plan` private `engagements/` | Active next | kit created with COI, consent, diagnose, plan, and metrics placeholders | run only with appropriate private handling |
| Command Room fit assessment | `diagnose-to-plan` | Active next | assessment decides portal vs checklist vs no private surface | complete before UI |
| Proof/redaction use | `diagnose-to-plan` | Active next | proof packet and redaction queue item created for one claim candidate | keep internal until reviewed |
| Handoff/runbook | `diagnose-to-plan` plus project repo | Ready | owner-safe handoff exists | after build scope is known |
| Public proof promotion | `consulting` | Blocked | permission, redaction, reviewer, evidence, and caveat all approved | no auto-publish |

## Epic 9: Adjacent Project Touch Lanes

Goal: ensure every workspace repo benefits without unnecessary churn.

| Story | Repo | Status | Done gate | Next action |
|---|---|---|---|---|
| Omnexus verification cockpit review | `fitness-app` | Later | active PR/branch human-reviewed, reusable lessons extracted | do not mutate until reopened |
| DeMario launch/proof pass | `demario-pickleball-1` | Later | manual launch/venue/permission gates complete | owner-safe proof only |
| FamilyTrips privacy maintenance pass | `FamilyTrips` | Later | data validation/build/test and privacy notes complete | before new features or AI/public sharing |
| DSE COI-aware proof pass | `dse-content` | Later | COI screen and live branch verification complete | internal/professional only |
| Engineering playbook pointer audit | `engineering-playbook` | Later | doctrine points to DTP without duplicating roadmap ownership | after DTP contracts settle |

## Current Active Next Queue

1. Review and accept `docs/HOSTED_DTP_PHASE_0.md` and the DTP efficiency pilot.
2. Run the Mom nonprofit Client Operating Kit pilot privately.
3. Use the Command Room fit assessment before deciding on any portal.
4. Use proof/redaction templates on the first proof candidate.
5. Add Hub prompt/registry cross-validation after the pilot or when Hub resumes.

## Answer To The Kanban Question

Yes, the roadmap should be planned in epic/story fashion. Not every item is ready for implementation today, and that is intentional. The execution model is:

- Strategic roadmap: what matters and why.
- Execution backlog: epics, stories, statuses, Done gates, and next actions.
- Implementation plans: created only when a story moves to `Active next`.
- Code/docs/templates: built only when the story's gate and repo boundary are clear.
