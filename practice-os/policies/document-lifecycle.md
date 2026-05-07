---
data_class: P0
confidential: false
permission_level: internal_only
review_status: current
lifecycle_status: current
last_verified: 2026-05-07
owner: diagnose-to-plan
---

# Document Lifecycle

Use this policy when a DTP doc may be current, stale, historical, or replaced
by a newer operating artifact.

The goal is to reduce drift without deleting useful reference material.

## P0 Labels

| Label | Meaning | Use |
|---|---|---|
| `current` | This doc is active operating guidance. | Use directly unless a newer owner instruction conflicts. |
| `active` | Live work in progress. | Use as the current lane state, but expect updates. |
| `needs_stale_review` | The doc may be outdated or conflicting. | Do not use as current guidance until reviewed. |
| `historical_reference` | Useful evidence, not current guidance. | Use for context, receipts, or design history. |
| `superseded` | Replaced by a newer artifact. | Use the replacement first. |

## Recommended Frontmatter

```yaml
lifecycle_status: current
last_verified: 2026-05-07
owner: diagnose-to-plan
superseded_by:
recheck_trigger:
```

## Rules

- Do not delete stale docs by default.
- Label obvious stale docs before moving or archiving them.
- Use `superseded_by` when a newer artifact owns the current state.
- Use `historical_reference` when a doc remains useful but should not drive
  current action.
- Use `needs_stale_review` when the doc cannot be trusted yet, but the correct
  replacement is not obvious.
- Keep private engagement truth in `engagements/`; public DTP docs should carry
  only sanitized status, gates, and source pointers.

## Workflow Spine Relationship

Workflow Spine records should use stable current-state filenames such as
`active-workflow-spine.md`.

Receipts stay dated. The spine record must include a receipt register that
links to the dated receipts, meeting notes, post-meeting closeouts, and source
indexes that prove the current state.
