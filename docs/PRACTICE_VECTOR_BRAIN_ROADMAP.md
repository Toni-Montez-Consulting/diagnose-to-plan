---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Vector Brain Roadmap

Status: gated roadmap for semantic retrieval over the Practice OS.

Owner repo: `diagnose-to-plan`

## Why A Vector Brain Could Help

A vector layer can help agents and Toni find related work across messy wording:

- meeting prep from prior receipts;
- proof-gap lookup across project records;
- similar-problem search across consulting, Hub, Omnexus, DeMario, and CCAAP;
- architecture drift detection;
- source packs for future sessions;
- "what did we decide last time" retrieval when exact filenames are unknown.

The value is recall and synthesis. It is not authority. Retrieved material must
still cite a source artifact and respect privacy gates.

## Layer Sequence

| Layer | Status | Goal | Gate |
|---|---|---|---|
| Markdown corpus | Now | stable source-indexed records | Knowledge Base V1 records exist |
| Local sanitized retrieval | Next | test recall without private leakage | approved public/sanitized corpus only |
| Hosted/RLS retrieval | Later | query private records safely | hosted DTP auth/RLS/import-export accepted |
| Agent-integrated retrieval | Later | source packs for agents | citation tests, refusal tests, privacy tests |
| Predictive memory | Parked | pattern recommendations and drift alerts | evals, approval, and no self-modifying behavior |

## Candidate Corpus

Start with public/internal-safe docs:

- DTP roadmap and system docs;
- proof queue and offer matrix;
- repo manifests and evidence indexes;
- steward receipts that do not contain private records;
- consulting public-site docs;
- Hub runtime current-state docs;
- `tm-skills` public skill docs and smoke runbooks.

Private client engagement records stay excluded until hosted DTP/RLS boundaries
and import/export receipts exist.

## Retrieval Rules

- Every answer must cite source file paths.
- Every private or blocked source must be filtered before retrieval or refused
  after retrieval.
- Retrieval can suggest next sources to inspect, but cannot approve proof,
  publish copy, send messages, mutate repos, or schedule meetings.
- Drift detection should create review items, not auto-edit docs.

## Eval Seeds

Initial eval questions:

1. Which source controls consulting public proof promotion?
2. What is the current Hub boundary for intake/runtime?
3. Which active client loop should run first?
4. Which public proof claims are blocked?
5. Which repo owns reusable SDLC skill behavior?
6. What must happen before FAOS implementation?

Acceptance requires source-backed answers and safe refusal when a query asks for
private client details.

## Do Not Do Yet

- Do not add Mem0, Letta, Langfuse, sqlite-vec, fastembed, pgvector, Pinecone,
  or a hosted vector service from this doc alone.
- Do not ingest `engagements/` into public DTP.
- Do not expose vector memory through the consulting site.
- Do not let retrieval replace DTP source-of-truth records.

