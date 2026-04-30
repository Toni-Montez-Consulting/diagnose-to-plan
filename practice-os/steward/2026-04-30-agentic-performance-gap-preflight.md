---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Preflight: Agentic Performance Gap + Mom Pilot

Date: 2026-04-30

## Trigger

Toni identified that the previous system audit did not go far enough into agentic performance gaps. The system needed a recurring way to ask where agents failed to route, remember, validate, research, trigger the right skill, protect boundaries, or convert ideas into durable work.

## Classification

| Item | Classification | Owner | Gate |
|---|---|---|---|
| Agentic performance gap review | `dtp_template_update`, `roadmap_backlog_story`, `learning_loop` | `diagnose-to-plan` | required by `dtp practice doctor` |
| Safe `tm-skills` install | `global_sdlc_skill` | `tm-skills` | `install.ps1 -Apply` without `-Force`, then smoke evidence |
| Mom nonprofit kit refresh | `practice_os_template`, `proof_redaction_gate` | private `engagements/` vault | public facts only plus owner questions |
| Command Room fit assessment | `practice_os_template` | private Mom kit | handoff checklist first, no portal yet |
| First proof/redaction candidate | `proof_redaction_gate` | private Mom kit | internal only until evidence, permission, redaction, reviewer, caveat |

## Repo Boundaries

- `diagnose-to-plan`: owns the new required performance-gap review, steward receipt, decision record, and private kit workflow.
- `tm-skills`: owns global SDLC skill install checks and skill pointer documentation.
- `consulting`, Hub, Omnexus, DeMario, FamilyTrips, DSE, engineering-playbook, `hub-prompts`, and `hub-registry`: no direct edits in this pass.

## Safety Gates

- Global skill install: approved for `install.ps1 -Apply` only; no `-Force`.
- Private data: keep Mom kit in ignored `engagements/` and local vault.
- Public proof: no publication until evidence, permission, redaction, reviewer, and caveat are real.
- Hosted DTP: no app implementation in this pass.
- Autonomous agents: no agent manager or write-enabled automation in this pass.

## Next Queue

1. Add and enforce the Agentic Performance Gap Review.
2. Run safe `tm-skills` checks, apply install, and record smoke-test status.
3. Initialize the private vault and snapshot the Mom kit after refresh.
4. Refresh Mom public facts from the live site and add owner-facts intake questions.
5. Complete Command Room fit assessment with handoff checklist as the default recommendation.
6. Keep first proof/redaction candidate internal.
