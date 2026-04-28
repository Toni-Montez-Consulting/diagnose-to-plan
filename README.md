# diagnose-to-plan

`dtp` is Toni Montez's local AI consulting harness. It turns rough diagnose notes, practice ideas, and operator context into durable repo artifacts.

Current branch target: `v2/harness`.

Phase 1 scope:

- scaffold the repo structure from `docs/build-spec-v2.md`
- expose `dtp draft`
- expose `dtp skills --validate`
- keep `voice`, `pricing`, and `sow` as valid placeholder skills for Toni to author

Run the local checks:

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m dtp skills --validate
.\.venv\Scripts\python.exe -m dtp draft inputs/fixture-diagnose.md --output outputs/fixture-review.md
```

Do not build Phase 2 commands until Phase 1 is merged into `v2/harness` and Toni confirms the next move.
