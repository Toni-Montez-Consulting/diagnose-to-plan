---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Story Activation Contract

Use this when a roadmap or Kanban story needs an explicit link to the skill,
template, agent role, gate, or steward action that should activate for it.

Activation means "load the right operating context and checks." It does not mean
autonomous agent spawning, global skill install, public proof promotion, hosted
app implementation, or repo mutation without the existing gates.

## Story

- Epic:
- Story:
- Owning repo:
- Status:
- Done gate:
- Source backlog:
- Related roadmap section:

## Prompt Triggers

| Trigger phrase or intent | Classification | Notes |
|---|---|---|
|  | roadmap_backlog_story |  |

Classifications:

- `global_sdlc_skill`
- `dtp_practice_skill`
- `practice_os_template`
- `roadmap_backlog_story`
- `proof_redaction_gate`
- `coi_privacy_gate`
- `research_eval_lesson`
- `repo_touch_pass`
- `parked_gated_automation`

## Skill / Template Activation

| Asset | Role | Required? | When to use |
|---|---|---|---|
| `practice-os/templates/activation-routing-map.md` | route prompt to process | yes | before cross-lane execution |
| `practice-os/templates/roadmap-steward-review.md` | capture status/gates/follow-ups | yes | before/after major roadmap sessions |

## Agent Routing

| Agent role | Allowed? | Use when | Gate |
|---|---|---|---|
| local Codex session | yes | implementation is scoped and repo-local | normal repo gates |
| explorer subagent | only with explicit authorization | independent codebase question would unblock work | user asks for agent/delegation |
| worker subagent | only with explicit authorization | disjoint code-change slice is safe to delegate | user asks for agent/delegation and write scope is clear |
| autonomous manager | no | not V0/V1 | evals, guardrails, hosted queue, and human approval first |

## Gates

- Local gates:
- CI gates:
- Manual gates:
- Proof/redaction gates:
- COI/privacy gates:
- No-touch boundaries:

## Steward Checks

- Does this story still belong to the named repo?
- Does the next action match the current status?
- Are required skills/templates available?
- Is any global install, hosted implementation, public proof, or autonomous agent work being requested?
- Should this session create an agent flight record, lesson, eval candidate, proof item, research radar item, or decision record?

## Outcome

- Activated assets:
- Suggested agent role:
- Work performed:
- Work parked:
- Backlog update needed:
- Next steward review trigger:
