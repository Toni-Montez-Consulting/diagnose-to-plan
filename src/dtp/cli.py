from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from dtp.commands.capture_cmd import run_mentor, run_note, run_story
from dtp.commands.detect import run_detect
from dtp.commands.draft import run_draft, user_facing_error
from dtp.commands.index_cmd import run_index
from dtp.commands.kit import KIT_KINDS, KitError, render_status, run_kit_new, run_kit_status
from dtp.commands.lesson import run_lesson
from dtp.commands.practice import render_doctor, run_practice_doctor
from dtp.commands.recall import run_recall
from dtp.commands.redact import REDACT_PROFILES, RedactionError, run_redact_check
from dtp.commands.skills_cmd import run_validate
from dtp.commands.synthesize import run_synthesize
from dtp.config import load_config
from dtp.extract.indexer import ExtractError
from dtp.extract.recall import RecallResult
from dtp.skills_loader import SkillValidationError

app = typer.Typer(no_args_is_help=True, add_completion=False)
kit_app = typer.Typer(no_args_is_help=True, add_completion=False)
redact_app = typer.Typer(no_args_is_help=True, add_completion=False)
practice_app = typer.Typer(no_args_is_help=True, add_completion=False)
console = Console()
app.add_typer(kit_app, name="kit")
app.add_typer(redact_app, name="redact")
app.add_typer(practice_app, name="practice")


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


@app.command("note")
def note_command(
    text: Annotated[str, typer.Argument(help="Journal note text.")],
    tag: Annotated[
        list[str] | None,
        typer.Option("--tag", help="Repeatable tag for the note."),
    ] = None,
) -> None:
    config = load_config()
    try:
        result = run_note(text, config, tags=tuple(tag or ()))
    except Exception as error:
        message, code = user_facing_error(error)
        console.print(f"[red]{message}[/red]")
        raise typer.Exit(code=code) from error
    console.print(f"[green]wrote[/green] {result.relative_path}")


@app.command("story")
def story_command(
    title: Annotated[str, typer.Argument(help="Omnexus story title.")],
    source: Annotated[
        Path | None,
        typer.Option("--from", help="Optional source file inside this repo."),
    ] = None,
) -> None:
    config = load_config()
    try:
        result = run_story(title, config, source=source)
    except Exception as error:
        message, code = user_facing_error(error)
        console.print(f"[red]{message}[/red]")
        raise typer.Exit(code=code) from error
    console.print(f"[green]wrote[/green] {result.relative_path}")


@app.command("mentor")
def mentor_command(
    what: Annotated[str, typer.Argument(help="Decision or question for the mentor log.")],
    mentor: Annotated[
        str | None,
        typer.Option("--mentor", help="Mentor name to record."),
    ] = None,
    source: Annotated[
        Path | None,
        typer.Option("--from", help="Optional source file inside this repo."),
    ] = None,
) -> None:
    config = load_config()
    try:
        result = run_mentor(what, config, mentor=mentor, source=source)
    except Exception as error:
        message, code = user_facing_error(error)
        console.print(f"[red]{message}[/red]")
        raise typer.Exit(code=code) from error
    console.print(f"[green]wrote[/green] {result.relative_path}")


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


@app.command("index")
def index_command(
    repo: Annotated[
        str | None,
        typer.Argument(help="Workspace repo slug/name to index. Omit with --all."),
    ] = None,
    all_repos: Annotated[
        bool,
        typer.Option("--all", help="Index every repo in .dtp/workspace.yaml."),
    ] = False,
) -> None:
    config = load_config()
    try:
        results = run_index(config=config, repo=repo, all_repos=all_repos or repo is None)
    except ExtractError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error

    for result in results:
        relative = result.markdown_path.relative_to(config.repo_root).as_posix()
        signals = len(result.fingerprint.get("signals", ()))
        console.print(
            f"[green]indexed[/green] {result.repo_slug} -> {relative} ({signals} signals)"
        )


@app.command("detect")
def detect_command(
    repo: Annotated[str, typer.Argument(help="Workspace repo slug/name to inspect.")],
    signal: Annotated[
        str | None,
        typer.Option("--signal", help="Signal name to detect, such as admin-surface."),
    ] = None,
    all_signals: Annotated[
        bool,
        typer.Option("--all-signals", help="Write pattern candidates for every indexed signal."),
    ] = False,
    force: Annotated[
        bool,
        typer.Option("--force", help="Overwrite an existing pattern candidate."),
    ] = False,
) -> None:
    config = load_config()
    try:
        results = run_detect(
            config=config,
            repo=repo,
            signal=signal,
            all_signals=all_signals,
            force=force,
        )
    except ExtractError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error

    for result in results:
        relative = result.path.relative_to(config.repo_root).as_posix()
        console.print(
            f"[green]detected[/green] {result.repo_slug}:{result.signal} "
            f"-> {relative} ({result.confidence})"
        )


