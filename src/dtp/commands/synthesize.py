from __future__ import annotations

from dtp.config import DtpConfig
from dtp.extract.synthesizer import SynthesisResult, synthesize


def run_synthesize(
    *,
    config: DtpConfig,
    kind: str | None = None,
    regroup: bool = False,
    no_confirm: bool = False,
) -> tuple[SynthesisResult, ...]:
    return synthesize(
        config=config,
        kind=kind,
        regroup=regroup,
        no_confirm=no_confirm,
    )
