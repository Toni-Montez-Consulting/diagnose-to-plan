---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Tooling Steward

Status: operating pattern for connector, plugin, MCP, and local-tool review.

Owner repo: `diagnose-to-plan`

## Purpose

The Tooling Steward keeps Toni's tool stack useful instead of noisy. It reviews
the tools, plugins, connectors, CLIs, MCP servers, and future integrations that
Codex or the practice can use, then decides what should stay active, be parked,
be researched, be added, or be removed.

This is not an autonomous tool installer. It is a human-gated manager pattern.

## Why This Exists

The practice is starting to accumulate useful capabilities:

- Gmail for client replies and drafts.
- Notion for cockpit and idea capture.
- Google Calendar for internal resets and confirmed meetings.
- GitHub/local git for repo execution.
- Canva or design tools for future visual/proof assets.
- QuickBooks as a possible future finance source.
- Vercel, Supabase, Playwright, browser tools, and other dev/runtime tools for
  project delivery.

Without a steward loop, the stack can drift into one of two bad states:

- too many tools connected, with unclear data boundaries and too much noise;
- useful tools missing because nobody periodically asks what the workflow needs.

## Source Of Truth

- DTP owns tooling decisions, review receipts, connector boundaries, and parked
  tool stories.
- Notion may show a sanitized tool-status cockpit.
- Tool vendor dashboards own account/auth state.
- Secrets, tokens, app credentials, OAuth refresh tokens, API keys, realm IDs,
  and production credentials must stay outside tracked git.

## Tool Classes

| Class | Examples | Steward question |
|---|---|---|
| Communication | Gmail, Calendar | Does this reduce client follow-up friction without causing auto-send risk? |
| Cockpit / capture | Notion | Does this reduce mental load without becoming source of truth? |
| Repo execution | GitHub, local git, CI, Vercel | Does this make delivery state clearer and safer? |
| Browser / QA | Playwright, browser tools | Does this improve visible proof and regression confidence? |
| Business finance | QuickBooks | Can this be read-only and summary-first without exposing sensitive financials? |
| Design/proof | Canva, image tools, Figma | Does this produce permissioned, evidence-backed artifacts rather than generic assets? |
| CMS / owner editing | Sanity, Payload, Directus, Strapi, Tina, Decap, Builder.io, Contentful, Hygraph, Webflow, Framer, Notion | Does this solve a real public-content editing workflow without moving private data, launch config, proof gates, or app state into the wrong source of truth? |
| Data/runtime | Supabase, Hub, hosted DTP | Does this support real workflows without duplicating source-of-truth state? |
| Research / docs | web search, Context7, official docs | Does this improve current technical decisions with primary/current sources? |
| Agent infrastructure | MCP, skills, subagents, FAOS later | Is there enough repeated pain and eval coverage to justify more agency? |

## Evaluation Scorecard

Score each candidate or connected tool from 0 to 3.

| Criterion | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Workflow value | unused | occasional convenience | clear recurring use | critical to current loop |
| Data sensitivity fit | unclear/high-risk | sensitive with weak boundary | sensitive with clear boundary | low-risk or tightly scoped |
| Source-of-truth fit | duplicates truth | could confuse status | mirror/input only | cleanly reinforces DTP |
| Maintenance burden | heavy/unknown | moderate | low | almost none |
| Verification | untested | manually tested once | repeatable smoke | gated by runbook/evals |
| Replacement risk | many options | replaceable | preferred | best-known fit |

## Steward Decisions

Use one of these decisions:

- `keep_active`: tool is useful and bounded.
- `keep_manual`: useful, but do not automate yet.
- `research`: promising, but needs current docs/security/cost review.
- `pilot`: bounded trial with success criteria.
- `park`: not now; revisit trigger required.
- `remove_or_revoke`: too noisy, risky, duplicate, or unused.
- `blocked`: cannot proceed until auth, security, cost, COI, or source-of-truth
  rules are accepted.

## Current Known Tool Posture

| Tool / surface | Current posture | Steward decision |
|---|---|---|
| Gmail | Useful for drafts, sends, and reply intake when explicitly requested | `keep_active` with no auto-send |
| Notion | Useful phone cockpit and idea inbox | `keep_active` as mirror only |
| Google Calendar | Useful for internal reset and confirmed meetings | `keep_active` with no client invite until confirmed |
| GitHub/local git | Core repo execution surface | `keep_active` |
| Canva/design tools | Potential visual/proof support | `research` before proof use |
| Sanity / CMS-editor tooling | Useful for CCAAP updates/photos and possible future public-content workflows | `park` broadly; use `docs/CMS_EDITOR_TOOLING_DECISION_LADDER.md` before any new implementation |
| QuickBooks | Future financial input | `blocked` until read-only connector boundary is accepted |
| Hosted DTP | Future private operating app | `park` until real records justify implementation |
| FAOS/agent substrate | Future orchestration candidate | `park` until readiness review/evals exist |

## Monthly Tooling Steward Loop

Run monthly, or sooner when Toni asks about a new connector/tool.

1. List connected/authenticated tools.
2. List tools used in the last month.
3. List tools that caused friction, confusion, security concern, or duplicate
   state.
4. List missing tools that would reduce current friction.
5. Score active and candidate tools.
6. Decide: keep, manual, research, pilot, park, remove, or block.
7. Update `practice-os/templates/connector-map.md`.
8. Update roadmap/backlog if a tool needs real implementation.
9. Mirror only sanitized tool status into Notion if useful.
10. Leave a steward receipt for any meaningful change.

## Hard Rules

- Do not install, connect, or authorize a new tool just because it sounds useful.
- Do not store credentials, OAuth secrets, tokens, or private account IDs in
  tracked docs.
- Do not grant write-enabled access before a read-only pilot proves value.
- Do not let tool availability decide the operating model. DTP still owns the
  source-of-truth rules.
- Do not keep unused high-permission tools connected without a reason.

## Next Useful Slice

Create the first monthly tooling review after two Business Brain reset cycles.
That review should compare actual tool usage against the current active client
loop before adding QuickBooks, hosted DTP, two-way Notion sync, or broader agent
automation.
