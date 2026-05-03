---
title: "Hosted DTP Phase 0.2 governance before private records"
date: 2026-05-03
status: accepted
---

# Decision: Hosted DTP can run live, but non-smoke records need fallback rules

Hosted DTP Phase 0.2 accepts the live Supabase data plane as the private
operator app boundary, with these rules:

- Real operator policy: non-smoke private records belong to Toni's real
  operator account only.
- Smoke account policy: the two smoke operator accounts stay as clearly tagged
  regression fixtures for Auth/RLS checks.
- Smoke record policy: smoke records may remain in the live project while they
  are useful for RLS regression; rotate or delete them only if they create scan
  noise.
- Deployment posture: keep the app local/private with the dedicated live
  Supabase project for now; do not deploy a public web surface yet.
- Backup/export rule: no non-smoke private engagement can be stored only in
  Supabase until a markdown export fallback exists and has been verified for
  that lane.

This decision does not unlock client portals, public dashboards, QuickBooks
writes, Stripe work, autonomous agents, FAOS implementation, or public proof.

Hosted DTP remains the private DTP operating brain. DTP markdown/private kits
remain the fallback and audit surface until backup, export, and access rules
are proven across real operating cycles.
