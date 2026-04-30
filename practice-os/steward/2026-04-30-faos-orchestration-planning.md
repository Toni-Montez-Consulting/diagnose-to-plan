---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Receipt: FAOS Orchestration Planning

Date: 2026-04-30

## Trigger

Toni asked to merge the Frontier Agentic Operating System build spec and Phase 0 prompt into the master plan, Kanban backlog, epic/story planning, and agent-management/orchestration roadmap.

## Classification

| Item | Classification | Owner | Gate |
|---|---|---|---|
| FAOS roadmap integration | `roadmap_backlog_story`, `research_eval_lesson` | `diagnose-to-plan` | roadmap/backlog/docs updated |
| FAOS Phase 0 implementation | `parked_gated_automation` | future `faos` repo plus DTP adapters | Phase 0A readiness review accepted |
| Spec-Kit workflow | `practice_os_template`, `roadmap_backlog_story` | DTP plus future FAOS | CLI syntax verified and fit proven |
| Trace/memory substrate | `parked_gated_automation`, `coi_privacy_gate` | future FAOS/DTP | redaction, retention, and storage isolation accepted |
| Subagents/hooks/durable workflows | `parked_gated_automation` | future FAOS | evals, safety gates, and explicit approval |

## Findings

- FAOS is directionally aligned with DTP's Future Intelligence, Roadmap Steward, Activation Map, Workspace Efficiency, and `tm-skills` work.
- The Phase 0 prompt is not safe to run as written because it contains technical and boundary conflicts.
- The largest implementation blockers are Langfuse v3 topology, `uv`-only package management, Mem0/Letta storage isolation, DTP tracing boundaries, trace redaction, and COI ownership.
- The current roadmap order should not change. FAOS belongs as a gated orchestration-substrate lane after the current pilot/proof/smoke/Hub-validation path.

## Repo Boundaries

- Changed now: DTP docs, Practice OS template, steward receipt.
- Not changed now: consulting, Hub, `tm-skills`, Omnexus, DeMario, FamilyTrips, DSE, engineering-playbook, `hub-prompts`, `hub-registry`.
- Not created now: `C:\Users\tonimontez\code\faos`.

## Next Queue Impact

The active queue remains:

1. Mom nonprofit private kit.
2. Command Room fit and proof/redaction pilot.
3. `tm-skills` external reload/smoke tests.
4. Hub prompt/registry cross-validation.
5. Repo manifests/touch passes.

FAOS adds a later readiness story, not an active implementation story.

