# Extracts

This directory is Toni's reusable build-pattern library.

- `index/` contains deterministic repo fingerprints.
- `patterns/` contains grounded pattern candidates from indexed signal files.
- `lessons/` contains human-reviewed lessons and decisions.

Everything here is committed except `.recall.db`, which is a local SQLite cache rebuilt by `dtp recall --rebuild-index`.
