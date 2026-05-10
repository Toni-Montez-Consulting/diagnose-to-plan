---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Steward V0 Receipt - 2026-05-10

## Trigger

After Memory Steward proved useful as a read-only recommendation surface, Toni
approved Research Steward as the next active role. The goal was to keep the
Research Arm iterative and ambitious without letting research automatically
change public claims, offers, tools, repos, client communication, or runtime
behavior.

## Decision

Build Research Steward as a practical V0 layer:

- role spec first;
- read-only CLI recommendation command second;
- no Notion live mirror;
- no autonomous research agent;
- no public site copy;
- no tool adoption;
- no client deliverables.

This follows the same operating posture as Memory Steward: make the queue
visible, recommend the next move, and leave authority with Toni.

## Implemented Surface

- Role spec: `practice-os/agents/research-steward.md`
- CLI command: `dtp research steward`
- Command code: `src/dtp/commands/research.py`
- Routing update: `practice-os/templates/activation-routing-map.md`
- Command docs: `docs/02-commands.md`
- Source docs updated:
  - `docs/RESEARCH_ARM_V0.md`
  - `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md`
  - `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md`
  - `docs/DOCUMENTATION_MAP.md`

## What Research Steward Reads

- Research Arm digests in `practice-os/research/digests/`
- Research pattern candidates in `practice-os/research/pattern-candidates/`
- Research-flavored Kaizen rows from `practice-os/kaizen/intake.jsonl`

## First Live Review

Command:

```powershell
.\.venv\Scripts\dtp.exe research steward --limit 8
```

Result:

- pattern candidates needing review: 1
- Kaizen research items needing attention: 2
- research digests needing attention: 1

The surfaced queue was:

- draft Research Arm digest for AI agents, operating intelligence, and human
  authority;
- draft research-pattern candidate for status visibility preventing lightweight
  capture drift;
- parked Harvey MCP legal-work research signal;
- parked 2026 State of AI Agents report reference.

## Authority Boundary

Research Steward can recommend:

- finish a digest;
- classify a research signal;
- create a radar item;
- create a bounded research spike;
- create or review a pattern candidate;
- park, reject, or promote after review.

Research Steward cannot authorize:

- public claims;
- offer or pricing changes;
- tool installs;
- repo changes;
- client communication;
- Notion sync;
- autonomous runtime.

## Validation

Passed:

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check src tests
.\.venv\Scripts\dtp.exe practice doctor
.\.venv\Scripts\dtp.exe kaizen status --limit 10
.\.venv\Scripts\dtp.exe research steward --limit 8
git diff --check
```

`pytest` result: 127 passed, 3 skipped.

`git diff --check` emitted line-ending warnings only.

## Next Review Trigger

Run Research Steward again after:

- the next Research Arm digest;
- a new research article/report/tool signal;
- Harvey MCP becomes active for legal/compliance work;
- the AI Agents report is used in a practice, offer, or client artifact;
- a research-pattern candidate is reviewed or promoted.

## Notes

Research Steward is the second active steward role. Do not add more roles by
default. Add another role only when a repeated workflow cannot be covered by
the current first-wave role set plus Memory Steward and Research Steward.
