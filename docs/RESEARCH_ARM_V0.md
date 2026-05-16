---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Arm V0

Status: manual-first operating loop

Owner repo: `diagnose-to-plan`

## Thesis

The consulting practice needs a research and intelligence arm that helps Toni
stay current, translate AI/software changes into business language, and turn
useful signals into better offers, diagnostics, prompts, templates, skills,
client explanations, and implementation proposals.

The system should not become a pile of hype, links, or autonomous changes.

Key rule:

> Agents can run continuously, but authority should not run continuously.

Research may run on a cadence. Synthesis may be frequent. Recommendations may
be proactive. Authority still flows through Toni before public positioning,
pricing, offers, client deliverables, repo changes, tool installs, or live
automation changes.

## Why This Exists

AI, agent tooling, coding workflows, enterprise adoption patterns, governance
expectations, and workflow automation patterns are changing too quickly for the
practice to rely on occasional manual link chasing.

The Research Arm should help answer:

- What changed?
- Why does it matter?
- Is it useful, hype, risky, or not relevant?
- What should Toni learn from it?
- What should Toni explain to clients?
- What should change in the consulting practice?
- What should become a new diagnostic, checklist, prompt, template, skill,
  offer component, client education artifact, content seed, roadmap item, or
  future implementation proposal?
- What should be ignored?

## Source Inputs

Initial source signals came from Toni's founder-email captures on 2026-05-09:

- `Squad ideas`
- `Ideas for clients`
- Microsoft Work Trend Index link on agents and human agency
- Chris Hood AI governance article
- local `2026 State of AI Agents Report.pdf`

The 2026-05-15 `Research continued` founder email added the Pattern
Intelligence loop: study strong AI and workflow companies, extract the
underlying work pattern, and translate it into consulting diagnostics,
workflows, templates, client explanations, skills, runbooks, or parked future
ideas.

These are source prompts for the system, not automatic proof for public claims.
Public claims still need primary-source review, caveats, and approval.

Recurring source list:

- `docs/RESEARCH_ARM_SOURCE_LIST_V0.md`

The source list defines the default recurring sources, source tiers, review
triggers, and public-claim boundary. It is a research input map, not an
autonomous crawler.

## V0 Operating Loop

V0 is intentionally small:

1. Capture a research signal.
2. Classify the signal.
3. Produce a short digest.
4. Map it into the practice.
5. Recommend one of: adopt, pilot, watch, reject, or ignore.
6. Propose a next artifact only when useful.
7. Ask for human approval before implementation.
8. Mirror a sanitized status to Notion only when needed.

Minimum loop:

```text
source signal -> digest -> recommendation -> approval -> implementation proposal
```

The default trigger is event-based, not scheduled. Use the loop when Toni saves
or forwards a signal, a client question needs evidence, a platform used by the
practice changes, a knowledge base feels stale, or a recurring practice pattern
appears.

Use `practice-os/templates/research-decision-record.md` when the research event
requires an adopt, pilot, watch, reject, or park decision.

Use `docs/KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md` when the research event implies
a broader knowledge-base update across memory, operations, project execution,
agent roles, messaging, or repo-local docs.

## Research Steward Layer

Research Steward is the read-only review surface for this loop.

Use:

```powershell
.\.venv\Scripts\dtp.exe research steward
```

It reads Research Arm digests, research-pattern candidates, and
research-flavored Kaizen rows, then recommends whether each item should be
finished, promoted, parked, rejected, or converted into a bounded experiment.
It does not authorize public claims, offer changes, tool installs, repo
changes, client communication, Notion sync, or autonomous runtime.

## Authority Boundary

Allowed without separate approval:

- maintain the recurring source list;
- search and read public sources;
- summarize source material;
- compare sources;
- classify signals;
- draft digests;
- draft research decision records;
- recommend next actions;
- propose repo/doc/template updates;
- create research radar items;
- create implementation proposal drafts;
- identify drift or stale assumptions.

Approval required:

- public claims;
- public positioning changes;
- pricing or offer changes;
- client deliverable changes;
- legal/compliance/governance language;
- Microsoft-related positioning;
- COI-sensitive work;
- tool/OAuth/connector installation;
- write-enabled automation;
- live cloud/database/billing changes;
- commits, pushes, PRs, or deployments when not explicitly requested.

Blocked:

- using confidential Microsoft information;
- implying Microsoft endorsement;
- targeting Microsoft customers through Toni's W-2 role;
- publishing research claims without review;
- auto-updating public site copy;
- auto-changing agent instructions, offers, or pricing;
- autonomous self-learning without reviewed evidence and gates.

## Source Quality Rules

Prefer:

- official product documentation;
- primary research reports;
- standards or governance bodies;
- vendor changelogs;
- reputable technical blogs with source links;
- repo evidence from Toni's own work;
- client/operator field notes that are approved for internal use.

Avoid:

- social-media takes without source material;
- hype threads;
- uncited statistics;
- screenshots without provenance;
- claims that sound useful but cannot be traced.

## Digest Output

Use `practice-os/templates/research-arm-digest.md`.

Every digest should include:

- source list;
- what changed;
- why it matters;
- hype filter;
- practice impact;
- client explanation;
- recommended classification;
- proposed artifact;
- approval gate;
- next review date.

