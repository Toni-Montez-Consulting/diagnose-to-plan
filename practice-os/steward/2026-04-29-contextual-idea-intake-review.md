---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Contextual Idea Intake Review

## Session

- Date: 2026-04-29
- Steward: Codex
- Trigger: operator asked for new ideas/designs/development/business/project prompts to progressively and contextually activate the right roadmap items, skills, agents, and gates
- Repos touched: `diagnose-to-plan`
- Roadmap files reviewed: `docs/ROADMAP_EXECUTION_BACKLOG.md`, `docs/ROADMAP_STORY_ACTIVATION_INDEX.md`, `docs/PRACTICE_PRODUCTION_ROADMAP.md`, `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`
- Activation files reviewed: `practice-os/templates/activation-routing-map.md`, `practice-os/templates/roadmap-steward-review.md`, `practice-os/templates/story-activation-contract.md`

## Activation Result

- Prompt shape: make new idea/design/work prompts route progressively into the right execution surface.
- Primary activation: Activation Routing Map, Story Activation Index, and Roadmap Steward.
- Classification: `contextual_idea_intake`, `roadmap_backlog_story`, `practice_os_template`.
- Gated paths not activated: autonomous agent manager, subagent spawning, global skill install, hosted DTP implementation, public proof promotion.

## Implemented

- Added `docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md` as the idea-to-roadmap routing contract.
- Added `practice-os/templates/contextual-idea-intake.md` as the reusable intake artifact for new ideas, designs, development enhancements, project work, business moves, proof candidates, research items, and automation concepts.
- Made contextual idea intake required by `dtp practice doctor`.
- Updated the Activation Routing Map so new ideas and design/development/business/project prompts route through contextual intake before implementation.
- Updated the Roadmap Steward template so idea capture includes activation, owning repo, action, and gate.
- Updated the Story Activation Index with an idea-to-story activation section.
- Updated roadmap/documentation pointers so future agents can find the playbook.

## Decision

The practice now has three progressive activation layers:

1. Prompt activation: what should activate based on Toni's wording.
2. Contextual idea intake: what the idea is, where it belongs, and what artifact should come next.
3. Story activation: what should activate based on the Kanban epic/story.

This keeps new ideas alive without letting them automatically interrupt the roadmap, mutate repos, create public proof, or spawn agents.

## Operating Rule

When Toni submits a new idea or design, the steward should decide whether it is:

- a quick answer;
- a roadmap/backlog story;
- a work item spec;
- a decision record;
- a proof/redaction item;
- a research radar item or research spike;
- an eval/lesson candidate;
- a repo manifest/evidence-index update;
- a direct implementation;
- a parked item.

## Safety Notes

- No private engagement material, secrets, raw intake, Microsoft confidential material, unredacted logs, or unsupported public proof claims were added.
- Suggested agents remain gated by explicit authorization.
