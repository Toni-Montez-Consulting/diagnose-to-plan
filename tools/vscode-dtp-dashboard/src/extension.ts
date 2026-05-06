import * as childProcess from 'child_process';
import { existsSync } from 'fs';
import { readFile } from 'fs/promises';
import * as os from 'os';
import * as path from 'path';
import * as vscode from 'vscode';

let dashboardPanel: vscode.WebviewPanel | undefined;

export function activate(context: vscode.ExtensionContext): void {
  context.subscriptions.push(
    vscode.commands.registerCommand('dtpDashboard.open', () => openDashboard(context, false)),
    vscode.commands.registerCommand('dtpDashboard.refresh', () => openDashboard(context, true)),
    vscode.commands.registerCommand('dtpDashboard.openSourceDocs', () => openSourceDocs()),
  );
}

export function deactivate(): void {
  dashboardPanel = undefined;
}

async function openDashboard(
  context: vscode.ExtensionContext,
  refreshFirst: boolean,
): Promise<void> {
  const root = resolveDtpRoot();
  if (!root) {
    vscode.window.showErrorMessage(
      'DTP Workspace Dashboard could not find diagnose-to-plan. Open toni-consulting-ops.code-workspace or set dtpDashboard.dtpRoot.',
    );
    return;
  }

  const panel = ensurePanel(context);
  panel.reveal(vscode.ViewColumn.Beside);

  if (refreshFirst) {
    await refreshDashboard(root, panel);
    return;
  }

  await loadCachedDashboard(root, panel);
}

function ensurePanel(context: vscode.ExtensionContext): vscode.WebviewPanel {
  if (dashboardPanel) {
    return dashboardPanel;
  }

  dashboardPanel = vscode.window.createWebviewPanel(
    'dtpWorkspaceDashboard',
    'DTP Workspace Dashboard',
    vscode.ViewColumn.Beside,
    {
      enableFindWidget: true,
      enableScripts: false,
      localResourceRoots: [],
      retainContextWhenHidden: false,
    },
  );
  dashboardPanel.iconPath = vscode.Uri.joinPath(context.extensionUri, 'media', 'icon.svg');
  dashboardPanel.onDidDispose(() => {
    dashboardPanel = undefined;
  });
  return dashboardPanel;
}

async function refreshDashboard(root: string, panel: vscode.WebviewPanel): Promise<void> {
  panel.webview.html = renderMessage('Refreshing workspace dashboard...');
  try {
    await runDtpDashboard(root);
    await loadCachedDashboard(root, panel);
    vscode.window.setStatusBarMessage('DTP workspace dashboard refreshed', 4000);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    panel.webview.html = renderMessage('Dashboard refresh failed', message);
    vscode.window.showErrorMessage(`DTP dashboard refresh failed: ${message}`);
  }
}

async function loadCachedDashboard(root: string, panel: vscode.WebviewPanel): Promise<void> {
  const dashboardPath = path.join(root, 'outputs', 'workspace-dashboard.html');
  if (!existsSync(dashboardPath)) {
    panel.webview.html = renderMessage(
      'No cached dashboard yet',
      'Run DTP: Refresh Workspace Dashboard to generate outputs/workspace-dashboard.html.',
    );
    return;
  }
  panel.webview.html = await readFile(dashboardPath, 'utf8');
}

async function runDtpDashboard(root: string): Promise<void> {
  const pythonPath = resolvePythonPath(root);
  const args = [
    '-m',
    'dtp',
    'workspace',
    'dashboard',
    '--surface',
    'vscode',
    '--out',
    'outputs/workspace-dashboard.html',
  ];

  await execFile(pythonPath, args, {
    cwd: root,
    env: { ...process.env, DTP_HOME: root },
    maxBuffer: 1024 * 1024,
    timeout: 120000,
    windowsHide: true,
  });
}

function resolveDtpRoot(): string | undefined {
  const folders = vscode.workspace.workspaceFolders ?? [];
  const workspaceRoot = folders.find((folder) => {
    return folder.name === 'diagnose-to-plan' || path.basename(folder.uri.fsPath) === 'diagnose-to-plan';
  });
  if (workspaceRoot) {
    return workspaceRoot.uri.fsPath;
  }

  const configured = vscode.workspace
    .getConfiguration('dtpDashboard')
    .get<string>('dtpRoot', '')
    .trim();
  return configured ? expandHome(configured) : undefined;
}

function resolvePythonPath(root: string): string {
  const venvPython = path.join(root, '.venv', 'Scripts', 'python.exe');
  if (existsSync(venvPython)) {
    return venvPython;
  }

  const configured = vscode.workspace
    .getConfiguration('dtpDashboard')
    .get<string>('pythonPath', '')
    .trim();
  return configured ? expandHome(configured) : 'python';
}

async function openSourceDocs(): Promise<void> {
  const root = resolveDtpRoot();
  if (!root) {
    vscode.window.showErrorMessage(
      'DTP Workspace Dashboard could not find diagnose-to-plan. Open toni-consulting-ops.code-workspace or set dtpDashboard.dtpRoot.',
    );
    return;
  }
  const uri = vscode.Uri.file(path.join(root, 'docs', 'WORKSPACE_DASHBOARD_READONLY.md'));
  await vscode.window.showTextDocument(uri, { preview: false });
}

function execFile(
  file: string,
  args: string[],
  options: childProcess.ExecFileOptions,
): Promise<void> {
  return new Promise((resolve, reject) => {
    childProcess.execFile(file, args, options, (error, stdout, stderr) => {
      if (!error) {
        resolve();
        return;
      }
      const detail = [String(stderr).trim(), String(stdout).trim()].filter(Boolean).join('\n');
      reject(new Error(detail || error.message));
    });
  });
}

function expandHome(value: string): string {
  if (value === '~') {
    return os.homedir();
  }
  if (value.startsWith(`~${path.sep}`) || value.startsWith('~/')) {
    return path.join(os.homedir(), value.slice(2));
  }
  return value;
}

function renderMessage(title: string, detail = ''): string {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>DTP Workspace Dashboard</title>
  <style>
    :root {
      color-scheme: light dark;
    }
    body {
      margin: 0;
      padding: 24px;
      background: var(--vscode-editor-background);
      color: var(--vscode-foreground);
      font-family: var(--vscode-font-family);
      font-size: var(--vscode-font-size);
    }
    main {
      max-width: 760px;
      padding: 18px;
      border: 1px solid var(--vscode-panel-border);
      border-radius: 8px;
      background: var(--vscode-sideBar-background);
    }
    h1 {
      margin: 0 0 8px;
      font-size: 22px;
      font-weight: 700;
    }
    p {
      margin: 0;
      color: var(--vscode-descriptionForeground);
      line-height: 1.5;
      white-space: pre-wrap;
    }
  </style>
</head>
<body>
  <main>
    <h1>${escapeHtml(title)}</h1>
    <p>${escapeHtml(detail)}</p>
  </main>
</body>
</html>`;
}

function escapeHtml(value: string): string {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}
