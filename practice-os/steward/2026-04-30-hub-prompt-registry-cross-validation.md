---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Review: Hub Prompt/Registry Cross-Validation

## Session

- Date: 2026-04-30
- Steward: Codex
- Trigger: implement the queued Hub prompt/registry cross-validation story
- Repos reviewed: `hub-prompts`, `hub-registry`, `hub`, `diagnose-to-plan`
- Roadmap files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`, `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`, `docs/PRACTICE_VERIFICATION_SPINE.md`
- Backlog files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`
- Story activation files reviewed: `docs/ROADMAP_STORY_ACTIVATION_INDEX.md`
- Contextual intake files reviewed: not needed; this continued an accepted backlog story

## Source Of Truth Check

- DTP remains the practice roadmap source of truth: yes
- `docs/ROADMAP_EXECUTION_BACKLOG.md` reflects current story status: updated to mark local prompt id validation done
- Repo manifests/evidence indexes were checked where available: yes, Hub evidence index updated
- No sibling repo is being treated as the practice-wide roadmap owner: yes

## Workspace Coverage

- `consulting`: unchanged; public proof remains gated.
- `diagnose-to-plan`: source-of-truth docs updated.
- `hub`: unchanged runtime; evidence index updated to reflect prompt/registry gate.
- `engineering-playbook`: unchanged.
- `hub-prompts`: validated with `npm test`; prompt content unchanged.
- `hub-registry`: owns the new local prompt-id validator.
- `fitness-app`: untouched; active branch work remains out of scope.
- `FamilyTrips`: unchanged.
- `demario-pickleball-1`: unchanged.
- `dse-content`: unchanged.
- `tm-skills`: unchanged; external Claude/Copilot smoke remains manual.

## Active Next Queue

- Current next story: Hub prompt/registry cross-validation
- Owning repo: `hub-registry`, with `hub-prompts` as read-only sibling source
- Status: implemented as local workspace gate
- Done gate: `hub-registry npm test` validates registry shape, sibling manifests, and prompt ids against `hub-prompts`
- Story activation: Hub prompt/registry validation lane
- Suggested skill/template: `tm-skills/testing-ladder`, `tm-skills/delivery-baseline`
- Suggested agent role: local coding agent
- Local gates: `hub-prompts npm test`; `hub-registry npm run validate`, `npm run validate:manifests`, `npm run validate:prompt-ids`, `npm test`
- CI or manual gates: `hub-registry` CI remains repo-scoped and runs `npm run validate`
- Blockers: cross-repo CI requires explicit private sibling-repo access before promotion
- What must not be touched yet: prompt content, registry target activation, Hub runtime automation, private proof, hosted DTP implementation

## Idea Capture

| Idea | Classification | Owning repo | Activation | Action | Gate |
|---|---|---|---|---|---|
| Validate registry prompt ids against prompt catalogue before runtime | story | `hub-registry` | testing ladder | add `validate:prompt-ids` and wire into local `npm test` | local validation and negative check |
| Promote prompt-id validation into CI | parked | `hub-registry` | delivery baseline | defer until private sibling checkout/access is approved | explicit access decision |

## Process Compliance

- Proof/redaction needed before public claim: no public claim.
- COI or permission review needed: no.
- Agent flight record needed: no; steward receipt is sufficient.
- Story activation index update needed: no; existing row already covers this lane.
- Research radar item needed: no.
- Eval fixture candidate: not yet; future prompt evals remain separate.
- Decision record needed: no; this follows the accepted backlog plan.
- Hosted app, global install, public proof, or autonomous agent work is gated: yes.

## Outcome

- Backlog update needed: complete.
- Roadmap update needed: complete.
- Template update needed: no.
- Repo manifest/evidence index update needed: Hub evidence index and manifest updated.
- Next steward review trigger: before first adjacent-project touch pass or before promoting cross-repo validation into CI.

## Safety Notes

Do not include secrets, private client details, raw intake, Microsoft confidential material, unredacted logs, or unsupported public proof claims.
