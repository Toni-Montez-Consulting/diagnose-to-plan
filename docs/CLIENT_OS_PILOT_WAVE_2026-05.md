---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Client OS Pilot Wave - May 2026

Status: sanitized operating plan for the first Practice OS proof loop.

Private working records live in the nested `engagements` vault. This public DTP
doc is a lane map and acceptance contract only.

## Why This Comes First

The practice needs real operating loops before more platform surface. Greg,
CCAAP, and Cam cover three different jobs:

- product/discovery and proof boundaries;
- prototype review and owner-input gates;
- business-platform validation with COI and data boundaries.

Those loops are better schema inputs than abstract platform planning.

## Pilot Order

| Order | Lane | Current role | Primary date | Acceptance |
|---|---|---|---|---|
| 1 | Greg / TheGrantApp.io | first Client OS pilot | 2026-05-08 | private packet, receipt, source index, permission state, next action |
| 2 | CCAAP | second pilot with product/prototype-review emphasis | 2026-05-12 | owner-input receipt, launch/proof gates, next owner packet |
| 3 | Cam / SMB M&A platform | third pilot after cadence and item packet are confirmed | 2026-05-15 or later | confirmation receipt, item-packet intake if received, COI/data guardrails |

DeMario/Mario and Omnexus are completed reference projects for this wave. They
should inform patterns and proof gates, but they are not the next operating
pilot.

## Required Packet Shape

Each active pilot uses `practice-os/templates/client-os-pilot-packet.md` or a
private engagement-kit equivalent.

Required sections:

- source index;
- meeting intent;
- permission/privacy notes;
- draft-only automation boundary;
- post-meeting receipt checklist;
- open-loop list;
- next-action packet;
- proof/public-copy gate;
- squad handoff when Delivery or Business Justification squads are used.

## Squad Use

Use Agent Squads V0 when the session changes:

- proof posture;
- public copy;
- offer/positioning;
- client communication;
- repo implementation;
- production writes;
- a recurring operating pattern.

The Business Justification Squad answers whether the work deserves time and what
operator problem it solves. The Delivery Squad answers how the work should be
implemented, verified, and handed off.

## Post-Meeting Receipt

After each meeting:

1. Update the private engagement-kit notes first.
2. Extract decisions, blockers, owner actions, and proof gates.
3. Update sanitized DTP lane status only if the public DTP repo needs a status
   record.
4. Mirror sanitized Notion status only after DTP is updated.
5. Do not send, publish, schedule, or mutate a project repo unless Toni approves
   that specific action.

## Acceptance Checks

- No raw client notes or private records are copied into public DTP docs.
- Every next action names an owner and gate.
- Every proof candidate remains blocked until evidence, permission, redaction,
  reviewer, and caveat pass.
- Every automation output is a draft.
- Friction is recorded so Knowledge Base V1 and hosted DTP schema can improve.

