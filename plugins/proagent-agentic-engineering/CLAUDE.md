# ProAgent Agentic Engineering Plugin

This plugin provides comprehensive tooling for building, orchestrating, and optimizing AI agent systems with Claude Code.

## What This Plugin Provides

- **Skill**: `Building Agentic Systems` -- Comprehensive autonomous capability covering agent design, skill/command/hook creation, MCP server development, multi-agent orchestration, prompt engineering, and agent evaluation. Located in `skills/agentic-engineering-assistant/SKILL.md`.

- **Agent**: `agentic-engineering-specialist` -- Specialist sub-agent with deep knowledge of Claude Code component architecture, multi-agent patterns, and context engineering. Located in `agents/agentic-engineering-specialist.md`.

- **Commands**:
  - `/proagent-agentic-engineering` -- Hub command showing capabilities and routing to sub-commands
  - `/proagent-agentic-engineering-run` -- Task runner for creating agents, skills, commands, hooks, MCP servers, plugins, orchestrating workflows, and evaluating agents
  - `/proagent-agentic-engineering-review` -- Review agent systems, skills, prompts, and orchestration patterns for quality

- **Hooks**: PreToolUse validation for agent artifacts, PostToolUse audit logging, and SessionStart context loading. Configured in `hooks/hooks.json`.

- **MCP Servers**: Pre-configured connections for agent development and testing. Configured in `.mcp.json`:
  - **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
  - **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
  - **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
  - **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
  - **GitLab**: Merge requests, CI/CD pipelines, and project management via `@modelcontextprotocol/server-gitlab`
  - **Playwright**: Browser automation for E2E testing and visual validation via `@playwright/mcp@latest`
  - **Rube (Composio)**: SaaS automation gateway providing access to 200+ integrations with session-based isolation and automatic OAuth via `https://rube.app/mcp`

## Key Conventions

- Agent definitions use YAML frontmatter with `name`, `description` (with `<example>` blocks), optional `tools`, `model`, and `color` fields
- Skills require YAML frontmatter with `name` and `description` (including trigger terms) in a `SKILL.md` file within a named directory
- Commands use YAML frontmatter with `description` and `argument-hint`, supporting `$ARGUMENTS`, `$1`/`$2`, `@file`, and `!command`
- Hooks are JSON configurations in `.claude/settings.json` with event names as keys, matchers for tool filtering, and shell commands that process stdin JSON via `jq`
- Plugins require `.claude-plugin/plugin.json` with `name`, `version` (semver), and `description`
- MCP servers should be workflow-oriented (not raw API wrappers) with input validation and actionable error messages

## Source Repositories

This plugin synthesizes patterns from 19 repositories with 612 total assets:
- casdk-harness (context engineering plugin, 14 agents, 12 skills)
- superpowers (SDD, parallel agents, TDD, brainstorming, 13 skills)
- awesome-claude-skills (skill-creator, mcp-builder, 30+ skills)
- taches-cc-resources (agent/hook/command creation, 27 commands)
- ralph-orchestrator (PDD, eval, code-assist, 12 skills)
- proagent-repo GUI (TAC principles: ADW, Core Four, Trust Ladder)
- planning-with-files (file-based planning with hooks)
- awos (product-to-implementation pipeline, 16 commands)
