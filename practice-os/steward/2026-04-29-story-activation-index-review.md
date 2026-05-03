---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Story Activation Index Review

## Session

- Date: 2026-04-29
- Steward: Codex
- Trigger: operator asked whether agents and skills can be intuitively tied to the relevant roadmap/Kanban epic/story
- Repos touched: `diagnose-to-plan`
- Roadmap files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`, `docs/PRACTICE_PRODUCTION_ROADMAP.md`, `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`
- Activation files reviewed: `practice-os/templates/activation-routing-map.md`, `practice-os/templates/roadmap-steward-review.md`

## Activation Result

- Prompt shape: connect roadmap stories to agent/skill activation.
- Primary activation: Activation Routing Map plus Roadmap Steward review.
- Classification: `roadmap_backlog_story`, `practice_os_template`, `parked_gated_automation`.
- Gated paths not activated: autonomous agent manager, subagent spawning, global skill install, hosted DTP implementation, public proof promotion.

## Implemented

- Added `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` as the canonical story-to-skill/template/agent-role routing index.
- Added `practice-os/templates/story-activation-contract.md` for stories that need a dedicated activation record.
- Updated the Activation Routing Map to route prompts about story/agent/skill alignment to the story activation index.
- Updated the Roadmap Steward review template to record story activation, suggested skill/template, suggested agent role, and whether the story activation index needs updates.
- Made the story activation contract a required Practice OS template through `dtp practice doctor`.
- Updated roadmap/documentation pointers so the backlog, production roadmap, workspace roadmap, and documentation map all explain the layer.

## Decision

The practice now has two activation levels:

- Prompt activation: what should happen based on what Toni asks.
- Story activation: what should happen based on which Kanban epic/story is active.

This is deliberately not autonomy. Suggested agents are routing hints. They do not authorize agent spawning, repo mutation, public proof, hosted implementation, or global installs.

## Current Operating Rule

Before advancing a major roadmap story, the steward should check:

1. `practice-os/templates/activation-routing-map.md`
2. `docs/ROADMAP_STORY_ACTIVATION_INDEX.md`
3. `practice-os/templates/roadmap-steward-review.md`

If the story needs special routing, create a one-off contract from:

- `practice-os/templates/story-activation-contract.md`

## Safety Notes

- No private engagement material, secrets, raw intake, Microsoft confidential material, unredacted logs, or unsupported public proof claims were added.
- The layer makes future agent use easier to choose, but does not grant autonomous authority.
