# ProAgent Agentic Engineering

Provectus plugin for building, orchestrating, and optimizing AI agent systems with Claude Code. Features a **Workflow Factory** for template-driven artifact creation with mandatory complexity assessment, design decisions, inter-artifact contracts, and coherence validation. Consolidates patterns from 16 source repositories including ralph-orchestrator, casdk-harness, Auto-Claude, gastown, proagent-repo, planning-with-files, superpowers, taches-cc-resources, awesome-claude-skills, and AWOS.

## Features

- **Agent Design**: Create specialized sub-agents with focused responsibilities, discovery-optimized descriptions, and appropriate tool restrictions
- **Skill Creation**: Build model-invoked autonomous capabilities with progressive disclosure and trigger-term optimization
- **Command Creation**: Design user-invoked slash commands with argument handling, file references, and bash execution
- **Workflow Factory**: Create complete workflow artifacts from high-level descriptions with complexity assessment, design decisions, canonical templates, inter-artifact contracts, and coherence validation
- **Hook Configuration**: Automate lifecycle events with Python scripts (preferred) or shell commands for formatting, logging, validation, and notifications
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
      "version": "1.0.0",
      "enabled": true
    }
  }
}
```

### Claude Desktop

Add the MCP servers from `.mcp.json` to your Claude Desktop configuration at `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS), `%APPDATA%\Claude\claude_desktop_config.json` (Windows), or `~/.config/Claude/claude_desktop_config.json` (Linux):

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
/proagent-agentic-engineering-run create-workflow
/proagent-agentic-engineering-run expert-system
```

### Workflow Factory

```
/proagent-agentic-engineering-create "a code review pipeline with security and style agents"
/proagent-agentic-engineering-create "an expert system for Terraform infrastructure"
```

Creates complete workflow artifacts from high-level descriptions. Runs a mandatory 6-step process: Parse Request, Survey Codebase, Assess Complexity, Make Design Decisions, Generate Artifacts, and Validate Coherence.

### Reviewer

```
/proagent-agentic-engineering-review
/proagent-agentic-engineering-review path/to/agents/
```

Reviews agent systems, skills, prompts, orchestration patterns, workflow coherence, and expert systems for quality and best practices.

### Direct Agent Usage

The `agentic-engineering-specialist` agent can be invoked directly or discovered automatically when you ask about creating agents, skills, commands, hooks, MCP servers, or multi-agent workflows.

### Automatic Skill Activation

The `Building Agentic Systems` skill activates autonomously when you mention agent design, skill creation, MCP development, orchestration patterns, or related topics.

## Plugin Structure

```
proagent-agentic-engineering/
├── .claude-plugin/
│   └── plugin.json                                # Plugin metadata (v1.0.0)
├── skills/
│   └── agentic-engineering-assistant/
│       ├── SKILL.md                               # Comprehensive agentic engineering skill
│       ├── references/
│       │   ├── component-architecture.md          # Component specs & creation guides
│       │   ├── orchestration-patterns.md          # Multi-agent orchestration patterns
│       │   ├── workflow-patterns.md               # Creation workflows & composition patterns
│       │   ├── quality-checklists.md              # Quality & coherence checklists
│       │   ├── external-frameworks.md             # External framework reference cards
│       │   ├── artifacts.md                       # Artifact types & frontmatter schemas
│       │   ├── complexity.md                      # Complexity assessment tiers
│       │   ├── contracts.md                       # Inter-artifact contract templates
│       │   ├── error-handling.md                  # Error handling patterns
│       │   ├── naming-conventions.md              # Naming & placement rules
│       │   └── report-types.md                    # 8 report type templates
│       └── templates/
│           ├── command-body.md                    # Command canonical template
│           ├── skill-body.md                      # Skill canonical template
│           ├── agent-body.md                      # Agent canonical template
│           ├── hook-body.py                       # Hook Python template
│           ├── hook-settings.json                 # Hook settings template
│           ├── expert-plan.md                     # Expert System: Plan command
│           ├── expert-build.md                    # Expert System: Build command
│           ├── expert-improve.md                  # Expert System: Improve command
│           ├── design-decisions.md                # Design decisions template
│           └── creation-report.md                 # Creation report template
├── commands/
│   ├── proagent-agentic-engineering.md             # Hub command
│   ├── proagent-agentic-engineering-run.md         # Task runner (13 workflows)
│   ├── proagent-agentic-engineering-review.md      # Reviewer (11 dimensions)
│   └── proagent-agentic-engineering-create.md      # Workflow Factory
├── agents/
│   └── agentic-engineering-specialist.md           # Specialist agent
├── hooks/
│   ├── hooks.json                                  # Lifecycle hooks (Python)
│   ├── validate-artifact-structure.py              # PreToolUse validation
│   ├── audit-artifact-modification.py              # PostToolUse audit logging
│   ├── session-start-banner.py                     # SessionStart banner
│   └── legacy/
│       └── shell-hooks-v0.3.0.json                # Legacy shell hooks backup
├── .mcp.json                                       # MCP server configurations
├── CLAUDE.md                                       # Context for Claude sessions
└── README.md                                       # This file
```

## Components

### Skill: Building Agentic Systems

Comprehensive autonomous capability covering agent design, skill creation, command creation, hook configuration, plugin development, MCP server development, multi-agent orchestration, autonomous coding loops (ralph, casdk-harness, Auto-Claude, gastown), context engineering (3-file planning, knowledge graphs), spec-driven development (AWOS, ProAgent SDLC), multi-backend adapters, trust/autonomy frameworks, thinking model commands, prompt engineering, and agent evaluation. Includes 15+ external skill references, workflow patterns, quality checklists, and decision matrices.

### Agent: agentic-engineering-specialist

Expert sub-agent with deep knowledge of Claude Code component architecture and routing-level knowledge for autonomous loop frameworks (ralph-orchestrator, casdk-harness, Auto-Claude, gastown), multi-backend LLM adapters, spec-driven development pipelines, context engineering patterns, and ZTE trust ladder. Creates, reviews, and optimizes all types of agentic engineering artifacts. Coordinates with other practice agents for cross-domain tasks.

### Commands

| Command | Description |
|---------|-------------|
| `/proagent-agentic-engineering` | Hub -- show capabilities, route to sub-commands |
| `/proagent-agentic-engineering-run` | Execute workflows: create-agent, create-skill, create-command, create-hook, create-mcp, create-plugin, orchestrate, evaluate, bootstrap-loop, spec-driven, context-plan, create-workflow, expert-system |
| `/proagent-agentic-engineering-review` | Review agents, skills, commands, hooks, plugins, MCP servers, orchestration patterns, workflow coherence, and expert systems |
| `/proagent-agentic-engineering-create` | Workflow Factory -- create complete workflow artifacts from high-level descriptions with complexity assessment, design decisions, and coherence validation |

### Hooks

| Event | Matcher | Handler | Purpose |
|-------|---------|---------|---------|
| PreToolUse | Write, Edit | `validate-artifact-structure.py` | Validate agent artifact structure before writing |
| PostToolUse | Write, Edit | `audit-artifact-modification.py` | Log modifications to agent artifacts for audit |
| SessionStart | * | `session-start-banner.py` | Display plugin version and available commands |

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

## What's New in 1.0.0

- **Workflow Factory** (`/proagent-agentic-engineering-create`) — Template-driven artifact creation with mandatory 6-step process: complexity assessment, design decisions, canonical templates, inter-artifact contracts, and coherence validation
- **10 Canonical Templates** — Standardized body templates for commands, skills, agents, hooks, expert systems, design decisions, and creation reports
- **7 New Reference Files** — Artifacts catalog, complexity tiers, contracts, error handling patterns, naming conventions, report types, and external framework cards
- **7 Composition Patterns** — Linear Pipeline, Parallel Fan-Out, Chained Slash Commands, Fire-and-Forget, Self-Improving Expert Loop, Agent Teams, Skill+Agent Composition
- **Expert Systems** — Plan/Build/Improve trio pattern with shared Expertise sections and self-improvement loops
- **Enhanced Review** — 11 review dimensions (added Workflow Coherence and Expert Systems)
- **Python Hooks** — Migrated from shell+jq to Python with Graceful Degradation pattern
- **Honest Framework Cards** — Explicit confidence levels for 6 external frameworks (20-50% context reliability)
- **2 New Run Workflows** — `create-workflow` and `expert-system` added to task runner

## License

MIT
