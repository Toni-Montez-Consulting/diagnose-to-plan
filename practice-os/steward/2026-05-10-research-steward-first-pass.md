---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Steward First Pass - 2026-05-10

## Trigger

After Research Steward V0 merged, Toni approved using it against the live queue
instead of leaving it as infrastructure.

## Command

```powershell
.\.venv\Scripts\dtp.exe research steward --limit 8
```

## Live Queue Before Review

Research Steward surfaced:

- draft digest: `practice-os/research/digests/2026-05-09-ai-agent-operating-shift.md`
- draft pattern candidate:
  `practice-os/research/pattern-candidates/2026-05-10-status-visibility-prevents-lightweight-capture-drift.md`
- parked research save: 2026 State of AI Agents report
- parked research save: Harvey MCP for future legal/compliance work

## Decision

Accept the AI agents / operating intelligence digest for internal Practice OS
use.

Reason:

- it already had sources, hype filter, practice impact, classification,
  approval gate, and next action;
- its main next artifact, `docs/OPPORTUNITY_OS_V0.md`, already exists;
- it remains internal-only and does not authorize public claims, public site
  copy, offer changes, tool installs, client communication, or runtime changes.

## Steward Improvement

The first pass exposed a useful queue-noise issue: accepted digests and promoted
research patterns should not keep appearing as "needing attention" unless a new
review trigger appears.

The Research Steward command was tightened so the default recommendation queue
tracks:

- draft, reviewed, and parked digests;
- draft, reviewed, and parked research-pattern candidates;
- active or parked research-flavored Kaizen rows.

Accepted digests and promoted patterns are still source artifacts, but they do
not remain in the default attention queue.

## Result After Review

The digest is now:

- Status: `accepted`
- Next action: choose the next research item through
  `dtp research steward`
- Boundary: internal support only; no public claims or client deliverables.

## Remaining Queue

After this pass, Research Steward should continue surfacing:

- the status-visibility research pattern candidate;
- the parked AI Agents report reference;
- the parked Harvey MCP legal-work research signal.

## Next Good Research Move

The most useful next research move is probably the status-visibility pattern
candidate, because it directly improves the Practice Evolution and Opportunity
OS operating loops.

Harvey MCP should stay parked until a legal/compliance workflow or General
Counsel mode needs a bounded research spike.

The AI Agents report should stay parked until a specific claim, offer, client
education artifact, or research digest needs source review.
