---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Review: DeMario Adjacent Touch Pass

## Session

- Date: 2026-04-30
- Steward: Codex
- Trigger: continue the roadmap after Hub prompt/registry validation and choose the next executable, non-blocked step
- Repos reviewed: `diagnose-to-plan`, `fitness-app`, `demario-pickleball-1`, `FamilyTrips`, `dse-content`
- Roadmap files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`, `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`, `docs/DOCUMENTATION_MAP.md`
- Backlog files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`
- Story activation files reviewed: `docs/ROADMAP_STORY_ACTIVATION_INDEX.md`
- Contextual intake files reviewed: activation/steward guidance already selected the repo touch pass lane

## Source Of Truth Check

- DTP remains the practice roadmap source of truth: yes
- `docs/ROADMAP_EXECUTION_BACKLOG.md` reflects current story status: updated for the DeMario manifest/evidence pass
- Repo manifests/evidence indexes were checked where available: yes
- No sibling repo is being treated as the practice-wide roadmap owner: yes

## Workspace Coverage

- `consulting`: unchanged; public proof remains gated.
- `diagnose-to-plan`: owns the new manifest, evidence index, steward receipt, and roadmap updates.
- `hub`: unchanged; Hub prompt/registry validation remains local-first.
- `engineering-playbook`: unchanged; doctrine pointer audit remains later.
- `hub-prompts`: unchanged.
- `hub-registry`: unchanged.
- `fitness-app`: inspected only; branch `main` is clean but remains a separate Omnexus reference lane.
- `FamilyTrips`: inspected only; branch `main` is clean and remains privacy-first future lane.
- `demario-pickleball-1`: inspected and validated locally; no tracked repo changes remain.
- `dse-content`: inspected only; active branch has uncommitted work and remains out of scope.
- `tm-skills`: unchanged; Claude Code and GitHub Copilot smoke tests remain manual.

## Active Next Queue

- Current next story: first adjacent-project touch pass
- Owning repo: `diagnose-to-plan` for the planning receipt; `demario-pickleball-1` remains the source repo for its own launch gates
- Status: implemented as DTP-owned manifest/evidence index
- Done gate: DeMario purpose, boundaries, gates, evidence, proof blockers, and next touch triggers are captured without mutating the app repo
- Story activation: Adjacent Project Touch Lanes and Workspace Efficiency Layer
- Suggested skill/template: `tm-skills/delivery-baseline`, `tm-skills/testing-ladder`, Roadmap Steward Review
- Suggested agent role: local coding agent
- Local gates: DeMario `npm run ci` passed; DTP validation runs after roadmap edits
- CI or manual gates: DeMario GitHub Actions CI run `25125162032` passed; release/proof gates remain manual
- Blockers: public proof requires owner permission, source evidence, redaction, reviewer, launch context, and caveats
- What must not be touched yet: public consulting proof pages, live production admin actions, Vercel/Supabase/Google OAuth settings, student data, payment records, DSE active branch work, and Omnexus active PR work

## Idea Capture

| Idea | Classification | Owning repo | Activation | Action | Gate |
|---|---|---|---|---|---|
| Add a DTP-owned DeMario manifest/evidence index | repo touch pass | `diagnose-to-plan` | Workspace Efficiency Layer | create manifest and evidence receipt | local DeMario gate and DTP validation |
| Use DeMario as command-room proof | proof item | `demario-pickleball-1`, `consulting`, DTP proof flow | Proof And Redaction Governance | keep internal until permissioned | owner permission, redaction, reviewer, caveat |
| Stabilize `next-env.d.ts` typed-route churn | story | `demario-pickleball-1` | Delivery baseline | park unless it keeps dirtying future gates | tested repo-local fix or explicit doc decision |
| Node 24 runner/toolchain maintenance | story | `demario-pickleball-1` | Delivery baseline | keep on developer roadmap | tested migration branch before runner default matters |

## Process Compliance

- Proof/redaction needed before public claim: yes, for any DeMario proof or screenshots.
- COI or permission review needed: permission yes; COI no by default.
- Agent flight record needed: no; steward receipt is sufficient.
- Story activation index update needed: no; existing adjacent touch lane covers this.
- Research radar item needed: no.
- Eval fixture candidate: no.
- Decision record needed: no.
- Hosted app, global install, public proof, or autonomous agent work is gated: yes.

## Outcome

- Backlog update needed: complete.
- Roadmap update needed: complete.
- Template update needed: no.
- Repo manifest/evidence index update needed: complete for DeMario.
- Next steward review trigger: before choosing the next adjacent project touch pass or before promoting DeMario proof into consulting.

## Safety Notes

Do not include student PII, payment records, private admin screenshots, venue agreements, insurance certificates, OAuth values, Supabase values, secrets, or unapproved testimonial/review claims in public docs or proof.
