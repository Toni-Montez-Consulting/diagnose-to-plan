---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
---

# Owner Call To Action Extraction

Use this template when a client or owner call needs to become a clean work queue instead of disappearing into loose notes.

The system is intentionally small:

1. Ask from a prepared guide.
2. Capture a clean synthesis, not a raw transcript.
3. Extract facts, decisions, blockers, owner actions, implementation inputs, handoff changes, and proof gates.
4. Send the owner a short action packet.
5. Update the implementation only from owner-approved values.

## Safety Boundary

Do not store:

- passwords or account recovery details;
- payment, donor, member, student, patient, or customer records;
- raw form submissions;
- private inbox contents;
- unapproved photos, screenshots, quotes, or names;
- source files that belong in a private drive instead of the DTP kit.

## Source Chain

| Stage | Artifact | Purpose |
|---|---|---|
| Call prep | `[engagement]/owner-conversation-guide.md` | Decide what to ask. |
| Synthesis | `[engagement]/owner-conversation-synthesis.md` | Preserve the useful signal without raw transcript bulk. |
| Fact intake | `[engagement]/owner-facts-intake.md` | Store owner-confirmed facts and constraints. |
| Action packet | `[engagement]/owner-action-items.md` | Give the owner a short list of next actions. |
| Extraction ledger | `[engagement]/owner-call-action-extraction.md` | Map notes to facts, blockers, implementation, handoff, and proof gates. |
| Handoff | `[engagement]/handoff/checklist.md` | Keep the owner able to operate the result. |
| Proof | `[engagement]/proof/` | Govern public claims, screenshots, permission, redaction, and caveats. |

## Extraction Categories

| Category | Meaning | Destination |
|---|---|---|
| `fact` | Owner-confirmed reality that should guide the build | Facts intake |
| `decision` | A selected path or rejected path | Plan or decision log |
| `blocker` | Missing input required before launch or implementation | Action packet and plan |
| `owner_action` | Human task owned by the client/owner | Action packet |
| `implementation_change` | Repo/content/settings change after approval | Owning repo |
| `handoff_change` | Routine workflow the owner must understand | Handoff checklist |
| `proof_gate` | Permission/redaction/reviewer/evidence/caveat item | Proof folder |
| `parking_lot` | Useful later, not needed for current version | Plan or backlog |

## Note-To-Queue Table

| Raw note or synthesized point | Category | Owner-confirmed? | Action or artifact | Owner | Due / trigger |
|---|---|---|---|---|---|
|  | fact | no |  |  |  |
|  | blocker | no |  |  |  |
|  | implementation_change | no |  |  |  |

## Owner Action Packet Shape

Keep this packet short enough to text or email:

1. What I need from you.
2. What not to send.
3. Which items block launch.
4. Which items improve polish but can follow.
5. What I will do after you reply.

## Agent Routine

After each call or owner reply:

1. Read the conversation guide, synthesis, current facts intake, plan, and handoff checklist.
2. Add or update the extraction ledger for this engagement.
3. Promote only owner-confirmed stable facts into the facts intake.
4. Keep unresolved questions in the owner action packet.
5. Keep proof internal unless the proof packet has explicit permission and reviewer approval.
6. Do not mutate a live site or app with inferred private facts.
7. Record the pass in the engagement build log.

## Acceptance Criteria

- The owner can understand the action packet without knowing DTP.
- The agent can identify which inputs are P0 launch blockers.
- The implementation repo receives only approved values.
- Private records and secrets stay out of Git, Notion, public docs, and generated summaries.
- Handoff and proof surfaces are updated when the call changes ownership or permission state.
