# diagnose-to-plan

`dtp` is Toni Montez's local AI consulting harness. It turns rough diagnose notes, practice ideas, and operator context into durable repo artifacts.

Current branch target: `main`.

Canonical roadmap:

- `docs/PRACTICE_PRODUCTION_ROADMAP.md` is the source of truth for practice production work: hosted DTP, Practice OS, Client Operating Kits, redaction, COI, proof promotion, pilot sequencing, and parked ideas.
- `docs/DOCUMENTATION_MAP.md` explains which docs in DTP, consulting, and Hub own which decisions.
- `docs/PRACTICE_MACHINE_OPERATING_MAP.md` is the offer-led compression map for deciding which ideas are Now, Next, Later, or Hold across DTP, consulting, Hub, prompts, skills, and project repos.
- `docs/PRACTICE_ROADMAP_HORIZONS_2026.md` is the urgent/short/mid/long horizon overlay for deciding what to do now, what to improve next, and what remains gated.
- `docs/PRACTICE_KAIZEN_KANBAN_SYSTEM.md` is the DTP-first continuous-improvement loop for capturing and routing meaningful ideas, asks, blockers, proof candidates, repo issues, client signals, corrections, and process improvements.
- `docs/WORKSPACE_OPERATOR_RUNBOOK.md` names safe cross-repo command classes, repo ownership, verification paths, and no-touch boundaries.
- `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md` is the proof movement gate before any evidence, claim, screenshot, or metric becomes public.
- `docs/PRACTICE_THESIS_AND_OFFER_MAP.md` is the internal one-page thesis and offer map for deciding what the current pilots prove before public copy changes.
- `docs/OFFER_LED_PRACTICE_PACKAGING.md` defines the first internal offer packaging source for later consulting-site copy.
- `docs/CLIENT_COMMAND_ROOM_PATTERN.md` captures the reusable admin/customer portal concept from the DeMario pickleball admin portal for Toni and future client engagements.
- `docs/CLI_VERIFICATION_AUTOMATION_PATTERN.md` captures the Omnexus-style CLI verification, support, and evidence pattern that should come before heavier hosted product work.
- `docs/MOBILE_APP_REVIEW_AND_LAUNCH_PATTERN.md` captures the Omnexus App Store approval journey as a reusable mobile app review, approval, and first-user launch pattern for future client builds.
- `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md` is the implementation handoff for the separate `tm-skills` repo, which will own reusable cross-repo software-development Skills.

Current scope:

- `dtp draft` turns diagnose notes into draft SOW markdown
- `dtp skills --validate` validates local skills
- `dtp note`, `dtp story`, and `dtp mentor` capture practice context without an agent call
- `dtp index`, `dtp detect`, `dtp lesson`, `dtp recall`, and `dtp synthesize` power Extract Through Synthesis
- `dtp kit`, `dtp redact`, and `dtp practice doctor` power the Practice OS + Client Operating Kit workflow
- `dtp kaizen capture/update/status/mirror --dry-run` powers the lightweight intake/index loop before ideas become backlog stories, steward receipts, proof packets, engagement kits, or Notion mirror rows
- `dtp workspace report` powers the read-only Workspace Command Center V0 report from DTP-owned manifests, evidence indexes, backlog docs, and blockers
- `dtp web` opens a local DTP Workbench UI over the same markdown artifacts
- `dtp vault` gives private `engagements/` artifacts their own git-backed durability path
- `voice`, `pricing`, and `sow` stay valid placeholder skills for Toni to author
- Client Command Room fit/spec templates live in `practice-os/templates/` for owner operating rooms that are justified by recurring workflow pain
- Mobile app review journey templates live in `practice-os/templates/` for future App Store, Play Console, approval closeout, and first-72-hour launch work

## Local Workbench And Private Vault

DTP currently has a local UI backed by the existing markdown contracts. The production roadmap now points toward a hosted private DTP app with Supabase Auth/RLS/storage, while this local Workbench remains the fallback, prototype, and import/export surface:

```powershell
.\.venv\Scripts\python.exe -m dtp web
```

