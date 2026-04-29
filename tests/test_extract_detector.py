from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import frontmatter

from dtp.config import DtpConfig
from dtp.extract.detector import (
    FileSlice,
    _prioritized_files,
    build_constrained_prompt,
    detect_signal,
)


def test_detector_writes_constrained_pattern_with_confidence(tmp_path: Path) -> None:
    config = _config(tmp_path)
    repo = tmp_path / "consulting"
    page_dir = repo / "src" / "pages"
    page_dir.mkdir(parents=True)
    files = []
    for name, marker in {
        "admin.astro": "commandLinks",
        "status.astro": "statusRows",
        "triage.astro": "triageRows",
        "runbook.astro": "runbookItems",
    }.items():
        path = page_dir / name
        path.write_text(
            f"const {marker} = [];\n"
            "ANTHROPIC_API_KEY=sk-ant-api03-secret\n"
            "<section>Admin dashboard</section>\n",
            encoding="utf-8",
        )
        files.append(path.relative_to(repo).as_posix())

    result = detect_signal(
        config=config,
        index={"repo_slug": "consulting", "repo_path": str(repo)},
        signal_data={
            "name": "admin-surface",
            "evidence": "Admin, console, or dashboard surface",
            "files": files,
        },
        clock=datetime(2026, 4, 28, tzinfo=UTC),
    )

    post = frontmatter.load(result.path)
    assert post.metadata["repo"] == "consulting"
    assert post.metadata["signal"] == "admin-surface"
    assert post.metadata["pattern_slug"] == "admin-command-room"
    assert post.metadata["confidence"] == "high"
    assert set(post.metadata["files_read"]) == set(files)
    assert post.metadata["promoted"] is False
    assert post.metadata["private_review_required"] is True
    assert "no filesystem tools" in post.content
    assert "src/pages/admin.astro:1-1" in post.content
    assert "sk-ant-api03-secret" not in post.content
    assert "[redacted secret-bearing line]" in post.content


def test_detector_prompt_embeds_only_file_slices() -> None:
    prompt = build_constrained_prompt(
        signal_name="admin-surface",
        evidence="Admin surface",
        slices=(
            FileSlice(
                path="src/pages/admin.astro",
                total_lines=2,
                included_ranges=((1, 2),),
                text="1: const commandLinks = [];\n2: const runbookItems = [];",
                truncated=False,
            ),
        ),
    )

    assert "no filesystem tools" in prompt
    assert "src/pages/admin.astro" in prompt
    assert "commandLinks" in prompt


def test_detector_prioritizes_admin_code_over_docs_and_tests() -> None:
    files = _prioritized_files(
        "admin-surface",
        [
            "SETUP.md",
            "api/_lib/console-store.test.ts",
            "api/console/dashboard.ts",
            "apps/web/src/App.tsx",
        ],
    )

    assert files[:2] == ["api/console/dashboard.ts", "apps/web/src/App.tsx"]
    assert files[-1] == "SETUP.md"


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
