# ProAgent SDLC Plugin

This plugin provides end-to-end software development lifecycle management for Claude Code.

## Plugin Structure

```
proagent-sdlc/
├── .claude-plugin/plugin.json    # Plugin manifest (name, version, category)
├── .mcp.json                     # MCP server configs (GitHub, GitLab, Jira, Confluence)
├── skills/
│   └── sdlc-assistant/SKILL.md   # Core skill: Managing Software Development Lifecycle
├── commands/
│   ├── hub.md                    # Command hub: list and route to SDLC commands
│   ├── run.md                    # Execute: architect, review-code, plan-release, document, version
│   └── review.md                 # Review: pr, architecture, test-coverage, release-readiness
├── agents/
│   └── sdlc-specialist.md        # SDLC specialist subagent for code review and assessments
├── hooks/
│   └── hooks.json                # Pre-commit quality gates, post-review notifications, pre-push validation
├── CLAUDE.md                     # This file
└── README.md                     # User-facing documentation
```

## Usage

### Skill
Use the `proagent-sdlc:sdlc-assistant` skill when managing any SDLC phase. It covers architecture decisions, code review, testing strategy, release management, documentation, versioning, and git workflows.

### Commands
- `/proagent-sdlc:hub` -- See all available commands and choose the right workflow
- `/proagent-sdlc:run <mode>` -- Execute a workflow (architect, review-code, plan-release, document, version)
- `/proagent-sdlc:review <type>` -- Run a quality review (pr, architecture, test-coverage, release-readiness)

### Agent
The `proagent-sdlc:sdlc-specialist` agent can be dispatched as a subagent for code reviews, architecture assessments, and release readiness checks. It produces structured reports with findings categorized by severity.

### Hooks
Three hooks enforce quality gates:
1. **Pre-commit:** Validates conventional commit format, checks for TODO/FIXME in staged changes, verifies test files exist for new source files
2. **Post-review:** Formats review findings into a structured summary with severity counts and next steps
3. **Pre-push:** Prevents pushing WIP/fixup commits and warns if the branch is behind the remote

### MCP Servers

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **GitLab**: Merge requests, CI/CD pipelines, and project management via `@modelcontextprotocol/server-gitlab`
- **Jira**: Issue tracking, sprint management, and backlog grooming via `@modelcontextprotocol/server-atlassian`
- **Confluence**: Documentation, ADRs, and knowledge base management via `@modelcontextprotocol/server-atlassian`

## Source Attribution

> Built from Provectus internal engineering practices.
