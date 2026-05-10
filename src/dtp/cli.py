from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from dtp.commands.capture_cmd import run_mentor, run_note, run_story
from dtp.commands.client_os import (
    ClientOsError,
    render_bridge_export,
    render_closeout,
    render_preflight,
    render_scaffold,
    run_client_os_bridge_export,
    run_client_os_closeout,
    run_client_os_preflight,
    run_client_os_scaffold,
    run_client_os_status,
)
from dtp.commands.client_os import (
    render_status as render_client_os_status,
)
from dtp.commands.detect import run_detect
from dtp.commands.draft import run_draft, user_facing_error
from dtp.commands.evolution import (
    EVOLUTION_KINDS,
    EvolutionError,
    render_evolution_new,
    render_evolution_status,
    run_evolution_dashboard,
    run_evolution_new,
    run_evolution_status,
)
from dtp.commands.index_cmd import run_index
from dtp.commands.kaizen import (
    KaizenError,
    render_capture,
    render_mirror,
    render_update,
    run_kaizen_capture,
    run_kaizen_mirror,
    run_kaizen_status,
    run_kaizen_update,
)
from dtp.commands.kaizen import (
    render_status as render_kaizen_status,
)
from dtp.commands.kit import KIT_KINDS, KitError, render_status, run_kit_new, run_kit_status
from dtp.commands.lesson import run_lesson
from dtp.commands.memory import (
    render_memory_status,
    render_memory_steward_review,
    run_memory_status,
    run_memory_steward_review,
)
from dtp.commands.practice import render_doctor, run_practice_doctor
from dtp.commands.recall import run_recall
from dtp.commands.redact import REDACT_PROFILES, RedactionError, run_redact_check
from dtp.commands.research import render_research_steward_review, run_research_steward_review
from dtp.commands.research_source_freshness import (
    ResearchSourceFreshnessError,
    render_source_freshness_dry_run,
    run_research_source_freshness_dry_run,
)
from dtp.commands.skills_cmd import run_validate
from dtp.commands.source_packs import (
    render_source_pack_validation,
    run_source_pack_validation,
)
from dtp.commands.synthesize import run_synthesize
from dtp.commands.vault import (
    VaultError,
    render_vault_status,
    run_vault_init,
    run_vault_snapshot,
    run_vault_status,
)
from dtp.commands.web import run_workbench_server
from dtp.commands.workspace_dashboard import (
    DashboardSurface,
    run_workspace_dashboard,
    run_workspace_dashboard_validation,
)
from dtp.commands.workspace_report import render_workspace_report, run_workspace_report
from dtp.commands.workspace_tasks import run_workspace_recover, run_workspace_task_add
from dtp.config import load_config
from dtp.extract.indexer import ExtractError
from dtp.extract.recall import RecallResult
from dtp.skills_loader import SkillValidationError

app = typer.Typer(no_args_is_help=True, add_completion=False)
kit_app = typer.Typer(no_args_is_help=True, add_completion=False)
redact_app = typer.Typer(no_args_is_help=True, add_completion=False)
practice_app = typer.Typer(no_args_is_help=True, add_completion=False)
practice_client_os_app = typer.Typer(no_args_is_help=True, add_completion=False)
practice_source_packs_app = typer.Typer(no_args_is_help=True, add_completion=False)
kaizen_app = typer.Typer(no_args_is_help=True, add_completion=False)
evolution_app = typer.Typer(no_args_is_help=True, add_completion=False)
memory_app = typer.Typer(no_args_is_help=True, add_completion=False)
research_app = typer.Typer(no_args_is_help=True, add_completion=False)
vault_app = typer.Typer(no_args_is_help=True, add_completion=False)
workspace_app = typer.Typer(no_args_is_help=True, add_completion=False)
workspace_task_app = typer.Typer(no_args_is_help=True, add_completion=False)
console = Console()
app.add_typer(kit_app, name="kit")
app.add_typer(redact_app, name="redact")
app.add_typer(practice_app, name="practice")
practice_app.add_typer(practice_client_os_app, name="client-os")
practice_app.add_typer(practice_source_packs_app, name="source-packs")
app.add_typer(kaizen_app, name="kaizen")
app.add_typer(evolution_app, name="evolution")
app.add_typer(memory_app, name="memory")
app.add_typer(research_app, name="research")
app.add_typer(vault_app, name="vault")
app.add_typer(workspace_app, name="workspace")
workspace_app.add_typer(workspace_task_app, name="task")


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


