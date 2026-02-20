# proagent-documentation

Provectus Documentation practice plugin for the agentic coding platform. Provides automated documentation generation from GitHub and GitLab repositories, with direct Confluence publishing and synchronization.

## Installation

Copy the `proagent-documentation/` directory into your Claude Code plugins directory, or install via the Provectus marketplace.

## What It Does

- **Repository Analysis** — Scan any GitHub or GitLab repo to extract project structure, tech stack, API endpoints, dependencies, and CI/CD configuration
- **Document Generation** — Generate README, architecture docs, API reference, onboarding guides, and operational runbooks
- **Confluence Publishing** — Create or update Confluence pages with proper formatting, macros, labels, and page hierarchy
- **Documentation Sync** — Detect repo changes and update stale Confluence pages automatically
- **Batch Processing** — Process multiple repos and generate a documentation index
- **Documentation Review** — Audit quality, coverage, and freshness of existing documentation

## Commands

| Command | Description |
|---------|-------------|
| `/proagent-documentation-hub` | Browse documentation capabilities and get routed to the right operation |
| `/proagent-documentation-run analyze-repo` | Scan a GitHub/GitLab repo — extract structure, tech stack, patterns |
| `/proagent-documentation-run generate-docs` | Generate documentation (README, architecture, API, onboarding, runbook) |
| `/proagent-documentation-run publish-confluence` | Create or update a Confluence page from generated docs |
| `/proagent-documentation-run sync-docs` | Compare repo state with Confluence pages, update stale content |
| `/proagent-documentation-run batch-docs` | Process multiple repos and generate a documentation index |
| `/proagent-documentation-review doc-quality` | Assess documentation completeness, accuracy, and readability |
| `/proagent-documentation-review confluence-audit` | Check Confluence pages for staleness, broken links, outdated content |
| `/proagent-documentation-review coverage` | Identify undocumented repos, modules, or APIs |

## Plugin Structure

```
proagent-documentation/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── documentation-assistant/
│       └── SKILL.md
├── commands/
│   ├── proagent-documentation-hub.md
│   ├── proagent-documentation-run.md
│   └── proagent-documentation-review.md
├── agents/
│   ├── documentation-specialist.md
│   ├── repo-analyzer.md
│   └── confluence-publisher.md
├── hooks/
│   └── hooks.json
├── .mcp.json
├── CLAUDE.md
└── README.md
```

## Agents

| Agent | Role |
|-------|------|
| **documentation-specialist** | Primary orchestrator — coordinates analysis, generation, and publishing |
| **repo-analyzer** | Scans GitHub/GitLab repos to extract structured project metadata |
| **confluence-publisher** | Handles Confluence page creation, updates, formatting, and label management |

## Hooks

| Hook | Trigger | Purpose |
|------|---------|---------|
| PreToolUse (Bash) | Destructive commands on doc directories | Block accidental deletion of documentation |
| PreToolUse (Write) | Overwriting existing doc files | Warn before overwriting manually-written docs |
| PostToolUse (Write) | Documentation file written | Remind to review before publishing |
| PostToolUse (Task) | Confluence publish task | Remind to verify published page |

## MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| GitHub | `@modelcontextprotocol/server-github` | Repository file access, PR scanning, Actions config |
| GitLab | `@modelcontextprotocol/server-gitlab` | Repository file access, MR scanning, CI pipeline config |
| Confluence | `@modelcontextprotocol/server-atlassian` | Page creation, update, publishing, label management |
| Slack | `slack-mcp-server@latest` | Notification of doc updates, team collaboration |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Import/export from Google Docs and Sheets |
| Google Workspace | `mcp-gsuite` | Calendar integration for doc review scheduling |

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GITHUB_PERSONAL_ACCESS_TOKEN` | Yes | GitHub PAT for repository access |
| `GITLAB_PERSONAL_ACCESS_TOKEN` | For GitLab repos | GitLab PAT for repository access |
| `GITLAB_API_URL` | No | GitLab API URL (default: `https://gitlab.com/api/v4`) |
| `ATLASSIAN_SITE_URL` | For Confluence | Your Atlassian site URL (e.g., `https://yoursite.atlassian.net`) |
| `ATLASSIAN_USER_EMAIL` | For Confluence | Atlassian account email |
| `ATLASSIAN_API_TOKEN` | For Confluence | Atlassian API token |
| `SLACK_MCP_XOXC_TOKEN` | For Slack | Slack xoxc token |
| `SLACK_MCP_XOXD_TOKEN` | For Slack | Slack xoxd token |

## Version

0.2.0
