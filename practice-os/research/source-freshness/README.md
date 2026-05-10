---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Source Freshness Reviews

This folder stores reviewed source-freshness items that should survive in DTP.

Raw dry-run output belongs under ignored `outputs/research-source-freshness/`.
Only promote sanitized, reviewed items here.

Use `practice-os/templates/research-source-freshness-item.md`.

## Rules

- DTP remains the source of truth.
- Do not store raw private client material here.
- Do not store secrets, credentials, Microsoft confidential context, or raw
  Gmail content here.
- Do not treat source changes as public claims.
- Do not create client communications, Notion sync, repo changes, tool installs,
  or autonomous actions from this folder alone.

## First Source Subset

The first dry-run source subset is defined in
`docs/RESEARCH_SOURCE_FRESHNESS_DRY_RUN_V0.md`.
