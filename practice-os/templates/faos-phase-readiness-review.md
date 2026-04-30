---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# FAOS Phase Readiness Review

Use this before any Frontier Agentic Operating System phase is implemented.

This template prevents agent-orchestration work from becoming a second operating system that bypasses DTP. It also checks whether the phase is technically current, safe, and valuable before any repo is created or mutated.

## Phase

- Phase:
- Source spec section:
- Proposed branch:
- Proposed repo:
- Requested by:
- Review date:

## Intended Capability

- What the operator should be able to do after this phase:
- Which current pain this solves:
- Which DTP roadmap item or backlog story owns it:

## Existing Equivalent

| Proposed FAOS component | Existing DTP / tm-skills / Hub / repo equivalent | Reuse, improve, replace, or defer |
|---|---|---|
|  |  |  |

## Technical Accuracy Check

| Item | Current-source verification | Result | Correction needed |
|---|---|---|---|
| CLI flags and install commands |  | pass / fail / unknown |  |
| Docker Compose/service topology |  | pass / fail / unknown |  |
| Package manager compliance (`uv`, npm, etc.) |  | pass / fail / unknown |  |
| Database/storage isolation |  | pass / fail / unknown |  |
| Tracing/telemetry path |  | pass / fail / unknown |  |
| MCP/tool surface |  | pass / fail / unknown |  |
| Hook/subagent behavior |  | pass / fail / unknown |  |
| Eval harness behavior |  | pass / fail / unknown |  |

## Boundary Check

- Repos allowed to change:
- Repos explicitly not allowed to change:
- Private/client data boundary:
- Microsoft/COI boundary:
- Hosted DTP boundary:
- Public proof boundary:
- Global skill install boundary:
- Autonomous/write-enabled automation boundary:

## Trace And Memory Safety

- What data will be traced:
- What data must be redacted before trace:
- What data must never be traced:
- Retention expectation:
- Memory scopes:
- Memory write approval:
- Memory delete/export path:

## Acceptance Criteria Rewrite

Original acceptance criteria:

- [ ] 

Corrected acceptance criteria:

- [ ] 

Manual verification:

- [ ] 

## Decisions Required Before Build

| Decision | Owner | Required before implementation? | Notes |
|---|---|---|---|
|  |  | yes / no |  |

## Value Gate

Check every value created by this phase:

- [ ] Agent routing accuracy
- [ ] Context durability
- [ ] Verification quality
- [ ] Research-to-roadmap quality
- [ ] Proof safety or evidence quality
- [ ] Cross-repo delivery speed
- [ ] Business workflow reliability
- [ ] Lower memory burden for Toni

Reject or defer if the phase mostly adds ceremony, duplicate state, sensitive trace risk, or a dashboard without a workflow.

## Recommendation

- Decision: Adopt / Pilot / Watch / Reject / Park
- Confidence: low / medium / high
- Next action:
- Backlog update needed:
- Related decision record:

