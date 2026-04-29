from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pytest

from dtp.config import DtpConfig
from dtp.extract.indexer import ExtractError, index_repos


def test_fixture_repo_indexing_writes_json_and_markdown(tmp_path: Path) -> None:
    config = _config(tmp_path)
    repo = tmp_path / "fixture-site"
    (repo / "src" / "pages").mkdir(parents=True)
    (repo / "package.json").write_text('{"dependencies":{"astro":"latest"}}\n', encoding="utf-8")
    (repo / "src" / "pages" / "admin.astro").write_text(
        "const runbookItems = [];\n<section>Admin command room</section>\n",
        encoding="utf-8",
    )
    (repo / ".playwright-mcp").mkdir()
    (repo / ".playwright-mcp" / "page.yml").write_text(
        "url: http://127.0.0.1/admin\ntext: generated admin snapshot\n",
        encoding="utf-8",
    )
    _workspace(config, "fixture-site", repo)

    (result,) = index_repos(
        config=config,
        repo="fixture-site",
        clock=datetime(2026, 4, 28, tzinfo=UTC),
    )

    assert result.repo_slug == "fixture-site"
    assert result.json_path.exists()
    assert result.markdown_path.exists()
    assert result.fingerprint["stack"]["frameworks"] == ["Astro"]
    admin_signal = next(
        signal for signal in result.fingerprint["signals"] if signal["name"] == "admin-surface"
    )
    assert not any(path.startswith(".playwright-mcp/") for path in admin_signal["files"])


def test_index_invalid_repo_raises_extract_error(tmp_path: Path) -> None:
    config = _config(tmp_path)
    _workspace(config, "fixture-site", tmp_path / "fixture-site")

    with pytest.raises(ExtractError, match="unknown repo"):
        index_repos(config=config, repo="missing")


def _config(root: Path) -> DtpConfig:
    return DtpConfig(
        repo_root=root,
        inputs_dir=root / "inputs",
        outputs_dir=root / "outputs",
        skills_dir=root / "skills",
        extracts_dir=root / "extracts",
        practice_os_dir=root / "practice-os",
        engagements_dir=root / "engagements",
        workspace_file=root / ".dtp" / "workspace.yaml",
        agent_enabled=False,
    )


def _workspace(config: DtpConfig, name: str, repo: Path) -> None:
    config.workspace_file.parent.mkdir(parents=True, exist_ok=True)
    config.workspace_file.write_text(
        f"repos:\n  - name: {name}\n    path: {repo}\n    access: read\n",
        encoding="utf-8",
    )
