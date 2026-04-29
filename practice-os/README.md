---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Practice OS

Reusable operating assets for the consulting practice. This folder is the Practice Brain: policies, templates, Skills, and reviewed Bottleneck Patterns that can be reused without carrying client-private context.

Rules:

- Keep client-sensitive work in `engagements/`.
- Promote only redacted, reviewed lessons into `practice-os/`.
- Use `extracts/` for raw DTP pattern extraction and `practice-os/patterns/` for reusable judgment.
- No credentials, client financial specifics, raw intake, Microsoft confidential information, or unreviewed case-study claims.

Command-room templates:

- `templates/client-command-room-fit-assessment.md` decides whether to build a command room, use a handoff checklist, skip the private surface, or defer.
- `templates/client-command-room-spec.md` defines owner dashboard, owner tasks, business roadmap, developer roadmap, handoff/rules, and placeholder-only support/verification surfaces.

Future Intelligence templates:

- `templates/lesson-capture.md` turns delivery outcomes and failures into reusable lessons.
- `templates/research-radar-item.md` tracks AI/dev signals as `Adopt`, `Pilot`, `Watch`, or `Reject`.
- `templates/research-spike.md` scopes a bounded tool/protocol/framework investigation.
- `templates/portfolio-scorecard.md` summarizes repo health, proof readiness, and next touch lane.
- `templates/agent-session-record.md` leaves a receipt for major agent sessions.
- `templates/ai-red-team-plan.md` plans adversarial checks before risky AI workflows.
- `templates/feature-flag-kill-switch-plan.md` records rollout and rollback controls.
- `templates/supply-chain-baseline.md` captures release trust and dependency evidence.

These are optional until real usage proves they should become gates.

Workspace Efficiency templates:

- `templates/repo-manifest.md` records repo purpose, owner lane, gates, deploy target, evidence paths, and sensitivity rules.
- `templates/evidence-index.md` indexes latest verification receipts, proof packets, redaction state, CI runs, and deploys.
- `templates/decision-record.md` captures architecture, workflow, proof, dependency, and automation decisions.
- `templates/workspace-command-center-spec.md` scopes a future cross-repo command center before implementation.
- `templates/dependency-maintenance-plan.md` records Renovate/Dependabot grouping, schedule, and approval rules.
- `templates/dev-environment-baseline.md` records tool-version and setup expectations.
- `templates/ci-cache-plan.md` records cache keys, dependency paths, affected-only checks, and invalidation rules.
- `templates/project-starter-baseline.md` records the minimum baseline for new client/project repos.

These are optional until a real repo-manifest/evidence-index pilot proves they should become standards.