@practice_source_packs_app.command("validate")
def practice_source_packs_validate_command(
    path: Annotated[
        Path | None,
        typer.Option("--path", help="Optional source-pack path to validate."),
    ] = None,
) -> None:
    config = load_config()
    result = run_source_pack_validation(config, path=path)
    console.print(render_source_pack_validation(result, config.repo_root), end="")
    if not result.ok:
        raise typer.Exit(code=1)


@practice_client_os_app.command("preflight")
def practice_client_os_preflight_command(
    client: Annotated[str, typer.Argument(help="Client slug or name.")],
    engagement: Annotated[str, typer.Option("--engagement", help="Engagement/project slug.")],
    meeting_date: Annotated[str, typer.Option("--date", help="Meeting date as YYYY-MM-DD.")],
    profile: Annotated[
        str,
        typer.Option("--profile", help="Client OS profile: base, infra, or full."),
    ] = "base",
) -> None:
    config = load_config()
    try:
        result = run_client_os_preflight(
            config=config,
            client=client,
            engagement=engagement,
            meeting_date=meeting_date,
            profile=profile,
        )
    except ClientOsError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    console.print(render_preflight(result, config.repo_root), end="")
    if not result.ok:
        raise typer.Exit(code=1)


@practice_client_os_app.command("scaffold")
def practice_client_os_scaffold_command(
    client: Annotated[str, typer.Argument(help="Client slug or name.")],
    engagement: Annotated[str, typer.Option("--engagement", help="Engagement/project slug.")],
    meeting_date: Annotated[str, typer.Option("--date", help="Meeting date as YYYY-MM-DD.")],
    profile: Annotated[
        str,
        typer.Option("--profile", help="Client OS profile: base, infra, or full."),
    ] = "base",
    force: Annotated[
        bool,
        typer.Option("--force", help="Overwrite existing scaffold files."),
    ] = False,
) -> None:
    config = load_config()
    try:
        result = run_client_os_scaffold(
            config=config,
            client=client,
            engagement=engagement,
            meeting_date=meeting_date,
            profile=profile,
            force=force,
        )
    except ClientOsError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    console.print(render_scaffold(result, config.repo_root), end="")


@practice_client_os_app.command("status")
def practice_client_os_status_command(
    client: Annotated[str, typer.Argument(help="Client slug or name.")],
    engagement: Annotated[str, typer.Option("--engagement", help="Engagement/project slug.")],
    meeting_date: Annotated[str, typer.Option("--date", help="Meeting date as YYYY-MM-DD.")],
    profile: Annotated[
        str,
        typer.Option("--profile", help="Client OS profile: base, infra, or full."),
    ] = "full",
    json_output: Annotated[
        bool,
        typer.Option("--json", help="Print machine-readable cockpit output."),
    ] = False,
) -> None:
    config = load_config()
    try:
        result = run_client_os_status(
            config=config,
            client=client,
            engagement=engagement,
            meeting_date=meeting_date,
            profile=profile,
        )
    except ClientOsError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    if json_output:
        typer.echo(json.dumps(result.to_dict(config.repo_root), indent=2, sort_keys=True))
        return
    console.print(render_client_os_status(result, config.repo_root), end="")


