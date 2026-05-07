---
data_class: P0
confidential: false
permission_level: internal_only
review_status: current
lifecycle_status: current
last_verified: 2026-05-07
owner: diagnose-to-plan
---

# tm-skills Readiness Scorecard

Owner repo: `diagnose-to-plan`

Skill repo: `C:\Users\tonimontez\tm-skills`

Purpose: make `tm-skills` usable as the reusable agent-behavior layer without
letting it override DTP's client, proof, COI, or public-claim gates.

## Current Gate Result

Status: ready for P0 Workflow Spine support, not ready for broad skill
promotion.

Observed during the 2026-05-07 audit:

- `.\scripts\doctor.ps1` passed.
- `.\scripts\freshness-check.ps1` passed.
- `.\scripts\install.ps1 -WhatIf` confirmed global links are already in place.
- Doctor warned about untracked candidate skill folders:
  - `skills/docx`
  - `skills/excalidraw`
  - `skills/expense-report`
  - `skills/loop`
  - `skills/pptx`
  - `skills/web-artifacts-builder`
  - `skills/xlsx`

No candidate skill is promoted by this scorecard.

## Readiness Table

| Skill or group | Phase | Manifest status | Eval status | External smoke | Allowed use | Blocked use | Next gate |
|---|---|---|---|---|---|---|---|
| `review-checklist` | phase-1 | present | present | Codex available; Claude/Copilot CLI smoke previously recorded; VS Code Copilot Chat remains optional manual | code review, regression risk, missing tests, release risk | client proof, COI, public claims, live writes | keep watching for real misfires |
| `frontend-craft` | phase-1 | present | present | Codex available; external smoke previously recorded | UI polish, responsive layout, domain-fit design | public proof or client copy without DTP gates | keep DTP custom-interface standard aligned |
| `backend-design` | phase-1 | present | present | Codex available; external smoke previously recorded | backend boundaries, persistence, auth, queues, jobs | production access or client data mutation without approval | use with repo-local gates |
| `testing-ladder` | phase-1 | present | present | Codex available; external smoke previously recorded | risk-based verification planning | claiming release readiness without evidence | keep verification receipts source-backed |
| `delivery-baseline` | phase-1 | present | present | Codex available; external smoke previously recorded | branch, CI, deploy, repo hygiene, handoff | commit/push/deploy without explicit task and repo gates | keep repo-state checks live |
| `systems-health-review` | phase-1 | present | present | Codex available; external smoke runbook updated | weakest-system reviews across workflows | replacing DTP proof/COI gates | keep activation map aligned |
| Azure and Foundry skills | incubator | present | present | Claude/Copilot CLI smoke previously recorded for canaries; Codex targeted real-work loop still pending | internal Azure/Foundry planning and validation with active-tool translation | live cloud mutation, client COI bypass, credential handling | use only on safe internal Azure task first |
| Office/document skills: `docx`, `pptx`, `xlsx` | parked candidate | not in manifest | missing or unreviewed | not accepted | none by default | client deliverables or public docs without source/license/eval review | source/license review, frontmatter cleanup, trigger eval, output eval |
| `excalidraw` | candidate | not in manifest | missing or unreviewed | not accepted | none by default | architecture/proof diagrams as official artifacts | evals, DTP routing alignment, output safety review |
| `expense-report` | high-risk parked | not in manifest | missing or unreviewed | not accepted | none by default | finance submission, browser writes, external workspace actions | finance/tooling gate, visible-browser approval, no-submit guarantee |
| `loop` | high-risk parked | not in manifest | missing or unreviewed | not accepted | none by default | Microsoft workspace edits, browser writes, client/admin records | workspace authority gate, browser boundary, evals |
| `web-artifacts-builder` | parked candidate | not in manifest | missing or unreviewed | not accepted | none by default | replacing `frontend-craft` or consulting UI standards | source/theme review, conflict check, evals |

## Always-On DTP Override

`tm-skills` may improve how an agent reviews, designs, tests, or finishes work.
It does not authorize:

- public proof movement;
- client communication sends;
- COI-sensitive work;
- accepting confidential client/employer data;
- production writes;
- repo mutation outside the scoped task;
- global install changes;
- candidate skill promotion.

Use DTP gates first when the work touches:

- client facts;
- proof;
- redaction;
- public claims;
- COI;
- money or billing;
- live external writes;
- production data;
- public offer movement.

## Update Triggers

Update this scorecard when:

- a skill changes phase;
- a candidate skill is promoted, parked, or removed;
- `manifest.json` changes;
- external smoke status changes;
- a trigger miss becomes a `MISFIRES.md` entry;
- `practice-os/templates/activation-routing-map.md` changes for skill routing.
