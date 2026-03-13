# proagent-provrag

Provectus ProRAG framework plugin for the agentic coding platform. Enables scaffolding, customizing, and operating ProRAG projects.

## Overview

This plugin gives Claude Code full knowledge of ProRAG -- Provectus's internal RAG accelerator. It covers:
- Project scaffolding via `provrag init` with lifecycle monitoring
- Pipeline customization (PDF ingestion, cross-encoder reranking, hybrid search, custom chunking)
- Lifecycle operations (ingest, serve, status, list, clean, connect, disconnect)
- Pipeline architecture review and quality audits

Components: 1 skill, 4 commands, 10 mode files, 3 reference files, 1 agent, 2 hooks

## Commands

| Command | Description |
|---------|-------------|
| `/proagent-provrag` | Unified assistant: architecture interview, routing, debugging |
| `/proagent-provrag-hub` | Overview and capability guide |
| `/proagent-provrag-run bootstrap` | Check/install prerequisites |
| `/proagent-provrag-run init` | Scaffold new ProRAG project with status monitoring |
| `/proagent-provrag-run customize-ingestion` | Modify ingestion pipeline (PDF, chunking, etc.) |
| `/proagent-provrag-run customize-rag` | Modify RAG pipeline (reranking, hybrid search, etc.) |
| `/proagent-provrag-run add-step` | Add custom pipeline step |
| `/proagent-provrag-run ingest` | Run ingestion pipeline |
| `/proagent-provrag-run serve` | Query the deployed API via tunnels |
| `/proagent-provrag-run operate` | Status, list, clean, connect, disconnect |
| `/proagent-provrag-review` | Review ProRAG project quality |

## Plugin Structure

```
proagent-provrag/
├── .claude-plugin/plugin.json
├── skills/provrag-developer/
│   ├── SKILL.md
│   └── references/
│       ├── cli-reference.md
│       ├── settings-reference.md
│       └── customization-cookbook.md
├── commands/
│   ├── proagent-provrag.md
│   ├── proagent-provrag-hub.md
│   ├── proagent-provrag-run.md
│   ├── proagent-provrag-review.md
│   └── modes/ (10 mode files, incl. architecture-interview, review)
├── agents/provrag-specialist.md
├── hooks/hooks.json
├── .mcp.json
├── CLAUDE.md
└── README.md
```

## Prerequisites

- Python 3.13 (via mise)
- uv, go-task, Docker, AWS CLI
- AWS SSO (`provectus-demos` profile)
- ProRAG installed from AWS CodeArtifact (`task ca:login && task setup`)

Run `/proagent-provrag-run bootstrap` to verify all prerequisites.

## Key Features

### Live API Reading
Instead of hardcoding ProRAG API signatures, this plugin instructs Claude to read the installed ProRAG library source directly. This ensures it always uses the latest API even after `task upgrade`.

### Status Monitoring
When creating new projects, the init workflow launches a background subagent that monitors `provrag status` to track CI/CD progress and report when setup completes.

### Safety Hooks
- Warns before `provrag clean` (index deletion)
- Reminds to run `task check` after pipeline file modifications

## Version

0.2.0
