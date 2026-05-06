# DTP Workspace Dashboard

Local VS Code panel for the DTP workspace planning and roadmap dashboard.

This extension is intentionally tiny. It does not run a server, watch files,
deploy anything, call cloud APIs, or execute sibling-repo checks. It opens a
webview panel and manually refreshes `outputs/workspace-dashboard.html` by
running the DTP read-only dashboard command.

## Commands

- `DTP: Open Workspace Dashboard`
- `DTP: Refresh Workspace Dashboard`
- `DTP: Open Dashboard Source Docs`

## Install Locally

```powershell
cd C:\Users\tonimontez\Projects\diagnose-to-plan\tools\vscode-dtp-dashboard
npm install
npm run package:vsix
code --install-extension dist/dtp-workspace-dashboard.vsix --force
```

If the `code` shim rejects `--install-extension` on Toni's Windows machine, use:

```powershell
& "$env:LOCALAPPDATA\Programs\Microsoft VS Code\bin\code.cmd" --install-extension dist\dtp-workspace-dashboard.vsix --force
```

Open `C:\Users\tonimontez\toni-consulting-ops.code-workspace`, then run
`DTP: Open Workspace Dashboard` from the command palette.

## Boundary

The panel renders the cross-workspace planning state owned by DTP. DTP remains
the source of truth for roadmap, Kaizen, proof, evidence, and repo coverage.
The extension is only a local viewer and manual refresh button.
