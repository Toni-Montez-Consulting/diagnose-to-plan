# ruff: noqa: E501

from __future__ import annotations

import html
import json
import webbrowser
from dataclasses import dataclass
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, quote, unquote, urlparse

from dtp.commands.kit import KIT_KINDS, KitError, run_kit_new, run_kit_status
from dtp.commands.practice import run_practice_doctor
from dtp.commands.redact import REDACT_PROFILES, RedactionError, run_redact_check
from dtp.commands.vault import VaultError, run_vault_snapshot, run_vault_status
from dtp.config import DtpConfig


@dataclass(frozen=True)
class WorkbenchServer:
    host: str
    port: int

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"


def run_workbench_server(
    *,
    config: DtpConfig,
    host: str = "127.0.0.1",
    port: int = 8765,
    open_browser: bool = True,
) -> WorkbenchServer:
    handler = _handler(config)
    server = ThreadingHTTPServer((host, port), handler)
    address = WorkbenchServer(host=host, port=port)
    if open_browser:
        webbrowser.open(address.url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return address


def build_workbench_state(config: DtpConfig) -> dict[str, Any]:
    doctor = run_practice_doctor(config)
    kits = run_kit_status(config=config)
    vault = run_vault_status(config)
    checks = [{"ok": True, "message": item} for item in doctor.checks]
    checks.extend({"ok": False, "message": item} for item in doctor.problems)
    return {
        "repo_root": config.repo_root.as_posix(),
        "practice_os": {
            "path": _relative(config.practice_os_dir, config.repo_root),
            "doctor_ok": doctor.ok,
            "checks": checks,
            "pattern_count": _count_markdown(config.practice_os_dir / "patterns"),
            "policy_count": _count_markdown(config.practice_os_dir / "policies"),
            "template_count": _count_markdown(config.practice_os_dir / "templates"),
        },
        "engagements": {
            "path": _relative(config.engagements_dir, config.repo_root),
            "kits": [
                {
                    "client_id": kit.client_id,
                    "path": _relative(kit.root, config.repo_root),
                    "phase": kit.phase,
                    "ready": kit.ready,
                    "missing": list(kit.missing),
                    "metrics_ready": kit.metrics_ready,
                    "redaction_ready": kit.redaction_ready,
                    "handoff_ready": kit.handoff_ready,
                }
                for kit in kits
            ],
        },
        "vault": {
            "path": _relative(vault.root, config.repo_root),
            "exists": vault.exists,
            "ready": vault.ready,
            "git_initialized": vault.git_initialized,
            "branch": vault.branch,
            "head": vault.head,
            "dirty": vault.dirty,
            "remote": vault.remote,
            "has_remote": vault.has_remote,
        },
        "contracts": {
            "storage": "markdown-first",
            "private": "engagements are local/private and ignored by the DTP code repo",
            "public": "consulting receives only redacted proof packets",
            "database": "defer until two or three real engagements expose query pain",
        },
    }


def render_workbench_html(
    state: dict[str, Any],
    *,
    notice: str = "",
    error: str = "",
) -> str:
    kits = state["engagements"]["kits"]
    kit_rows = "\n".join(_kit_row(kit) for kit in kits) or _empty_kit_row()
    doctor_rows = "\n".join(
        f"<li data-ok=\"{str(check['ok']).lower()}\">"
        f"<span>{'ok' if check['ok'] else 'fix'}</span>{_e(check['message'])}</li>"
        for check in state["practice_os"]["checks"]
    )
    notice_html = f"<div class=\"notice\">{_e(notice)}</div>" if notice else ""
    error_html = f"<div class=\"notice notice--error\">{_e(error)}</div>" if error else ""
    vault = state["vault"]
    vault_state = "ready" if vault["ready"] else "local only"
    if vault["dirty"]:
        vault_state = "unsnapped changes"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex,nofollow">
  <title>DTP Workbench</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #101214;
      --panel: #171a1d;
      --panel-2: #1d2226;
      --ink: #f2eee7;
      --muted: #b5ada1;
      --rule: #353a3f;
      --accent: #7ec4b5;
      --warn: #e6bc71;
      --bad: #e07a6f;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background:
        linear-gradient(90deg, rgba(126, 196, 181, .05) 1px, transparent 1px),
        linear-gradient(rgba(126, 196, 181, .04) 1px, transparent 1px),
        var(--bg);
      background-size: 34px 34px, 34px 34px, auto;
      color: var(--ink);
    }}
    a {{ color: inherit; }}
    main {{
      display: grid;
      grid-template-columns: 270px minmax(0, 1fr);
      min-height: 100svh;
    }}
    aside {{
      position: sticky;
      top: 0;
      height: 100svh;
      border-right: 1px solid var(--rule);
      background: rgba(16, 18, 20, .86);
      padding: 24px;
    }}
    .brand {{
      display: grid;
      gap: 8px;
      margin-bottom: 30px;
    }}
    .brand strong {{
      font-family: Georgia, "Times New Roman", serif;
      font-size: 30px;
      font-weight: 500;
      letter-spacing: 0;
    }}
    .brand span,
    .label,
    button,
    input,
    select {{
      font-size: 12px;
      letter-spacing: .07em;
      text-transform: uppercase;
    }}
    .brand span,
    .muted,
    td,
    .panel p,
    .notice {{
      color: var(--muted);
    }}
    nav {{
      display: grid;
      gap: 10px;
    }}
    nav a {{
      border: 1px solid var(--rule);
      border-radius: 7px;
      padding: 11px 12px;
      text-decoration: none;
    }}
    section {{
      padding: 28px;
    }}
    .hero {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) 360px;
      gap: 24px;
      align-items: stretch;
    }}
    h1 {{
      max-width: 900px;
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(44px, 7vw, 88px);
      font-weight: 500;
      line-height: .92;
      letter-spacing: 0;
    }}
    h2 {{
      margin: 0 0 18px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: 34px;
      font-weight: 500;
      letter-spacing: 0;
    }}
    .lead {{
      max-width: 820px;
      margin: 22px 0 0;
      color: var(--muted);
      font-size: 18px;
      line-height: 1.55;
    }}
    .panel {{
      border: 1px solid var(--rule);
      border-radius: 8px;
      background: color-mix(in oklch, var(--panel) 94%, black);
      padding: 20px;
    }}
    .panel--tight {{ padding: 0; overflow: hidden; }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
      margin-top: 22px;
    }}
    .metric strong {{
      display: block;
      margin-top: 10px;
      font-size: 28px;
      font-weight: 600;
    }}
    .status {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      color: var(--accent);
      font-size: 12px;
      letter-spacing: .08em;
      text-transform: uppercase;
    }}
    .status:before {{
      content: "";
      width: 8px;
      height: 8px;
      border-radius: 999px;
      background: currentColor;
    }}
    .status--warn {{ color: var(--warn); }}
    .status--bad {{ color: var(--bad); }}
    table {{
      width: 100%;
      border-collapse: collapse;
    }}
    th,
    td {{
      border-bottom: 1px solid var(--rule);
      padding: 14px 16px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      color: var(--ink);
      font-size: 12px;
      letter-spacing: .08em;
      text-transform: uppercase;
    }}
    form {{
      display: grid;
      gap: 12px;
    }}
    .form-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr)) auto;
      gap: 10px;
      align-items: end;
    }}
    label {{
      display: grid;
      gap: 7px;
    }}
    input,
    select {{
      min-height: 42px;
      width: 100%;
      border: 1px solid var(--rule);
      border-radius: 7px;
      background: var(--panel-2);
      color: var(--ink);
      padding: 0 12px;
      text-transform: none;
      letter-spacing: 0;
    }}
    button {{
      min-height: 42px;
      border: 1px solid color-mix(in oklch, var(--accent) 70%, white);
      border-radius: 7px;
      background: var(--accent);
      color: #0b1111;
      padding: 0 16px;
      cursor: pointer;
      font-weight: 700;
    }}
    .stack {{
      display: grid;
      gap: 18px;
      margin-top: 22px;
    }}
    .doctor {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 0;
      margin: 0;
      padding: 0;
      list-style: none;
    }}
    .doctor li {{
      display: flex;
      gap: 10px;
      border-bottom: 1px solid var(--rule);
      padding: 12px 14px;
      color: var(--muted);
    }}
    .doctor li:nth-child(odd) {{ border-right: 1px solid var(--rule); }}
    .doctor span {{ color: var(--accent); font-weight: 700; }}
    .doctor li[data-ok="false"] span {{ color: var(--bad); }}
    .notice {{
      border: 1px solid var(--rule);
      border-radius: 7px;
      background: var(--panel);
      margin-bottom: 14px;
      padding: 12px 14px;
    }}
    .notice--error {{
      border-color: color-mix(in oklch, var(--bad) 70%, var(--rule));
      color: var(--bad);
    }}
    @media (max-width: 980px) {{
      main {{ grid-template-columns: 1fr; }}
      aside {{ position: static; height: auto; }}
      .hero,
      .grid,
      .form-grid,
      .doctor {{ grid-template-columns: 1fr; }}
      .doctor li:nth-child(odd) {{ border-right: 0; }}
    }}
  </style>
