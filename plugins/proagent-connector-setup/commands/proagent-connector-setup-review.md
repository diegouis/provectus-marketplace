---
description: >
  Review and audit MCP connector configurations: token health, file permissions,
  storage locations, credential expiration, and end-to-end connectivity verification
  with remediation guidance.
argument-hint: "[connector]"
allowed-tools: Read, Bash, Glob, Grep
---

# /proagent-connector-setup-review - Review Connector Configurations

You are the Provectus Connector Setup review agent. When the user invokes `/proagent-connector-setup-review`, perform a comprehensive audit of MCP connector configurations.

## Usage

```
/proagent-connector-setup-review [connector]
```

If no connector is specified, review all configured connectors.

## Review Targets

### Auto-Detection

When no specific connector is provided, scan for all known credential sources:

| Priority | Credential Source | Review Type |
|----------|------------------|-------------|
| 1 | `SLACK_MCP_XOXC_TOKEN` / `SLACK_MCP_XOXD_TOKEN` (env vars) | Slack token health |
| 2 | `.env`, `.env.local`, `.env.production` files | Token storage and exposure |
| 3 | `gcp-oauth.keys.json` | Google Drive OAuth credential file |
| 4 | `~/.gdrive-mcp/` or equivalent token cache | Google Drive token cache |
| 5 | `.mcp.json` files in plugin directories | MCP server configuration |
| 6 | Shell profile files (`~/.zshrc`, `~/.bashrc`) | Credential exports |
| 7 | `claude_desktop_config.json` | Claude Desktop MCP-native token storage |

### Slack Connector Review

**Token Presence:**
- [ ] `SLACK_MCP_XOXC_TOKEN` is set and non-empty
- [ ] `SLACK_MCP_XOXD_TOKEN` is set and non-empty

**Token Format:**
- [ ] `xoxc-` token has correct prefix and reasonable length (50+ chars)
- [ ] `xoxd-` token has correct prefix and reasonable length (50+ chars)
- [ ] Neither token contains placeholder text (`your-token-here`, `TODO`, `xxx`)

**Storage Security:**
- [ ] Tokens are not hardcoded in tracked files (`git ls-files` check)
- [ ] `.env` files containing tokens are in `.gitignore`
- [ ] Token files have restrictive permissions (not world-readable)
- [ ] Tokens are not present in shell history

**Claude Desktop Config (`claude_desktop_config.json`):**
- [ ] If tokens are stored in `claude_desktop_config.json`, the file is not tracked by git
- [ ] Slack MCP server entry under `mcpServers.slack` has correct structure (command, args, env)
- [ ] `SLACK_MCP_XOXC_TOKEN` and `SLACK_MCP_XOXD_TOKEN` in env block have correct prefixes
- [ ] Config file is not world-readable

**Connectivity:**
- [ ] Slack MCP server starts without error
- [ ] Server can list at least one channel (token is valid and not expired)

### Google Drive Connector Review

**OAuth Credentials:**
- [ ] `gcp-oauth.keys.json` exists in expected location
- [ ] Credential file contains valid JSON with `client_id` and `client_secret`
- [ ] Credential file has restrictive permissions (not world-readable)
- [ ] Credential file is not tracked by git

**Token Cache:**
- [ ] OAuth token cache exists (authorization flow was completed)
- [ ] Token cache has restrictive permissions
- [ ] Token cache is not tracked by git

**GCP Project:**
- [ ] Drive API is referenced in credentials (correct project)
- [ ] OAuth client type is "Desktop" (not "Web application")

**Connectivity:**
- [ ] Google Drive MCP server starts without error
- [ ] Server can list files (token is valid and not expired)

### Cross-Connector Review

**MCP Configuration:**
- [ ] `.mcp.json` files reference correct server packages
- [ ] Environment variable names match what servers expect
- [ ] No conflicting credential definitions across plugins

**File Permissions Audit:**
- [ ] All credential files: `chmod 600` or more restrictive
- [ ] All credential directories: `chmod 700` or more restrictive
- [ ] No credential files owned by root when user runs as non-root

**Git Safety:**
- [ ] `.gitignore` includes: `.env*`, `*.keys.json`, `gcp-oauth.*`, token cache dirs
- [ ] No credentials appear in `git log` history
- [ ] No credentials in staged or unstaged changes

## Output Format

For each reviewed connector, provide:

```
## Review: <connector>

### Summary
<one-line assessment: READY / NEEDS ATTENTION / DEGRADED / NOT CONFIGURED>

### Checks

#### Passed
- [x] <check description>

#### Failed
- [ ] <check description> — <remediation>

#### Skipped
- [-] <check description> — <reason>

### Connectivity: PASS / FAIL / SKIPPED
```

After all connectors are reviewed, provide:

```
## Overall Connector Health

### Status: HEALTHY / NEEDS ATTENTION / DEGRADED

| Connector | Status | Issues |
|-----------|--------|--------|
| Slack     | ...    | ...    |
| Google Drive | ... | ...    |

### Remediation Steps (ordered by priority)
1. <highest priority fix with specific commands>
2. <next priority fix>
3. ...

### Security Notes
- <any security concerns found>
```
