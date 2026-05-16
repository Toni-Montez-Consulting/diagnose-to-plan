---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Glean Company-Pattern Study - Business Memory Layer

## Study Metadata

- Study id: company-pattern-2026-05-15-glean-business-memory-layer
- Created: 2026-05-15
- Source type: field_note + official_public_sources
- Reviewer: Toni
- Status: draft
- Public status: not public copy

## Sources

| Source | Type | Date checked | Link / Path | Use |
|---|---|---|---|---|
| Toni founder memo: `Raw memo: Glean, business memory, and the consulting practice` | field_note | 2026-05-15 | user-provided email text | Primary internal interpretation and consulting translation. |
| Glean homepage | official_public_source | 2026-05-15 | https://www.glean.com/ | Product positioning, assistant, agents, search, app connectors, permissions language. |
| Glean Knowledge Graph docs | official_public_source | 2026-05-15 | https://docs.glean.com/security/knowledge-graph | Knowledge graph, content/people/activity model, and permission-aware indexing. |
| Glean Connectors docs | official_public_source | 2026-05-15 | https://docs.glean.com/connectors/about | Connector role, source permissions, and data-source integration boundary. |

## Company Pattern

Glean is not only interesting as enterprise search. The useful pattern is a
business memory layer: one trusted surface that understands where company
knowledge lives, who can access it, how work is connected, and how a worker can
ask a question without first knowing which system contains the answer.

Glean's official material emphasizes a work AI platform with assistant, agents,
search, connectors, and permissions-aware company context. Its docs describe a
knowledge graph built from content, people, and activity, plus connectors that
fetch data and permissions from source systems.

## Pain Solved

- Employees waste time remembering where knowledge lives before they can use it.
- Company answers are split across docs, email, chat, tickets, CRM, project
  tools, cloud drives, and people's memory.
- New employees and cross-functional operators have to ask humans for context
  that often already exists somewhere.
- AI without source context can produce confident but ungrounded answers.

## Workflow Collapsed

Old workflow:

1. Know the right system.
2. Search that system.
3. Ask a coworker if the search fails.
4. Cross-check the answer in another system.
5. Manually write or perform the follow-up action.

Collapsed workflow:

1. Ask one business-memory surface.
2. Get an answer grounded in the systems the user can access.
3. Use the result to draft, decide, or trigger the next workflow.

## Old Way Replaced

The old way is not just "bad search." It is owner/operator memory as the
router. Someone has to know where answers live, whether they are current, who
owns them, and whether they are safe to use.

The Glean pattern replaces the human routing burden with a structured knowledge
layer that sits above tools but still respects source systems and permissions.

## Transferable To Toni's Practice

The transferable pattern is not enterprise search at full scale. It is:

- map where the business's answers live;
- identify repeated owner, employee, customer, and vendor questions;
- separate trusted sources from stale sources;
- decide which answers are safe for AI to search, draft, or route;
- build one useful assistant or workflow around the highest-value repeated
  question set;
- leave behind a runbook, source map, and handoff.

This directly supports the Business Memory OS lane.

## Not Transferable Yet

Do not copy these parts:

- full enterprise connector library;
- broad multi-tenant SaaS platform;
- enterprise permission graph;
- always-on indexing across all client systems;
- autonomous agents that act across a whole company;
- public claims that Glean proves SMB demand for Toni's offer.

Those are scale and security problems, not the first consulting product.

## Small-Business Translation

The SMB version should not start with "connect everything."

It should start with:

1. List the 25 recurring questions the business answers every month.
2. Identify where each answer currently lives.
3. Mark who owns the answer and how often it changes.
4. Classify each question as search only, draft only, workflow, or do not
   automate.
5. Pick one assistant/workflow that reduces a real bottleneck.
6. Hand off the source map, runbook, and maintenance rhythm.

## Internal Practice Translation

Toni can use the same pattern inside the consulting practice:

- client context file as the memory layer;
- source-material index as the permission/source map;
- decision log as institutional memory;
- runbook as handoff memory;
- weekly owner memo as operating surface;
- reusable skills/templates as workflow memory;
- proof/redaction gates as access control.

This makes DTP and Practice OS the internal version of the same pattern without
building a Glean competitor.

## Diagnostic Artifact Candidate

Use this diagnostic prompt:

> List the 25 questions this business owner, employee, customer, or vendor
> might ask every month. For each question, identify where the answer currently
> lives, who owns it, how often it changes, whether it is safe for AI to answer,
> and what action should happen after the answer is found.

Then classify each question:

- Search only: find the answer.
- Draft only: help write the response.
- Workflow: take the next step.
- Do not automate: human judgment required.

## Offer Translation

Keep this internal for now:

- Diagnostic: Knowledge Layer Audit.
- Focused build: Business Memory Assistant.
- Premium engagement: Business Memory OS.

Public language should avoid "Mini-Glean" and avoid implying endorsement.

Plain version:

> Most small businesses do not need another AI tool. They need their business
> knowledge cleaned up, connected to the right places, and turned into
> something the owner and team can actually use.

## Evidence Limits

- Supported: Glean publicly positions around assistant, agents, search,
  connectors, and permission-aware company context; Toni's field note shows why
  that pattern matters for consulting.
- Anecdotal: one friend's description of how Glean feels inside his company.
- Unproven: whether small businesses will pay for a named Business Memory OS
  package, which vertical will buy first, and which pricing tier will convert.
- Cannot claim publicly: Glean endorses Toni, Glean proves the offer, Glean is
  the same as the SMB service, or Toni has built an enterprise knowledge graph.
- COI/privacy boundary: use only public Glean sources and Toni-provided field
  notes. Do not use Microsoft-confidential or employer-specific material.

## Parked Ideas

- A Business Memory OS public offer page after one paid/permissioned example.
- A reusable `business-memory-os-diagnostic.md` client worksheet variant.
- A private Practice OS memory assistant after more client loops prove the need.
- A vertical donor-operations assistant for nonprofit CRM-adjacent clients.
- A connector-readiness audit for clients that are not ready to connect tools.

## Next Review

- Toni reviews whether the study fields are useful.
- If useful, create a reusable company-pattern study template.
- If not useful, keep Pattern Intelligence as occasional research notes and do
  not expand the process.

## Next Experiment

- Where to test this next: apply the Business Memory OS diagnostic to one
  known small business or hypothetical local service business before naming a
  public offer.
- What signal would confirm it is useful: the diagnostic produces a source map,
  three ranked workflow opportunities, and one clear assistant/workflow build
  without needing a broad connector platform.
- What signal would make us drop it: the exercise becomes generic AI tooling
  advice, source cleanup with no workflow value, or a fake "AI search" pitch.

## Promotion Decision

- Recommended state: pattern_candidate
- Reviewer: Toni
- Approved state:
- Destination if promoted:
  `practice-os/patterns/` or a reusable company-pattern study template after
  Toni reviews this pilot.

## Notion Mirror Summary

Safe to mirror: yes

If yes:

- Topic: Glean company-pattern study for Business Memory OS
- Classification: Pilot produced, review needed
- Why it matters: translates enterprise knowledge-layer movement into a
  small-business diagnostic and delivery pattern.
- Next action: Toni reviews study fields before any template or public offer.
- DTP source path:
  `practice-os/research/pattern-candidates/2026-05-15-glean-business-memory-company-pattern-study.md`
