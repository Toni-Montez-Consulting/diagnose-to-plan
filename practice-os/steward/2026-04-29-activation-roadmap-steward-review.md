---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Activation + Roadmap Steward Review

## Session

- Date: 2026-04-29
- Steward: Codex
- Trigger: "Great, lets roll" after Roadmap Steward V0 and AI Activation Map V0 implementation
- Repos reviewed: `diagnose-to-plan`, `tm-skills`, workspace coverage table
- Roadmap files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`, `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`, `docs/PRACTICE_PRODUCTION_ROADMAP.md`
- Activation files reviewed: `practice-os/templates/activation-routing-map.md`, `practice-os/templates/roadmap-steward-review.md`

## Activation Result

- Prompt shape: execute the next roadmap step and preserve the new process layer.
- Primary activation: Roadmap Steward review plus Activation Routing Map.
- Supporting activation: `tm-skills/delivery-baseline` behavior once global skill install is approved.
- Classification: `roadmap_backlog_story`, `practice_os_template`, `repo_touch_pass`.
- Gated paths not activated: global skill install, hosted DTP implementation, public proof promotion, autonomous roadmap manager, write-enabled agent automation.

## Source Of Truth Check

- DTP remains the practice roadmap source of truth.
- `docs/ROADMAP_EXECUTION_BACKLOG.md` remains the Kanban execution surface.
- `tm-skills` remains the global SDLC skills repo, not the practice roadmap owner.
- Repo manifests/evidence indexes remain pilots; they should inform future steward reviews but do not yet drive automation.

## Workspace Coverage

Every workspace repo remains represented in the roadmap/backlog:

- `consulting`: public storefront, proof surface, Hub intake path.
- `diagnose-to-plan`: Practice OS, roadmap, proof/redaction, hosted DTP boundary.
- `hub`: runtime intake, console records, prompts/runs support.
- `engineering-playbook`: doctrine and pointer audit lane.
- `hub-prompts`: prompt catalog and future eval lane.
- `hub-registry`: automation target routing and future prompt id validation.
- `fitness-app`: Omnexus verification cockpit reference and product proof lane.
- `FamilyTrips`: privacy-first family app lane.
- `demario-pickleball-1`: local-business launch proof and Command Room reference.
- `dse-content`: COI-aware internal proof lane.
- `tm-skills`: reusable SDLC skills and global activation lane.

## Active Next Queue

1. Process-layer preservation: done.
   - DTP commit: `91e7c6a docs: add roadmap steward activation layer`.
   - `tm-skills` commit: `383d4f2 docs: align skills with activation map`.
2. First live steward receipt: active in this file.
3. Review and accept hosted DTP Phase 0 plus DTP efficiency pilot.
4. Run Mom nonprofit as the first private Client Operating Kit pilot.
5. Use Command Room fit assessment before any portal decision.
6. Use proof/redaction templates on the first proof candidate before anything moves to consulting proof.
7. Add Hub prompt/registry cross-validation after the pilot or when Hub work resumes.

## Idea Capture

| Idea | Classification | Owning repo | Action | Gate |
|---|---|---|---|---|
| Roadmap should not rely on Toni's memory | `practice_os_template` | `diagnose-to-plan` | Use Roadmap Steward review around major sessions | steward template exists and first receipt created |
| Prompt should activate the right skill/process | `practice_os_template` | `diagnose-to-plan` | Use Activation Routing Map | activation map exists and practice doctor enforces it |
| SDLC skills should align with DTP routing | `global_sdlc_skill` | `tm-skills` | Keep trigger changes synced to activation map | doctor/freshness/install preview pass |
| Future automated steward command | `parked_gated_automation` | `diagnose-to-plan` | Keep `dtp steward review` later | manual loop must prove useful first |

## Process Compliance

- Proof/redaction needed before public claim: yes, for any consulting proof promotion.
- COI/privacy review needed: yes, for Microsoft/DSE/client-adjacent work.
- Agent flight record needed: recommended after the next complex implementation, but this steward receipt covers the current process handoff.
- Research radar item needed: no new external research signal in this step.
- Eval fixture candidate: future candidate if prompt routing misfires.
- Decision record needed: no new architecture decision beyond the already-documented private DTP boundary.
- Hosted app, global install, public proof, and autonomous agent work remain gated.

## Verification Snapshot

- DTP validation before preservation: `pytest`, `ruff check .`, `dtp skills --validate`, `dtp practice doctor`, targeted redaction checks.
- `tm-skills` validation before preservation: `doctor.ps1`, `freshness-check.ps1`, `install.ps1 -WhatIf`.
- DTP commit hook secret scan: passed for commit `91e7c6a`.
- Global install: not run.

## Outcome

- Backlog update needed: none before hosted DTP review; the backlog already marks steward and activation map V0 as done.
- Roadmap update needed: none before hosted DTP review.
- Template update needed: none until first misroute or first live pilot teaches a better trigger.
- Repo manifest/evidence index update needed: review DTP pilot before expanding to consulting, Hub, or `tm-skills`.
- Next steward review trigger: before accepting hosted DTP Phase 0 or starting the Mom nonprofit kit.

## Safety Notes

No secrets, raw private client details, Microsoft confidential material, unredacted logs, or unsupported proof claims were added.