@practice_client_os_app.command("closeout")
def practice_client_os_closeout_command(
    client: Annotated[str, typer.Argument(help="Client slug or name.")],
    engagement: Annotated[str, typer.Option("--engagement", help="Engagement/project slug.")],
    meeting_date: Annotated[str, typer.Option("--date", help="Meeting date as YYYY-MM-DD.")],
    json_output: Annotated[
        bool,
        typer.Option("--json", help="Print machine-readable closeout output."),
    ] = False,
) -> None:
    config = load_config()
    try:
        result = run_client_os_closeout(
            config=config,
            client=client,
            engagement=engagement,
            meeting_date=meeting_date,
        )
    except ClientOsError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    if json_output:
        typer.echo(json.dumps(result.to_dict(config.repo_root), indent=2, sort_keys=True))
    else:
        console.print(render_closeout(result, config.repo_root), end="")
    if not result.ok:
        raise typer.Exit(code=1)


@practice_client_os_app.command("bridge-export")
def practice_client_os_bridge_export_command(
    client: Annotated[str, typer.Argument(help="Client slug or name.")],
    engagement: Annotated[str, typer.Option("--engagement", help="Engagement/project slug.")],
    meeting_date: Annotated[str, typer.Option("--date", help="Meeting date as YYYY-MM-DD.")],
    json_output: Annotated[
        bool,
        typer.Option("--json", help="Print machine-readable dry-run bridge output."),
    ] = False,
) -> None:
    config = load_config()
    try:
        result = run_client_os_bridge_export(
            config=config,
            client=client,
            engagement=engagement,
            meeting_date=meeting_date,
        )
    except ClientOsError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    if json_output:
        typer.echo(json.dumps(result.to_dict(config.repo_root), indent=2, sort_keys=True))
    else:
        console.print(render_bridge_export(result, config.repo_root), end="")
    if not result.ok:
        raise typer.Exit(code=1)


@kaizen_app.command("capture")
def kaizen_capture_command(
    text: Annotated[str, typer.Argument(help="Idea, ask, blocker, proof item, or state change.")],
    item_type: Annotated[
        str,
        typer.Option("--type", help="Kaizen type, or auto for classifier routing."),
    ] = "auto",
    status: Annotated[
        str,
        typer.Option(
            "--status",
            help=(
                "Kanban status: inbox, now, next, waiting, blocked, parked, done, "
                "cancelled, superseded, discarded."
            ),
        ),
    ] = "inbox",
    sensitivity: Annotated[
        str,
        typer.Option(
            "--sensitivity",
            help="public-safe, internal-only, private-client, coi-gated, or auto.",
        ),
    ] = "auto",
    repo: Annotated[
        str,
        typer.Option("--repo", help="Owning repo or lane."),
    ] = "diagnose-to-plan",
    source: Annotated[
        str,
        typer.Option("--source", help="Capture source such as codex, notion, meeting, repo."),
    ] = "codex",
    dtp_source_path: Annotated[
        str,
        typer.Option("--dtp-path", help="DTP source path backing this record."),
    ] = "practice-os/kaizen/intake.jsonl",
    notion_target: Annotated[
        str,
        typer.Option("--notion-target", help="Notion mirror surface, or auto."),
    ] = "auto",
    next_action: Annotated[
        str,
        typer.Option("--next-action", help="Smallest next action before promotion."),
    ] = "steward triage",
    tag: Annotated[
        list[str] | None,
        typer.Option("--tag", help="Repeatable lightweight tag."),
    ] = None,
    closed_at: Annotated[
        str,
        typer.Option("--closed-at", help="Closure timestamp for terminal records."),
    ] = "",
    closure_reason: Annotated[
        str,
        typer.Option("--closure-reason", help="Why this terminal record closed."),
    ] = "",
    evidence_ref: Annotated[
        list[str] | None,
        typer.Option("--evidence-ref", help="Repeatable evidence pointer for terminal records."),
    ] = None,
    superseded_by: Annotated[
        str,
        typer.Option("--superseded-by", help="Replacement record, story, or artifact."),
    ] = "",
    json_output: Annotated[
        bool,
        typer.Option("--json", help="Print the captured record as JSON."),
    ] = False,
) -> None:
    config = load_config()
    try:
        result = run_kaizen_capture(
            config,
            text,
            item_type=item_type,
            status=status,
            sensitivity=sensitivity,
            repo=repo,
            source=source,
            dtp_source_path=dtp_source_path,
            notion_target=notion_target,
            next_action=next_action,
            tags=tuple(tag or ()),
            closed_at=closed_at,
            closure_reason=closure_reason,
            evidence_refs=tuple(evidence_ref or ()),
            superseded_by=superseded_by,
        )
    except KaizenError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error

    if json_output:
        typer.echo(json.dumps(result.record.to_dict(), indent=2, sort_keys=True))
        return
    console.print(render_capture(result, config.repo_root), end="")


