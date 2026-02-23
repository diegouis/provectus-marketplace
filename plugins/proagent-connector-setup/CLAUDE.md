# Provectus Connector Setup Plugin

This plugin provides a guided setup wizard for configuring shared MCP server credentials. It helps users extract Slack tokens from browser DevTools and configure Google Drive OAuth via the GCP Console, then verifies everything works.

## Plugin Scope

The Connector Setup plugin covers two connectors:

1. **Slack** — Extracts `xoxc-` and `xoxd-` tokens from browser cookies and network requests, persists them as environment variables, and verifies live MCP connectivity
2. **Google Drive** — Walks through GCP project creation, Drive API enablement, OAuth consent screen configuration, Desktop app credential creation, OAuth authorization flow, and verification

## Key Conventions

### Security
- Never echo real tokens in shell commands (they'd appear in history)
- Only show first 10 characters of tokens for confirmation
- Use `Write` or `Edit` tools to persist credentials to files
- Hook detects placeholder tokens, not real ones (avoids exposure in hook output)

### User Experience
- Detect OS and shell before giving commands
- Adequacy gates: confirm each step before proceeding
- Bounded iteration: max 3 failed attempts per step, then offer pause/skip/restart
- Lazy-load references only at the step where they're needed

### Architecture
- Empty `.mcp.json`: this plugin configures credentials, it doesn't consume MCP servers
- Thin dispatcher routes to mode files to minimize context loaded per operation
- Single SKILL.md is the source of truth for principles; mode files handle workflow steps

## Plugin Structure

```
proagent-connector-setup/
  .claude-plugin/plugin.json              — v0.1.0 manifest
  .mcp.json                               — Empty (configures, not consumes)
  skills/
    connector-setup-assistant/
      SKILL.md                            — Core skill: scope, principles, verification standards
      references/
        slack-setup.md                    — Token extraction steps, formats, troubleshooting
        google-drive-setup.md             — GCP project, OAuth, auth flow, troubleshooting
  commands/
    proagent-connector-setup-hub.md       — Capabilities overview, command table, quick start
    proagent-connector-setup-run.md       — Thin dispatcher: routes to mode files
    proagent-connector-setup-review.md    — Audit connector configs: token health, permissions, remediation
    modes/
      setup-slack.md                      — 5-step Slack workflow with adequacy gates
      setup-google-drive.md               — 6-step Google Drive workflow with adequacy gates
      verify-all.md                       — Diagnostic status report for all connectors
  agents/
    connector-setup-specialist.md         — Specialist subagent for MCP credential setup and troubleshooting
  hooks/
    hooks.json                            — PostToolUse: detects placeholder tokens in written files
  CLAUDE.md                               — This file
  README.md                               — User-facing installation and usage guide
```

## Design Notes

- **Why empty `.mcp.json`?** If we listed Slack/Google Drive servers here, they'd fail on startup before credentials exist. Other plugins declare these servers — this plugin just configures the credentials they need.
- **Why thin dispatcher + modes/?** Only the relevant mode file gets loaded per invocation, keeping context efficient per PLUGIN-DESIGN-GUIDELINES §1.1.
- **Why lazy-loaded references?** The detailed browser extraction steps and GCP console walkthroughs are only needed at specific steps. Loading them upfront wastes context tokens.
