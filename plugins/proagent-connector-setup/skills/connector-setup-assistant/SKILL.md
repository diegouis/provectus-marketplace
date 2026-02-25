---
name: connector-setup-assistant
description: MCP connector credential setup wizard — guides users through extracting Slack tokens (xoxc/xoxd) from browser DevTools, configuring Google Drive OAuth via GCP console, persisting credentials, and verifying live MCP connectivity. Use when setting up, troubleshooting, or verifying Slack or Google Drive MCP server credentials.
---

# MCP Connector Setup Assistant

Guides users through first-time credential configuration for shared MCP servers (Slack, Google Drive). This skill orchestrates the setup workflow — it does NOT consume MCP servers itself.

## CRITICAL: Ask First, Load Later

**DO NOT** read reference files, run environment detection commands, or load mode files until the user has told you what they want to do. When invoked:

1. **Greet the user** and present the available options
2. **Wait for their choice** before loading anything
3. **Only then** load the relevant mode file for their chosen connector

This prevents context explosion from eagerly loading all instructions at once.

## When to Use

- User needs to set up Slack or Google Drive MCP credentials
- User wants to verify existing connector credentials
- User is troubleshooting MCP authentication failures

## Scope

Covers **credential setup only** — not day-to-day use of Slack or Google Drive.

| Connector | MCP Package | Required Credentials |
|-----------|-------------|---------------------|
| Slack | `slack-mcp-server` | `SLACK_MCP_XOXC_TOKEN`, `SLACK_MCP_XOXD_TOKEN` (env vars or `claude_desktop_config.json`) |
| Google Drive | `@modelcontextprotocol/server-gdrive` | `~/gcp-oauth.keys.json` + OAuth auth cache |

## Routing

When the user states their intent, route to the appropriate mode file:

| User wants to... | Action |
|-------------------|--------|
| Set up Slack | Read and follow `commands/modes/setup-slack.md` |
| Set up Google Drive | Read and follow `commands/modes/setup-google-drive.md` |
| Verify all connectors | Read and follow `commands/modes/verify-all.md` |
| General question | Answer from your knowledge — do NOT load mode files |

## Principles (apply to all flows)

1. **Never display real tokens** — Use `Write`/`Edit` to persist credentials; show only first 10 characters for confirmation
2. **Adequacy gates** — Confirm each step before proceeding (user may need to switch to browser)
3. **Bounded iteration** — After 3 failed attempts at any step, offer to pause/skip/restart
4. **Verify before declaring success** — Every setup ends with a live connectivity check
5. **Detect environment at the start of a flow** — Not upfront when the skill loads, but as the first step of the chosen mode

## Reference Files (lazy-load only)

These contain detailed extraction steps. **DO NOT read them until the corresponding mode file instructs you to:**

- `skills/connector-setup-assistant/references/slack-setup.md` — Slack token extraction details
- `skills/connector-setup-assistant/references/google-drive-setup.md` — GCP OAuth setup details
