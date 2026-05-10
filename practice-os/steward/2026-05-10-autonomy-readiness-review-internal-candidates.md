---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
template_name: autonomy-readiness-review
---

# Autonomy Readiness Review - Internal Practice OS Candidates

Date: 2026-05-10

Reviewer: Codex with Toni direction

Workflow: Research source freshness, Memory review queue, Practice/status
dashboards, and Knowledge-base drift review

Owning repo/lane: `diagnose-to-plan` / internal Practice OS

Current autonomy level: A1

Requested next level: A4 for Research source freshness only; keep the others at
A1/A2 until more evidence exists

Decision: pilot next level for Research source freshness as a dry-run design;
keep current level for the other candidates

## Why This Workflow Wants More Autonomy

Toni wants the practice to keep learning and improving without requiring him to
manually maintain every source, memory item, research signal, operating pattern,
or project-execution lesson. The Research Arm, Memory Steward, Research
Steward, KB Event Workflow, Practice Evolution dashboard, and Operating Review
Loop now exist, but they still depend on Toni or Codex remembering when to
rerun them.

The right next step is not live autonomous action. It is a bounded dry-run
workflow that can surface stale or changed research sources into an internal
review queue.

## Current Manual Evidence

- Existing docs/templates/receipts:
  - `docs/RESEARCH_ARM_SOURCE_LIST_V0.md`
  - `docs/RESEARCH_ARM_V0.md`
  - `practice-os/templates/research-decision-record.md`
  - `practice-os/templates/research-pattern-candidate.md`
  - `practice-os/templates/research-arm-digest.md`
  - `practice-os/agents/research-steward.md`
  - `practice-os/steward/2026-05-10-research-source-list-and-kb-event-workflow.md`
  - `practice-os/steward/2026-05-10-practice-operating-review-001.md`
- Number of successful manual runs:
  - Research Steward has already run read-only review against parked research
    rows.
  - The first Practice Operating Review used Research Steward output to keep
    AI/legal research parked until a real spike opens.
  - The source list has a clear event-based workflow and recurring-source
    table.
- Known failures or misses:
  - No dry-run source freshness sweep exists yet.
  - No source-change queue exists yet.
  - No eval fixture exists for deciding whether a source update is meaningful
    versus noise.
- User value observed:
  - Toni wants help keeping knowledge bases updated and refined without doing
    all maintenance himself.
  - Toni wants eventual autonomous agents, but with staged authority and human
    review.

## Candidate Comparison

| Candidate | Current Level | Possible Next Level | Decision | Rationale |
|---|---|---|---|---|
| Research source freshness | A1 | A4 | pilot next level as dry-run only | best first candidate: public/internal approved source list, review output can be queued, no client/live/public action needed |
| Memory review queue | A1 | A2 | keep current level | useful, but memory promotion touches operating behavior and should stay human-reviewed until more review cycles exist |
| Practice/status dashboards | A1 | A3/A4 | keep current level | dashboard is useful, but another review cycle should prove the right fields before scheduled generation |
| Knowledge-base drift review | A1 | A4 | keep current level | strong candidate, but should follow source freshness because research-source drift is narrower and easier to evaluate |

## Source Scope

- Allowed sources:
  - `docs/RESEARCH_ARM_SOURCE_LIST_V0.md`
  - local DTP research digests, research-pattern candidates, Kaizen research
    rows, and steward receipts
  - public Tier 1 and Tier 2 sources already listed in the source list
  - Toni-provided saved reports and founder-email research signals only when
    already captured into DTP or explicitly provided for the review
- Blocked sources:
  - secrets, credentials, raw private client material, Microsoft confidential
    context, private relationship records, raw Gmail content unless Toni
    explicitly asks to use it, paid/private databases, and unsourced social
    claims as action evidence
- Source freshness risk:
  - high for vendor release notes and AI platform docs;
  - medium for governance/security sources;
  - low for internal DTP receipts but they can become stale as decisions change.
- Private/client-sensitive data involved: no for the first dry-run design.

## Allowed Actions

- Allowed reads:
  - DTP source-list docs and DTP research artifacts;
  - approved public sources when the operator explicitly runs a source review;
  - current date and source metadata.
- Allowed writes:
  - local ignored or committed review artifacts, depending on sensitivity;
  - research decision record drafts;
  - research pattern candidate drafts;
  - steward receipts;
  - a dry-run output queue if implemented later.
- Allowed tools/connectors:
  - local shell/CLI;
  - web browsing only when a source review needs current public facts;
  - no Gmail/Notion/Calendar/Hub/Supabase writes.
