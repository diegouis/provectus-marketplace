# proagent-backend

Provectus Backend practice plugin for the agentic coding platform. Provides Claude with production-tested patterns for API design, database engineering, microservices architecture, authentication, caching, and performance optimization.

## Installation

Copy the `proagent-backend/` directory into your Claude Code plugins directory or reference it from your marketplace configuration.

## What It Does

This plugin equips Claude with specialized backend engineering knowledge drawn from real Provectus repositories. It covers:

- **API Design** - REST, GraphQL, and gRPC API creation with proper resource modeling, pagination, error handling, and documentation
- **Database Schema Engineering** - PostgreSQL and MongoDB schema design with normalization, constraints, indexes, migrations, and query optimization
- **Microservices Architecture** - Service boundary definition, inter-service communication, resilience patterns, and event-driven design
- **Authentication and Authorization** - JWT, OAuth2, RBAC, password hashing, rate limiting, and security hardening
- **Caching and Queues** - Redis caching, message queue integration, background job processing
- **Performance Optimization** - N+1 query fixes, index tuning, connection pooling, async I/O, and streaming

## Commands

| Command | Description |
|---------|-------------|
| `/proagent-backend-hub` | Overview of all backend capabilities and quick start guide |
| `/proagent-backend-run create-api` | Scaffold a REST, GraphQL, or gRPC API with validation and docs |
| `/proagent-backend-run design-schema` | Design a database schema with constraints, indexes, and migrations |
| `/proagent-backend-run build-service` | Create a complete microservice with API, data, and infra layers |
| `/proagent-backend-run setup-auth` | Add JWT/OAuth2 authentication and RBAC authorization |
| `/proagent-backend-run optimize-queries` | Profile and optimize database queries and caching |
| `/proagent-backend-review` | Review backend code for API design, security, performance, and architecture |

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

This plugin synthesizes patterns from the following Provectus engineering repositories:

| Repository | Assets Used |
|-----------|-------------|
| **proagent** | Backend engineer role with API design, database schema, security hardening, performance optimization, and code review skills |
| **agents** | Backend architect agent, API design principles plugin with FastAPI patterns and DataLoader |
| **casdk-harness** | Python/FastAPI expert agent, Node.js and Go expert agents, API development harness |
| **claude-ui** | Express server with SSE streaming, session-based authentication, SQLite database model |
| **tac** | SQL injection protection module, NL-to-SQL LLM processor |
| **skills** | MCP server references for Node.js and Python |
| **proagent-repo GUI** | Backend validation workflows |
| **specs** | Developer role implementation specifications |
| **awesome-claude-skills** | MCP builder guide for API integration servers |

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
| GitLab | `@modelcontextprotocol/server-gitlab` | Merge requests, pipeline management for backend projects |

## Version

0.2.0
