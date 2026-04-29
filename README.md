# diagnose-to-plan

`dtp` is Toni Montez's local AI consulting harness. It turns rough diagnose notes, practice ideas, and operator context into durable repo artifacts.

Current branch target: `v2/harness`.

Current scope:

- `dtp draft` turns diagnose notes into draft SOW markdown
- `dtp skills --validate` validates local skills
- `dtp note`, `dtp story`, and `dtp mentor` capture practice context without an agent call
- `dtp index`, `dtp detect`, `dtp lesson`, `dtp recall`, and `dtp synthesize` power Extract Through Synthesis
- `dtp kit`, `dtp redact`, and `dtp practice doctor` power the Practice OS + Client Operating Kit workflow
- `dtp web` opens a local DTP Workbench UI over the same markdown artifacts
- `dtp vault` gives private `engagements/` artifacts their own git-backed durability path
- `voice`, `pricing`, and `sow` stay valid placeholder skills for Toni to author

## Local Workbench And Private Vault

DTP can have a UI without becoming a hosted SaaS. The first full-stack move is a local browser workbench backed by the existing markdown contracts:

```powershell
.\.venv\Scripts\python.exe -m dtp web
```

The workbench runs on `http://127.0.0.1:8765`, creates kits, shows readiness, runs redaction checks, and displays Practice OS health. It does not expose private client material to the public consulting site.

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
.\.venv\Scripts\python.exe -m dtp index --all
.\.venv\Scripts\python.exe -m dtp synthesize --no-confirm
.\.venv\Scripts\python.exe -m dtp practice doctor
```