@app.command("lesson")
def lesson_command(
    repo: Annotated[str, typer.Argument(help="Workspace repo slug/name for the lesson.")],
    pattern: Annotated[
        str | None,
        typer.Option("--pattern", help="Pattern slug this lesson belongs to."),
    ] = None,
    kind: Annotated[
        str,
        typer.Option("--type", help="Record type: lesson or decision."),
    ] = "lesson",
    source: Annotated[
        Path | None,
        typer.Option("--from", help="Optional source file from DTP or the selected repo."),
    ] = None,
) -> None:
    config = load_config()
    try:
        destination = run_lesson(
            config=config,
            repo=repo,
            pattern=pattern,
            kind=kind,
            source=source,
        )
    except ExtractError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error

    console.print(f"[green]wrote[/green] {destination.relative_to(config.repo_root).as_posix()}")


@app.command("recall")
def recall_command(
    query: Annotated[str, typer.Argument(help="Search query for stored extracts.")],
    repo: Annotated[
        str | None,
        typer.Option("--repo", help="Limit recall to one repo slug."),
    ] = None,
    kind: Annotated[
        str | None,
        typer.Option("--type", help="Filter by index, pattern, lesson, or decision."),
    ] = None,
    since: Annotated[
        str | None,
        typer.Option("--since", help="Filter items created on/after YYYY-MM-DD."),
    ] = None,
    json_output: Annotated[
        bool,
        typer.Option("--json", help="Print machine-readable JSON results."),
    ] = False,
    rebuild_index: Annotated[
        bool,
        typer.Option("--rebuild-index", help="Rebuild extracts/.recall.db before searching."),
    ] = False,
) -> None:
    config = load_config()
    try:
        output = run_recall(
            config=config,
            query=query,
            repo=repo,
            kind=kind,
            since=since,
            json_output=json_output,
            rebuild_index=rebuild_index,
        )
    except ExtractError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error

    if isinstance(output, str):
        console.print(output, end="")
        return

    for result in output:
        _print_recall_result(config.repo_root, result)
    if not output:
        console.print("No extracts matched.")


@app.command("synthesize")
def synthesize_command(
    kind: Annotated[
        str | None,
        typer.Option("--type", help="Limit sources to pattern, lesson, or decision."),
    ] = None,
    regroup: Annotated[
        bool,
        typer.Option("--regroup", help="Regenerate grouping metadata."),
    ] = False,
    no_confirm: Annotated[
        bool,
        typer.Option("--no-confirm", help="Mark the run as intentionally non-interactive."),
    ] = False,
) -> None:
    config = load_config()
    try:
        results = run_synthesize(
            config=config,
            kind=kind,
            regroup=regroup,
            no_confirm=no_confirm,
        )
    except ExtractError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error

    for result in results:
        relative = result.path.relative_to(config.repo_root).as_posix()
        console.print(
            f"[green]synthesized[/green] {result.group} -> {relative} "
            f"({result.source_count} sources, canonical: {result.canonical_repo})"
        )


@kit_app.command("new")
def kit_new_command(
    client: Annotated[str, typer.Argument(help="Client slug or name.")],
    project: Annotated[
        str,
        typer.Option("--project", help="Engagement/project slug."),
    ],
    kind: Annotated[
        str,
        typer.Option("--kind", help=f"One of: {', '.join(sorted(KIT_KINDS))}."),
    ] = "launch",
) -> None:
    config = load_config()
    try:
        result = run_kit_new(config=config, client=client, project=project, kind=kind)
    except KitError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error

    relative = result.root.relative_to(config.repo_root).as_posix()
    console.print(
        f"[green]kit[/green] {result.client_id}/{result.engagement_id} -> {relative} "
        f"({len(result.created)} created, {len(result.existing)} existing)"
    )


@kit_app.command("status")
def kit_status_command(
    client: Annotated[
        str | None,
        typer.Argument(help="Optional client slug/name."),
    ] = None,
) -> None:
    config = load_config()
    try:
        statuses = run_kit_status(config=config, client=client)
    except KitError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    if not statuses:
        console.print("No engagement kits found.")
        return
    console.print(render_status(statuses, config.repo_root), end="")


@redact_app.command("check")
def redact_check_command(
    path: Annotated[Path, typer.Argument(help="Markdown file or directory to scan.")],
    profile: Annotated[
        str,
        typer.Option("--profile", help=f"One of: {', '.join(sorted(REDACT_PROFILES))}."),
    ] = "practice",
) -> None:
    config = load_config()
    try:
        findings = run_redact_check(config=config, path=path, profile=profile)
    except RedactionError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error

    if not findings:
        console.print("[green]redaction check passed[/green]")
        return

    for finding in findings:
        relative = finding.path.relative_to(config.repo_root).as_posix()
        console.print(f"[red]finding[/red] {relative}: {finding.message}")
    raise typer.Exit(code=2)


@practice_app.command("doctor")
def practice_doctor_command() -> None:
    config = load_config()
    result = run_practice_doctor(config)
    console.print(render_doctor(result), end="")
    if not result.ok:
        raise typer.Exit(code=1)


def _print_recall_result(repo_root: Path, result: RecallResult) -> None:
    path = result.path.relative_to(repo_root).as_posix()
    console.print(
        f"[green]{result.type}[/green] {result.repo} "
        f"[dim]score={result.score}[/dim] {path}\n{result.title}\n{result.snippet}\n"
    )


def main() -> None:
    app()
