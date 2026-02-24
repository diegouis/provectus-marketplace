---
name: Building Agentic Systems
description: >
  Comprehensive skill for designing, building, orchestrating, and optimizing AI agent systems
  with Claude Code. Covers agent design patterns, multi-agent orchestration, skill/command/hook
  creation, MCP server development, prompt engineering, plugin architecture, agent evaluation,
  context engineering, autonomous coding loops, multi-backend orchestration, trust/autonomy
  frameworks, spec-driven development, and thinking model commands.

  This skill should be used when the user mentions:
  - Creating agents, skills, commands, hooks, or plugins for Claude Code
  - Multi-agent orchestration, parallel agents, subagent workflows
  - MCP server development or integration
  - Prompt engineering, context engineering, or prompt-driven development
  - Agent evaluation, testing agent systems, or agent quality assurance
  - Claude Code extensions, customization, or configuration
  - Agentic development workflows (ADW), trust ladder, progressive autonomy
  - Subagent-driven development (SDD), dispatching parallel agents
  - File-based planning with hooks, plan execution with agents
  - Autonomous coding loops (ralph, casdk-harness, Auto-Claude, gastown)
  - Multi-backend adapters (Claude, Kiro, Gemini, Codex)
  - Spec-driven development (AWOS spec/implement/verify, ProAgent SDLC pipeline)
  - Tool registry, plugin lifecycle, knowledge graph integration
  - Thinking models, first-principles reasoning, mental model commands
  - 3-file planning pattern, context handoff, session persistence

  Do NOT use for:
  - General software development without an agentic component (use sdlc or backend/frontend skills)
  - DevOps infrastructure without agent involvement (use devops skills)
  - Pure testing without agent evaluation (use qa skills)
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebFetch, WebSearch
---

# Building Agentic Systems

Comprehensive skill for building, orchestrating, and optimizing AI agent systems using Claude Code.

## Overview

This skill covers the full lifecycle of agentic engineering: from designing individual agents to orchestrating complex multi-agent workflows, building MCP servers, creating plugins, and evaluating agent systems.

## Reference Routing

> **CONTEXT GUARD**: Load reference files only when the user's request matches a specific topic below. Do NOT load all references upfront.

| User Intent | Reference File |
|---|---|
| Creating agents, skills, commands, hooks, plugins, or MCP servers | `references/component-architecture.md` |
| Multi-agent orchestration, autonomous coding loops, context engineering, agent teams, spec-driven dev | `references/orchestration-patterns.md` |
| Prompt engineering, context engineering, trust ladder, agent evaluation, thinking models | `references/prompt-engineering.md` |
| Step-by-step workflows for creating agents, skills, commands, hooks, plugins, MCP servers | `references/workflow-patterns.md` |
| Quality checklists, AWOS architecture, confirmation patterns, Composio SDK, decision matrix | `references/quality-checklists.md` |

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate agent orchestration flows, MCP server architecture diagrams, plugin component maps, and fan-out/fan-in pattern visualizations. Describe what you need in natural language.
