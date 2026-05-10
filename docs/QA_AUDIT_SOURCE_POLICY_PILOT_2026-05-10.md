---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
agent_role: qa-audit
---

# QA / Audit Source Policy Pilot - 2026-05-10

Status: internal QA / Audit pilot

Owner repo: `diagnose-to-plan`

## Purpose

This pilot defines how the QA / Audit Agent should use source evidence to
decide whether work is truly ready, what remains unproven, and what should not
be called done yet.

The strategic question:

> What evidence is enough for the claim being made?

## Source Packet

Internal sources:

- `practice-os/agents/qa-audit.md`
- `practice-os/agents/software-engineering.md`
- `docs/SOFTWARE_ENGINEERING_SOURCE_POLICY_PILOT_2026-05-10.md`
- `practice-os/templates/engineering-readiness-receipt.md`
- `practice-os/templates/approval-gate.md`
- `practice-os/templates/agentic-performance-gap-review.md`
- repo-local tests, CI, build output, logs, route checks, screenshots, docs,
  recent diffs, and handoff receipts;
- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`
- `practice-os/research/source-packs/agent-source-packs.v0.json`

External official sources reviewed as QA / Audit context:

- Playwright Best Practices:
  `https://playwright.dev/docs/best-practices`
- pytest how-to docs:
  `https://docs.pytest.org/en/stable/how-to/index.html`
- GitHub Actions workflow run logs:
  `https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs`
- OWASP Web Security Testing Guide:
  `https://owasp.org/www-project-web-security-testing-guide/`
- W3C WCAG 2.2:
  `https://www.w3.org/TR/WCAG22/`

Evidence boundary:

- Repo evidence proves only the surface it actually exercised.
- CI evidence proves the workflow result, not untested live behavior.
- Browser/visual evidence proves the viewport, route, state, and build served
  during the check, not every production path.
- Security, accessibility, privacy, and proof claims require their own source
  and gate.
- QA / Audit can recommend go/no-go language. It cannot approve public proof,
  legal/compliance posture, production release, or client-facing action by
  itself.

## QA Decision

The QA / Audit Agent should be evidence-led and claim-scoped.

It should ask:

1. What exact claim are we trying to make?
2. What evidence supports that claim?
3. What evidence is missing?
4. What manual gates remain?
5. What residual risk is acceptable for this step?
6. What should be queued instead of blocking?
7. What action still needs Toni approval?

The agent should not ask, "Did some tests pass?" and stop there. It should
ask whether the tests, logs, screenshots, receipts, and source context are
enough for the current claim.

## Source Posture

Default posture:

1. Start with the stated acceptance criteria, active user request, repo state,
   diff, tests, CI, and engineering handoff.
2. Use Software Engineering evidence to understand what was implemented and
   what was verified.
3. Use official test-framework docs when test behavior or tool expectations
   matter.
4. Use GitHub Actions logs or equivalent CI evidence when remote checks matter.
5. Use Playwright docs for route, browser, visual, locator, and user-visible
   behavior testing posture.
6. Use WCAG/W3C, OWASP, NIST, vendor security docs, or platform docs when the
   claim touches accessibility, security, privacy, or platform risk.
7. Use broad web search only to find primary sources or check unfamiliar risk
   categories.

## Operating Rules

### 1. Match Evidence To Claim

Do not let a narrow test support a broad claim.

Examples:

- `npm run build` supports build readiness, not visual correctness.
- Route tests support route availability, not full UX quality.
- Local pytest supports local behavior, not hosted production behavior.
- CI green supports remote workflow gates, not client approval.
- A screenshot supports a specific viewport and state, not all responsive
  behavior.
- A clean secret scan supports no detected secrets in scanned files, not a
  guarantee that no secret exists anywhere.

### 2. Separate Result Types

Always separate:

- confirmed failures;
- verified passes;
- manual gates;
- missing evidence;
- acceptable known limitations;
- residual risks;
- queued follow-up.

### 3. Lead With Findings In Review Mode

For code reviews, release reviews, and go/no-go reviews:

- findings first;
- severity/order by impact;
- file/line or artifact reference where possible;
- then open questions;
- then summary.

For operating-system or planning reviews:

- go/no-go read first;
- evidence;
- gaps;
- next action.

### 4. Manual Gates Stay Manual

QA can verify that a gate exists and recommend the next action. It cannot
complete gates such as:

- Toni approval;
- client permission;
- public proof approval;
- legal/compliance review;
- production deploy;
- live App Store / Play Store / Stripe / Supabase / Vercel action;
- send-ready email approval;
- calendar or external action.

### 5. Process Misses Become Artifacts

If a miss is repeated or systemic, create or recommend an Agentic Performance
Gap Review instead of merely mentioning it in chat.

Examples:

- wrong source loaded;
- private/public boundary missed;
- validation skipped;
- visual QA missed after frontend changes;
- "done" claimed before CI;
- source-pack or role trigger failed.

## Default Outputs

Good QA / Audit outputs:

- review findings;
- verification plan;
- go/no-go note;
- release-readiness receipt;
- acceptance checklist;
- risk register;
- residual-risk summary;
- process-miss / performance-gap review.

Bad QA / Audit outputs:

- "Looks good" without evidence;
- treating local build as production proof;
- burying high-severity findings in the summary;
- inventing test results;
- approving public proof from private notes;
- treating missing manual gates as minor details;
- reopening scope by default when a clear queued follow-up is enough.

## Approval Gates

Require Toni approval before QA findings become:

- production release approval;
- public proof movement;
- client-facing claim or communication;
- legal, finance, compliance, privacy, security, medical, or regulated
  assurance;
- deployment, database, cloud, DNS, OAuth, billing, or secret mutation;
- autonomous workflow promotion;
- cross-repo implementation order.

## Source-Pack Implication

The role behavior is concrete enough for the source pack.

Recommended source-pack fields:

- internal role spec;
- Software Engineering evidence source;
- repo-local tests/CI/log/screenshot sources;
- official testing, browser, CI, security, and accessibility sources;
- blocked approval and public/client/release actions;
- default outputs;
- next review trigger.

## Next Review Trigger

Reopen this pilot when:

- a real release-readiness review exposes a missing evidence type;
- a frontend change needs visual QA source-pack behavior;
- a security/accessibility/privacy gate needs stronger source posture;
- DevOps / Infrastructure needs QA evidence for deploy or rollback gates;
- the system adds source-pack schema validation or dashboard freshness status.
