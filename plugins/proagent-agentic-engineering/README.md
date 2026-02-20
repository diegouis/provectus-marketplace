# ProAgent Agentic Engineering

Provectus plugin for building, orchestrating, and optimizing AI agent systems with Claude Code. Consolidates patterns from 16 source repositories including ralph-orchestrator, casdk-harness, Auto-Claude, gastown, proagent-repo, planning-with-files, superpowers, taches-cc-resources, awesome-claude-skills, and AWOS.

## Features

- **Agent Design**: Create specialized sub-agents with focused responsibilities, discovery-optimized descriptions, and appropriate tool restrictions
- **Skill Creation**: Build model-invoked autonomous capabilities with progressive disclosure and trigger-term optimization
- **Command Creation**: Design user-invoked slash commands with argument handling, file references, and bash execution
- **Hook Configuration**: Automate lifecycle events with deterministic shell commands for formatting, logging, validation, and notifications
- **Plugin Development**: Bundle agents, skills, commands, hooks, and MCP servers into distributable packages
- **MCP Server Development**: Build Model Context Protocol servers to connect Claude to external APIs
- **Multi-Agent Orchestration**: Design sequential pipelines, parallel fan-out, hierarchical delegation, and state machine workflows
- **Autonomous Coding Loops**: Bootstrap sustained autonomous operation with ralph-orchestrator, casdk-harness, Auto-Claude, or gastown frameworks
- **Multi-Backend Adapters**: Orchestrate across Claude, Kiro, Gemini, and Codex LLM backends (ralph-orchestrator)
- **Spec-Driven Development**: Architecture-to-verified-implementation pipelines (AWOS, ProAgent SDLC 5-stage pipeline)
- **Context Engineering**: 3-file planning patterns, context priming, knowledge graph integration, and session handoff protocols
- **Trust/Autonomy Frameworks**: ZTE 5-level trust ladder (Observer through Autonomous) with progressive tool unlocking
- **Thinking Model Commands**: First-principles reasoning and structured mental models for design decisions
- **Prompt Engineering**: Apply Prompt-Driven Development, Agentic Development Workflow, and Trust Ladder patterns
- **Agent Evaluation**: Test and evaluate agent effectiveness with structured criteria
- **Extended Skill Library**: 15+ skills from superpowers, awesome-claude-skills, taches-cc-resources, and agents marketplace

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
      "version": "0.3.0",
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
/proagent-agentic-engineering-run bootstrap-loop
/proagent-agentic-engineering-run spec-driven
/proagent-agentic-engineering-run context-plan
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

Comprehensive autonomous capability covering agent design, skill creation, command creation, hook configuration, plugin development, MCP server development, multi-agent orchestration, autonomous coding loops (ralph, casdk-harness, Auto-Claude, gastown), context engineering (3-file planning, knowledge graphs), spec-driven development (AWOS, ProAgent SDLC), multi-backend adapters, trust/autonomy frameworks, thinking model commands, prompt engineering, and agent evaluation. Includes 15+ external skill references, workflow patterns, quality checklists, and decision matrices.

### Agent: agentic-engineering-specialist

Expert sub-agent with deep knowledge of Claude Code component architecture, four autonomous loop frameworks (ralph-orchestrator, casdk-harness, Auto-Claude, gastown), multi-backend LLM adapters, spec-driven development pipelines, context engineering patterns, and ZTE trust ladder. Creates, reviews, and optimizes all types of agentic engineering artifacts. Coordinates with other practice agents for cross-domain tasks.

### Commands

| Command | Description |
|---------|-------------|
| `/proagent-agentic-engineering` | Hub -- show capabilities, route to sub-commands |
| `/proagent-agentic-engineering-run` | Execute workflows: create-agent, create-skill, create-command, create-hook, create-mcp, create-plugin, orchestrate, evaluate, bootstrap-loop, spec-driven, context-plan |
| `/proagent-agentic-engineering-review` | Review agents, skills, commands, hooks, plugins, MCP servers, orchestration patterns, autonomous loops, and spec-driven workflows |

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
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |
| GitLab | `@modelcontextprotocol/server-gitlab` | Repository management, CI/CD integration |
| Playwright | `@playwright/mcp` | Browser automation for testing agent-built applications |
| Rube | `rube.app/mcp` | SaaS automation via Composio SDK |

## License

MIT
