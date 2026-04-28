from __future__ import annotations

from dtp.config import DtpConfig
from dtp.skills_loader import Skill, validate_skills


def run_validate(config: DtpConfig) -> tuple[Skill, ...]:
    return validate_skills(config.skills_dir)
