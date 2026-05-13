---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Tooling Steward Review

Use this to evaluate connected tools, plugins, MCP servers, CLIs, and candidate
integrations before adding more infrastructure.

## Trigger

- Date:
- Review type: monthly / new-tool request / security concern / workflow pain
- Prompt or reason:
- Tools in scope:

## Inventory

| Tool | Type | Auth state | Used recently? | Current owner | Notes |
|---|---|---|---|---|---|
|  |  | connected / available / not_connected / unknown | yes / no / unknown |  |  |

## Evaluation

| Tool | Workflow value 0-3 | Data fit 0-3 | Source-of-truth fit 0-3 | Maintenance burden 0-3 | Verification 0-3 | Decision |
|---|---:|---:|---:|---:|---:|---|
|  |  |  |  |  |  | keep_active / keep_manual / research / pilot / park / remove_or_revoke / blocked |

## Missing Tools

| Need | Candidate tool | Why it may help | Risk | Next action |
|---|---|---|---|---|
|  |  |  |  |  |

## CMS / Editor Fit Check

Use this only when the review includes Sanity, a CMS, owner editing, public
content management, page builders, or `/admin` publishing workflows. Pair with
`docs/CMS_EDITOR_TOOLING_DECISION_LADDER.md`.

| Repo / lane | Content owner | Content types | Public/private boundary | Candidate decision | Implementation posture |
|---|---|---|---|---|---|
|  | Toni / owner / client / mixed |  |  | git_static / sanity_structured_public_content / supabase_app_data / custom_or_open_source_admin / git_backed_editor / visual_page_builder / enterprise_headless_cms / notion_mirror_only / park / blocked | planning_only / ready_after_approval / blocked |

## Remove Or Park

| Tool | Reason | Disable path | Follow-up |
|---|---|---|---|
|  |  |  |  |

## Decisions

- Keep active:
- Keep manual:
- Research:
- Pilot:
- Park:
- Remove/revoke:
- Blocked:

## Source-Of-Truth Updates

- Connector map updated:
- Roadmap/backlog updated:
- Notion mirror updated:
- Steward receipt created:
- Repo implementation needed:

## Follow-Up

| Owner | Action | Due / cadence | Gate |
|---|---|---|---|
| Toni |  |  |  |
| Codex |  |  |  |
