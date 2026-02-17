# ProAgent Agentic Engineering

Provectus plugin for building, orchestrating, and optimizing AI agent systems with Claude Code.

## Features

- **Agent Design**: Create specialized sub-agents with focused responsibilities, discovery-optimized descriptions, and appropriate tool restrictions
- **Skill Creation**: Build model-invoked autonomous capabilities with progressive disclosure and trigger-term optimization
- **Command Creation**: Design user-invoked slash commands with argument handling, file references, and bash execution
- **Hook Configuration**: Automate lifecycle events with deterministic shell commands for formatting, logging, validation, and notifications
- **Plugin Development**: Bundle agents, skills, commands, hooks, and MCP servers into distributable packages
- **MCP Server Development**: Build Model Context Protocol servers to connect Claude to external APIs
- **Multi-Agent Orchestration**: Design sequential pipelines, parallel fan-out, hierarchical delegation, and state machine workflows
- **Prompt Engineering**: Apply Prompt-Driven Development, Agentic Development Workflow, and Trust Ladder patterns
- **Agent Evaluation**: Test and evaluate agent effectiveness with structured criteria

## Installation

### Claude Code (CLI)

Install from local path:

```bash
claude /plugin install /path/to/proagent-agentic-engineering
```

Or add to project `.claude/settings.json` for automatic team installation:

```json
{
  "plugins": {
    "proagent-agentic-engineering": {
      "source": "file:./plugins/proagent-agentic-engineering",
      "version": "0.2.0",
      "enabled": true
    }
  }
}
```

### Claude Desktop

Add the MCP servers from `.mcp.json` to your Claude Desktop configuration at `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token-here"
      }
    },
    "gitlab": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gitlab"],
      "env": {
        "GITLAB_PERSONAL_ACCESS_TOKEN": "your-token-here",
        "GITLAB_API_URL": "https://gitlab.com/api/v4"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "slack": {
      "command": "npx",
      "args": ["-y", "slack-mcp-server@latest", "--transport", "stdio"],
      "env": {
        "SLACK_MCP_XOXC_TOKEN": "your-xoxc-token",
        "SLACK_MCP_XOXD_TOKEN": "your-xoxd-token"
      }
    },
    "google-drive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gdrive"]
    },
    "google-workspace": {
      "command": "uvx",
      "args": ["mcp-gsuite"]
    },
    "rube": {
      "url": "https://rube.app/mcp"
    }
  }
}
```

## Usage

### Hub Command

```
/proagent-agentic-engineering
```

Shows all capabilities and routes to sub-commands.

### Task Runner

```
/proagent-agentic-engineering-run create-agent
/proagent-agentic-engineering-run create-skill
/proagent-agentic-engineering-run create-command
/proagent-agentic-engineering-run create-hook
/proagent-agentic-engineering-run create-mcp
/proagent-agentic-engineering-run create-plugin
/proagent-agentic-engineering-run orchestrate
/proagent-agentic-engineering-run evaluate
```

### Reviewer

```
/proagent-agentic-engineering-review
/proagent-agentic-engineering-review path/to/agents/
```

Reviews agent systems, skills, prompts, and orchestration patterns for quality and best practices.

### Direct Agent Usage

The `agentic-engineering-specialist` agent can be invoked directly or discovered automatically when you ask about creating agents, skills, commands, hooks, MCP servers, or multi-agent workflows.

### Automatic Skill Activation

The `Building Agentic Systems` skill activates autonomously when you mention agent design, skill creation, MCP development, orchestration patterns, or related topics.

## Plugin Structure

```
proagent-agentic-engineering/
├── .claude-plugin/
│   └── plugin.json                                # Plugin metadata
├── skills/
│   └── agentic-engineering-assistant/
│       └── SKILL.md                               # Comprehensive agentic engineering skill
├── commands/
│   ├── proagent-agentic-engineering.md             # Hub command
│   ├── proagent-agentic-engineering-run.md         # Task runner
│   └── proagent-agentic-engineering-review.md      # Reviewer
├── agents/
│   └── agentic-engineering-specialist.md           # Specialist agent
├── hooks/
│   └── hooks.json                                  # Lifecycle hooks
├── .mcp.json                                       # MCP server configurations
├── CLAUDE.md                                       # Context for Claude sessions
└── README.md                                       # This file
```

## Components

### Skill: Building Agentic Systems

Comprehensive autonomous capability covering nine domains: agent design, skill creation, command creation, hook configuration, plugin development, MCP server development, multi-agent orchestration, prompt engineering, and agent evaluation. Includes workflow patterns, quality checklists, and decision matrices.

### Agent: agentic-engineering-specialist

Expert sub-agent that understands the complete Claude Code component architecture and can create, review, and optimize all types of agentic engineering artifacts. Coordinates with other practice agents for cross-domain tasks.

### Commands

| Command | Description |
|---------|-------------|
| `/proagent-agentic-engineering` | Hub -- show capabilities, route to sub-commands |
| `/proagent-agentic-engineering-run` | Execute workflows: create-agent, create-skill, create-command, create-hook, create-mcp, create-plugin, orchestrate, evaluate |
| `/proagent-agentic-engineering-review` | Review agents, skills, commands, hooks, plugins, MCP servers, and orchestration patterns |

### Hooks

| Event | Matcher | Purpose |
|-------|---------|---------|
| PreToolUse | Write, Edit | Validate agent artifact structure before writing |
| PostToolUse | Write, Edit | Log modifications to agent artifacts for audit |
| SessionStart | * | Display plugin loaded message |

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| GitLab | `@modelcontextprotocol/server-gitlab` | Repository management, CI/CD integration |
| Playwright | `@playwright/mcp` | Browser automation for testing agent-built applications |
| Rube | `rube.app/mcp` | SaaS automation via Composio SDK |

## Source Repositories

This plugin synthesizes patterns from 19 repositories containing 612 assets (445 high-reuse):

| Repository | Key Assets |
|------------|-----------|
| casdk-harness | Context engineering plugin (5 skills), 14 agent definitions, orchestration patterns |
| superpowers | Subagent-driven development, parallel agents, TDD, brainstorming, 13 skills |
| awesome-claude-skills | Skill creator, MCP builder, template skill, 30+ skills |
| taches-cc-resources | Agent/hook/command creation skills, 27 commands, 3 auditor agents |
| ralph-orchestrator | Prompt-Driven Development, evaluation framework, code-assist |
| proagent-repo GUI | TAC principles (ADW, Core Four, Trust Ladder), Google Drive MCP |
| planning-with-files | File-based planning with hooks, plan execution |
| awos | Product-to-implementation pipeline (16 commands) |

## License

MIT
