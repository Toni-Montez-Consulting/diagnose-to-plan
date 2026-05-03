from __future__ import annotations

from dtp.config import DtpConfig
from dtp.extract.recall import RecallResult, recall, results_to_json, validate_kind


def run_recall(
    *,
    config: DtpConfig,
    query: str,
    repo: str | None = None,
    kind: str | None = None,
    since: str | None = None,
    json_output: bool = False,
    rebuild_index: bool = False,
) -> str | tuple[RecallResult, ...]:
    validate_kind(kind)
    results = recall(
        config=config,
        query=query,
        repo=repo,
        kind=kind,
        since=since,
        rebuild_index=rebuild_index,
    )
    if json_output:
        return results_to_json(results)
    return results
