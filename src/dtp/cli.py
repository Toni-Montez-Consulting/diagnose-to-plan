from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from dtp.commands.draft import run_draft, user_facing_error
from dtp.commands.skills_cmd import run_validate
from dtp.config import load_config
from dtp.skills_loader import SkillValidationError

app = typer.Typer(no_args_is_help=True, add_completion=False)
console = Console()


@app.command("draft")
def draft_command(
    input_path: Annotated[Path, typer.Argument(help="Diagnose note to turn into a draft SOW.")],
    client: Annotated[
        str | None,
        typer.Option("--client", help="Client slug for clients/<name>/sow.md."),
    ] = None,
    deep: Annotated[bool, typer.Option("--deep", help="Use the deeper draft model.")] = False,
    skip_coi: Annotated[
        bool,
        typer.Option("--skip-coi", help="Mark COI as skipped in output."),
    ] = False,
    out: Annotated[
        Path | None,
        typer.Option("--out", "--output", help="Output path inside this repo."),
    ] = None,
) -> None:
    config = load_config()
    try:
        destination = run_draft(
            input_path=input_path,
            config=config,
            client=client,
            deep=deep,
            skip_coi=skip_coi,
            out=out,
        )
    except Exception as error:
        message, code = user_facing_error(error)
        console.print(f"[red]{message}[/red]")
        raise typer.Exit(code=code) from error

    console.print(f"[green]wrote[/green] {destination.relative_to(config.repo_root)}")


@app.command("skills")
def skills_command(
    validate: Annotated[
        bool,
        typer.Option("--validate", help="Validate every skills/*/SKILL.md file."),
    ] = False,
) -> None:
    config = load_config()
    if not validate:
        console.print("Use --validate to validate skills.")
        return
    try:
        skills = run_validate(config)
    except SkillValidationError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    for skill in skills:
        console.print(f"[green]ok[/green] {skill.name}")
    console.print(f"validated {len(skills)} skills")


def main() -> None:
    app()
