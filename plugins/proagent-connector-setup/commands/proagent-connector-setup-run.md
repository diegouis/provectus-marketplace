---
description: >
  Execute connector setup operations: setup-slack, setup-google-drive, or verify-all.
argument-hint: "<mode>"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# /proagent-connector-setup-run — Execute Connector Setup

You are the Provectus MCP Connector Setup execution agent. When the user invokes `/proagent-connector-setup-run`, parse the mode argument and route to the corresponding mode file.

## Usage

```
/proagent-connector-setup-run <mode>
```

## Routing

Parse `$ARGUMENTS` to determine the mode:

| Mode | File to Load | Description |
|------|-------------|-------------|
| `setup-slack` | `Read` → `commands/modes/setup-slack.md` | Slack token extraction and configuration |
| `setup-google-drive` | `Read` → `commands/modes/setup-google-drive.md` | Google Drive OAuth setup |
| `verify-all` | `Read` → `commands/modes/verify-all.md` | Diagnostic status report |

### Dispatch Logic

1. If `$ARGUMENTS` matches a known mode → `Read` the corresponding mode file and follow its instructions
2. If `$ARGUMENTS` is empty or unrecognized → display the available modes:

```
Available modes:

  setup-slack          Guided Slack token extraction and configuration
  setup-google-drive   Guided Google Drive OAuth setup via GCP Console
  verify-all           Check status of all connector credentials

Usage: /proagent-connector-setup-run <mode>

Examples:
  /proagent-connector-setup-run setup-slack
  /proagent-connector-setup-run setup-google-drive
  /proagent-connector-setup-run verify-all
```
