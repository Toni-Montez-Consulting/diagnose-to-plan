# diagnose-to-plan

`dtp` is Toni Montez's local AI consulting harness. It turns rough diagnose notes, practice ideas, and operator context into durable repo artifacts.

Current branch target: `v2/harness`.

Current scope:

- `dtp draft` turns diagnose notes into draft SOW markdown
- `dtp skills --validate` validates local skills
- `dtp note`, `dtp story`, and `dtp mentor` capture practice context without an agent call
- `voice`, `pricing`, and `sow` stay valid placeholder skills for Toni to author

Run the local checks:

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m dtp skills --validate
.\.venv\Scripts\python.exe -m dtp draft inputs/fixture-diagnose.md --output outputs/fixture-review.md
```
