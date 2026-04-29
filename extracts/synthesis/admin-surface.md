---
group: admin-surface
synthesized_at: '2026-04-29T14:08:49Z'
source_types:
- lesson
- pattern
source_paths:
- extracts/patterns/consulting--admin-command-room.md
- extracts/patterns/hub--admin-console.md
- extracts/lessons/consulting--2026-04-28-admin-surface.md
canonical_repo: consulting
canonical_repos:
- consulting
- hub
pattern_count: 2
lesson_count: 1
decision_count: 0
promoted: false
private_review_required: true
regrouped: false
no_confirm: true
---

# Admin Surface

## Synthesis

This synthesis combines 3 extract sources: 2 pattern(s), 1 lesson(s), and 0 decision(s). The current canonical repo is `consulting`, based on promoted status, captured lessons/decisions, detector confidence, and evidence breadth.

## Canonical Evidence

- `extracts/patterns/consulting--admin-command-room.md` (pattern, repo: `consulting`): Admin Command Room
- `extracts/patterns/hub--admin-console.md` (pattern, repo: `hub`): Admin Console
- `extracts/lessons/consulting--2026-04-28-admin-surface.md` (lesson, repo: `consulting`): consulting admin-surface

## Reusable Shape

Use a two-layer operating pattern: a public-safe command room for status, links, triage, work orders, and runbook boundaries; and a protected private console for records, notes, workflow state, and owner decisions.

## What Varies

Domain language, triage stages, record schema, auth level, health checks, and the public/private boundary should vary by client and deployment risk.

## Do Not Reuse Blindly

Do not copy private rows, client notes, service-role behavior, raw intake content, or workflow records into a public surface. Reuse the boundary, not the private data.

## Drafting Use

When a diagnose note asks for `admin-surface`-adjacent work, cite this synthesis as prior operating evidence, then name which parts are being reused and which parts must be adapted for the client.

## Source Notes

- `extracts/patterns/consulting--admin-command-room.md` is a `medium` confidence pattern candidate.
- `extracts/patterns/hub--admin-console.md` is a `medium` confidence pattern candidate.
- `extracts/lessons/consulting--2026-04-28-admin-surface.md` records a lesson for `admin-surface`.

## Review Checklist

- No secrets or credentials.
- No raw intake records.
- No private client notes.
- No service-role values.
- `promoted` remains false until this synthesis helps real work.
