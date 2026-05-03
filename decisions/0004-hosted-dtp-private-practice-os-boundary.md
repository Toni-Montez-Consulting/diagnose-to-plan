---
title: "Hosted DTP remains the private Practice OS"
date: 2026-04-29
status: accepted
---

# Decision: Hosted DTP is not Hub, CRM, or a client portal

Hosted DTP Phase 0 will be designed as Toni's private Practice OS surface for engagement state, artifacts, evidence, redaction, proof review, and decisions.

It will not start as:

- a public consulting site;
- a Hub runtime console;
- a CRM;
- a billing or e-signature product;
- a default client portal;
- a multi-user SaaS;
- a dashboard that has no real artifacts behind it.

This keeps the practice architecture clean:

- Consulting owns the public storefront, `/start`, proof surface, and noindex command room.
- Hub owns runtime intake, private console rows, webhooks, captures, runs, prompts, and support records.
- DTP owns Client Operating Kits, methodology, redaction/COI, proof governance, pattern promotion, and hosted engagement-state planning.
- Project repos keep their own product/app truth.

The design boundary, proof/redaction templates, and first DTP repo manifest/evidence-index pilot were accepted on 2026-04-29 in `practice-os/steward/2026-04-29-hosted-dtp-phase-0-acceptance-review.md`.

Hosted implementation remains gated until there is a separate implementation request and the Mom nonprofit or another real pilot creates records worth persisting.
