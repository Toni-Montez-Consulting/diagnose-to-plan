---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Client Command Room Fit Assessment

Use this before proposing or building a Client Command Room. The default answer is not
"build a portal"; the default answer is "choose the smallest operating surface that helps
the owner run the workflow after delivery."

## Project

- Client/project:
- Engagement:
- Date:
- Assessor:
- Source kit:
- Related pattern:
  - `docs/CLIENT_COMMAND_ROOM_PATTERN.md`

## Workflow Pain

| Workflow | Current home | Frequency | Owner pain | Business risk | Evidence |
|---|---|---:|---|---|---|
| | texts / email / sheet / app / memory | daily / weekly / monthly | | | |

## Recurring Operating Decisions

List only decisions the owner will keep making after launch.

| Decision | Who decides | Inputs needed | Output | Deadline or cadence |
|---|---|---|---|---|
| | | | | |

## Existing Tool Check

If one of these already solves the problem, do not build a Command Room yet.

| Existing tool | Already used? | Gap | Keep / replace / augment |
|---|---|---|---|
| Notion/Airtable/Sheets | | | |
| Existing CRM/admin | | | |
| Email or form inbox | | | |
| Calendar/scheduler | | | |
| Payment processor dashboard | | | |

## Decision

Choose one.

- [ ] **Build a Client Command Room**
  - There is recurring operational work.
  - The owner needs one protected place to act.
  - Existing tools are scattered, risky, or too hard to use.
  - The room can be tied to real workflow state.

- [ ] **Create a handoff checklist instead**
  - The client needs clear instructions, not live state.
  - The workflow is mostly one-time launch/setup work.
  - A static runbook, roadmap, or checklist will reduce confusion enough.

- [ ] **No private surface**
  - The project is a simple marketing site, one-time audit, or public-only asset.
  - There is no recurring owner action worth productizing.

- [ ] **Defer**
  - The pain is plausible but not proven.
  - Capture the workflow in the Client Operating Kit and revisit after launch.

## When Not To Build

Do not build a Command Room when:

- the client only needs a static handoff document;
- the workflow already works in an existing tool;
- the room would mostly show vanity metrics;
- the room would mix public proof with private records;
- the owner would be forced to manage developer tasks;
- support or verification panels would be manually maintained;
- the database exists only to make the UI look alive.

## Owner / Developer Boundary

Owner-facing surfaces may include:

- live operating state;
- owner tasks;
- business roadmap;
- handoff rules;
- safe support status written in owner language.

Developer/system surfaces may include:

- implementation roadmap;
- release gates;
- env/config notes;
- verification evidence;
- deferred technical work.

Keep these separate. The client should not have to reason about code, infra, secrets, or
developer backlog to run the business.

## Support And Verification Readiness

Support/verification panels are placeholders until they connect to real evidence artifacts.

| Evidence source | Exists? | Artifact path or command | Hard / advisory / manual |
|---|---|---|---|
| Build/deploy status | | | |
| Intake/form health | | | |
| Auth/owner access | | | |
| Payment or booking system | | | |
| Redaction/permission status | | | |

## Proof Potential

If this becomes public proof later, define the receipt shape now.

- Baseline:
- After-state:
- Useful screenshot or walkthrough:
- Metric:
- Caveat:
- Permission level:
- Redaction reviewer:

## Recommendation

- Recommended path:
- Why:
- Smallest useful first version:
- What stays manual on purpose:
- Next review date:
