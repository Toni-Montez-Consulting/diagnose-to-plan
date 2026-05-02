---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# ADR Location

DTP uses `decisions/` as its ADR-lite decision-record directory.

Do not duplicate decision records here. When an instruction asks for ADRs under
`docs/adr`, create the decision record in `decisions/` unless a future accepted
repo-structure decision moves ADRs.

Current Practice OS source-material decision:

- `decisions/0007-practice-os-source-material-integration.md`
