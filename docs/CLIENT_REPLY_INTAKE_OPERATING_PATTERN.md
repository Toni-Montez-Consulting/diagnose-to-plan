---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Client Reply Intake Operating Pattern

Status: active operating pattern for turning replies and owner updates into DTP state.

Owner: `diagnose-to-plan`

Purpose: prevent live client work from living in Toni's head, Gmail, Notion, or chat memory. Every meaningful reply should update the private kit first, then mirror only sanitized status into Notion.

## When To Use

Use this pattern when any of these arrive:

- Cam, Greg, CCAAP, or another client replies to a follow-up.
- A meeting note produces a decision, blocker, action, or proof boundary.
- A casual owner conversation produces a clear fact or approved detail.
- A client sends source material, availability, permission, or constraints.
- A waiting state changes.

Do not use this pattern for raw archive dumping. The goal is extraction into operating state.

## Intake Sequence

1. Check the source.
   - Search the relevant Gmail thread or meeting source.
   - Confirm whether attachments are present.
   - Record the message id or thread id when available.

2. Classify the content.
   - `fact`
   - `decision`
   - `blocker`
   - `owner_action`
   - `toni_action`
   - `source_material`
   - `proof_gate`
   - `coi_data_ip_gate`
   - `scheduling_input`

3. Update DTP first.
   - Add a checked reply note or meeting note.
   - Update `action-extraction.md`.
   - Update `decision-log.md` only for explicit decisions.
   - Update `owner-action-items.md` for client-owned work.
   - Update `diagnose.md` for changed bottlenecks or stable facts.
   - Update `plan.md` for changed path or gates.
   - Update source, proof, handoff, COI, or data files only when relevant.

4. Mirror the sanitized cockpit fields to Notion.
   - `next_meeting`
   - `waiting_on`
   - `next_action`
   - `blocked_by`
   - `last_updated`

5. Schedule only after confirmation.
   - Create internal reminders freely.
   - Create client calendar invites only after the time, attendees, and meeting title are confirmed.

## Current Client Routing

| Engagement | Reply handling | Scheduling rule | Blocked work |
|---|---|---|---|
| Cam / SMB M&A platform | Capture safe artifacts, methodology, proof constraints, mock-data confirmation, compensation path, and Friday cadence preference. | Weekly 45-minute Friday cadence only after Cameron confirms a time. | No repo access, build work, live data, or public proof until COI/data/IP gates are clear. |
| Greg / TheGrantApp.io | Capture discovery availability, case-study permission, bug status, soft-launch preference, and approval flow. | One discovery session first; biweekly cadence only after discovery confirms value. | No public case study, screenshots, metrics, proof claims, or production promises until Greg approves. |
| CCAAP / Mom nonprofit | Capture owner-approved PayPal, membership, contact, spam, meeting, board bio, photo, DNS, and proof decisions. | Monthly formal owner check-in after Dad/Leah clarify launch inputs. | No production launch, proof, or assistant work until owner review and launch gates clear. |
| Toni / Business Brain reset | Capture stale waiting states, proof gates, reply gaps, and the next three actions. | Weekly 30-minute internal reset. | No hosted DTP, live runner, or automation until manual loops show real pain. |

## Notion Boundary

Notion is the cockpit, not the archive.

Allowed:

- sanitized current status;
- waiting-on items;
- next action;
- blocker;
- next meeting;
- DTP path pointer;
- non-secret evidence status.

Blocked:

- raw replies or transcripts;
- private terms;
- client data;
- employer/client confidential context;
- payment, member, donor, student, or form records;
- raw screenshots or attachments;
- unsupported proof claims;
- secrets, credentials, or tokens.

## Done Signal

A reply is operationally handled when:

- DTP reflects the current fact/action/blocker state;
- Notion shows only sanitized cockpit fields;
- scheduling is either completed or explicitly waiting on availability;
- proof/COI/data/IP gates are unambiguous;
- the next action is visible without rereading the email thread.
