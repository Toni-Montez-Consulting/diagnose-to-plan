---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Review: Repo Manifest Expansion

## Session

- Date: 2026-04-30
- Steward: Codex
- Trigger: after Mom pilot/proof governance and `tm-skills` Codex discovery smoke, expand the Workspace Efficiency pilot to the core touched lanes
- Repos reviewed: `diagnose-to-plan`, `consulting`, `hub`, `tm-skills`
- Roadmap files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`, `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`, `docs/DOCUMENTATION_MAP.md`
- Backlog files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`
- Story activation files reviewed: `practice-os/templates/activation-routing-map.md`, `docs/ROADMAP_STORY_ACTIVATION_INDEX.md`
- Contextual intake files reviewed: not needed; this continued an existing queued workspace-efficiency story

## Source Of Truth Check

- DTP remains the practice roadmap source of truth: yes
- `docs/ROADMAP_EXECUTION_BACKLOG.md` reflects current story status: update needed for repo manifest expansion
- Repo manifests/evidence indexes were checked where available: yes, DTP pilot accepted and extended to consulting, Hub, and `tm-skills`
- No sibling repo is being treated as the practice-wide roadmap owner: yes

## Workspace Coverage

- `consulting`: public storefront/proof lane now has a DTP-owned manifest and evidence index.
- `diagnose-to-plan`: Practice OS source of truth; existing pilot manifest/index kept current.
- `hub`: runtime/intake lane now has a DTP-owned manifest and evidence index.
- `engineering-playbook`: remains future touch pass; doctrine/check scripts lane unchanged.
- `hub-prompts`: remains future prompt eval/cross-validation lane.
- `hub-registry`: remains future registry validation/cross-validation lane.
- `fitness-app`: remains Omnexus reference verification cockpit and future touch pass.
- `FamilyTrips`: remains privacy-first validation/build/test lane.
- `demario-pickleball-1`: remains command-room/reference and launch-gate lane.
- `dse-content`: remains Microsoft/COI-aware internal proof lane.
- `tm-skills`: global SDLC skills lane now has a DTP-owned manifest and evidence index.

## Active Next Queue

- Current next story: Workspace Efficiency repo manifest expansion
- Owning repo: `diagnose-to-plan`
- Status: implemented for core touched lanes
- Done gate: DTP contains manifests/evidence indexes for DTP, consulting, Hub, and `tm-skills` without mutating unrelated adjacent repos
- Story activation: Workspace Efficiency Layer and Roadmap Steward
- Suggested skill/template: `practice-os/templates/repo-manifest.md`, `practice-os/templates/evidence-index.md`, `tm-skills/delivery-baseline`
- Suggested agent role: documentation/steward agent with read-only repo inspection
- Local gates: DTP validation and targeted redaction checks
- CI or manual gates: DTP CI after push
- Blockers: adjacent repo manifests should wait for real touch passes
- What must not be touched yet: Omnexus active branch work, client/private data, hosted DTP implementation, public proof publication

## Idea Capture

| Idea | Classification | Owning repo | Activation | Action | Gate |
|---|---|---|---|---|---|
| Keep repo context durable so agents do not rediscover purpose/gates every session | story | `diagnose-to-plan` | Workspace Efficiency Layer | add core manifests/evidence indexes | DTP validation and redaction checks |
| Expand manifests to adjacent projects eventually | repo touch pass | selected project repo plus DTP | Roadmap Steward | add only when lane is active | avoid noisy bulk edits |

## Process Compliance

- Proof/redaction needed before public claim: yes, for consulting proof and Mom/Omnexus/DeMario proof promotion.
- COI or permission review needed: yes, for DSE/Microsoft-adjacent material and client proof.
- Agent flight record needed: no; steward receipt is sufficient for this docs-only pass.
- Story activation index update needed: no; existing Workspace Efficiency lane covers this.
- Research radar item needed: no new research method adopted.
- Eval fixture candidate: no.
- Decision record needed: no; this follows the accepted Workspace Efficiency plan.
- Hosted app, global install, public proof, or autonomous agent work is gated: yes.

## Outcome

- Backlog update needed: mark core manifest expansion complete and keep adjacent expansion future.
- Roadmap update needed: update Workspace Efficiency status.
- Template update needed: no.
- Repo manifest/evidence index update needed: complete for consulting, Hub, and `tm-skills`.
- Next steward review trigger: before Hub prompt/registry cross-validation or the first adjacent-project touch pass.

## Safety Notes

Do not include secrets, private client details, raw intake, Microsoft confidential material, unredacted logs, or unsupported public proof claims.
