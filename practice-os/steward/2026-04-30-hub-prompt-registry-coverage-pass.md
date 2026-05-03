---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Review: Hub Prompt/Registry Coverage Pass

Date: 2026-04-30

## Trigger

Toni approved the next Workspace Efficiency batch: close the Workspace Command Center's missing coverage for `hub-prompts` and `hub-registry` without changing prompt content, registry targets, Hub runtime behavior, CI tokens, DSE, FAOS, consulting proof, or the Mom private kit.

## Active Story

- Story: Hub prompt/registry workspace coverage
- Repo edited: `diagnose-to-plan`
- Repos checked read-only: `hub-prompts`, `hub-registry`
- Status after this pass: DTP-owned manifests/evidence indexes added for both repos
- Command Center expected result: `hub-prompts` and `hub-registry` should report `manifest=ok; evidence=ok`; `dse-content` remains intentionally missing

## Repo Boundaries

- `hub-prompts`: owns prompt Markdown, prompt ids, prompt metadata, prompt schema validation, and future prompt eval/golden fixtures.
- `hub-registry`: owns target/routing config, registry validation, sibling manifest validation, and local prompt-id cross-validation.
- Hub: owns runtime prompt sync, records, webhook/dispatch behavior, and production support checks.
- DTP: owns this coverage receipt, roadmap status, and Workspace Command Center reporting.

## Validation Evidence

| Repo | Command | Result | Evidence |
|---|---|---|---|
| `hub-prompts` | `git status --short --branch` | clean | `## main...origin/main` |
| `hub-prompts` | `npm test` | pass | `npm run validate` and `npm run validate:phase0`; 6 prompts checked; Phase 0 prompts valid |
| `hub-prompts` | CI read | pass | GitHub Actions `Validate Prompts` run 25132070092 |
| `hub-registry` | `git status --short --branch` | clean | `## main...origin/main` |
| `hub-registry` | `npm run validate` | pass | 9 targets, 11 prompt-trigger pairs, 1 cron schedule |
| `hub-registry` | `npm run validate:manifests` | pass | 8 manifests valid; `fitness-app` deferred by design |
| `hub-registry` | `npm run validate:prompt-ids` | pass | 3 referenced prompt ids exist in sibling `hub-prompts` |
| `hub-registry` | `npm test` | pass | registry shape, sibling manifests, and prompt ids passed |
| `hub-registry` | CI read | pass | GitHub Actions `Validate registry` run 25144066822 |

## No-Touch Boundaries

- Do not change prompt content in `hub-prompts`.
- Do not change targets, triggers, or activation policy in `hub-registry`.
- Do not add private sibling-repo checkout tokens or cross-repo CI access.
- Do not touch Hub runtime, consulting public proof, DSE, FAOS, or the Mom private kit.
- Do not treat these manifests as runtime configuration.

## Blockers And Follow-Ups

- DSE remains intentionally missing from Workspace Command Center coverage until its active branch is clean or explicitly selected with COI-aware scope.
- Mom nonprofit owner facts, proof permission, after-state evidence, redaction, reviewer, and caveat gates remain pending.
- Claude Code and GitHub Copilot `tm-skills` smoke tests remain manual/back-burner.
- FAOS readiness remains parked; no FAOS repo or substrate work is authorized.
- Private sibling-repo CI access remains deferred until local-first validation becomes a real bottleneck.

## Acceptance

- `hub-prompts` manifest and evidence index exist in `practice-os/efficiency/`.
- `hub-registry` manifest and evidence index exist in `practice-os/efficiency/`.
- `dtp workspace report` should leave only `dse-content` as missing coverage.
- Full DTP validation and targeted redaction checks must pass before commit/push.
