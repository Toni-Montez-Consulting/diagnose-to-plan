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
- Keep all gated actions gated: global skill install, hosted DTP implementation, public proof promotion, write-enabled automation, autonomous agents, and production/client data changes.

## Prompt Activation Matrix

| Prompt shape | Primary activation | Supporting asset | Gate |
|---|---|---|---|
| "review my changes", "review this PR", "find regressions" | `tm-skills/review-checklist` | repo-local tests and CI evidence | no merge/push unless requested |
| "make this UI feel better", "polish this dashboard", "responsive/mobile QA" | `tm-skills/frontend-craft` | visual QA and design-system docs | preserve existing product/design boundary |
| "add auth/schema/API/storage", "design hosted boundary", "smallest backend" | `tm-skills/backend-design` | `docs/HOSTED_DTP_PHASE_0.md` for hosted DTP | boundary accepted before implementation |
| "what tests should run", "CI failed", "verification depth" | `tm-skills/testing-ladder` | repo manifest, evidence index, verification pattern | hard gates stay hard |
| "validate branch", "what is left", "committed/pushed?", "prepare handoff" | `tm-skills/delivery-baseline` | evidence index, git status, CI status | do not commit/push unless requested |
| "what is next on the roadmap", "keep everything aligned", "capture this idea" | Roadmap Steward review | `docs/ROADMAP_EXECUTION_BACKLOG.md` | update status only with real evidence |
| "new idea", "design idea", "business idea", "development enhancement", "project idea", "can we add this later" | contextual idea intake | `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md`, story activation index | classify before implementation |
| "which agent/skill should this story use", "tie this to Kanban", "activate for this epic" | story activation index | `docs/ROADMAP_STORY_ACTIVATION_INDEX.md`, story activation contract | suggested agents require explicit delegation approval |
| "audit the agent system", "what gaps did we miss", "why did this not activate", "I caught a design hole" | Agentic Performance Gap Review | `docs/PRACTICE_SYSTEM_AGENTIC_PERFORMANCE_GAP_REVIEW.md`, Roadmap Steward review | convert misses into durable artifacts, not autonomy |
| "can this become proof", "case study", "public claim" | proof/redaction templates | evidence source, asset inventory, claim review | permission, redaction, reviewer required |
| "client uses Azure/Copilot/Microsoft", "DSE", "COI" | DTP COI screen | data classification and redaction policy | pause before scoping/coding |
| "does this need a portal", "command room", "owner dashboard" | Command Room fit assessment | Command Room spec if fit passes | checklist/no surface is allowed |
| "new client kit", "Mom nonprofit", "engagement plan" | Client Operating Kit | diagnose, plan, consent, data inventory | private engagement material stays private |
| "research this tool/protocol", "should we adopt X" | research radar or research spike | Future Intelligence layer | classify Adopt/Pilot/Watch/Reject |
| "agent failed", "lesson learned", "make this self-learning" | lesson capture and eval candidate | agent session record | human approves skill/eval updates |
| "red-team this AI flow", "guardrails", "prompt injection" | AI red-team plan | OWASP/NIST/OpenAI guardrail references | before public/write-enabled AI |
| "feature flag", "kill switch", "rollback plan" | feature flag/kill switch plan | release trust/supply-chain baseline | required for risky client-facing automation |
| "which repo should this touch", "all apps covered?" | repo manifest and portfolio scorecard | workspace roadmap/backlog | do not force churn into every repo |
| "install skills globally", "activate tm-skills everywhere" | `tm-skills` install dry-run first | `doctor.ps1`, `freshness-check.ps1`, `install.ps1 -WhatIf` | `install.ps1 -Apply` needs explicit approval |
| "build an agent manager", "autonomous steward", "self-modifying skills" | parked/gated automation | Roadmap Steward V0 and Future Intelligence | manual loop, evals, guardrails first |

## Classification Labels

Use these labels in Roadmap Steward reviews and handoffs:

- `global_sdlc_skill`
- `dtp_practice_skill`
- `contextual_idea_intake`
- `practice_os_template`
- `roadmap_backlog_story`
- `proof_redaction_gate`
- `coi_privacy_gate`
- `research_eval_lesson`
- `repo_touch_pass`
- `parked_gated_automation`

## Update Rules

- When a `tm-skills` trigger description, trigger eval, or expected behavior changes, update this map or record why no map update is needed.
- When a DTP Practice OS template becomes required by `dtp practice doctor`, add it to this map if a future prompt should route to it.
- When a new repo lane is added to the workspace roadmap, add or update the relevant routing row.
- When a new idea introduces a new roadmap lane, business direction, design pattern, agent behavior, or recurring trigger, capture it through contextual idea intake before promoting it.
- When a backlog story changes status or ownership, check whether `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` needs a matching activation update.
- When a prompt repeatedly misroutes, capture the miss in a lesson, eval, `tm-skills/MISFIRES.md`, or Roadmap Steward review.
- When Toni identifies a missing agent behavior, process gap, or repeated planning miss, run the Agentic Performance Gap Review and decide whether the fix is a template, eval, skill update, research item, backlog story, decision record, or parked automation.

## Safety Notes

Do not include secrets, private client details, raw intake, Microsoft confidential material, unredacted logs, or unsupported public proof claims.
