from __future__ import annotations

from pathlib import Path

from dtp.extract.signals import detect_signals, signal_names


def test_signal_names_include_core_extract_contract() -> None:
    names = set(signal_names())

    assert {
        "admin-surface",
        "web-routes",
        "component-library",
        "design-tokens",
        "api-surface",
        "auth-system",
        "db-migrations",
        "agent-runtime",
        "prompt-registry",
        "mcp-config",
        "permission-tiers",
    }.issubset(names)


def test_signal_matching_finds_admin_surface_and_web_routes(tmp_path: Path) -> None:
    repo = tmp_path / "site"
    pages = repo / "src" / "pages"
    pages.mkdir(parents=True)
    admin = pages / "admin.astro"
    admin.write_text(
        "const commandLinks = [];\nconst statusRows = [];\n<section>Admin dashboard</section>\n",
        encoding="utf-8",
    )

    files = tuple(repo.rglob("*"))
    hits = {hit.name: hit for hit in detect_signals(repo, files)}

    assert "admin-surface" in hits
    assert "web-routes" in hits
    assert "src/pages/admin.astro" in hits["admin-surface"].files