@kaizen_app.command("status")
def kaizen_status_command(
    status_filter: Annotated[
        str | None,
        typer.Option("--status", help="Limit output records to one Kanban status."),
    ] = None,
    limit: Annotated[
        int,
        typer.Option("--limit", help="Maximum records per active status bucket."),
    ] = 5,
    json_output: Annotated[
        bool,
        typer.Option("--json", help="Print machine-readable Kaizen counts and records."),
    ] = False,
) -> None:
    config = load_config()
    try:
        status = run_kaizen_status(config, status_filter=status_filter, limit=limit)
    except KaizenError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error

    if json_output:
        typer.echo(json.dumps(status.to_dict(), indent=2, sort_keys=True))
        return
    typer.echo(render_kaizen_status(status), nl=False)


@kaizen_app.command("update")
def kaizen_update_command(
    record_id: Annotated[str, typer.Argument(help="Kaizen record ID to update.")],
    item_type: Annotated[
        str | None,
        typer.Option("--type", help="New Kaizen type."),
    ] = None,
    status: Annotated[
        str | None,
        typer.Option(
            "--status",
            help=(
                "New Kanban status: inbox, now, next, waiting, blocked, parked, done, "
                "cancelled, superseded, discarded."
            ),
        ),
    ] = None,
    sensitivity: Annotated[
        str | None,
        typer.Option("--sensitivity", help="New sensitivity."),
    ] = None,
    repo: Annotated[
        str | None,
        typer.Option("--repo", help="New owning repo or lane."),
    ] = None,
    source: Annotated[
        str | None,
        typer.Option("--source", help="New capture source."),
    ] = None,
    dtp_source_path: Annotated[
        str | None,
        typer.Option("--dtp-path", help="New DTP source path."),
    ] = None,
    notion_target: Annotated[
        str | None,
        typer.Option("--notion-target", help="New Notion mirror surface, or auto."),
    ] = None,
    next_action: Annotated[
        str | None,
        typer.Option("--next-action", help="New smallest next action."),
    ] = None,
    tag: Annotated[
        list[str] | None,
        typer.Option("--tag", help="Replace tags with repeated values."),
    ] = None,
    closed_at: Annotated[
        str | None,
        typer.Option("--closed-at", help="Closure timestamp for terminal records."),
    ] = None,
    closure_reason: Annotated[
        str | None,
        typer.Option("--closure-reason", help="Why this terminal record closed."),
    ] = None,
    evidence_ref: Annotated[
        list[str] | None,
        typer.Option("--evidence-ref", help="Replace evidence refs with repeated values."),
    ] = None,
    superseded_by: Annotated[
        str | None,
        typer.Option("--superseded-by", help="Replacement record, story, or artifact."),
    ] = None,
    json_output: Annotated[
        bool,
        typer.Option("--json", help="Print the updated record as JSON."),
    ] = False,
) -> None:
    config = load_config()
    try:
        result = run_kaizen_update(
            config,
            record_id,
            item_type=item_type,
            status=status,
            sensitivity=sensitivity,
            repo=repo,
            source=source,
            dtp_source_path=dtp_source_path,
            notion_target=notion_target,
            next_action=next_action,
            tags=tuple(tag) if tag is not None else None,
            closed_at=closed_at,
            closure_reason=closure_reason,
            evidence_refs=tuple(evidence_ref) if evidence_ref is not None else None,
            superseded_by=superseded_by,
        )
    except KaizenError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error

    if json_output:
        typer.echo(json.dumps(result.record.to_dict(), indent=2, sort_keys=True))
        return
    console.print(render_update(result, config.repo_root), end="")


