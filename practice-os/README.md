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

Business Brain:

- `../docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md` is the normalized source map for
  the Business Brain / Consulting OS.
- `commands/` stores command contracts such as `/diagnose-prospect`,
  `/coi-screen`, `/draft-proposal`, and `/comms-kit` before any automation is
  implemented.
- `agents/` stores draft-producing role specs such as Controller, General
  Counsel, and COO. These are not autonomous actors.
- `fixtures/business-brain/` stores reusable internal fixtures for Greg,
  Cameron, and Mom/Mario. Live private work stays in `engagements/`.
- `comms/` stores private-first communication drafts, visual briefs, diagrams,
  slide outlines, and social candidates with public review gates.

Kaizen Kanban:

- `../docs/PRACTICE_KAIZEN_KANBAN_SYSTEM.md` is the operating contract for
  capture, classification, routing, staging, execution, verification, recording,
  and improvement.
- `kaizen/intake.jsonl` is the compact machine-readable index for meaningful
  new ideas, asks, blockers, proof candidates, repo issues, client signals,
  corrections, and process improvements.
- Use `dtp kaizen capture`, `dtp kaizen status`, and
  `dtp kaizen mirror --dry-run` before relying on chat memory or Notion as the
  active queue.
- Notion remains a sanitized mirror. Private-client, COI-gated, secret, raw
  transcript, payment, DSE, and unreviewed proof material stays out of mirror
  payloads.

Activation routing:

- `templates/activation-routing-map.md` maps prompt shapes to the right `tm-skills` skill, DTP Practice OS skill, template, roadmap lane, proof gate, COI gate, research/eval artifact, repo touch pass, or parked automation path.
- `../docs/CONTEXTUAL_ACTIVATION_PLAYBOOK.md` and `templates/contextual-idea-intake.md` progressively classify new ideas, designs, development enhancements, project work, business moves, proof candidates, research items, and automation concepts before they become stories or implementation.
- `../docs/ROADMAP_STORY_ACTIVATION_INDEX.md` maps roadmap epics/stories to the skills, templates, suggested agent roles, and gates that should activate when that story is in play.
- `templates/story-activation-contract.md` captures a one-off story activation record when a backlog item needs a more explicit skill/agent/gate contract.

Agent Squads + Knowledge Base:

- `../docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` is the canonical DTP-owned
  operating model for human-led Delivery and Business Justification squads.
- `templates/agent-squad-charter.md` names squad mission, scope, roles, and
  gates.
- `templates/knowledge-scope-source-index.md` records authoritative sources,
  blocked sources, freshness, and drift risk.
- `templates/business-justification-scorecard.md` answers the operator problem,
  why now, evidence, simpler alternative, value, and approval questions.
- `templates/approval-gate.md` records `required_approver`,
  `approval_state`, scope, evidence, and stop conditions.
- `templates/squad-handoff-receipt.md` ties story activation, squad ownership,
  decisions, verification, gates, and next action together.

These are manual V0 contracts. They do not authorize autonomous agents,
framework installs, public proof, client communication, production writes, or
repo mutation.

Command-room templates:

- `templates/client-command-room-fit-assessment.md` decides whether to build a command room, use a handoff checklist, skip the private surface, or defer.
- `templates/client-command-room-spec.md` defines owner dashboard, owner tasks, business roadmap, developer roadmap, handoff/rules, and placeholder-only support/verification surfaces.

Roadmap stewardship template:

- `templates/roadmap-steward-review.md` keeps roadmap execution, repo coverage, active-next decisions, idea capture, and process compliance out of chat memory and inside reviewable artifacts.
- `steward/` stores live Roadmap Steward receipts created from the activation map and steward review template.

Proof and redaction templates:

- `templates/proof-packet.md` captures baseline, after-state, evidence, caveat, permission, redaction, reviewer, and publish decision.
- `templates/redaction-queue-item.md` captures a review item before private material can move toward proof.
- `templates/permission-reviewer-checklist.md` records permission and reviewer gates.
- `templates/evidence-source-checklist.md` checks whether evidence is good enough to support a proof claim.
- `templates/public-claim-review.md` keeps public wording evidence-backed and caveated.
- `policies/authentic-voice-and-anti-slop.md` is the canonical voice standard for clear, specific, believable public/proof/client/planning language.
- `templates/copy-authenticity-audit.md` reviews public copy, client communication, proof language, assistant answers, and durable planning artifacts before promotion.
- `templates/asset-inventory.md` tracks screenshots, documents, walkthroughs, and other proof assets.

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

Workspace Efficiency pilots:

- `efficiency/diagnose-to-plan-repo-manifest.md` is the first repo manifest pilot.
- `efficiency/diagnose-to-plan-evidence-index.md` is the first evidence index pilot.

These are planning receipts, not runtime configuration.
