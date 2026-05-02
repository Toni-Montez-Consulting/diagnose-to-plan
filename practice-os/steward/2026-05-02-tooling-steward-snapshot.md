---
data_class: P0
confidential: false
permission_level: internal_only
review_status: checked
---

# Tooling Steward Snapshot

Date: 2026-05-02

Review type: infrastructure sprint snapshot

## Inventory

| Tool | Type | Auth state | Used recently? | Current owner | Notes |
|---|---|---|---|---|---|
| Gmail | communication | connected in current session | yes | Toni | useful for drafts, sends, and targeted reply checks; no auto-send |
| Google Calendar | scheduling | connected in current session | yes | Toni | internal Business Brain reset exists; no client invites until times confirmed |
| Notion | cockpit/capture | connected in current session | yes | Toni | Command Center exists; DTP remains source of truth |
| GitHub/local git | repo execution | local git active; GitHub connector candidate | yes | Toni / org repos | local git remains primary for repo-state truth |
| Browser/Playwright | QA | available by tool/skill when needed | yes | repo owner | useful for UI proof and browser validation; not needed for this docs-only slice |
| QuickBooks Online | business finance | not connected | no | Toni | blocked/manual-export-first until read-only boundary accepted |
| Canva/Figma/design tools | design/proof | available/candidate | no current proof use | Toni | research/pilot only after permissioned proof need |
| Vercel/Supabase/runtime tools | deployment/data | available by repo lane | yes in other lanes | repo owner | use only inside owning repo gates |
| Assistant runtime candidates | assistant infrastructure | not selected | no | future owner | consulting manifest is pre-code; runtime owner undecided |
| Hosted DTP | private operating app | not built | no | DTP future | parked until repeated records justify it |

## Evaluation

| Tool | Workflow value | Data fit | Source-of-truth fit | Maintenance burden | Verification | Decision |
|---|---:|---:|---:|---:|---:|---|
| Gmail | 3 | 2 | 2 | 2 | 2 | keep_active |
| Google Calendar | 2 | 3 | 2 | 2 | 2 | keep_active |
| Notion | 3 | 2 | 2 | 2 | 2 | keep_active |
| GitHub/local git | 3 | 3 | 3 | 2 | 3 | keep_active |
| Browser/Playwright | 2 | 3 | 2 | 2 | 3 | keep_active |
| QuickBooks Online | 2 | 1 | 1 | 1 | 0 | blocked |
| Canva/Figma/design tools | 1 | 2 | 2 | 2 | 1 | research |
| Vercel/Supabase/runtime tools | 2 | 2 | 2 | 2 | 2 | keep_manual |
| Assistant runtime candidates | 2 | 1 | 1 | 1 | 0 | park |
| Hosted DTP | 3 | 1 | 3 | 1 | 0 | park |

## Decisions

- Keep active: Gmail, Google Calendar, Notion, local git/GitHub, browser/Playwright.
- Keep manual: Vercel/Supabase/runtime tools by owning repo lane only.
- Research: Canva/Figma proof-design support.
- Park: hosted DTP, assistant runtime selection.
- Blocked: QuickBooks OAuth/API integration.

## Follow-Up

| Owner | Action | Due / cadence | Gate |
|---|---|---|---|
| Codex | Use this snapshot before recommending new connectors. | next tooling prompt | DTP remains source of truth |
| Toni | Approve any QuickBooks app/OAuth setup before implementation. | later | read-only boundary accepted |
| Codex | Convert consulting assistant fixtures into tests or QA checklist before runtime work. | later | runtime owner accepted |

## Notes

This is a tool-governance snapshot, not an install log. No credentials, OAuth
tokens, workspace IDs, QuickBooks realm IDs, secrets, or private data are stored
here.