@kaizen_app.command("mirror")
def kaizen_mirror_command(
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", help="Preview sanitized Notion rows. This is the default."),
    ] = False,
    apply: Annotated[
        bool,
        typer.Option("--apply", help="Attempt live Notion writes after reviewed dry-run."),
    ] = False,
    include_done: Annotated[
        bool,
        typer.Option(
            "--include-done",
            help="Include terminal done/cancelled/superseded/discarded records.",
        ),
    ] = False,
    limit: Annotated[
        int,
        typer.Option("--limit", help="Maximum rows to emit."),
    ] = 100,
) -> None:
    if apply and dry_run:
        console.print("[red]choose either --dry-run or --apply, not both[/red]")
        raise typer.Exit(code=1)
    config = load_config()
    try:
        result = run_kaizen_mirror(config, apply=apply, include_done=include_done, limit=limit)
    except KaizenError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    typer.echo(render_mirror(result), nl=False)


@evolution_app.command("new")
def evolution_new_command(
    title: Annotated[
        str | None,
        typer.Argument(help="Idea or research-pattern title. Optional with --from-kaizen."),
    ] = None,
    kind: Annotated[
        str,
        typer.Option("--kind", help=f"One of: {', '.join(EVOLUTION_KINDS)}."),
    ] = "idea",
    from_kaizen: Annotated[
        str,
        typer.Option("--from-kaizen", help="Optional Kaizen record ID to turn into a draft."),
    ] = "",
    lane: Annotated[
        str,
        typer.Option("--lane", help="Owning repo or practice lane."),
    ] = "diagnose-to-plan",
    sensitivity: Annotated[
        str,
        typer.Option("--sensitivity", help="Data sensitivity label."),
    ] = "internal-only",
    state: Annotated[
        str,
        typer.Option(
            "--state",
            help=(
                "Initial state. Defaults to raw_capture for ideas and draft "
                "for research patterns."
            ),
        ),
    ] = "",
    source: Annotated[
        str,
        typer.Option("--source", help="Source label such as codex, gmail, meeting, research."),
    ] = "codex",
    force: Annotated[
        bool,
        typer.Option("--force", help="Overwrite an existing generated draft."),
    ] = False,
) -> None:
    config = load_config()
    try:
        result = run_evolution_new(
            config,
            title=title or "",
            kind=kind,
            from_kaizen=from_kaizen,
            lane=lane,
            sensitivity=sensitivity,
            state=state,
            source=source,
            force=force,
        )
    except EvolutionError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    console.print(render_evolution_new(result, config.repo_root), end="")


@evolution_app.command("status")
def evolution_status_command() -> None:
    config = load_config()
    result = run_evolution_status(config)
    console.print(render_evolution_status(result, config.repo_root), end="")


@evolution_app.command("dashboard")
def evolution_dashboard_command(
    out: Annotated[
        Path,
        typer.Option("--out", help="Static HTML dashboard output path."),
    ] = Path("docs/practice-evolution-dashboard.html"),
) -> None:
    config = load_config()
    result = run_evolution_dashboard(config, output_path=out)
    console.print(f"[green]practice evolution dashboard written[/green] {result.path}")


