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
- Use `practice-os/templates/roadmap-steward-review.md` before or after major roadmap sessions.
- Use `practice-os/templates/story-activation-contract.md` when a story needs a one-off activation record.
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

## Epic Activation Map

| Epic | Story family | Primary activation | Suggested agent role | Required gates |
|---|---|---|---|---|
| Reusable Agent SDLC Layer | `tm-skills` creation, CI, install, canary, overlays | `tm-skills` repo docs, install dry-run, `testing-ladder`, `delivery-baseline` | `local-codex`; `reviewer` only after install/canary work | no `install.ps1 -Apply` without explicit approval; doctor/freshness/install dry-run; CI green |
| Practice OS And Client Command Rooms | pattern capture, fit assessment, command-room implementation, proof packet | Command Room fit/spec templates, Roadmap Steward, proof/redaction templates | `local-codex`; `explorer` for candidate repo discovery only if asked | fit assessment before portal UI; proof permission/redaction before screenshots or claims |
| Verification And CI Spine | thin CI, prompt/registry validation, reusable workflows | `testing-ladder`, `delivery-baseline`, repo manifest, evidence index, verification pattern | `local-codex`; `worker` only for disjoint CI slices if asked | run local gate before CI; hard gates stay hard; no shared workflow abstraction before repetition |
| Hosted DTP Phase 0 | schema/app boundary, app shell, import/export, MCP recall | `backend-design`, hosted DTP design doc, boundary decision, steward review | `local-codex`; `worker` only after implementation is explicitly approved | design accepted; hosted implementation requires separate request; no dashboard theater |
| Proof And Redaction Governance | proof templates, first proof pilot, consulting/Omnexus/DeMario/DSE proof lanes | proof packet, redaction queue, permission checklist, evidence checklist, public claim review | `local-codex`; `reviewer` for proof review only if asked | evidence, caveat, permission, redaction, reviewer before public proof |
| Workspace Efficiency Layer | repo manifests, evidence indexes, command-center spec, affected checks, dependency policy | repo manifest, evidence index, decision record, workspace command-center spec | `local-codex`; `explorer` for repo-specific discovery only if asked | do not mutate sibling repos without lane readiness; no command runner until manifests prove useful |
| Roadmap Steward Loop | steward template, activation map, steward command, hosted queue, agent manager | activation map, steward review, story activation contract | `local-codex`; `parked-autonomy` for future manager | no autonomous edits/status changes; manual loop proves value first |
| Future Intelligence Layer | flight records, research radar, eval garden, red-team lab | lesson capture, research radar, agent session record, red-team plan | `local-codex`; `reviewer` for red-team only if asked | human-approved learning; evals before autonomy; primary sources for research |
| First Client Operating Kit Pilot | Mom kit, fit assessment, proof/redaction, handoff/runbook, public proof | Client Operating Kit, Command Room fit, proof/redaction templates, handoff/runbook | `local-codex`; `explorer` only for public/source discovery if asked | private kit stays private; consent/COI first; public proof blocked until review |
| Adjacent Project Touch Lanes | Omnexus, DeMario, FamilyTrips, DSE, engineering-playbook | repo manifest, portfolio scorecard, proof/COI/privacy lane, repo-specific gates | `local-codex`; `explorer` for scoped repo discovery only if asked | do not disturb active branches; touch only when trigger is ready |

## Current Active Story Activation

| Active story | Trigger examples | Activation | Agent role | Done gate |
|---|---|---|---|---|
| Fill Mom nonprofit private kit | "use my mom's website", "scope nonprofit rebuild", "fill the Mom kit" | Client Operating Kit, public-source inventory, consent, diagnose, plan, metrics | `local-codex` | private kit updated, redaction check passes, no private data committed |
| Complete Command Room fit assessment | "does Mom need a portal", "owner dashboard", "command room" | Command Room fit assessment, no-portal/checklist decision path | `local-codex` | real owner workflow facts decide portal vs checklist vs defer |
| First proof/redaction packet | "can this become proof", "case study", "baseline screenshots" | proof packet, asset inventory, evidence checklist, redaction queue, permission checklist | `local-codex`; `reviewer` only if asked | evidence, caveat, permission, redaction, reviewer before public proof |
| Expand repo manifests | "make every repo covered", "what does this repo own", "which gates run" | repo manifest, evidence index, portfolio scorecard | `local-codex`; `explorer` only if asked | manifest names purpose, gates, proof/privacy lane, deploy/data boundaries |
| Hub prompt/registry validation | "Hub prompts", "registry cross-validation", "prompt ids" | `testing-ladder`, Hub prompt/registry validation story | `local-codex`; `worker` only if asked and write scopes are split | local gates pass in both repos; CI-safe path does not require private siblings unless configured |

## Story-Level Update Contract

When a backlog story changes status, also check whether one of these needs an update:

- this activation index;
- `practice-os/templates/activation-routing-map.md`;
- `practice-os/templates/roadmap-steward-review.md`;
- repo manifest or evidence index;
- proof/redaction template;
- `tm-skills` trigger description or eval;
- research radar item;
- lesson/eval/agent-session record.

## No-Touch Defaults

- Do not globally install `tm-skills` unless explicitly approved.
- Do not spawn agents unless Toni explicitly asks for agents, delegation, or parallel agent work.
- Do not start hosted DTP app implementation from a routing/steward prompt alone.
- Do not publish or prepare public proof without permission/redaction/reviewer gates.
- Do not mutate `fitness-app`/Omnexus while its active branch is not intentionally reopened.
- Do not fold Hub, consulting, DTP, and project repos into one ownership surface.
