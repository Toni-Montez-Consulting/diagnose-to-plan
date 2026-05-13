---
name: build-patterns
description: "Load prior build-pattern synthesis docs when drafting scopes, SOWs, proposals, or engagement plans that touch admin rooms, intake systems, app launches, agent runtimes, component libraries, or previously shipped patterns."
---

# Build Patterns

The synthesis docs in `extracts/synthesis/` and reviewed/draft patterns in `practice-os/patterns/` are the canonical record of patterns Toni has already proven or is actively reviewing.

When drafting a scope, SOW, operating pattern, admin surface, or public/editor-facing polish pass, scan those directories first. For each relevant synthesis or pattern doc, surface:

- the canonical implementation and source repos
- what can be reused
- what must vary by client
- what private or risky details must not be copied
- whether the pattern should be refreshed, promoted, superseded, or referenced

Use `practice-os/patterns/surface-translation-standard.md` when internal build notes need to become public, editor, owner, or client-facing language.

When citing a pattern in a draft, reference the synthesis or pattern doc by relative path.