@memory_app.command("status")
def memory_status_command() -> None:
    config = load_config()
    result = run_memory_status(config)
    console.print(render_memory_status(result, config.repo_root), end="", markup=False)
    if not result.ok:
        raise typer.Exit(code=1)


@memory_app.command("steward")
def memory_steward_command(
    limit: Annotated[
        int,
        typer.Option("--limit", help="Maximum recommendation rows to emit."),
    ] = 10,
) -> None:
    config = load_config()
    result = run_memory_steward_review(config, limit=limit)
    console.print(render_memory_steward_review(result, config.repo_root), end="", markup=False)


@research_app.command("steward")
def research_steward_command(
    limit: Annotated[
        int,
        typer.Option("--limit", help="Maximum recommendation rows to emit."),
    ] = 10,
) -> None:
    config = load_config()
    result = run_research_steward_review(config, limit=limit)
    console.print(render_research_steward_review(result, config.repo_root), end="", markup=False)


@research_app.command("source-freshness")
def research_source_freshness_command(
    source_id: Annotated[
        str,
        typer.Option("--source-id", help="Source subset id, or manual-source by default."),
    ] = "",
    source_name: Annotated[
        str,
        typer.Option("--source-name", help="Human-readable source name for manual sources."),
    ] = "",
    source_tier: Annotated[
        int | None,
        typer.Option("--source-tier", help="Source tier 0-4. Defaults from known source id."),
    ] = None,
    source_url_or_path: Annotated[
        str,
        typer.Option("--source-url-or-path", help="Canonical source URL or DTP path."),
    ] = "",
    notes: Annotated[
        list[str] | None,
        typer.Option("--note", help="Operator note to include. Can be repeated."),
    ] = None,
    urls: Annotated[
        list[str] | None,
        typer.Option("--url", help="URL metadata to include. Can be repeated."),
    ] = None,
    queries: Annotated[
        list[str] | None,
        typer.Option("--query", help="Search query to include. Can be repeated."),
    ] = None,
    fetch_urls: Annotated[
        bool,
        typer.Option("--fetch-url/--no-fetch-url", help="Fetch public URL excerpts for --url."),
    ] = False,
    search_web: Annotated[
        bool,
        typer.Option("--search-web/--no-search-web", help="Fetch a public search result page."),
    ] = False,
    official_first: Annotated[
        bool,
        typer.Option(
            "--official-first/--broad-first",
            help="Generate official-domain search URLs before the broad web query.",
        ),
    ] = True,
    freshness_state: Annotated[
        str,
        typer.Option("--freshness-state", help="Dry-run freshness classification."),
    ] = "needs_manual_review",
    recommended_action: Annotated[
        str,
        typer.Option("--recommended-action", help="Recommended human review action."),
    ] = "watch",
    change_summary: Annotated[
        str,
        typer.Option("--change-summary", help="Short source-change summary."),
    ] = "",
    why_it_matters: Annotated[
        str,
        typer.Option("--why-it-matters", help="Practice relevance."),
    ] = "",
    evidence_limit: Annotated[
        str,
        typer.Option("--evidence-limit", help="What this dry run does not prove."),
    ] = "",
) -> None:
    config = load_config()
    try:
        result = run_research_source_freshness_dry_run(
            config,
            source_id=source_id,
            source_name=source_name,
            source_tier=source_tier,
            source_url_or_path=source_url_or_path,
            notes=tuple(notes or ()),
            urls=tuple(urls or ()),
            queries=tuple(queries or ()),
            fetch_urls=fetch_urls,
            search_web=search_web,
            official_first=official_first,
            freshness_state=freshness_state,
            recommended_action=recommended_action,
            change_summary=change_summary,
            why_it_matters=why_it_matters,
            evidence_limit=evidence_limit,
        )
    except ResearchSourceFreshnessError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    console.print(render_source_freshness_dry_run(result, config.repo_root), end="", markup=False)


