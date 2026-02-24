---
description: >
  Guided Slack MCP credential setup: extract xoxc/xoxd tokens from browser DevTools,
  validate format, persist to environment, and verify live connectivity.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Setup Slack — MCP Token Configuration

Walk the user through extracting and configuring Slack MCP credentials. Follow each step sequentially — confirm completion at each adequacy gate before proceeding.

## Step 1: Prerequisites Check

1. Detect the user's OS and shell:
   ```bash
   uname -s && echo $SHELL
   ```
2. Verify `npx` is available:
   ```bash
   which npx 2>/dev/null && npx --version || echo "npx not found"
   ```
3. If `npx` is missing, guide installation (`brew install node` on macOS, or https://nodejs.org/) and **stop until resolved**.

**Adequacy gate**: Confirm OS, shell, and npx are detected before continuing.

## Step 2: Identify Workspace

Ask the user:
- Which Slack workspace do they need to connect?
- Are they currently logged into that workspace in their browser (Chrome or Firefox)?

If they use the desktop app only, explain they need to open `https://app.slack.com` in a browser for token extraction.

**Adequacy gate**: User confirms they have the workspace open in a browser tab.

## Step 3: Extract Tokens

> **CONTEXT GUARD**: ONLY read the reference file below when the user reaches this step. Do NOT pre-load it during earlier steps or at skill initialization.

Load the detailed reference:
```
Read file: skills/connector-setup-assistant/references/slack-setup.md
```

Guide the user through both extractions:

### 3a: Extract `xoxd-` Token (Session Cookie)
1. Walk through Application tab → Cookies → `d` cookie steps from the reference
2. Ask the user to paste the token
3. Validate format: must start with `xoxd-` and be 200+ characters

### 3b: Extract `xoxc-` Token (Client Token)
1. Walk through Network tab → API request → token field steps from the reference
2. Ask the user to paste the token
3. Validate format: must start with `xoxc-` and be 70+ characters

**Bounded iteration**: If validation fails, explain the issue and ask them to re-extract. After **3 failed attempts** per token, offer to:
- Pause and return later
- Try the alternative extraction method from the reference
- Skip Slack setup entirely

**Adequacy gate**: Both tokens pass format validation.

## Step 4: Persist Environment Variables

Present the three storage options from the reference:

| Option | Location | Scope |
|--------|----------|-------|
| A | Project `.env` file | This project only |
| B | Shell profile (`~/.zshrc` or `~/.bashrc`) | All projects |
| C | Dedicated secrets file (`~/.slack-mcp-credentials`) | All projects, isolated |

Ask the user which option they prefer.

**Important**: Use the `Write` tool or `Edit` tool to write tokens — NEVER use `echo` with real token values in Bash commands (they'd appear in shell history).

After writing:
1. Source the file or instruct the user to restart their terminal
2. Verify the variables are set:
   ```bash
   echo "${SLACK_MCP_XOXC_TOKEN:0:10}..." && echo "${SLACK_MCP_XOXD_TOKEN:0:10}..."
   ```
   (Only show first 10 characters for confirmation — never echo full tokens)

**Adequacy gate**: Environment variables are set and show correct prefixes.

## Step 5: Verify Live Connectivity

Test the Slack MCP server:

```bash
# Start the server and capture first 5 seconds of output
timeout 5 npx -y slack-mcp-server@latest --transport stdio 2>&1 || true
```

**Success indicators**:
- Server starts without `invalid_auth` or `not_authed` errors
- No `token_revoked` messages

**Failure handling**:
- `invalid_auth` → Tokens may be from wrong workspace or expired. Re-extract.
- `not_authed` → Environment variables not reaching the process. Check sourcing.
- `token_revoked` → Session expired. Log out/in to Slack in browser, re-extract.

**Bounded iteration**: After 3 failed verification attempts, offer to pause or restart.

## Completion Report

When verification succeeds, present:

```
Slack MCP Setup Complete
========================
Workspace:     [workspace name]
Token storage: [Option A/B/C — location]
xoxc- token:   [first 10 chars]...  ✓ valid format
xoxd- token:   [first 10 chars]...  ✓ valid format
Live test:     ✓ connected successfully

Next steps:
- Plugins with Slack in .mcp.json will now authenticate automatically
- Tokens expire after ~30 days of inactivity — re-run setup if you see auth errors
- Run /proagent-connector-setup-run verify-all to check all connectors
```