When the source is an observed business behavior, client/operator story,
market pattern, field note, or recurring workflow signal rather than only a
link or report, use
`practice-os/templates/research-pattern-candidate.md` before promoting the
lesson to `practice-os/patterns/`. The pattern candidate should preserve the
evidence limit, consulting translation, possible client artifact, and next
experiment instead of treating one observation as a reusable truth.

## Classification

Use the existing research radar language:

- `Adopt`: the practice should use this now.
- `Pilot`: test in a bounded internal workflow.
- `Watch`: useful but too early or not urgent.
- `Reject`: not useful, too risky, too costly, or misaligned.
- `Ignore`: not worth tracking further.

## Research Arm Workstreams

These are workstreams, not new autonomous roles yet.

| Workstream | Purpose | V0 Status |
|---|---|---|
| Research Arm | collect and synthesize external AI/software/workflow signals | active V0 |
| Practice Intelligence | translate research into offers, diagnostics, and client explanations | manual V0 |
| Pattern Intelligence | study company/product patterns and convert them into practical consulting assets | manual V0 |
| Pattern Extraction | turn real-world observations and research signals into reusable consulting pattern candidates | manual V0 |
| Repo Quality | find stale docs, conflicting instructions, and drift | future/manual |
| Roadmap Signal | suggest what should move, park, or become a template | manual V0 |
| Content Signal | create raw content seeds without polished social slop | future/manual |
| Implementation Proposal | turn accepted research into scoped build proposals | manual V0 |

Do not add these as separate specialized agent roles until repeated use proves
that the current first-wave role set cannot cover the work.

## Pattern Intelligence Loop

Pattern Intelligence is the company-pattern study function inside the Research
Arm.

It asks:

- What is the company really doing?
- What pain did it solve?
- What workflow did it collapse?
- What old way of working did it replace?
- What part is hype or scale-specific?
- What part could apply to small businesses?
- What part could improve Toni's internal operating system?
- What consulting diagnostic, workflow, assistant, runbook, template, offer
  component, or client explanation could come from it?

V0 company examples from Toni's memo:

- Glean: internal knowledge layer and Business Memory OS translation.
- Granola: meetings becoming business memory.
- Cursor / Lovable: idea-to-build speed and the rising importance of judgment,
  sequencing, and guardrails.
- Harvey: vertical AI with domain context and credibility.
- Sierra: customer communication as a managed system.
- n8n / Lindy: repeatable work units close to existing tools.
- Gamma: decision-ready artifacts, not just generated content.

These examples are study prompts, not public proof or endorsement. Each study
should produce one useful artifact candidate or be parked.

Current first Pattern Intelligence artifacts:

- `practice-os/research/digests/2026-05-15-pattern-intelligence-research-arm.md`
- `practice-os/research/radar/2026-05-15-pattern-intelligence-ai-company-patterns.md`
- `practice-os/research/pattern-candidates/2026-05-15-pattern-intelligence-research-to-offer-loop.md`
- `practice-os/research/pattern-candidates/2026-05-15-glean-business-memory-company-pattern-study.md`

The first Glean study is a produced pilot, not a promoted template. It should be
reviewed for field usefulness before Pattern Intelligence becomes a recurring
template, public offer input, or automation lane.

## Notion Mirror Rule

Notion can mirror:

- topic;
- classification;
- why it matters;
- next action;
- review date;
- DTP source path.

Notion should not hold:

- raw private notes;
- unreviewed claims;
- confidential source material;
- client-sensitive context;
- Microsoft-sensitive context;
- implementation authority.

If Notion and DTP disagree, DTP wins.

## Consulting Repo Boundary

The consulting repo may contain public-safe or repo-local pointers that explain
how Research Arm outputs influence site copy, offer positioning, proof posture,
or public docs.

The consulting repo should not become the source of truth for:

- the research operating model;
- private relationship records;
- private client facts;
- agent-system authority;
- raw research archive;
- Notion mirror state.

## Opportunity OS Boundary

The Opportunity OS is related but separate.

Research Arm answers:

> What is changing in AI, software, operations, and the market, and what should
> the practice do with that signal?

Opportunity OS answers:

> Which relationships, operators, businesses, and warm opportunities should
> Toni nurture without overcommitting?

V0 sequence:

1. Build Research Arm V0.
2. Pilot one weekly digest.
3. Then design Opportunity OS V0 around relationship/opportunity capture,
   scoring, follow-up, referral mapping, and capacity protection.

## First Pilot Digest Topics

Use the 2026-05-09 founder-email captures as the first manual digest packet:

- AI agents in production and multi-step workflows;
- human-led agency and learning-system behavior;
- adaptive AI governance;
- research-to-practice translation;
- lightweight intelligence loops as a future client concept.

First digest:

- `practice-os/research/digests/2026-05-09-ai-agent-operating-shift.md`

## Success Criteria

V0 is working if:

- research becomes fewer random links and more useful decisions;
- Toni can scan one digest and know what matters;
- client-facing explanations get clearer;
- roadmap changes are proposed, not silently made;
- research feeds artifacts, prompts, templates, or diagnostics only after
  review;
- the practice gets smarter without becoming AI slop.

## Non-Goals

- No always-on hosted agent runtime.
- No vector database.
- No autonomous browser/research loop.
- No auto-published content.
- No auto-created public proof.
- No unattended tool installs.
- No Microsoft-confidential or COI-sensitive research use.
- No Notion source-of-truth shift.
