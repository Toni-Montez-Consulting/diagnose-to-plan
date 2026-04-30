---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Review: Notion Mirror Capture Layer

Date: 2026-04-30

## Trigger

Toni wants the operating-system documentation, roadmap, Kanban planning, and daily ideas mirrored into Notion so he can capture and review work from his phone without needing his laptop.

## Active Story

- Story: Notion Mirror V0
- Repo: `diagnose-to-plan`
- Status after this pass: planned to source-of-truth boundary
- Done in this pass: DTP-owned Notion mirror spec, reusable mirror item template, roadmap/backlog pointers, and steward-loop update.
- Not done in this pass: Notion OAuth login, Notion database creation, Notion MCP writes, or automated sync.

## Boundary Confirmed

DTP remains the source of truth for roadmap execution, private engagement kits, repo gates, proof governance, steward receipts, and hosted-DTP readiness.

Notion may become:

- mobile idea inbox
- daily cockpit
- readable roadmap/Kanban mirror
- repo-health mirror
- proof queue mirror
- research radar mirror
- meeting/action-item capture surface

Notion must not become:

- private engagement vault
- source-of-truth roadmap owner
- proof publisher
- DSE/Microsoft confidential store
- secrets store
- repo-local validation replacement

## Safety Notes

Do not mirror secrets, raw transcripts, payment records, form submissions, student/member data, private emails, unapproved photos, raw logs, Microsoft confidential material, or public proof claims without permission, redaction, reviewer, evidence, and caveat gates.

## Open Blockers

- Notion MCP is not available as an active tool in this Codex session.
- Toni still needs to connect Notion through OAuth before Codex can write pages directly.
- Initial Notion databases need to be created manually or through a future authenticated Notion MCP session.

## Follow-Up

1. Toni can add Notion MCP to Codex user config and run `codex mcp login notion`.
2. Create the V0 Notion databases from `docs/NOTION_MIRROR_V0.md`.
3. Run a Roadmap Steward review that checks the Notion Idea Inbox and promotes accepted ideas into DTP.
4. Add a future `dtp notion export --dry-run` only after the manual mirror proves useful.