- Allowed triggers:
  - manual now;
  - event-based next;
  - scheduled only after a dry-run implementation proves low noise.
- Output destination:
  - DTP review artifact first;
  - later: a source-freshness dry-run queue under DTP-owned outputs or
    `practice-os/research/` after path decision.

## Explicitly Blocked Actions

This workflow cannot:

- send emails;
- draft or send client/prospect communications from research without a separate
  External Communications review;
- publish public claims;
- change public consulting copy;
- install tools or connectors;
- sync Notion;
- mutate Hub, consulting, Omnexus, DSE, or other sibling repos;
- create or run a live crawler;
- make pricing, legal, compliance, or proof claims;
- promote research into offer language without evidence and approval gates;
- read raw private client, relationship, or Microsoft-sensitive sources.

## Data And Privacy Boundary

- Data class: P1 for review artifacts; P0 for source docs.
- Redaction needed: yes if any source mention includes private/client-sensitive
  material; not needed for public-source names alone.
- Retention rule: committed DTP artifacts only for sanitized/internal material;
  private raw source material stays outside git or in approved private vaults.
- Logging/trace rule: record reviewed source names, dates, decisions, and
  evidence limits; do not store raw private text or secrets.
- Notion mirror allowed: no for V0 dry-run; possible later as sanitized status
  only after DTP remains source of truth.

## Validation And Evals

- Dry-run mode:
  - required before event-based or scheduled behavior.
- Test fixtures:
  - at least one unchanged source;
  - one source with a meaningful update;
  - one source with noisy/minor update;
  - one blocked/private source;
  - one stale local DTP research item.
- Expected output checks:
  - source name;
  - source tier;
  - reviewed date;
  - change summary;
  - evidence limit;
  - recommendation: ignore, watch, create decision record, create pattern
    candidate, create digest, or open implementation review.
- Regression checks:
  - no public claims;
  - no client communication;
  - no tool install;
  - no Notion sync;
  - no source-of-truth shift away from DTP.
- False-positive risks:
  - noisy changelogs creating too many review items;
  - trend content being mistaken for implementation evidence.
- False-negative risks:
  - missing a major platform change because the source list is stale;
  - ignoring a source that affects client trust, security, or workflow design.

## Audit, Rollback, And Override

- Audit log or receipt path:
  - this review;
  - future dry-run queue or research steward receipt.
- Rollback/undo path:
  - delete or supersede draft records before promotion;
  - revert committed DTP docs through normal PR process if a source is
    misclassified.
- Human override:
  - Toni can mark a source as ignore, watch, priority, blocked, or approved for
    deeper review.
- Kill switch:
  - stop after dry-run output; do not schedule or run automatically.
- Failure escalation:
  - if source review touches legal, privacy, proof, pricing, client data, or
    Microsoft-sensitive context, route to the relevant gate and pause.

## Cost And Runtime Boundary

- Runtime limit:
  - dry-run should stay small enough for an operator review; target less than
    10 minutes for a short source subset.
- Budget/cost limit:
  - no paid APIs, no paid crawlers, no new services.
- Rate limit:
  - respect public source access; prefer official RSS/changelog pages if later
    implemented.
- External service dependency:
  - none for this review;
  - future implementation may use web access only when the operator initiates
    the dry-run.

## Promotion Decision

Approve `Research source freshness` to move from A1 read-only recommendation
toward an A4 bounded scheduled workflow only as a dry-run design candidate.

This does not approve a live crawler, autonomous digest, scheduled job, Notion
sync, public claim feed, client communication, or repo mutation. It approves
the next artifact: a DTP-local dry-run workflow spec and/or CLI plan that
outputs source freshness findings for human review.

Keep Memory review queue, Practice/status dashboards, and Knowledge-base drift
review at their current levels until source freshness proves the dry-run pattern
or another review gives stronger evidence.

## Next Artifact

Create a `Research Source Freshness Dry-Run V0` spec or work item that defines:

- source subset for the first run;
- output schema;
- dry-run queue path;
- fixture examples;
- validation command;
- blocked-source behavior;
- human review decision states.

Do not implement a scheduled workflow until the dry-run surface is reviewed.

## Review Trigger

Reopen this readiness review after:

- the first source-freshness dry-run spec exists;
- a manual source freshness dry-run produces an output queue;
- Toni asks for scheduled source review;
- Research Steward starts recommending repeated source freshness checks;
- or a source update affects public claims, client trust, security, legal,
  pricing, or implementation architecture.
