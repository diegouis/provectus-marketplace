# proagent-platform

ProAgent plugin for **Platform Engineering** — developer experience, internal tooling, service catalogs, golden paths, scaffolding, MCP server development, plugin systems, document generation (PDF/DOCX/PPTX/XLSX), reproducible environments, and setup orchestration. Built from 107 assets across 13 source repositories.

## Installation

### Claude Code (CLI)

```bash
# Add to your project's settings
claude settings add plugin /path/to/proagent-platform
```

### Claude Desktop

Add to your Claude Desktop MCP configuration (see Claude Desktop docs for plugin support).

## Commands

| Command | Description |
|---------|-------------|
| `/proagent-platform:hub` | Browse all platform assets and capabilities |
| `/proagent-platform:run scaffold` | Generate projects from golden path templates (Python, TypeScript) |
| `/proagent-platform:run create-template` | Build reusable project/component templates |
| `/proagent-platform:run build-tool` | Create CLI tools, integrations, or MCP servers |
| `/proagent-platform:run setup-dx` | Set up or audit developer experience (incl. Nix/devenv) |
| `/proagent-platform:run generate-doc` | Generate documents (PDF, DOCX, PPTX, XLSX) |
| `/proagent-platform:review dx` | DX scorecard (discoverability, onboarding, tooling, docs, feedback) |
| `/proagent-platform:review tooling` | Internal tooling quality and health audit |
| `/proagent-platform:review templates` | Template library coverage, quality, and freshness |
| `/proagent-platform:review plugins` | Plugin system health, lifecycle, and extensibility audit |

## Components

- **Skill**: Building Developer Platforms & Tooling (9 capability areas incl. document generation, reproducible environments, file organization)
- **Agent**: Platform engineering specialist (scaffolding, MCP servers, DX optimization, document generation, setup orchestration)
- **Hooks**: Template validation, plugin manifest checks, DX metric tracking
- **MCP**: GitHub, GitLab, Slack, Google Drive, Google Workspace, Excalidraw, Rube integrations

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |
| GitLab | `@modelcontextprotocol/server-gitlab` | Project templates, CI/CD pipelines |
| Rube | `rube.app/mcp` | SaaS automation via Composio SDK |

## Source Repositories

> Built from 107 assets across 13 repos: agents, awesome-claude-code, awesome-claude-skills, awos, casdk-harness, gastown, planning-with-files, proagent-repo, provectus-marketplace, ralph-orchestrator, skills, superpowers, taches-cc-resources.

## Requirements

| Tool | Purpose |
|------|---------|
| Claude Code 2.0+ | Plugin runtime |
| Node.js 18+ | MCP server execution |
| GitHub CLI (`gh`) | Repository operations |

## Environment Variables

```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your-token"
export GITLAB_PERSONAL_ACCESS_TOKEN="your-token"
export SLACK_BOT_TOKEN="your-slack-bot-token"
export SLACK_TEAM_ID="your-team-id"
```

## Version

0.3.0
