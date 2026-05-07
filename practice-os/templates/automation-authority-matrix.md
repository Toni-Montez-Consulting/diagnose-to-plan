---
data_class: P0
confidential: false
permission_level: internal_only
review_status: template
---

# Automation Authority Matrix

Use this before adding or expanding automation in DTP, Hub, consulting,
`tm-skills`, project repos, Notion, Gmail, Calendar, GitHub, or external tools.

## Scope

- automation_name:
- owning_repo_or_tool:
- workflow_supported:
- default_authority: draft_only
- reviewer:

## Authority Levels

| Level | Meaning | Examples | First-wave status |
|---|---|---|---|
| draft | prepare text, packets, checklists, notes, proposed actions | briefs, email drafts, PR notes | allowed |
| read | inspect approved sources and summarize with citations | docs, calendar availability, public repo status | allowed only when source is approved |
| record | write internal records in the owning source of truth | DTP receipts, private kit updates | review required unless already scoped |
| propose_action | create a suggested external action for human approval | calendar draft, GitHub issue draft | allowed as draft only |
| act | execute an external or irreversible action | send email, publish, deploy, mutate data | blocked without explicit approval |

## Action Matrix

| Action | Authority level | Allowed source | Output destination | Approval required | Stop condition |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Privacy And Proof Rules

- public proof requires evidence, permission, redaction, reviewer, and caveat;
- private records stay in the private vault or hosted DTP;
- Notion is cockpit/mirror only;
- Hub runtime rows do not become DTP source truth;
- tool access does not grant action authority.

## Verification

- dry run:
- local gate:
- external smoke:
- audit/receipt:

