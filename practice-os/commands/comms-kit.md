---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Command Contract: /comms-kit

## Purpose

Generate communication assets that explain Toni's consulting practice to a
specific audience without generic AI-consultant language.

## Inputs

- Audience: coworkers/tech peers, friends/family, spouse/family, business
  professionals, prospects, or general audience.
- Destination: private conversation, internal/private network, client-facing
  draft, or public internet.
- Allowed proof points.
- Artifact shape: pitch, explainer, infographic brief, diagram, slides, email,
  LinkedIn, or X thread.
- Source rules from `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md`.

## Allowed Reads

- `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md`
- `practice-os/comms/`
- relevant reviewed proof/redaction artifacts
- user-provided notes

## Output

Markdown under `practice-os/comms/{audience}/` or visual/slide subfolders.
Public-ready output must remain marked as draft until human review.

## Required Sections

- Destination and audience.
- Allowed proof points.
- Draft artifact.
- Public/private gate.
- Anti-generic-copy check.
- Missing facts or TODOs.

## Guards

- Do not use unsupported AI adoption statistics as fact.
- Do not imply employer endorsement.
- Do not publish services/pricing.
- Do not use client-private facts or proof without permission.
- Avoid generic AI-consulting boilerplate called out in the ethos.

## Acceptance Criteria

- Output sounds like a person who builds and hands off systems.
- It leads with the operator problem for non-technical audiences.
- It leads with architecture and compounding system design for AI-fluent peers.
- It preserves Operator-path as the flagship.
- It clearly labels public review gates.

## Fixtures

- First private communications kit:
  `practice-os/comms/private/business-brain-pitch-kit-2026-05-01.md`
