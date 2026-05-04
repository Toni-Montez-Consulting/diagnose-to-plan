---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Contextual Idea Intake

Use this when Toni submits a new idea, design, business move, development
enhancement, project request, product direction, process improvement, or "what if"
that should not depend on memory.

The goal is progressive activation: capture the idea, classify it, attach it to the
right repo/roadmap lane, activate the right skill/template/gate, and decide the
next artifact. Do not turn every idea into implementation immediately.

Default quick capture:

```powershell
.\.venv\Scripts\python.exe -m dtp kaizen capture "..."
```

Use this full template only when the Kaizen record needs deeper classification,
promotion, or steward review.

## Raw Idea

- Date:
- Submitted by:
- Original prompt or design:
- Source file/link/image:
- Urgency:

## Idea Type

Choose the primary type and any secondary types.

- [ ] development enhancement
- [ ] development implementation
- [ ] product/design
- [ ] project/client work
- [ ] business/offer/pricing
- [ ] proof/case study
- [ ] research/tooling
- [ ] process/infrastructure
- [ ] agent/skill/automation
- [ ] COI/privacy/security
- [ ] parked/future

## Context Classification

| Question | Answer |
|---|---|
| Which repo owns this? |  |
| Which roadmap epic/story does it map to? |  |
| Is this new, existing, or replacing something? |  |
| Is it public, private, internal, or client-facing? |  |
| Is there sensitive data, COI, proof, or permission risk? |  |
| Does this need research before execution? |  |
| Does this need user confirmation before execution? |  |

## Activation Routing

Use `practice-os/templates/activation-routing-map.md` and
`docs/ROADMAP_STORY_ACTIVATION_INDEX.md`.

| Activation target | Selected asset | Why | Gate |
|---|---|---|---|
| Skill |  |  |  |
| Template |  |  |  |
| Roadmap story |  |  |  |
| Repo lane |  |  |  |
| Suggested agent role | local-codex |  | explicit delegation required for subagents |

## Progressive Next Step

Choose the smallest useful next artifact.

- [ ] answer in chat only
- [ ] roadmap/backlog story
- [ ] work item spec
- [ ] decision record
- [ ] proof/redaction item
- [ ] research radar item
- [ ] research spike
- [ ] eval/lesson candidate
- [ ] repo manifest/evidence index update
- [ ] implementation plan
- [ ] direct implementation
- [ ] parked item

## Gates Before Implementation

- Local gates:
- CI/manual gates:
- Proof/redaction gates:
- COI/privacy/security gates:
- User approval needed:
- No-touch boundaries:

## Steward Outcome

- Kaizen record ID:
- Captured as:
- Owning repo:
- Owning roadmap story:
- Activated skill/template:
- Suggested agent role:
- Next action:
- Follow-up record:
