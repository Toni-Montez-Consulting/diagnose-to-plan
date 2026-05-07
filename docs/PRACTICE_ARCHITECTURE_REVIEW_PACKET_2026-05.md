---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Architecture Review Packet - May 2026

Status: architecture and systems-health packet for the Practice OS backlog.

Owner repo: `diagnose-to-plan`

## System Map

```text
Client/prospect/operator signals
  -> Gmail, Calendar, live meetings, intake, project repos, Notion inbox
  -> DTP source routing and private engagement vault
  -> Agent Squads V0 and Knowledge Base V1 records
  -> Hub runtime support where runtime is needed
  -> consulting public proof/storefront after proof gates
  -> tm-skills reusable SDLC behavior after smoke/canary gates
```

## Ownership Boundaries

| Layer | Owns | Does not own |
|---|---|---|
| DTP | roadmap, proof gates, private-to-public routing, Practice OS docs, templates, receipts | live Hub runtime rows, public site rendering, reusable SDLC skill files |
| Engagement vault | private client/prospect truth | public proof or source-of-truth docs |
| Consulting | public storefront, CTA, proof presentation, design system | private client records, proof approval, squad state |
| Hub | intake runtime, console/runtime evidence, prompts, webhooks, health | CRM, billing, client kits, public proof, DTP cockpit |
| tm-skills | reusable coding-agent behavior and evals | client facts, COI, proof, roadmap ownership |
| Project repos | product/client implementations | practice-wide state or public proof promotion |

## Systems Health Review

### Weakest Systems

- System: Memory and retrieval
- Evidence: Knowledge exists across DTP docs, private vault, Hub docs, consulting
  docs, and chat memory.
- Why it matters: future agents can miss the right source or over-trust stale
  chat.
- Smallest useful fix: Knowledge Base V1 metadata, source indexes, and memory
  promotion records before vector retrieval.
- Fix now / queue / ignore: fix now.

### Weakest Systems

- System: Public proof promotion
- Evidence: consulting needs stronger proof, but proof gates live in DTP and
  client-specific material is private.
- Why it matters: premature public copy can leak or overclaim.
- Smallest useful fix: audit consulting now, publish proof only after the DTP
  proof path clears.
- Fix now / queue / ignore: fix audit now, queue proof.

### Weakest Systems

- System: Runtime authority
- Evidence: Hub can receive intake and support console/runtime flows, but DTP
  owns practice decisions.
- Why it matters: Hub expansion could accidentally become CRM or practice
  cockpit.
- Smallest useful fix: Hub readiness note and route classification before new
  runtime features.
- Fix now / queue / ignore: fix now.

### Weakest Systems

- System: Agent behavior portability
- Evidence: tm-skills has healthy Phase 1 skills, plus untracked candidate
  skill folders that need classification.
- Why it matters: reusable behavior can drift if install/smoke is stale.
- Smallest useful fix: run checks, record candidate status, and keep external
  smoke manual until observed.
- Fix now / queue / ignore: fix now.

## Architecture Review Sequence

1. Run Client OS pilots.
2. Capture friction into Knowledge Base V1.
3. Audit consulting proof/design architecture without changing public proof.
4. Tighten Hub runtime readiness.
5. Classify tm-skills candidates and smoke reusable skills.
6. Revisit hosted DTP schema from repeated records.
7. Revisit vector memory.
8. Revisit FAOS readiness.

## Draft-Only Automation Boundary

| Action class | First-wave authority |
|---|---|
| Preflight briefs | draft allowed |
| Source indexes | draft/update allowed inside owning private/public lane |
| Meeting notes and extraction | draft/update private kit only |
| Client emails | draft only |
| Calendar changes | draft/suggest only |
| Public proof | blocked until proof gates |
| Consulting copy changes from proof | blocked until proof gates |
| Hub runtime writes | blocked unless explicitly scoped |
| tm-skills global install | blocked unless explicitly approved |
| Project repo implementation | blocked unless owning repo lane is explicitly active |