</head>
<body>
<main>
  <aside>
    <div class="brand">
      <strong>DTP</strong>
      <span>local practice workbench</span>
    </div>
    <nav aria-label="Workbench sections">
      <a href="#kits">Client kits</a>
      <a href="#vault">Private vault</a>
      <a href="#doctor">Practice doctor</a>
      <a href="/api/state">JSON state</a>
    </nav>
  </aside>
  <section>
    {notice_html}
    {error_html}
    <div class="hero">
      <div>
        <h1>Operate the practice from the artifacts.</h1>
        <p class="lead">This is a local-only UI over DTP's markdown contracts. It creates kits, shows readiness, runs redaction checks, and keeps private client work out of the public consulting site.</p>
      </div>
      <div class="panel">
        <p class="label">Storage contract</p>
        <p>Practice OS is reusable and commit-safe. Engagements are private by default. The vault gives those private artifacts a separate durability path.</p>
      </div>
    </div>

    <div class="grid">
      <div class="panel metric">
        <p class="label">Practice doctor</p>
        <strong>{'OK' if state['practice_os']['doctor_ok'] else 'Needs work'}</strong>
      </div>
      <div class="panel metric">
        <p class="label">Client kits</p>
        <strong>{len(kits)}</strong>
      </div>
      <div class="panel metric">
        <p class="label">Vault</p>
        <strong>{_e(vault_state)}</strong>
      </div>
    </div>

    <div id="kits" class="stack">
      <div class="panel">
        <h2>Create a kit</h2>
        <form method="post" action="/kits/new">
          <div class="form-grid">
            <label><span class="label">Client</span><input name="client" placeholder="mom-nonprofit" required></label>
            <label><span class="label">Project</span><input name="project" placeholder="site-rebuild" required></label>
            <label><span class="label">Kind</span><select name="kind">{_kind_options()}</select></label>
            <button type="submit">Create</button>
          </div>
        </form>
      </div>
      <div class="panel panel--tight">
        <table>
          <thead><tr><th>Client</th><th>Phase</th><th>Readiness</th><th>Missing</th></tr></thead>
          <tbody>{kit_rows}</tbody>
        </table>
      </div>
    </div>

    <div id="vault" class="stack">
      <div class="panel">
        <h2>Private vault</h2>
        <p>Path: <code>{_e(vault['path'])}</code></p>
        <p>Status: <span class="{_status_class(vault['ready'], vault['dirty'])}">{_e(vault_state)}</span></p>
        <p>Head: {_e(vault['head'] or 'no private commits yet')} - Remote: {_e(vault['remote'] or 'not set')}</p>
        <form method="post" action="/vault/snapshot">
          <div class="form-grid">
            <label><span class="label">Snapshot message</span><input name="message" value="Snapshot DTP private artifacts" required></label>
            <label><span class="label">Push</span><select name="push"><option value="false">Local commit only</option><option value="true">Commit and push</option></select></label>
            <span></span>
            <button type="submit">Snapshot</button>
          </div>
        </form>
      </div>
    </div>

    <div id="redact" class="stack">
      <div class="panel">
        <h2>Redaction check</h2>
        <form method="post" action="/redact/check">
          <div class="form-grid">
            <label><span class="label">Path</span><input name="path" value="practice-os" required></label>
            <label><span class="label">Profile</span><select name="profile">{_profile_options()}</select></label>
            <span></span>
            <button type="submit">Check</button>
          </div>
        </form>
      </div>
    </div>

    <div id="doctor" class="stack">
      <div class="panel panel--tight">
        <ul class="doctor">{doctor_rows}</ul>
      </div>
    </div>
  </section>
