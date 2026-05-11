---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Intelligence Control Plane

Status: V0 operating layer for reducing mental load before adding hosted memory,
private retrieval, assistant runtime, or connector automation.

Owner repo: `diagnose-to-plan`

## Purpose

This is the "do the right thing first" layer for Toni's consulting practice.
It ties together rehydration, input routing, client waiting states, Notion
cockpit use, tool stewardship, public-assistant gates, and memory promotion.

It does not replace the existing DTP architecture. It sits on top of:

- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`
- `docs/CLIENT_OS_PILOT_WAVE_2026-05.md`
- `docs/PRACTICE_MEMORY_CONTROL_PLANE.md`
- `docs/PRACTICE_MEMORY_OPTIMIZATION_PLAN.md`
- `docs/KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md`
- `docs/AUTONOMY_READINESS_LADDER_V0.md`
- `docs/PRACTICE_OPERATING_REVIEW_LOOP_V0.md`
- `docs/PRACTICE_TOOLING_STEWARD.md`
- `docs/CLIENT_REPLY_INTAKE_OPERATING_PATTERN.md`
- `docs/RECURRING_CLIENT_CADENCE_OPERATING_PATTERN.md`
- `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md`
- `docs/NOTION_MIRROR_V0.md`

## Core Contract

Every broad work block should answer six questions before implementation:

1. What source is authoritative?
2. What changed since the last steward receipt?
3. Who is waiting on whom?
4. Which gate blocks action?
5. Which artifact should own the new input?
6. What can be mirrored safely to Notion?

DTP remains authoritative. Notion remains the cockpit. Gmail, Calendar,
QuickBooks, GitHub, browser tools, and project repos are input or execution
surfaces. They are not the practice memory by themselves.

## Start-Of-Work Rehydration

Use this sequence when a prompt spans multiple clients, repos, connectors, or
infrastructure layers.

| Step | Source | Purpose | Allowed action |
|---|---|---|---|
| 1 | `git status --short --branch` | confirm repo dirt and branch | read-only |
| 2 | `dtp workspace report` | see recorded repo lanes, blockers, and evidence | read-only |
| 3 | active kit status | see Cam, Greg, and CCAAP gates | read-only |
| 4 | recent steward receipts | avoid rediscovering prior decisions | read-only |
| 5 | Gmail targeted thread search | confirm replies before changing waiting state | read-only unless Toni asks to draft/send |
| 6 | Calendar targeted search | confirm internal holds and client invites | read-only unless time is confirmed |
| 7 | Notion Command Center | inspect cockpit visibility | mirror only after DTP update |
| 8 | owning docs/templates | select the right artifact before editing | update only the scoped layer |

Use `practice-os/templates/session-rehydration-checklist.md` when the session is
large enough that a future agent should see the exact sources checked.

## Input Router

Route new material to the lightest durable artifact that preserves momentum and
protects the right gate.

| Input | Primary destination | Mirror | Gate |
|---|---|---|---|
| Client reply | private kit reply intake | sanitized client snapshot | no calendar/build/proof changes until extracted |
| Prospect intake | prospect-intake triage plus selected Practice OS artifact and draft-only follow-up template when needed | sanitized next-action/status only | no client communication, proof, production write, or integration expansion before approval |
| Meeting notes | private kit meeting notes plus extraction | sanitized meeting status | mark AI notes unverified until checked |
| Rough idea | Thought Inbox or Input Studio | Idea Inbox summary | no implementation until classified |
| Client/source artifact | private kit source-material index | waiting/action summary only | classify sensitivity before use |
| Proof candidate | proof packet and redaction queue | proof gate status | permission, redaction, reviewer, evidence, caveat |
| Tool/plugin idea | Tooling Steward review | tool status summary | no OAuth/write access before accepted boundary |
| Finance/admin idea | connector map or QuickBooks boundary | financials unavailable/blocked summary | manual export first, read-only later |
| Site assistant idea | assistant manifest/source corpus/refusal fixtures | assistant lane status | no widget/runtime before launch gate |
| Durable memory candidate | memory review queue | none or sanitized status | human approval before pattern/playbook memory |
| Knowledge-base maintenance event | `docs/KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md` plus owning source doc/template | sanitized changed/parked status | human-gated; no autonomous promotion or public/client action |
| Autonomy candidate | `docs/AUTONOMY_READINESS_LADDER_V0.md` plus `practice-os/templates/autonomy-readiness-review.md` | readiness level/status only | no scheduled, write-enabled, live, or external action until readiness review is accepted |
| Broad status/review request | `docs/PRACTICE_OPERATING_REVIEW_LOOP_V0.md` plus `practice-os/templates/practice-operating-review.md` | sanitized next-action/status only | review can recommend action but does not bypass proof/client/tool/runtime/autonomy gates |
| Repo implementation | owning repo plan/spec | repo-health summary | repo-local gates and no-touch boundaries |

If an input can fit more than one row, choose the row with the highest risk
gate first: privacy, COI, money movement, public proof, live data, client
communication, repo access, or irreversible action.

## Notion Cockpit Fields

Every active client or operating lane should be readable through these fields:

- `next_meeting`
- `waiting_on`
- `next_action`
- `blocked_by`
- `last_updated`

Notion must not hold raw transcripts, private terms, confidential notes, client
data, payment/member records, private contact details, credentials, proof
claims, or source artifacts. If Notion and DTP disagree, DTP wins until a
steward review updates DTP.

## Current Live Lanes

| Lane | Current operating state | Next safe move |
|---|---|---|
| Greg / TheGrantApp.io | First Client OS pilot; discovery cadence accepted, permission/proof boundaries still gated. | Run the 2026-05-08 pilot packet and update private kit first. |
| CCAAP | Second Client OS pilot; owner-approved launch/proof inputs still gate public movement. | Run the 2026-05-12 prototype-review packet and capture owner decisions before site/proof changes. |
| Cam / SMB marketplace | Third Client OS pilot after active cadence and item-packet state are confirmed. | Confirm meeting/item-packet state before build, proof, or schedule changes. |
| Toni / Business Brain | Weekly internal reset is the anchor habit. | Use reset to close stale waiting states and pick three actions. |
| Consulting public assistant | Manifest and repo-local pre-code corpus/refusal fixtures exist. | Convert fixtures into tests or QA checklist before runtime work. |
| QuickBooks | Not connected; read-only candidate only. | Use manual export or mark financials unavailable. |

## Tooling Boundary

The control plane can notice tools, score tools, and recommend tools. It does
not authorize connecting or expanding tools by itself.

Use `docs/PRACTICE_TOOLING_STEWARD.md` and
`practice-os/templates/tooling-steward-review.md` before:

- adding OAuth scopes;
- granting write access;
- installing new automation;
- creating a connector;
- trusting a tool as source of truth;
- storing credentials;
- moving from manual export to live import.

## Assistant Boundary

The site assistant idea is valid, but V0 is pre-code until the accepted
manifest is backed by:

- approved public source corpus;
- blocked source list;
- refusal and handoff fixtures;
- logging and analytics policy;
- runtime owner;
- rate limit and environment plan;
- route/widget smoke tests;
- launch review.

The consulting site remains the first pilot. CCAAP assistant work stays parked
until launch inputs, owner review, contact routing, DNS, assets, and
proof/privacy decisions are stable.

## Memory Promotion

Use the Practice OS memory levels:

1. Raw capture
2. Working memory
3. Decision memory
4. Pattern memory
5. Playbook memory

Nothing becomes durable reusable playbook memory because it appeared in chat,
Notion, Gmail, or one session. Promotion requires human approval and a source
pointer.

## End-Of-Work Closeout

Before finishing a meaningful work block:

1. Update DTP source-of-truth artifacts.
2. Mirror sanitized Notion status only if status changed.
3. Record a steward receipt.
4. Update the roadmap/backlog when priority or story state changed.
5. Run the appropriate DTP checks.
6. Commit tracked DTP infrastructure when it is meant to be durable.

For broad "where are we?" or "what is next?" reviews, use
`docs/PRACTICE_OPERATING_REVIEW_LOOP_V0.md` before creating new work.

## Non-Goals

- No hosted DTP implementation.
- No vector database.
- No private Business Brain assistant.
- No two-way Notion sync.
- No QuickBooks OAuth.
- No public assistant widget or runtime.
- No client portal.
- No autonomous runtime or agent authority without an accepted autonomy
  readiness review.
- No unmanaged self-learning.
- No auto-send or auto-schedule behavior.
