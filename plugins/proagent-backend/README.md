# proagent-backend

Provectus Backend practice plugin for the agentic coding platform. Provides Claude with production-tested patterns for API design, database engineering, microservices architecture, authentication, caching, and performance optimization.

## Installation

Copy the `proagent-backend/` directory into your Claude Code plugins directory or reference it from your marketplace configuration.

## What It Does

This plugin equips Claude with specialized backend engineering knowledge drawn from 83 assets across 10 Provectus repositories (`agents`, `Auto-Claude`, `casdk-harness`, `claude-ui`, `gastown`, `proagent-repo`, `provectus-marketplace`, `ralph-orchestrator`, `skills`, `taches-cc-resources`). It covers:

- **API Design** - REST, GraphQL, and gRPC API creation with proper resource modeling, pagination, error handling, and documentation; Fastify+tRPC type-safe APIs
- **Database Schema Engineering** - PostgreSQL (deep expertise), MongoDB, SQLite schema design with normalization, constraints, indexes, migrations, and query optimization
- **Microservices Architecture** - Service boundary definition, inter-service communication, resilience patterns, and event-driven design
- **CQRS and Event Sourcing** - Command/query separation, event stores, projections, saga orchestration (choreography and orchestration)
- **Authentication and Authorization** - JWT, OAuth2, RBAC, password hashing, rate limiting, and security hardening
- **Caching and Queues** - Redis caching, message queue integration, background job processing
- **Performance Optimization** - N+1 query fixes, index tuning, connection pooling, async I/O, and streaming
- **MCP Server Development** - Building MCP servers in Python and TypeScript for exposing backend tools to LLM clients
- **Framework Specialists** - FastAPI, Django, Express, Fastify+tRPC, Go (Gin/Echo/Chi), Rust streaming adapters

## Commands

| Command | Description |
|---------|-------------|
| `/proagent-backend-hub` | Overview of all backend capabilities and quick start guide |
| `/proagent-backend-run create-api` | Scaffold a REST, GraphQL, or gRPC API with validation and docs |
| `/proagent-backend-run design-schema` | Design a database schema with constraints, indexes, and migrations |
| `/proagent-backend-run build-service` | Create a complete microservice with API, data, and infra layers |
| `/proagent-backend-run setup-auth` | Add JWT/OAuth2 authentication and RBAC authorization |
| `/proagent-backend-run optimize-queries` | Profile and optimize database queries and caching |
| `/proagent-backend-run implement-cqrs` | Implement CQRS, event sourcing, and saga orchestration |
| `/proagent-backend-run create-mcp-server` | Build an MCP server in Python or TypeScript |
| `/proagent-backend-review` | Review backend code for API design, security, performance, CQRS, and MCP servers |

## Plugin Structure

```
proagent-backend/
  .claude-plugin/
    plugin.json          # Plugin metadata, skill/agent/command registry
  skills/
    backend-assistant/
      SKILL.md           # Core skill: API design, database, auth, caching, performance
  commands/
    proagent-backend-hub.md   # Practice hub with capabilities overview
    proagent-backend-run.md   # Execution commands (create-api, design-schema, etc.)
    proagent-backend-review.md # Code review for APIs, schemas, security, architecture
  agents/
    backend-specialist.md     # Senior backend engineer agent definition
  hooks/
    hooks.json                # Pre-tool validation for API and schema operations
  .mcp.json                   # MCP server configs for GitHub, GitLab
  CLAUDE.md                   # Practice conventions and standards
  README.md                   # This file
```

## Source Repositories

Built from 10 Provectus internal repositories: `agents`, `Auto-Claude`, `casdk-harness`, `claude-ui`, `gastown`, `proagent-repo`, `provectus-marketplace`, `ralph-orchestrator`, `skills`, `taches-cc-resources`. Total: 83 cataloged assets (50 newly discovered in latest scan). Key external assets include CQRS and saga orchestration patterns from `agents`, MCP server development patterns from `taches-cc-resources` and `casdk-harness`, Fastify+tRPC stack from `ralph-orchestrator`, Express reference implementation from `claude-ui`, and framework specialists from `agents`.

## Hooks

The plugin includes pre-tool validation hooks that check:

- **API Design Standards** - Resource URL conventions, HTTP method semantics, versioning, error response structure
- **Error Handling** - Try/except blocks, status codes, structured error bodies, timeout handling
- **Input Validation** - Schema validation, type checking, length limits, SQL injection prevention
- **Authentication Checks** - Auth middleware on protected endpoints, permission verification, token validation
- **Schema Design** - Primary keys, foreign keys, indexes, timestamps, constraints, migration safety
- **Query Safety** - Parameterized queries, column specification, LIMIT clauses, index usage

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |
| GitLab | `@modelcontextprotocol/server-gitlab` | Merge requests, pipeline management for backend projects |

## Version

0.3.0
