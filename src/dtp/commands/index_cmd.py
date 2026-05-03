from __future__ import annotations

from dtp.config import DtpConfig
from dtp.extract.indexer import IndexResult, index_repos


def run_index(
    *,
    config: DtpConfig,
    repo: str | None = None,
    all_repos: bool = False,
) -> tuple[IndexResult, ...]:
    return index_repos(config=config, repo=repo, all_repos=all_repos)
