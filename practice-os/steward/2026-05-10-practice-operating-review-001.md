---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Practice Operating Review - 2026-05-10

Date: 2026-05-10

Reviewer: Codex with Toni direction

Review type: first weekly operating review

## Ledger

- Current focus: internal Practice OS, memory, research, KB events, status
  visibility, and autonomy-readiness infrastructure.
- What changed: PRs #35-#43 created a coherent DTP spine for Practice
  Evolution, Memory Steward, Research Steward, research sources, KB event
  workflows, status-surface patterns, Autonomy Readiness, and this operating
  review loop.
- Decision needed: what should move forward now that capture/routing surfaces
  exist.
- Next best move: use this review to create the first operating receipt, then
  run a focused autonomy-readiness review for the safest internal candidates
  before building runtime behavior.

## Sources Checked

- `dtp kaizen status --limit 10`: no `now`, `next`, or inbox items; two waiting,
  two blocked, two parked.
- `dtp evolution status`: four idea records, one research pattern candidate;
  states include parked, pattern candidate, playbook memory, promoted, and
  working memory.
- `dtp memory steward --limit 10`: two evolution items need review; six Kaizen
  items need attention.
- `dtp research steward --limit 10`: two parked research items need attention
  only if an accepted research spike or roadmap story opens.
- `dtp practice doctor`: passed.
- `git status --short --branch`: DTP clean on `main...origin/main` before this
  receipt.
- Other: recent merged PR list and current DTP operating docs.

## Current State

DTP now has enough internal operating infrastructure to stop relying on chat
memory for practice evolution. The system can capture ideas, classify them,
show their status, run read-only memory and research recommendations, route KB
maintenance events, classify autonomy candidates, and now return to all of
those surfaces through a recurring review loop.

The system is still intentionally internal. It does not authorize public site
copy, client communications, Notion sync, connector expansion, runtime
automation, hosted FAOS, or autonomous actions.

## Decisions

| Item | Decision | Why | Artifact / Owner |
|---|---|---|---|
| Practice Evolution status dashboard V0 | keep visible | Used again during this review; useful, but needs one more review cycle before promotion beyond working memory. | `practice-os/evolution/records/2026-05-10-practice-evolution-status-dashboard-v0.md` |
| Multiple record evolution rehearsal pattern | keep as pattern candidate | The pattern makes sense and helped test dashboard states, but needs another system/template rehearsal before pattern-memory promotion. | `practice-os/evolution/records/2026-05-10-multiple-record-evolution-rehearsal-pattern.md` |
| Status visibility prevents lightweight capture drift | keep promoted internally | Already promoted to an internal pattern and reinforced by this review. | `practice-os/patterns/status-surface-before-scale.md` |
| 2026 State of AI Agents Report | park | Useful future research source, but no accepted research spike is open right now. | `practice-os/kaizen/intake.jsonl` |
| Harvey MCP legal workflow idea | park | Good future legal/compliance workflow candidate, but must be verified from primary sources when the General Counsel/legal lane opens. | `practice-os/kaizen/intake.jsonl` |
| CCAAP owner-input waiting item | keep waiting | Client lane should not reopen without new owner inputs. | Kaizen waiting row |
| Omnexus subscription/app-store proof item | keep waiting | Operator says subscriptions work; next action still requires App Store candidate/build evidence before release-proof changes. | Kaizen waiting row |
| Hub PR #68 Tailwind blocker | keep blocked | Needs targeted Hub-local migration/fix pass, not DTP internal OS work. | Kaizen blocked row |
| DSE sensitive triage item | keep blocked | Requires explicit COI-aware scope and live repo validation. | Kaizen blocked row |

## Next One To Three Actions

1. Create and merge this first Practice Operating Review receipt.
2. Run an Autonomy Readiness Review for the safest internal candidates:
   Research source freshness, Memory review queue, Practice/status dashboards,
   and KB drift review.
3. After the autonomy review, decide whether the next build is a read-only
   scheduled/dry-run surface, a richer status dashboard, or a client-lane return.

## Steward Recommendations

### Memory

- Promote: none today.
- Keep visible: Practice Evolution status dashboard V0.
- Park: none from the two active evolution recommendations.
- Needs Toni decision: whether multiple-record rehearsal should become a
  playbook rule after another successful use.

### Research

- Review now: none.
- Watch: AI agent operating-model research, legal/compliance MCP tooling.
- Park: 2026 State of AI Agents Report, Harvey MCP.
- Needs source verification: Harvey MCP before any legal workflow adoption;
  AI-agent report claims before any public/offer use.

## Autonomy Readiness Candidates

| Workflow | Current Level | Possible Next Level | Decision |
|---|---|---|---|
| Research source freshness | A1 | A4 | review next; likely first scheduled/dry-run candidate |
| Memory review queue | A1 | A2 | review next; keep promotion human-approved |
| Practice/status dashboards | A1 | A3/A4 | review next; internal-only and low risk |
| Knowledge-base drift review | A1 | A4 | review next; good dry-run candidate |
| External communications drafts | A2 | A3 local draft files only | not next; useful but higher business-risk because of client tone and send gates |
| Notion mirror draft updates | A2 | A5 later | not next; useful later after DTP source remains dominant |

## Approval Gates

- Public proof: blocked unless proof/redaction/permission/reviewer/caveat gates
  pass.
- Client communication: draft/review only; no sending from this loop.
- Notion sync: blocked; Notion remains mirror/cockpit only.
- Tool/connector: no new install, OAuth, or write scope.
- Production/repo mutation: DTP docs/templates only in this pass.
- Autonomy: next step can review readiness; no runtime or scheduled workflow
  exists yet.

## Parked But Valuable

- Richer Practice Evolution review room after the status dashboard gets more
  real usage.
- AI agent report as future Practice OS / consulting-offer / adoption strategy
  research.
- Harvey MCP as future General Counsel/legal workflow research.
- Notion mirror for review cockpit after DTP records remain source of truth.
- FAOS as future substrate after readiness review and more operating evidence.

## Validation

- Commands run:
  - `dtp kaizen status --limit 10`
  - `dtp evolution status`
  - `dtp memory steward --limit 10`
  - `dtp research steward --limit 10`
  - `dtp practice doctor`
- Result: inputs loaded and `practice doctor` passed.
- Known gaps:
  - no autonomy-readiness review has been filled yet;
  - no scheduled/dry-run workflow has been designed;
  - no Notion mirror/status cockpit update was attempted;
  - no client-lane work was reopened.

## Next Review Trigger

Run this loop again after the autonomy-readiness review, after the next
substantial internal OS build, or before returning to Greg/Cam/CCAAP lanes.
