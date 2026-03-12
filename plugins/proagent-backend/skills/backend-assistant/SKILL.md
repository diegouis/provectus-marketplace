---
name: backend-assistant
description: Building Scalable Backend Services - APIs (REST, GraphQL, gRPC), database schema engineering, microservices architecture, CQRS/event-sourcing, saga orchestration, authentication and authorization, message queues, caching strategies, performance optimization, and MCP server development. Use when performing any backend development, API design, database design, service architecture, or MCP server creation task.
---

# Building Scalable Backend Services

Comprehensive backend engineering skill covering API design, database schema engineering, microservices architecture, CQRS/event-sourcing, authentication, caching, performance optimization, and MCP server development.

## When to Use This Skill

- Designing REST, GraphQL, or gRPC APIs for new services
- Engineering database schemas for relational (PostgreSQL) and NoSQL (MongoDB) databases
- Architecting microservices with clear boundaries and inter-service communication
- Implementing authentication (JWT, OAuth2) and authorization (RBAC, ABAC)
- Setting up message queues for asynchronous processing
- Implementing caching layers and optimizing performance
- Implementing CQRS, event sourcing, and saga orchestration
- Building MCP servers in Python and TypeScript
- Scaffolding Fastify+tRPC or FastAPI backends

## When Invoked Without Clear Intent

**Use `AskUserQuestion`** to present options as a selector widget:

```
AskUserQuestion(
  header: "Backend",
  question: "What backend engineering topic do you need help with?",
  options: [
    { label: "API Design", description: "REST, GraphQL, gRPC, pagination, error handling" },
    { label: "Database Engineering", description: "PostgreSQL/MongoDB schemas, indexes, migrations" },
    { label: "Auth & Security", description: "JWT, OAuth2, RBAC, rate limiting, input validation" },
    { label: "Microservices", description: "Service boundaries, DDD, circuit breaker, message queues" }
  ]
)
```

If the user selects "Other", present: Caching & Performance, CQRS / Event Sourcing, MCP Server Development, Framework Patterns.

## Reference Routing

> **CONTEXT GUARD**: Load reference files only when the user's request matches a specific topic below. Do NOT load all references upfront.

| User Intent | Reference File |
|---|---|
| REST API design, GraphQL schemas, gRPC services, pagination, error responses | `references/api-patterns.md` |
| PostgreSQL schemas, MongoDB document design, indexes, triggers, migrations | `references/database-patterns.md` |
| JWT auth, refresh tokens, RBAC, rate limiting, input validation, file uploads, secrets management | `references/auth-patterns.md` |
| Redis caching, cache invalidation, N+1 fixes, query optimization, async I/O, connection pooling | `references/caching-performance.md` |
| Service boundaries, DDD, circuit breaker, retry, message queues, event-driven architecture | `references/microservices-patterns.md` |
| CQRS, event sourcing, saga orchestration, choreography, compensating transactions | `references/cqrs-patterns.md` |
| MCP server development, Python MCP, TypeScript MCP, tool definitions | `references/mcp-server-patterns.md` |
| Fastify+tRPC, Express, Go backend, Rust streaming, FastAPI, Django, Python 3.12+ | `references/framework-patterns.md` |

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate interactive architecture diagrams, database ERDs, auth flows, and message queue topology maps. Describe what you need in natural language.
