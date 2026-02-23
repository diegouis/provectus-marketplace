# proagent-connector-setup

Guided setup wizard for configuring shared MCP server credentials (Slack, Google Drive). Walks users through token extraction, OAuth configuration, credential storage, and end-to-end verification.

## Installation

### Option 1: Copy to your project

```bash
cp -r proagent-connector-setup/ /path/to/your-project/.claude/plugins/proagent-connector-setup/
```

### Option 2: Reference from the marketplace

```json
{
  "plugins": ["proagent-connector-setup"]
}
```

### Option 3: Symlink for development

```bash
ln -s /path/to/provectus-marketplace/plugins/proagent-connector-setup /path/to/your-project/.claude/plugins/proagent-connector-setup
```

## Prerequisites

| Requirement | Purpose |
|-------------|---------|
| Node.js + `npx` | Running MCP servers for verification |
| Chrome or Firefox | Extracting Slack tokens from browser DevTools |
| Google account | Creating GCP project and OAuth credentials |

## Usage

### Check what's configured

```
/proagent-connector-setup-run verify-all
```

Reports READY / NEEDS SETUP / DEGRADED for each connector.

### Set up Slack

```
/proagent-connector-setup-run setup-slack
```

Guides you through:
1. Opening your Slack workspace in a browser
2. Extracting the `xoxd-` token from browser cookies
3. Extracting the `xoxc-` token from network requests
4. Persisting tokens (project `.env`, shell profile, or dedicated file)
5. Verifying live MCP connectivity

### Set up Google Drive

```
/proagent-connector-setup-run setup-google-drive
```

Guides you through:
1. Creating a GCP project and enabling the Drive API
2. Configuring the OAuth consent screen
3. Creating Desktop app OAuth credentials
4. Downloading and placing the credential file
5. Running the OAuth authorization flow
6. Verifying live MCP connectivity

### Overview

```
/proagent-connector-setup-hub
```

Shows all capabilities, available commands, and quick-start routing.

## Component Inventory

| Component | Path | Purpose |
|-----------|------|---------|
| Plugin manifest | `.claude-plugin/plugin.json` | Name, version, description |
| MCP config | `.mcp.json` | Empty — this plugin configures, not consumes |
| Core skill | `skills/connector-setup-assistant/SKILL.md` | Principles, scope, verification standards |
| Slack reference | `skills/.../references/slack-setup.md` | Token extraction, formats, troubleshooting |
| Google Drive reference | `skills/.../references/google-drive-setup.md` | GCP setup, OAuth, troubleshooting |
| Hub command | `commands/proagent-connector-setup-hub.md` | Capabilities overview |
| Run command | `commands/proagent-connector-setup-run.md` | Thin dispatcher to mode files |
| Slack mode | `commands/modes/setup-slack.md` | 5-step Slack setup workflow |
| Google Drive mode | `commands/modes/setup-google-drive.md` | 6-step Google Drive setup workflow |
| Verify mode | `commands/modes/verify-all.md` | Diagnostic status report |
| Hooks | `hooks/hooks.json` | Placeholder token detection |

## Version

- Plugin version: 0.1.0
- Category: setup
- Author: Provectus