The workbench runs on `http://127.0.0.1:8765`, creates kits, shows readiness, runs redaction checks, and displays Practice OS health. It does not expose private client material to the public consulting site and should not be deployed as-is without hosted auth/storage work.

For permanent private artifacts, initialize a separate git vault inside the ignored `engagements/` directory:

```powershell
.\.venv\Scripts\python.exe -m dtp vault status
.\.venv\Scripts\python.exe -m dtp vault init
.\.venv\Scripts\python.exe -m dtp vault snapshot -m "Snapshot nonprofit site-rebuild kit"
```

Add a private remote later with `dtp vault init --remote <private-git-url>`, then use `dtp vault snapshot --push`. Keep the main DTP repo for reusable code, policies, templates, and reviewed patterns; keep the vault for private engagement records.

## Practice OS + Client Operating Kits

`practice-os/` is the committed Practice Brain: reusable policies, templates, operator Skills, and reviewed Bottleneck Patterns. It must not contain client-private details.

`engagements/` is the local private work area for client kits and is gitignored except for its README.

```powershell
.\.venv\Scripts\python.exe -m dtp practice doctor
.\.venv\Scripts\python.exe -m dtp kit new mom-nonprofit --project site-rebuild --kind launch
.\.venv\Scripts\python.exe -m dtp kit status mom-nonprofit
.\.venv\Scripts\python.exe -m dtp redact check practice-os --profile practice
.\.venv\Scripts\python.exe -m dtp redact check engagements/mom-nonprofit/site-rebuild/case-study/redacted.md --profile case-study
```

Use `extracts/` for raw pattern extraction. Promote only redacted, reviewed judgment into `practice-os/patterns/`.

Use Kaizen capture before relying on chat memory for meaningful new work:

```powershell
.\.venv\Scripts\python.exe -m dtp kaizen capture "New idea or request"
.\.venv\Scripts\python.exe -m dtp kaizen update kzn-YYYYMMDD-slug-hash --status now
.\.venv\Scripts\python.exe -m dtp kaizen status
.\.venv\Scripts\python.exe -m dtp kaizen mirror --dry-run
```

## Extract Through Synthesis

The extraction loop now runs through synthesis. It indexes repo shape, captures constrained pattern candidates, records human-readable lessons/decisions, searches the markdown/JSON extract store, and groups proven-looking sources into synthesis docs. It does not scaffold new client work yet.

```powershell
.\.venv\Scripts\python.exe -m dtp index consulting
.\.venv\Scripts\python.exe -m dtp index --all
.\.venv\Scripts\python.exe -m dtp detect consulting --signal admin-surface
.\.venv\Scripts\python.exe -m dtp lesson consulting --pattern admin-surface --from docs/BUILD_SPEC_EXTRACT_REVIEW.md
.\.venv\Scripts\python.exe -m dtp recall admin --type pattern --json --rebuild-index
.\.venv\Scripts\python.exe -m dtp synthesize --no-confirm
```

Extracts live under `extracts/`:

- `extracts/index/` stores deterministic repo fingerprints.
- `extracts/patterns/` stores detector output with file citations and review flags.
- `extracts/lessons/` stores lessons and decisions with optional source material.
- `extracts/synthesis/` stores grouped pattern memory used by `skills/build-patterns`.
- `extracts/.recall.db` is a local SQLite cache and is intentionally gitignored.

Detector rules are intentionally narrow: it reads only indexed signal files, embeds file slices into the prompt, requires path citations, computes confidence in the wrapper, and leaves `promoted: false` plus `private_review_required: true` until the pattern has been reviewed.

Synthesis docs also start as `promoted: false`. They are planning memory, not scaffolding instructions. The `build-patterns` skill points `dtp draft` at synthesis docs so future scopes can cite prior work by path.

Run the local checks:

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m dtp skills --validate
.\.venv\Scripts\python.exe -m dtp draft inputs/fixture-diagnose.md --output outputs/fixture-review.md
.\.venv\Scripts\python.exe -m dtp workspace report
.\.venv\Scripts\python.exe -m dtp index --all
.\.venv\Scripts\python.exe -m dtp synthesize --no-confirm
.\.venv\Scripts\python.exe -m dtp practice doctor
```
