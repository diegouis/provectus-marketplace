# ProAgent Platform Engineering Plugin

This plugin provides platform engineering capabilities for Claude Code — developer experience, internal tooling, service catalogs, golden paths, scaffolding, MCP server development, plugin systems, document generation (PDF/DOCX/PPTX/XLSX), reproducible environments, and setup orchestration. Built from 107 assets across 13 source repositories.

## Structure

```
proagent-platform/
├── .claude-plugin/plugin.json    # Plugin manifest
├── skills/
│   └── platform-assistant/       # Core skill: Building Developer Platforms & Tooling
├── commands/
│   ├── proagent-platform-hub.md     # /proagent-platform:hub — capabilities overview
│   ├── proagent-platform-run.md     # /proagent-platform:run — scaffold, create-template, build-tool, setup-dx
│   └── proagent-platform-review.md  # /proagent-platform:review — review dx, tooling, templates
├── agents/platform-specialist.md # Platform engineering specialist subagent
├── hooks/hooks.json              # Template validation, plugin manifest checks, DX tracking
├── .mcp.json                     # GitHub, GitLab, Slack integrations
└── README.md                     # Installation & usage
```

## Commands

| Command | Description |
|---------|-------------|
| `/proagent-platform:hub` | Browse all 107 platform assets by type |
| `/proagent-platform:run scaffold` | Generate projects from golden path templates |
| `/proagent-platform:run create-template` | Build reusable project templates |
| `/proagent-platform:run build-tool` | Create CLI tools, integrations, MCP servers |
| `/proagent-platform:run setup-dx` | Set up or audit developer experience |
| `/proagent-platform:run generate-doc` | Generate documents (PDF, DOCX, PPTX, XLSX) |
| `/proagent-platform:review dx` | DX scorecard across 5 dimensions |
| `/proagent-platform:review tooling` | Internal tooling quality and health |
| `/proagent-platform:review templates` | Template library coverage and freshness |
| `/proagent-platform:review plugins` | Plugin system health, lifecycle, and extensibility |

## MCP Integrations

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **GitLab**: Project templates, CI/CD pipelines, and merge requests via `@modelcontextprotocol/server-gitlab`
- **Rube (Composio)**: SaaS automation gateway for Notion, Confluence, Figma, and 200+ integrations via `https://rube.app/mcp`

## Key Conventions

- All scaffolded projects must include a CLAUDE.md, README.md, and CI config
- Templates use variable interpolation with `{{variable}}` syntax
- MCP servers follow the official `@modelcontextprotocol/server-*` package pattern
- Plugin manifests must validate against the `.claude-plugin/plugin.json` schema
- Document generation follows the awesome-claude-skills patterns (PDF via `pdf/SKILL.md`, DOCX via `docx/SKILL.md`, PPTX via `pptx/SKILL.md`, XLSX via `xlsx/SKILL.md`)
- Project scaffolding supports Python (`python-scaffold.md`) and TypeScript (`typescript-scaffold.md`) golden paths from the agents repo
- Plugin lifecycle management follows patterns from casdk-harness (`plugin_manager.py`) and gastown (`internal/cmd/plugin.go`)

## Source Repositories

> Built from 107 assets across 13 Provectus source repos: agents, awesome-claude-code, awesome-claude-skills, awos, casdk-harness, gastown, planning-with-files, proagent-repo, provectus-marketplace, ralph-orchestrator, skills, superpowers, taches-cc-resources.
