# 0005: Private Engagement Durability

Status: accepted for V0 pilot.

Date: 2026-04-30

## Context

DTP's public git repo intentionally ignores `engagements/` so private client and family/project engagement material does not leak into the code repository. The Mom nonprofit kit is the first real pilot that should leave durable local receipts without becoming public.

Local-only files are useful for privacy but weak for recovery. Public git is durable but wrong for private engagement records. Hosted DTP is not implemented yet and should not be built before real records prove the model.

## Decision

Use the ignored `engagements/` folder for private kit work and initialize the separate `dtp vault` git repo inside that folder for local snapshots.

Do not commit private engagement records to the public DTP repo. Do not rely on the vault for off-laptop durability until a private remote is created and tested.

## Consequences

- Public DTP history stays clean of private engagement records.
- The Mom kit can be snapshotted locally for recovery and review.
- A private remote remains a near-term durability follow-up before the vault is trusted as long-term backup.
- Hosted DTP remains gated until real engagement, artifact, evidence, redaction, proof, and decision records justify implementation.
