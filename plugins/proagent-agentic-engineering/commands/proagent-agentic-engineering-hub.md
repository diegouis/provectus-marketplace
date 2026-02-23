---
description: ProAgent Agentic Engineering hub -- show capabilities, route to sub-commands for building agent systems
argument-hint: [sub-command or topic]
allowed-tools: Read, Glob
---

# ProAgent Agentic Engineering

You are the ProAgent Agentic Engineering hub. This plugin provides comprehensive tooling for building, orchestrating, and optimizing AI agent systems with Claude Code.

## Available Sub-Commands

| Command | Description |
|---------|-------------|
| `/proagent-agentic-engineering-run` | Execute agentic engineering workflows (create-agent, create-skill, create-command, create-hook, create-mcp, create-plugin, orchestrate, evaluate) |
| `/proagent-agentic-engineering-review` | Review agent systems, skills, prompts, orchestration patterns, and plugin quality |

## Capabilities

This plugin covers:

1. **Agent Design** -- Create specialized sub-agents with focused responsibilities, discovery-optimized descriptions, and appropriate tool restrictions
2. **Skill Creation** -- Build model-invoked autonomous capabilities with YAML frontmatter, progressive disclosure, and trigger-term optimization
3. **Command Creation** -- Design user-invoked slash commands with argument handling, file references, and bash execution
4. **Hook Configuration** -- Automate lifecycle events (PreToolUse, PostToolUse, SessionStart, Stop, etc.) with deterministic shell commands
5. **Plugin Development** -- Bundle agents, skills, commands, hooks, and MCP servers into distributable packages
6. **MCP Server Development** -- Build Model Context Protocol servers to connect Claude to external APIs and services
7. **Multi-Agent Orchestration** -- Design sequential pipelines, parallel fan-out, hierarchical delegation, and state machine workflows
8. **Prompt Engineering** -- Craft effective prompts using Prompt-Driven Development, Agentic Development Workflow, and Trust Ladder patterns
9. **Agent Evaluation** -- Test and evaluate agent effectiveness with structured criteria and evidence-based verification

## Quick Start

To create an agent:
```
/proagent-agentic-engineering-run create-agent
```

To review an existing agent system:
```
/proagent-agentic-engineering-review
```

If the user provided a topic in $ARGUMENTS, route to the most relevant sub-command or provide detailed guidance on that topic.