</main>
</body>
</html>"""


def _handler(config: DtpConfig) -> type[BaseHTTPRequestHandler]:
    class WorkbenchHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            route = urlparse(self.path)
            if route.path == "/api/state":
                _send_json(self, build_workbench_state(config))
                return
            if route.path != "/":
                _send_text(self, "Not found", HTTPStatus.NOT_FOUND)
                return
            params = parse_qs(route.query)
            state = build_workbench_state(config)
            body = render_workbench_html(
                state,
                notice=_first(params, "notice"),
                error=_first(params, "error"),
            )
            _send_html(self, body)

        def do_POST(self) -> None:  # noqa: N802
            route = urlparse(self.path)
            form = _read_form(self)
            try:
                if route.path == "/kits/new":
                    result = run_kit_new(
                        config=config,
                        client=_required(form, "client"),
                        project=_required(form, "project"),
                        kind=form.get("kind", "launch"),
                    )
                    _redirect(
                        self,
                        f"/?notice={quote(f'created kit {result.client_id}/{result.engagement_id}')}",
                    )
                    return
                if route.path == "/redact/check":
                    findings = run_redact_check(
                        config=config,
                        path=Path(_required(form, "path")),
                        profile=form.get("profile", "practice"),
                    )
                    if findings:
                        _redirect(self, f"/?error={quote(f'{len(findings)} redaction finding(s)')}")
                    else:
                        _redirect(self, "/?notice=redaction check passed")
                    return
                if route.path == "/vault/snapshot":
                    result = run_vault_snapshot(
                        config=config,
                        message=_required(form, "message"),
                        push=form.get("push") == "true",
                    )
                    if result.committed:
                        message = "vault snapshot committed"
                    else:
                        message = "vault already clean"
                    if result.pushed:
                        message += " and pushed"
                    _redirect(self, f"/?notice={quote(message)}")
                    return
            except (KitError, RedactionError, VaultError, ValueError) as error:
                _redirect(self, f"/?error={quote(str(error))}")
                return
            _send_text(self, "Not found", HTTPStatus.NOT_FOUND)

        def log_message(self, format: str, *args: object) -> None:
            return

    return WorkbenchHandler


def _send_json(handler: BaseHTTPRequestHandler, payload: dict[str, Any]) -> None:
    body = json.dumps(payload, indent=2).encode("utf-8")
    handler.send_response(HTTPStatus.OK)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def _send_html(handler: BaseHTTPRequestHandler, body: str) -> None:
    encoded = body.encode("utf-8")
    handler.send_response(HTTPStatus.OK)
    handler.send_header("Content-Type", "text/html; charset=utf-8")
    handler.send_header("Content-Length", str(len(encoded)))
    handler.end_headers()
    handler.wfile.write(encoded)


def _send_text(
    handler: BaseHTTPRequestHandler,
    body: str,
    status: HTTPStatus = HTTPStatus.OK,
) -> None:
    encoded = body.encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "text/plain; charset=utf-8")
    handler.send_header("Content-Length", str(len(encoded)))
    handler.end_headers()
    handler.wfile.write(encoded)


def _redirect(handler: BaseHTTPRequestHandler, location: str) -> None:
    handler.send_response(HTTPStatus.SEE_OTHER)
    handler.send_header("Location", location)
    handler.end_headers()


def _read_form(handler: BaseHTTPRequestHandler) -> dict[str, str]:
    size = int(handler.headers.get("Content-Length") or "0")
    raw = handler.rfile.read(size).decode("utf-8") if size else ""
    return {key: values[-1] for key, values in parse_qs(raw).items()}


def _kit_row(kit: dict[str, Any]) -> str:
    checks = [
        ("metrics", kit["metrics_ready"]),
        ("redaction", kit["redaction_ready"]),
        ("handoff", kit["handoff_ready"]),
    ]
    readiness = " · ".join(f"{label}: {'ok' if ready else 'needed'}" for label, ready in checks)
    missing = ", ".join(kit["missing"]) if kit["missing"] else "none"
    status_class = _status_class(bool(kit["ready"]), False)
    return (
        "<tr>"
        f"<td><strong>{_e(kit['client_id'])}</strong><br><span class=\"muted\">{_e(kit['path'])}</span></td>"
        f"<td>{_e(kit['phase'])}</td>"
        f"<td><span class=\"{status_class}\">{_e('ready' if kit['ready'] else readiness)}</span></td>"
        f"<td>{_e(missing)}</td>"
        "</tr>"
    )


def _empty_kit_row() -> str:
    return (
        "<tr><td colspan=\"4\">No kits yet. Create the mom nonprofit kit when you are ready."
        "</td></tr>"
    )


def _kind_options() -> str:
    return "\n".join(
        f"<option value=\"{_e(kind)}\"{' selected' if kind == 'launch' else ''}>{_e(kind)}</option>"
        for kind in sorted(KIT_KINDS)
    )


def _profile_options() -> str:
    return "\n".join(
        f"<option value=\"{_e(profile)}\"{' selected' if profile == 'practice' else ''}>{_e(profile)}</option>"
        for profile in sorted(REDACT_PROFILES)
    )


def _status_class(ok: bool, dirty: bool) -> str:
    if dirty:
        return "status status--warn"
    return "status" if ok else "status status--warn"


def _relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def _count_markdown(path: Path) -> int:
    if not path.exists():
        return 0
    return len(tuple(path.glob("*.md")))


def _required(form: dict[str, str], key: str) -> str:
    value = form.get(key, "").strip()
    if not value:
        raise ValueError(f"missing required field: {key}")
    return value


def _first(params: dict[str, list[str]], key: str) -> str:
    values = params.get(key) or [""]
    return unquote(values[-1])


def _e(value: object) -> str:
    return html.escape(str(value), quote=True)