@vault_app.command("init")
def vault_init_command(
    remote: Annotated[
        str | None,
        typer.Option("--remote", help="Optional private git remote for engagements/."),
    ] = None,
) -> None:
    config = load_config()
    try:
        status = run_vault_init(config, remote=remote)
    except VaultError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    console.print(render_vault_status(status, config.repo_root), end="")


@vault_app.command("status")
def vault_status_command() -> None:
    config = load_config()
    status = run_vault_status(config)
    console.print(render_vault_status(status, config.repo_root), end="")


@vault_app.command("snapshot")
def vault_snapshot_command(
    message: Annotated[
        str,
        typer.Option("--message", "-m", help="Private vault commit message."),
    ] = "Snapshot DTP private artifacts",
    push: Annotated[
        bool,
        typer.Option("--push", help="Push to the vault origin after committing."),
    ] = False,
) -> None:
    config = load_config()
    try:
        result = run_vault_snapshot(config, message=message, push=push)
    except VaultError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    if result.committed:
        console.print("[green]vault snapshot committed[/green]")
    else:
        console.print("[green]vault already clean[/green]")
    if result.pushed:
        console.print("[green]vault snapshot pushed[/green]")
    console.print(render_vault_status(result.status, config.repo_root), end="")


@workspace_app.command("report")
def workspace_report_command(
    json_output: Annotated[
        bool,
        typer.Option("--json", help="Print a machine-readable Workspace Command Center report."),
    ] = False,
) -> None:
    config = load_config()
    report = run_workspace_report(config)
    if json_output:
        typer.echo(json.dumps(report.to_dict(), indent=2))
        return
    typer.echo(render_workspace_report(report), nl=False)


@workspace_app.command("dashboard")
def workspace_dashboard_command(
    out: Annotated[
        Path,
        typer.Option("--out", help="Static HTML dashboard output path."),
    ] = Path("docs/workspace-dashboard.html"),
    surface: Annotated[
        DashboardSurface,
        typer.Option("--surface", help="Dashboard surface style."),
    ] = DashboardSurface.browser,
) -> None:
    config = load_config()
    result = run_workspace_dashboard(config, output_path=out, surface=surface)
    console.print(f"[green]workspace dashboard written[/green] {result.path}")
    console.print(
        f"repos={result.repo_count}; active_items={result.active_item_count}; "
        f"closed_items={result.closed_item_count}; "
        f"recovery_inbox={result.recovery_inbox_count}; "
        f"sweep_scopes={result.sweep_scope_count}; "
        f"proof_candidates={result.proof_candidate_count}"
    )


@workspace_app.command("validate-dashboard")
def workspace_validate_dashboard_command() -> None:
    config = load_config()
    result = run_workspace_dashboard_validation(config)
    categories = result.summary["categories"]
    status = "ok" if result.ok else "needs attention"
    console.print(f"[green]workspace dashboard validation[/green] {status}")
    console.print(
        "in_dashboard={in_dashboard}; recovery_inbox={recovery_inbox}; "
        "excluded_or_redacted={excluded_or_redacted}; duplicate_merged={duplicate_merged}; "
        "source_missing={source_missing}; count_mismatch={count_mismatch}; "
        "duplicate_task_ids={duplicate_task_ids}".format(
            **categories
        )
    )
    console.print(f"json={result.json_path}")
    console.print(f"markdown={result.markdown_path}")
    if not result.ok:
        raise typer.Exit(code=1)


