---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - Source Pack Schema CLI Validation

Date: 2026-05-10

Status: accepted internal validation slice

## Trigger

After seven source-policy pilots, the source-pack file became important enough
to protect with a local contract before adding more role packs or building a
dashboard.

## Decision Captured

Source packs should be validated locally through the DTP CLI and enforced by
the normal Practice OS doctor check.

The validation protects shape, uniqueness, authority-boundary flags, evidence
tiers, pilot-artifact references, and required promotion-gate fields. It does
not grant authority or judge source quality.

## Artifacts Added

- `src/dtp/commands/source_packs.py`
- `docs/AGENT_SOURCE_PACK_SCHEMA_V0.md`
- `decisions/0022-source-pack-schema-cli-validation.md`
- `practice-os/steward/2026-05-10-source-pack-schema-cli-validation.md`

## Artifacts Updated

- `src/dtp/commands/practice.py`
- `src/dtp/cli.py`
- `tests/test_agent_source_packs.py`
- `tests/test_cli.py`
- `tests/test_practice.py`
- `practice-os/research/source-packs/README.md`
- `docs/02-commands.md`
- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`
- `practice-os/templates/activation-routing-map.md`

## What Worked

- The source-pack contract now has one reusable implementation instead of
  scattered ad hoc assertions.
- `dtp practice source-packs validate` gives an operator-visible check.
- `dtp practice doctor` keeps source-pack drift visible during normal DTP
  validation.
- Future dashboard/freshness work can reuse the validator instead of creating a
  second source of truth.

## Operating Rule Reinforced

Source packs inform roles. They do not authorize action.

Search can be available to every role, but promotion still depends on evidence
quality, privacy/proof boundaries, and human approval.

## Next Recommendation

Build a lightweight source-pack freshness/status dashboard before adding many
more roles, unless a concrete client or product workflow makes Product
Strategy, UX / Design, Web Experience, General Counsel, Compliance, Data
Architecture, or Controller the more urgent role pilot.

## Blocked Actions

This validation slice does not approve:

- public copy changes;
- client communication;
- Notion sync;
- scheduled research/source workflows;
- autonomous agent behavior;
- live web freshness scoring;
- repo, production, cloud, billing, legal, finance, or compliance action.
