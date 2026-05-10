---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Evolution System V0 Receipt - 2026-05-10

## Trigger

Toni asked to stop letting valuable ideas, meta-patterns, collaboration
strategies, research observations, and messaging language get captured
lightly and then forgotten.

The immediate source signals were:

- the meta-pattern / idea-evolution thread;
- the founder-email messaging note;
- the Research Arm pattern-extraction note;
- the already accepted DTP posture that durable practice memory belongs in DTP,
  with Notion as a mirror and consulting as the public storefront.

## Decision

Create Practice Evolution System V0 as an internal DTP-owned operating spine.

The first slice is:

- evolution spine first;
- messaging and research patterns as pilot lanes;
- human-gated promotion;
- no public site, Notion live, client communication, runtime, or autonomous
  agent changes.

## Artifacts Added

- `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md`
- `practice-os/templates/idea-evolution-record.md`
- `practice-os/templates/research-pattern-candidate.md`
- `practice-os/comms/private/messaging-knowledge-base-2026-05-10.md`
- `practice-os/evolution/README.md`
- `practice-os/evolution/records/`
- `practice-os/research/pattern-candidates/`
- `src/dtp/commands/evolution.py`

## CLI Surface

- `dtp evolution new "..."` creates an idea/meta-pattern evolution draft.
- `dtp evolution new --from-kaizen RECORD_ID` turns a Kaizen capture into a
  reviewable evolution record.
- `dtp evolution new "..." --kind research-pattern` creates a research or
  field-observation pattern candidate.
- `dtp evolution status` lists generated records and state counts.

## Existing Surfaces Reused

- Kaizen remains the first intake/index surface.
- Remaining Locks Ledger remains the in-thread strategy continuity pattern.
- Memory Promotion Record remains the formal memory-promotion review template.
- Agent Squads remain review lenses, not autonomous authority.
- Research Arm remains the research-signal digest and recommendation loop.
- Opportunity OS remains separate and relationship-led.

## Boundary

Accepted:

- Capture broadly.
- Promote deliberately.
- Use the system to preserve ambition and improve future work.
- Use review lenses when they help.
- Use messaging internally before public-copy gates.
- Use research observations to create pattern candidates.

Rejected:

- autonomous self-learning;
- live Notion writes;
- public consulting site copy changes;
- client-facing changes;
- public proof movement;
- new agent runtime;
- raw private client or relationship storage in public/deploy-adjacent repos.

## Validation

Completed after implementation:

- `.\.venv\Scripts\dtp.exe practice doctor`: passed.
- `.\.venv\Scripts\dtp.exe kaizen status --limit 10`: passed; no `now`,
  `next`, or `inbox` items remain, and the three parked evolution/messaging/
  research-pattern records are closed to DTP evidence.
- `git diff --check`: passed.
- `.\.venv\Scripts\dtp.exe evolution status`: passed.
- `.\.venv\Scripts\python.exe -m pytest tests/test_evolution.py tests/test_cli.py tests/test_practice.py`:
  passed.
- `.\.venv\Scripts\python.exe -m pytest`: passed.
- `.\.venv\Scripts\python.exe -m ruff check src tests`: passed.
- Targeted routing search confirmed triggers for `Practice Evolution System`,
  `idea-evolution-record`, `research-pattern-candidate`, messaging knowledge
  base, meta-pattern, and "don't forget this" prompts.

## Next Review

After two or three real uses, review whether:

- the idea-evolution template is too heavy;
- the messaging knowledge base should become a public-copy brief;
- research-pattern candidates are producing reusable patterns;
- any Practice Steward or Memory Steward function needs a more explicit role
  spec.
