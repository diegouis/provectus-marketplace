# Slack MCP Token Extraction Reference

This reference is loaded at point-of-need during the Slack setup flow. It contains the detailed browser steps for extracting tokens.

## Token Types

| Token Prefix | Name | Source | Purpose |
|-------------|------|--------|---------|
| `xoxc-` | Client token | Browser cookies/network requests | API authentication |
| `xoxd-` | Session token | Browser `d` cookie | Session authentication |
| `xoxb-` | Bot token | Slack App dashboard | Bot user authentication (not used for MCP) |
| `xoxp-` | User token | Slack App dashboard | User-level OAuth (not used for MCP) |

The Slack MCP server requires **both** `xoxc-` and `xoxd-` tokens. These are extracted from your browser session — they are NOT available through the Slack API dashboard.

## Step-by-Step Extraction

### Prerequisites

- You must be logged into your Slack workspace in Chrome or Firefox
- You must have the workspace open in the browser (not the desktop app)

### Method 1: Extract `xoxd-` Token (Session Cookie)

1. Open your Slack workspace in the browser: `https://app.slack.com/client/YOUR_WORKSPACE`
2. Open DevTools: `Cmd+Option+I` (macOS) or `Ctrl+Shift+I` (Windows/Linux)
3. Navigate to **Application** tab (Chrome) or **Storage** tab (Firefox)
4. In the left sidebar, expand **Cookies** → click on `https://app.slack.com`
5. Find the cookie named **`d`**
6. Copy the cookie **Value** — it starts with `xoxd-`

> **Tip**: The `d` cookie value is very long (200+ characters). Make sure you copy the entire value. Double-click the value cell to select all of it.

### Method 2: Extract `xoxc-` Token (Client Token)

1. Stay in DevTools, switch to the **Network** tab
2. In the filter bar, type `api/` to filter for Slack API requests
3. Perform any action in Slack (send a message, switch channels, etc.) to trigger API calls
4. Click on any API request (e.g., `conversations.list`, `chat.postMessage`)
5. In the request details, look at the **Request Body** or **Form Data**
6. Find the `token` field — its value starts with `xoxc-`

> **Alternative**: You can also find `xoxc-` in the **Console** tab by running:
> ```javascript
> // In browser console on app.slack.com
> JSON.parse(localStorage.localConfig_v2).teams[Object.keys(JSON.parse(localStorage.localConfig_v2).teams)[0]].token
> ```

## Token Format Validation

| Token | Expected Pattern | Approximate Length |
|-------|-----------------|-------------------|
| `xoxc-` | `xoxc-` followed by alphanumeric + hyphens | 70–200 characters |
| `xoxd-` | `xoxd-` followed by URL-safe base64 | 200–400 characters |

Tokens that don't match these patterns are likely truncated or from the wrong source.

## Storage Options

The user chooses where to persist their tokens. Present all four options:

### Option A: Project `.env` File

```bash
# Add to .env in project root (already in .gitignore)
echo 'SLACK_MCP_XOXC_TOKEN=xoxc-YOUR-TOKEN-HERE' >> .env
echo 'SLACK_MCP_XOXD_TOKEN=xoxd-YOUR-TOKEN-HERE' >> .env
```

**Pros**: Scoped to project. **Cons**: Must repeat per project.

### Option B: Shell Profile (Global)

For zsh (`~/.zshrc`):
```bash
export SLACK_MCP_XOXC_TOKEN="xoxc-YOUR-TOKEN-HERE"
export SLACK_MCP_XOXD_TOKEN="xoxd-YOUR-TOKEN-HERE"
```

For bash (`~/.bashrc` or `~/.bash_profile`):
```bash
export SLACK_MCP_XOXC_TOKEN="xoxc-YOUR-TOKEN-HERE"
export SLACK_MCP_XOXD_TOKEN="xoxd-YOUR-TOKEN-HERE"
```

**Pros**: Available everywhere. **Cons**: Persists in dotfiles.

### Option C: Dedicated Secrets File

```bash
# Create a dedicated file
echo 'export SLACK_MCP_XOXC_TOKEN="xoxc-YOUR-TOKEN-HERE"' > ~/.slack-mcp-credentials
echo 'export SLACK_MCP_XOXD_TOKEN="xoxd-YOUR-TOKEN-HERE"' >> ~/.slack-mcp-credentials
chmod 600 ~/.slack-mcp-credentials

# Source it from your shell profile
echo 'source ~/.slack-mcp-credentials' >> ~/.zshrc
```

**Pros**: Isolated, restrictive permissions. **Cons**: Extra file to manage.

### Option D: Claude Desktop Config (MCP-native)

Write tokens directly into `claude_desktop_config.json` so Claude Desktop's Slack MCP server picks them up natively — no environment variables needed.

**macOS path**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows path**: `%APPDATA%\Claude\claude_desktop_config.json`

The Slack MCP server entry should look like:

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "slack-mcp-server@latest", "--transport", "stdio"],
      "env": {
        "SLACK_MCP_XOXC_TOKEN": "xoxc-YOUR-TOKEN-HERE",
        "SLACK_MCP_XOXD_TOKEN": "xoxd-YOUR-TOKEN-HERE",
        "SLACK_MCP_USERS_CACHE": ".users_cache.json",
        "SLACK_MCP_CHANNELS_CACHE": ".channels_cache_v2.json"
      }
    }
  }
}
```

**After editing**: Restart Claude Desktop so it loads the updated tokens. This applies whether you edited the file from Claude Code (CLI) or from Claude Desktop itself (via Cowork mode). Claude Desktop reads this config on launch, so a restart is required for changes to take effect.

**Pros**: Native MCP integration, no env vars to manage, tokens travel with Claude Desktop config.
**Cons**: Tokens are in a JSON file (ensure it's not tracked by git), scoped to Claude Desktop (Claude Code CLI plugins that reference `${SLACK_MCP_XOXC_TOKEN}` in `.mcp.json` still need env vars unless you also set them).

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Token starts with `xoxb-` or `xoxp-` | Extracted from Slack App dashboard, not browser | Use browser DevTools method above |
| `xoxd-` is short (<100 chars) | Cookie value truncated during copy | Double-click the cell in DevTools to select full value |
| `xoxc-` not found in network requests | No API calls captured | Perform an action in Slack (send message), then check network tab |
| MCP server starts but returns "invalid_auth" | Token expired or from wrong workspace | Re-extract tokens from a fresh browser session |
| MCP server starts but returns "token_revoked" | Slack session expired (e.g., password change) | Log out and back into Slack in the browser, then re-extract |
| "not_authed" error | Environment variable not set or empty | Verify with `echo $SLACK_MCP_XOXC_TOKEN | head -c 10` |
| Token works in curl but not MCP | Missing `xoxd-` token (both are required) | Ensure both `SLACK_MCP_XOXC_TOKEN` and `SLACK_MCP_XOXD_TOKEN` are set |

## Token Refresh

Slack browser tokens expire when:
- You log out of the workspace
- You change your password
- The workspace admin forces a session reset
- After approximately 30 days of inactivity

When tokens expire, re-run `/proagent-connector-setup-run setup-slack` to extract fresh tokens.
