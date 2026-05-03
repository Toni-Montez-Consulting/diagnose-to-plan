---
created: 2026-04-28T07:21:53.4725765-05:00
command: manual
type: decision
status: accepted
---

# 0003 - Private remote setup

## Decision

Configure `diagnose-to-plan` with a private GitHub remote at `Toni-Montez-Consulting/diagnose-to-plan` and push the Phase 1 branch history before opening Phase 2.

## Rationale

Phase 2 introduces durable practice memory: journal entries, COI verdicts, client folders, decision notes, and eventually client-confidential frontmatter. Keeping that only on one local disk is not acceptable once the harness becomes an operating record for the consulting practice.

## Visibility

The repository is private. It stays private indefinitely because the repo will eventually contain client-adjacent context, confidential flags, and operational notes that should not be indexed or exposed publicly.

## Secret scanning

`.gitleaks.toml` is committed with patterns for Anthropic keys, AWS access keys, private keys, GitHub tokens, OpenAI keys, Stripe keys, and generic assignment-style secrets. `gitleaks` is not installed on this Windows machine as of this setup, so no active `gitleaks protect` pre-commit hook was wired in this pass.

## Operating rule

Do not push client-specific artifacts until the Phase 2 confidentiality and COI paths are implemented and tested. When `gitleaks` is installed later, wire `gitleaks protect` into the repo's pre-commit hook before the first client folder contains real identifying detail.
