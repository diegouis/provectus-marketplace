---
name: connector-setup-assistant
description: MCP connector credential setup wizard — guides users through extracting Slack tokens (xoxc/xoxd) from browser DevTools, configuring Google Drive OAuth via GCP console, persisting credentials, and verifying live MCP connectivity. Use when setting up, troubleshooting, or verifying Slack or Google Drive MCP server credentials.
---

# MCP Connector Setup Assistant

Single source of truth for guiding users through first-time credential configuration for shared MCP servers (Slack, Google Drive). This skill orchestrates the setup workflow — it does NOT consume MCP servers itself.

## When to Use This Skill

- User needs to set up Slack MCP credentials for the first time
- User needs to configure Google Drive OAuth for MCP access
- User wants to verify that existing connector credentials are working
- User is troubleshooting authentication failures with Slack or Google Drive MCP servers
- User asks "how do I connect Slack?" or "set up Google Drive"

## Scope

This skill covers **credential setup only** — not the day-to-day use of Slack or Google Drive. Once credentials are configured, the user should use the respective MCP servers directly (via other plugins that declare them in `.mcp.json`).

### Supported Connectors

| Connector | MCP Package | Required Credentials |
|-----------|-------------|---------------------|
| Slack | `slack-mcp-server` | `SLACK_MCP_XOXC_TOKEN`, `SLACK_MCP_XOXD_TOKEN` |
| Google Drive | `@modelcontextprotocol/server-gdrive` | `~/gcp-oauth.keys.json` + OAuth auth cache |

## Principles

### 1. Detect the User's Environment First

Before giving shell commands, detect the OS and shell:

```bash
# Detect OS
uname -s  # Darwin = macOS, Linux = Linux

# Detect shell
echo $SHELL  # /bin/zsh, /bin/bash, /bin/fish
```

Adapt all file paths and export commands to the detected environment. Do not assume zsh on Linux or bash on macOS.

### 2. Never Display or Log Real Tokens

- When showing examples, use clearly fake tokens: `xoxc-EXAMPLE-NOT-REAL`, `xoxd-EXAMPLE-NOT-REAL`
- When the user pastes a real token, acknowledge receipt without echoing it back
- When writing tokens to files, use `Write` tool — never `echo` tokens into shell commands where they'd appear in history

### 3. Verify Before Declaring Success

Every setup flow must end with a live verification step. Do not tell the user "you're all set" until the MCP server actually responds:

- **Slack**: Start the MCP server process and confirm it connects without auth errors
- **Google Drive**: Run `npx @modelcontextprotocol/server-gdrive` and confirm OAuth flow completes

### 4. Adequacy Gates

Each step in a multi-step flow must confirm completion before proceeding. The user may need to switch to a browser, create a GCP project, or copy a cookie — these are async human actions. Always ask "Have you completed this step?" before moving on.

### 5. Bounded Iteration

If a verification step fails:
1. Explain what went wrong
2. Suggest a fix
3. Re-attempt verification

After **3 failed attempts** at the same step, offer to:
- Pause and come back later
- Skip to the next connector
- Restart the current connector setup from scratch

### 6. Fallback for Missing Tools

Before running `npx` or `uvx`, verify the tool exists:

```bash
which npx 2>/dev/null || echo "npx not found"
which uvx 2>/dev/null || echo "uvx not found"
```

If missing, provide installation guidance:
- `npx` → install Node.js from https://nodejs.org/ or via `brew install node`
- `uvx` → install uv from https://docs.astral.sh/uv/getting-started/installation/

## Reference Loading

Detailed extraction and troubleshooting steps are in reference files. Load them at the point of need, not upfront:

- **Slack token extraction**: `Read` file `skills/connector-setup-assistant/references/slack-setup.md` when the user reaches the token extraction step
- **Google Drive OAuth setup**: `Read` file `skills/connector-setup-assistant/references/google-drive-setup.md` when the user reaches the GCP project creation step

## Verification Standards

### Slack Verification

```bash
# Quick format check
echo "$SLACK_MCP_XOXC_TOKEN" | grep -qE '^xoxc-' && echo "xoxc format OK" || echo "xoxc format INVALID"
echo "$SLACK_MCP_XOXD_TOKEN" | grep -qE '^xoxd-' && echo "xoxd format OK" || echo "xoxd format INVALID"
```

Then attempt to start the MCP server and watch for auth errors in the first 5 seconds of output.

### Google Drive Verification

1. Check `~/gcp-oauth.keys.json` exists and contains valid JSON with `installed.client_id`
2. Check for auth cache at `~/.gdrive-server/credentials.json`
3. Attempt to start the MCP server and confirm OAuth handshake
