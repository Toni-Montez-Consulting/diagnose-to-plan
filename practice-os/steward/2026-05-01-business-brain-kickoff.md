---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Review: Business Brain Kickoff

## Session

- Date: 2026-05-01
- Steward: Codex
- Trigger: Toni asked to implement the Business Brain / Consulting OS roadmap
  plan and commit the context to durable repo artifacts.
- Repos reviewed: `diagnose-to-plan`, `consulting`
- Roadmap files reviewed: `docs/PRACTICE_PRODUCTION_ROADMAP.md`,
  `docs/ROADMAP_EXECUTION_BACKLOG.md`, `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`
- Backlog files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`
- Story activation files reviewed: `practice-os/templates/activation-routing-map.md`
- Contextual intake files reviewed: `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md`
- Notion mirror/inbox reviewed: no; Notion remains mirror/inbox only.

## Source Of Truth Check

- DTP remains the practice roadmap source of truth: yes.
- `docs/ROADMAP_EXECUTION_BACKLOG.md` reflects current story status: updated in
  this slice.
- Repo manifests/evidence indexes were checked where available: not needed for
  new Business Brain source docs.
- Notion is being treated as a mirror/capture surface, not the source of truth:
  yes.
- No sibling repo is being treated as the practice-wide roadmap owner: yes.

## Active Next Queue

- Current next story: Business Brain / Consulting OS source and first fixtures.
- Owning repo: `diagnose-to-plan`
- Status: Active next
- Done gate: source map, command contracts, fixtures, agent role specs, comms
  kit, roadmap entries, and validation exist.
- Story activation: DTP Practice OS skill plus roadmap stewardship.
- Suggested skill/template: `diagnose`, `coi-screen`, `proposal-draft`,
  `handoff-runbook`, agent-session record, roadmap steward review.
- Suggested agent role: local coding agent.
- Local gates: `dtp practice doctor`, `dtp skills --validate`, pytest, ruff,
  redaction check.
- CI or manual gates: no CI run required for docs-only changes; local validation
  is required.
- Blockers: live QuickBooks, n8n, and direct Notion writes are not confirmed.
- What must not be touched yet: CCAAP owner-input work, public storefront
  pricing/services, live integrations, auto-merge/self-refactor behavior,
  public proof promotion, and sibling repos.

## Idea Capture

| Idea | Classification | Owning repo | Activation | Action | Gate |
|---|---|---|---|---|---|
| Business Brain across business domains | story | `diagnose-to-plan` | Practice OS roadmap | Add source map, command contracts, fixtures, agents, comms | validation and no public claims |
| Business agents for Controller, General Counsel, COO | template | `diagnose-to-plan` | Practice OS agents | Add draft-producing role specs | no autonomy or external writes |
| AI adoption statistic from planning context | research radar item | `diagnose-to-plan` | Future Intelligence | Capture as fact-check item only | no public claim until verified |
| Communications kit | template | `diagnose-to-plan` | ETHOS/comms protocol | Draft private-first kit | public review gate |

## Process Compliance

- Proof/redaction needed before public claim: yes.
- COI or permission review needed: yes for Cameron before contracting and for
  any public proof.
- Agent flight record needed: yes, created with this slice.
- Story activation index update needed: later if Business Brain becomes a
  repeated story family.
- Research radar item needed: later for AI adoption statistics.
- Eval fixture candidate: yes; Greg/Cameron/Mom-Mario fixtures created.
- Decision record needed: no, source map is enough for this first slice.
- Hosted app, global install, public proof, or autonomous agent work is gated:
  yes.

## Outcome

- Backlog update needed: yes.
- Roadmap update needed: yes.
- Template update needed: yes, command contracts and role specs.
- Repo manifest/evidence index update needed: no.
- Next steward review trigger: after the first live Greg, Cameron, or Mom/Mario
  artifact is used in a real meeting or handoff.

## Safety Notes

No secrets, raw private records, Microsoft confidential material, pricing, or
unsupported public proof claims belong in this artifact.
