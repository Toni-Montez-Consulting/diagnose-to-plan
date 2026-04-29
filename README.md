# diagnose-to-plan

`dtp` is Toni Montez's local AI consulting harness. It turns rough diagnose notes, practice ideas, and operator context into durable repo artifacts.

Current branch target: `v2/harness`.

Current scope:

- `dtp draft` turns diagnose notes into draft SOW markdown
- `dtp skills --validate` validates local skills
- `dtp note`, `dtp story`, and `dtp mentor` capture practice context without an agent call
- `dtp index`, `dtp detect`, `dtp lesson`, `dtp recall`, and `dtp synthesize` power Extract Through Synthesis
- `dtp kit`, `dtp redact`, and `dtp practice doctor` power the Practice OS + Client Operating Kit workflow
- `voice`, `pricing`, and `sow` stay valid placeholder skills for Toni to author

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
