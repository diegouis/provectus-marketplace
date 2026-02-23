---
description: >
  Diagnostic status report for all MCP connectors: checks environment variables,
  token formats, credential files, auth caches, and reports READY/NEEDS SETUP/DEGRADED.
allowed-tools: Read, Bash, Glob, Grep
---

# Verify All — Connector Status Report

Run a comprehensive diagnostic across all supported MCP connectors and present a status report. This is a read-only operation — it does not modify any files or credentials.

## Diagnostic Procedure

Run all checks in sequence and collect results for the final report.

### 1. Slack Connector Checks

#### 1a. Environment Variables

```bash
# Check if variables are set (don't echo full values)
if [ -n "$SLACK_MCP_XOXC_TOKEN" ]; then
  echo "SLACK_MCP_XOXC_TOKEN: SET (${SLACK_MCP_XOXC_TOKEN:0:10}...)"
else
  echo "SLACK_MCP_XOXC_TOKEN: NOT SET"
fi

if [ -n "$SLACK_MCP_XOXD_TOKEN" ]; then
  echo "SLACK_MCP_XOXD_TOKEN: SET (${SLACK_MCP_XOXD_TOKEN:0:10}...)"
else
  echo "SLACK_MCP_XOXD_TOKEN: NOT SET"
fi
```

#### 1b. Token Format Validation

```bash
# Validate prefixes
echo "$SLACK_MCP_XOXC_TOKEN" | grep -qE '^xoxc-' && echo "xoxc format: VALID" || echo "xoxc format: INVALID or NOT SET"
echo "$SLACK_MCP_XOXD_TOKEN" | grep -qE '^xoxd-' && echo "xoxd format: VALID" || echo "xoxd format: INVALID or NOT SET"
```

#### 1c. Token Source Detection

```bash
# Check where tokens might be defined
grep -rl 'SLACK_MCP_XOXC_TOKEN' ~/.zshrc ~/.bashrc ~/.bash_profile .env ~/.slack-mcp-credentials 2>/dev/null || echo "Token source: not found in common locations"
```

### 2. Google Drive Connector Checks

#### 2a. OAuth Credential File

```bash
# Check credential file
if [ -f ~/gcp-oauth.keys.json ]; then
  echo "gcp-oauth.keys.json: PRESENT"
  python3 -c "
import json
with open('$HOME/gcp-oauth.keys.json') as f:
    data = json.load(f)
    if 'installed' in data:
        print('Credential type: Desktop app (correct)')
    elif 'web' in data:
        print('Credential type: Web application (WRONG — needs Desktop app)')
    else:
        print('Credential type: Unknown format')
" 2>/dev/null || echo "Credential file: INVALID JSON"
else
  echo "gcp-oauth.keys.json: NOT FOUND"
fi
```

#### 2b. Auth Cache

```bash
# Check auth cache
if [ -f ~/.gdrive-server/credentials.json ]; then
  echo "Auth cache: PRESENT"
else
  echo "Auth cache: NOT FOUND (need to run auth flow)"
fi
```

### 3. Tool Availability

```bash
# Check required CLI tools
which npx 2>/dev/null && echo "npx: $(npx --version)" || echo "npx: NOT FOUND"
which uvx 2>/dev/null && echo "uvx: available" || echo "uvx: NOT FOUND (optional)"
which node 2>/dev/null && echo "node: $(node --version)" || echo "node: NOT FOUND"
```

## Status Report

After collecting all diagnostic results, present the report as a table:

```
MCP Connector Status Report
============================

| Connector      | Status       | Details                                        |
|----------------|-------------|------------------------------------------------|
| Slack          | [STATUS]    | [details]                                      |
| Google Drive   | [STATUS]    | [details]                                      |

Tool Availability:
| Tool  | Status       |
|-------|-------------|
| npx   | [version or NOT FOUND] |
| uvx   | [available or NOT FOUND] |
| node  | [version or NOT FOUND] |
```

### Status Values

Determine each connector's status using this logic:

**READY** — All credentials present, format valid, files in place
- Slack: Both `SLACK_MCP_XOXC_TOKEN` (xoxc- prefix) and `SLACK_MCP_XOXD_TOKEN` (xoxd- prefix) set
- Google Drive: `~/gcp-oauth.keys.json` present with `"installed"` key AND `~/.gdrive-server/credentials.json` exists

**NEEDS SETUP** — Credentials missing entirely
- Slack: One or both env vars not set
- Google Drive: `~/gcp-oauth.keys.json` not found

**DEGRADED** — Credentials present but potentially invalid
- Slack: Env vars set but wrong prefix (e.g., xoxb- instead of xoxc-)
- Google Drive: Credential file present but wrong type (`"web"` instead of `"installed"`), or credential file present but auth cache missing

## Recommended Next Steps

Based on the status, recommend specific actions:

- If Slack is NEEDS SETUP or DEGRADED: `Run /proagent-connector-setup-run setup-slack`
- If Google Drive is NEEDS SETUP or DEGRADED: `Run /proagent-connector-setup-run setup-google-drive`
- If all READY: "All connectors are configured. Plugins with these MCP servers in their .mcp.json will authenticate automatically."