@workspace_app.command("recover")
def workspace_recover_command(
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", help="Write reviewable recovery candidates to ignored outputs/."),
    ] = False,
    apply: Annotated[
        bool,
        typer.Option("--apply", help="Import reviewed candidates into the workspace task ledger."),
    ] = False,
    approved: Annotated[
        Path | None,
        typer.Option("--approved", help="Reviewed candidate JSON from a prior dry run."),
    ] = None,
) -> None:
    if dry_run and apply:
        console.print("[red]choose either --dry-run or --apply, not both[/red]")
        raise typer.Exit(code=1)
    config = load_config()
    try:
        result = run_workspace_recover(config, apply=apply, approved_path=approved)
    except ValueError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    if apply:
        console.print(
            f"[green]workspace recovery imported[/green] {result.imported_count} "
            f"rows -> {result.ledger_path}"
        )
    else:
        console.print(
            f"[green]workspace recovery dry-run[/green] {len(result.candidates)} candidates"
        )
        if result.dry_run_json_path:
            console.print(f"json={result.dry_run_json_path}")
        if result.dry_run_markdown_path:
            console.print(f"markdown={result.dry_run_markdown_path}")
    if result.notion_export_path:
        console.print(f"notion_export={result.notion_export_path}")


@workspace_task_app.command("add")
def workspace_task_add_command(
    title: Annotated[str, typer.Option("--title", help="Reviewed workspace task title.")],
    repo: Annotated[str, typer.Option("--repo", help="Owning repo or workspace lane.")],
    status: Annotated[str, typer.Option("--status", help="Task status.")],
    priority: Annotated[str, typer.Option("--priority", help="Priority such as P1.")],
    next_action: Annotated[str, typer.Option("--next-action", help="Next action.")],
    source_ref: Annotated[str, typer.Option("--source-ref", help="DTP source pointer.")],
    sensitivity: Annotated[str, typer.Option("--sensitivity", help="Data sensitivity.")],
    confidence: Annotated[str, typer.Option("--confidence", help="Evidence confidence.")],
    lane: Annotated[
        str,
        typer.Option("--lane", help="Optional lane or workstream."),
    ] = "Manual Workspace Task",
    blocked_by: Annotated[
        str,
        typer.Option("--blocked-by", help="Optional blocker or gate."),
    ] = "",
    evidence_ref: Annotated[
        str,
        typer.Option("--evidence-ref", help="Optional evidence pointer."),
    ] = "",
    closed_at: Annotated[
        str,
        typer.Option("--closed-at", help="Optional closure date for terminal rows."),
    ] = "",
    closure_reason: Annotated[
        str,
        typer.Option("--closure-reason", help="Optional closure reason."),
    ] = "",
    superseded_by: Annotated[
        str,
        typer.Option("--superseded-by", help="Optional replacement pointer."),
    ] = "",
) -> None:
    config = load_config()
    try:
        task = run_workspace_task_add(
            config,
            title=title,
            repo=repo,
            status=status,
            priority=priority,
            next_action=next_action,
            source_ref=source_ref,
            sensitivity=sensitivity,
            confidence=confidence,
            lane=lane,
            blocked_by=blocked_by,
            evidence_ref=evidence_ref,
            closed_at=closed_at,
            closure_reason=closure_reason,
            superseded_by=superseded_by,
        )
    except ValueError as error:
        console.print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    console.print(f"[green]workspace task added[/green] {task.id}")


@app.command("web")
def web_command(
    host: Annotated[
        str,
        typer.Option("--host", help="Host for the local-only workbench server."),
    ] = "127.0.0.1",
    port: Annotated[
        int,
        typer.Option("--port", help="Port for the local-only workbench server."),
    ] = 8765,
    open_browser: Annotated[
        bool,
        typer.Option("--open/--no-open", help="Open the workbench in your browser."),
    ] = True,
) -> None:
    config = load_config()
    console.print(f"[green]DTP Workbench[/green] http://{host}:{port}")
    console.print("Press Ctrl+C to stop.")
    run_workbench_server(config=config, host=host, port=port, open_browser=open_browser)


def _print_recall_result(repo_root: Path, result: RecallResult) -> None:
    path = result.path.relative_to(repo_root).as_posix()
    console.print(
        f"[green]{result.type}[/green] {result.repo} "
        f"[dim]score={result.score}[/dim] {path}\n{result.title}\n{result.snippet}\n"
    )


def main() -> None:
    app()
