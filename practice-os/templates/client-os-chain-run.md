---
data_class: P0
confidential: false
permission_level: internal_only
review_status: template
---

# Client OS Chain Run

Use private client-specific copies in the private engagement vault to run one
meeting through preflight, capture, receipt, tasking, and bridge review.

## Chain Metadata

- Client/lane:
- Engagement:
- Meeting date:
- Automation authority: draft_only
- Chain status:

## Run Sequence

| Step | Owner | Input | Output | Gate | Status |
|---|---|---|---|---|---|
| Preflight | Agent | pilot packet + scaffolds | readiness report | no blockers | pending |
| Meeting brief | Toni | meeting-brief | live conversation | Toni review | pending |
| Notes capture | Toni/Agent | meeting | meeting notes | private only | pending |
| Receipt | Agent | notes + kit | post-meeting receipt | no unresolved owner | pending |
| Build task | Agent | receipt decisions | bounded task | Toni review | pending |
| Bridge queue | Agent | receipt + build task | dry-run actions | no live writes | pending |

## Authority Matrix

| Action | Allowed now? | Required gate |
|---|---|---|
| Update private kit files | yes | Toni review before relying on claims |
| Draft follow-up after meeting | yes | actual meeting facts first |
| Send email | no | explicit Toni approval |
| Calendar changes | no | explicit Toni approval |
| Hub/Notion mirror | dry-run only | sanitized payload + reviewer |
| Public proof/copy | no | permission, redaction, reviewer, evidence, caveat |

## Evidence Receipt

| Evidence | Location | Captured? | Notes |
|---|---|---|---|
| Preflight output | console | pending |  |
| Meeting notes | meeting-notes file | pending |  |
| Receipt | post-meeting receipt | pending |  |
| Bridge export | dry-run output | pending | no external writes |

## Stop Conditions

- Permission is unclear but public proof is requested.
- A row would expose private records, credentials, or raw client data.
- A proposed action would send, schedule, publish, or mutate externally.
- Scope expands beyond the accepted engagement without Toni review.
