from __future__ import annotations

from dtp.config import DtpConfig
from dtp.extract.detector import DetectionResult, detect_patterns


def run_detect(
    *,
    config: DtpConfig,
    repo: str,
    signal: str | None = None,
    all_signals: bool = False,
    force: bool = False,
) -> tuple[DetectionResult, ...]:
    return detect_patterns(
        config=config,
        repo=repo,
        signal=signal,
        all_signals=all_signals,
        force=force,
    )
