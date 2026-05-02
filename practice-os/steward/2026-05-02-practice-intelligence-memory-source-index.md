---
data_class: P0
confidential: false
permission_level: internal_only
review_status: checked
---

# Memory Source Index: Practice Intelligence Control Plane

Date: 2026-05-02

## Topic

- Name: Practice Intelligence Control Plane
- Why it matters: broad sessions now span clients, project repos, Notion,
  Gmail, Calendar, QuickBooks ideas, public assistants, source docs, and
  memory/persistence decisions.
- Owner: `diagnose-to-plan`
- Status: active V0 operating layer

## Authoritative Sources

| Topic | Path / pointer | Authority | Sensitivity | Last verified | Refresh command |
|---|---|---|---|---|---|
| Control plane | `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md` | source_of_truth | internal | 2026-05-02 | `Get-Content docs\PRACTICE_INTELLIGENCE_CONTROL_PLANE.md` |
| Memory rules | `docs/PRACTICE_MEMORY_CONTROL_PLANE.md` | source_of_truth | internal | 2026-05-02 | `Get-Content docs\PRACTICE_MEMORY_CONTROL_PLANE.md` |
| Rehydration ladder | `docs/PRACTICE_MEMORY_OPTIMIZATION_PLAN.md` | source_of_truth | internal | 2026-05-02 | `Get-Content docs\PRACTICE_MEMORY_OPTIMIZATION_PLAN.md` |
| Tool review | `docs/PRACTICE_TOOLING_STEWARD.md` | source_of_truth | internal | 2026-05-02 | `Get-Content docs\PRACTICE_TOOLING_STEWARD.md` |
| Notion cockpit | `docs/NOTION_MIRROR_V0.md` | source_of_truth | internal | 2026-05-02 | `Get-Content docs\NOTION_MIRROR_V0.md` |
| Client replies | `docs/CLIENT_REPLY_INTAKE_OPERATING_PATTERN.md` | source_of_truth | internal/private boundary | 2026-05-02 | `Get-Content docs\CLIENT_REPLY_INTAKE_OPERATING_PATTERN.md` |
| Cadence | `docs/RECURRING_CLIENT_CADENCE_OPERATING_PATTERN.md` | source_of_truth | internal/private boundary | 2026-05-02 | `Get-Content docs\RECURRING_CLIENT_CADENCE_OPERATING_PATTERN.md` |
| Assistant boundary | `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md` | source_of_truth | internal | 2026-05-02 | `Get-Content docs\CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md` |
| Consulting assistant manifest | `docs/assistant-manifests/consulting-public-v0.md` | source_of_truth | internal | 2026-05-02 | `Get-Content docs\assistant-manifests\consulting-public-v0.md` |
| Cam client state | `engagements/cameron-mckesson/` | private source_of_truth | private-client | 2026-05-02 | `dtp kit status cameron-mckesson` |
| Greg client state | `engagements/greg-thegrantapp/` | private source_of_truth | private-client | 2026-05-02 | `dtp kit status greg-thegrantapp` |
| CCAAP client state | `engagements/mom-nonprofit/` | private source_of_truth | private-client | 2026-05-02 | `dtp kit status mom-nonprofit` |
| Roadmap/Kanban | `docs/ROADMAP_EXECUTION_BACKLOG.md` | source_of_truth | internal | 2026-05-02 | `rg -n "Current Active Next Queue|Business Brain" docs\ROADMAP_EXECUTION_BACKLOG.md` |
| Evidence | `practice-os/efficiency/diagnose-to-plan-evidence-index.md` | source_of_truth | internal | 2026-05-02 | `Get-Content practice-os\efficiency\diagnose-to-plan-evidence-index.md` |

## Drift Risks

| Risk | Likelihood | Refresh trigger | Owner |
|---|---|---|---|
| Gmail reply state changes after a status snapshot | high | before changing waiting state, calendar, build scope, or proof posture | Codex/Toni |
| Calendar cadence gets scheduled manually | medium | before saying no meeting exists or creating invites | Codex/Toni |
| Notion cockpit drifts from DTP | medium | before relying on phone-visible status | Codex/Toni |
| QuickBooks connector docs or scopes change | medium | before any OAuth/app setup | Toni/Codex |
| Assistant manifest no longer matches consulting public site routes | medium | before assistant runtime work | Codex |
| Private engagement kits are ignored and not visible in git status | medium | before client action or proof claims | Codex |

## Retrieval Notes

- Best search terms: `Practice Intelligence Control Plane`, `Business Brain`,
  `Tooling Steward`, `QuickBooks`, `Notion`, `Client Reply Intake`,
  `consulting-public-v0`, `Memory Review Queue`.
- Useful commands:
  - `dtp workspace report`
  - `dtp kit status cameron-mckesson`
  - `dtp kit status greg-thegrantapp`
  - `dtp kit status mom-nonprofit`
  - `rg -n "Practice Intelligence|Tooling Steward|QuickBooks|assistant" docs practice-os`
- Known false lead: Notion has useful views but is not authoritative.
- Known false lead: source docs and starter SQL are additive strategy, not
  migrations or implementation overrides.

## Promotion Rule

When this topic changes materially, update:

- Source-of-truth doc: `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md`
- Roadmap/backlog: `docs/ROADMAP_EXECUTION_BACKLOG.md`
- Evidence index: `practice-os/efficiency/diagnose-to-plan-evidence-index.md`
- Notion mirror: sanitized Command Center status only
- Steward receipt: `practice-os/steward/YYYY-MM-DD-*.md`
