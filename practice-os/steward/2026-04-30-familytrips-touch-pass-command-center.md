---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Review: FamilyTrips Touch Pass And Command Center Spec

## Session

- Date: 2026-04-30
- Steward: Codex
- Trigger: implement next batch after DeMario adjacent pass while Mom owner facts remain pending
- Repos reviewed: `diagnose-to-plan`, `FamilyTrips`, `tm-skills`, `hub-registry`, `hub-prompts`, `engineering-playbook`
- Roadmap files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`, `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`, `docs/FAOS_ORCHESTRATION_ROADMAP.md`
- Backlog files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`
- Story activation files reviewed: `docs/ROADMAP_STORY_ACTIVATION_INDEX.md`
- Contextual intake files reviewed: no new idea intake needed; this follows accepted backlog lanes

## Source Of Truth Check

- DTP remains the practice roadmap source of truth: yes
- `docs/ROADMAP_EXECUTION_BACKLOG.md` reflects current story status: updated for FamilyTrips and Command Center V0 spec
- Repo manifests/evidence indexes were checked where available: yes
- No sibling repo is being treated as the practice-wide roadmap owner: yes

## Workspace Coverage

- `consulting`: unchanged; public proof remains gated.
- `diagnose-to-plan`: owns the new FamilyTrips receipts, Workspace Command Center V0 spec, and roadmap updates.
- `hub`: unchanged.
- `engineering-playbook`: inspected only; pointer/doctrine audit remains a future adjacent touch pass.
- `hub-prompts`: unchanged.
- `hub-registry`: unchanged; local-first `npm test` passed.
- `fitness-app`: unchanged; Omnexus remains reference verification cockpit and future proof lane.
- `FamilyTrips`: local pointer, verification date, and thin GitHub Actions CI added; no feature/auth/AI/platform changes.
- `demario-pickleball-1`: unchanged; manifest/evidence pass already exists.
- `dse-content`: unchanged and intentionally avoided.
- `tm-skills`: external smoke runbook added; links and preview are healthy, but Claude Code/GitHub Copilot reload smoke remains manual.

## Active Next Queue

- Current next story: FamilyTrips privacy-first adjacent touch pass and Workspace Command Center V0 spec
- Owning repo: `diagnose-to-plan` for receipts/spec; `FamilyTrips` for local playbook pointer and verification date
- Status: implemented as docs/evidence work
- Done gate: FamilyTrips local and CI gates pass, privacy model is recorded, DTP manifests/evidence indexes are updated, and Command Center remains read-only/spec-only
- Story activation: Adjacent Project Touch Lanes and Workspace Efficiency Layer
- Suggested skill/template: `tm-skills/delivery-baseline`, `tm-skills/testing-ladder`, Roadmap Steward Review
- Suggested agent role: local coding agent
- Local gates: FamilyTrips `validate:data`, lint, tests, build; DTP validation after docs edits; `tm-skills` doctor/freshness/install preview; `hub-registry npm test`
- CI or manual gates: FamilyTrips CI run `25158714066` passed with a Node 20 action-runtime deprecation advisory; tm-skills CI run `25158720574` passed; external Claude Code/GitHub Copilot smoke remains manual
- Blockers: Mom owner facts; public proof permissions; external skill reload verification; FAOS readiness acceptance
- What must not be touched yet: FAOS repo/services, Hub sibling-repo CI tokens, public proof pages, FamilyTrips auth/AI/public sharing, production Supabase/Vercel settings, and DSE active branch work

## Idea Capture

| Idea | Classification | Owning repo | Activation | Action | Gate |
|---|---|---|---|---|---|
| FamilyTrips privacy-first touch pass | repo touch pass | `FamilyTrips`, DTP | Workspace Efficiency Layer | add local pointer, DTP manifest, DTP evidence index | local gates pass |
| Workspace Command Center V0 | story | DTP | Workspace Efficiency Layer | create read-only docs/spec | no command runner or mutations |
| Claude Code and Copilot smoke | manual gate | `tm-skills` | delivery baseline | keep pending until tools are reloaded and observed | no false pass |
| Hub prompt/registry local-first validation | story evidence | `hub-registry`, `hub-prompts` | testing ladder | record local `npm test` pass | defer sibling CI tokens |
| FAOS Phase 0 readiness | parked/gated story | DTP/future `faos` | FAOS readiness | keep parked | pilot/proof/smoke path first |

## Process Compliance

- Proof/redaction needed before public claim: yes, for any future FamilyTrips screenshots/data or DeMario/Omnexus proof.
- COI or permission review needed: no for FamilyTrips by default; permission required for family data reuse.
- Agent flight record needed: no; steward receipt is sufficient.
- Story activation index update needed: no; existing Workspace Efficiency and adjacent touch lanes cover this.
- Research radar item needed: no.
- Eval fixture candidate: only if `tm-skills` external smoke reveals a trigger miss.
- Decision record needed: no.
- Hosted app, global install, public proof, or autonomous agent work is gated: yes.

## Outcome

- Backlog update needed: complete.
- Roadmap update needed: complete.
- Template update needed: no.
- Repo manifest/evidence index update needed: complete for FamilyTrips.
- Workspace Command Center V0 spec: complete as read-only docs; implementation remains later.
- Next steward review trigger: after Mom owner facts arrive, external skill smoke is performed, or the next adjacent repo lane is ready.

## Safety Notes

Do not include private family data, addresses, phone numbers, reservation details, budgets, passwords, private screenshots, client records, Microsoft/customer-adjacent material, secrets, or unredacted logs in public docs or proof.
