# Provectus Backend Practice Plugin

This plugin provides the Backend practice context for the Provectus agentic coding platform. It equips Claude with production-tested API design, database engineering, and service architecture patterns drawn from actual Provectus engineering repositories.

## Practice Scope

The Backend practice covers ten engineering domains:

1. **API Design** - RESTful endpoint design with resource modeling, pagination, filtering, and error handling; GraphQL schema-first development with DataLoaders and Relay pagination; gRPC service definitions with Protocol Buffers and streaming
2. **Database Schema Engineering** - Relational schema design (PostgreSQL, MySQL) with normalization, constraints, indexes, and triggers; document schema design (MongoDB, DynamoDB) with embedding strategies; query optimization with EXPLAIN ANALYZE; dedicated PostgreSQL expertise from `agents/plugins/database-design/skills/postgresql/SKILL.md`
3. **Microservices Architecture** - Service boundary definition with DDD, inter-service communication (sync and async), resilience patterns (circuit breaker, retry, timeout, bulkhead), event-driven architectures; microservices design patterns from `agents/plugins/backend-development/skills/microservices-patterns/SKILL.md`
4. **CQRS and Event Sourcing** - Command Query Responsibility Segregation implementation from `agents/plugins/backend-development/skills/cqrs-implementation/SKILL.md`; saga orchestration patterns (choreography and orchestration) from `agents/plugins/backend-development/skills/saga-orchestration/SKILL.md`; event-driven architecture with domain events and projections
5. **Authentication and Authorization** - JWT with refresh tokens, OAuth2/OIDC, RBAC/ABAC, password hashing, account lockout, MFA, session management; authentication patterns from `casdk-harness/src/harness/skills/api-development/patterns/authentication-patterns.md`
6. **Message Queues and Async Processing** - RabbitMQ, AWS SQS, Google Pub/Sub, Kafka; dead letter queues, idempotent consumers, background job processing
7. **Caching Strategies** - Redis/Memcached caching layers, HTTP caching with ETags, cache-aside and write-through patterns, cache invalidation, CDN integration
8. **Performance Optimization** - N+1 query fixes, index optimization, connection pooling, async I/O, response streaming, load testing
9. **MCP Server Development** - Building MCP servers in Python and TypeScript from `taches-cc-resources/skills/create-mcp-servers/SKILL.md`; Claude API streaming adapters in Rust from `ralph-orchestrator/crates/ralph-adapters/src/claude_stream.rs`
10. **Framework-Specific Patterns** - FastAPI specialist patterns from `agents/plugins/api-scaffolding/agents/fastapi-pro.md`; Django specialist from `agents/plugins/api-scaffolding/agents/django-pro.md`; GraphQL architect from `agents/plugins/api-scaffolding/agents/graphql-architect.md`; Express reference implementation from `claude-ui/server/index.js`; Fastify+tRPC+SQLite stack from `ralph-orchestrator/backend/ralph-web-server/package.json`; Go expert patterns from `casdk-harness/src/harness/agents/configs/dev-go-expert.md`

## Key Conventions

When performing backend development tasks, follow these standards:

### API Design
- Use resource-oriented URLs with plural nouns (e.g., `/api/v1/users`)
- Apply correct HTTP methods (GET reads, POST creates, PUT/PATCH updates, DELETE removes)
- Version all APIs from day one (`/api/v1/`)
- Return structured error responses with error code, message, and details fields
- Implement pagination for all list endpoints (cursor-based or offset)
- Document APIs with OpenAPI/Swagger for REST, SDL for GraphQL

### Database
- Every table must have a primary key, timestamps (created_at, updated_at), and appropriate indexes
- Use parameterized queries exclusively; never concatenate user input into SQL
- Index all foreign key columns and columns used in WHERE/JOIN clauses
- Migrations must include both upgrade and downgrade steps
- Use CHECK constraints to enforce business rules at the database level
- Use DECIMAL(10,2) for currency fields, never FLOAT

### Security
- Validate and sanitize all user input with schema validation libraries (Pydantic, Joi, Zod)
- Hash passwords with bcrypt or Argon2; never store plain text
- Protect all non-public endpoints with authentication middleware
- Verify resource ownership on every request (users access only their own data)
- Store secrets in environment variables or cloud secret managers, never in code
- Rate-limit authentication endpoints (5 requests per minute)
- Set security headers (X-Frame-Options, X-Content-Type-Options, Content-Security-Policy)

### Performance
- Measure with EXPLAIN ANALYZE and APM tools before optimizing
- Fix N+1 queries with eager loading, JOINs, or DataLoaders
- Cache expensive queries with Redis, with TTL and invalidation on write
- Use connection pooling for all database and HTTP client connections
- Use async I/O for parallel external API calls
- Stream large datasets; never load millions of rows into memory

### Code Quality
- Follow SOLID principles and clear separation of concerns
- Write unit tests for business logic and integration tests for API endpoints
- Use structured logging with correlation IDs for request tracing
- Document public APIs and configuration requirements
- Provide rollback procedures for database migrations

## MCP Integrations

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **GitLab**: Merge requests, pipeline management for backend projects via `@modelcontextprotocol/server-gitlab`

## Source Repositories

Built from 10 Provectus internal repositories: `agents`, `Auto-Claude`, `casdk-harness`, `claude-ui`, `gastown`, `proagent-repo`, `provectus-marketplace`, `ralph-orchestrator`, `skills`, `taches-cc-resources`. Total: 83 cataloged assets (50 newly discovered in latest scan).

## Plugin Structure

```
proagent-backend/
  .claude-plugin/plugin.json
  skills/backend-assistant/SKILL.md
  commands/proagent-backend-hub.md
  commands/proagent-backend-run.md
  commands/proagent-backend-review.md
  agents/backend-specialist.md
  hooks/hooks.json
  .mcp.json
  CLAUDE.md
  README.md
```
