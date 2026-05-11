---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Live Intake Operator Workflow Receipt

Date: 2026-05-11

Owner repo: `diagnose-to-plan`

Related runtime: `hub`

Related public surface: `consulting`

## Trigger

After the live consulting-to-Hub intake path was deployed and smoke-tested, the
next useful slice was to operationalize what happens after a submission lands.

The implementation keeps DTP as the source of truth, Hub as runtime support,
and consulting as the public storefront.

## Sources Checked

| Source | Why it mattered |
|---|---|
| `AGENTS.md` and `CLAUDE.md` | confirmed DTP source-of-truth, question checkpoint, and small additive slice rules |
| `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` | preserved human-led squad, source-index, business-justification, approval-gate, and handoff model |
| `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md` | confirmed broad input routing and DTP-first operating state |
| `docs/PRACTICE_SYSTEM_ARCHITECTURE.md` | confirmed consulting/Hub/DTP intake boundaries |
| `practice-os/templates/live-intake-receipt.md` | confirmed existing live-smoke receipt boundary |
| `dtp kaizen status --limit 5` | confirmed no active `now` or `next` Kaizen items |
| `dtp workspace report` | confirmed repo roles and open manual gates |

## Decisions

| Decision | Reason | Revisit trigger |
|---|---|---|
| Add a DTP-owned live-intake operating pattern | Runtime was proven, but the post-intake operator workflow was not explicit enough | Three real prospect intakes use the flow or Hub review becomes bottleneck |
| Add a Prospect Intake Triage template | Future agents need a repeatable way to summarize intake, choose a route, and preserve gates | Template feels too heavy/light after real use |
| Do not touch Hub runtime in this slice | Hub already stores runtime records; expanding it risks CRM/DTP drift before manual workflow proves pain | Manual triage reveals repeated Hub-console bottleneck |
| Do not touch consulting public copy | This is an internal operating workflow, not a new public offer-copy decision | Toni opens a public copy pass using DTP offer/proof sources |

## Work Performed

- Added `docs/LIVE_INTAKE_TO_PRACTICE_OS_WORKFLOW_V0.md`.
- Added `practice-os/templates/prospect-intake-triage.md`.
- Updated `docs/DOCUMENTATION_MAP.md`.
- Updated `docs/ROADMAP_EXECUTION_BACKLOG.md`.
- Updated `docs/PRACTICE_PRODUCTION_ROADMAP.md`.
- Updated `docs/PRACTICE_SYSTEM_ARCHITECTURE.md`.
- Updated `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md`.
- Updated `docs/integration/reprioritization_log.md`.

## Business Value Preserved

- Intake now leads to a decision instead of only a stored row.
- The workflow separates Diagnostic Call (`fit-call` internally), paid Blueprint, Fast Track, Custom SOW,
  advisory, parked, and bad-fit paths.
- Follow-up remains human-reviewed.
- Hub remains runtime support instead of becoming a CRM.
- DTP remains the place where method, proof, memory, and approvals live.

## Approval Gates

| Gate | State | Notes |
|---|---|---|
| Client communication | pending | no email or reply is sent by this workflow |
| Public proof | blocked | proof still requires proof promotion runbook |
| Production write | not_required | docs/templates only |
| Repo mutation | approved_by_prompt | Toni asked to keep moving; DTP is the owning repo |
| Hosted DTP / Notion / Gmail expansion | blocked | future integration requires separate approval and boundary review |

## Verification

| Check | Result |
|---|---|
| `dtp kaizen status --limit 5` | pass, no active `now` or `next` items |
| `dtp workspace report` | pass, read-only report generated |
| Local docs validation | pending at receipt creation; run before merge |

## Next Action

Use `practice-os/templates/prospect-intake-triage.md` on the next real prospect
intake. If the same route appears repeatedly, consider a reviewed offer-pattern
or memory candidate. If manual triage becomes repetitive, then scope a Hub or
hosted-DTP enhancement from evidence instead of guessing.

## Open Questions

None block this slice.

Useful next checkpoint questions:

1. Should the first real intake triage produce a paid Blueprint artifact by
   default, or only after a Diagnostic Call confirmation?
2. Should Hub eventually show a "DTP triage status" field, or should that stay
   manual until several real intakes prove the need?
3. Which route should get first-class treatment next: Diagnostic Call follow-up,
   Blueprint outline, or decline/park response?
