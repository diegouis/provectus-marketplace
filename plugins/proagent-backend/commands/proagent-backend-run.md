---
description: Execute backend operations - scaffold APIs, design schemas, build microservices, set up auth, optimize queries, implement CQRS, create MCP servers
argument-hint: <create-api|design-schema|build-service|setup-auth|optimize-queries|implement-cqrs|create-mcp-server> [options]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# /proagent-backend-run - Execute Backend Operations

You are the Provectus Backend execution agent. When the user invokes `/proagent-backend-run`, parse the operation argument and execute the corresponding workflow.

## Usage

```
/proagent-backend-run <operation> [options]
```

## Operations

### `create-api` - Scaffold a New API

Design and generate a complete API with endpoints, validation, error handling, and documentation.

**Steps:**
1. **Gather requirements:**
   - API style: REST, GraphQL, or gRPC
   - Programming language and framework (FastAPI, Express/NestJS, Go/Gin, Spring Boot)
   - Resources to expose (users, products, orders, etc.)
   - Operations needed (CRUD, search, aggregations, real-time)
   - Authentication method (JWT, OAuth2, API key, session)
   - Expected traffic volume and performance targets
2. **Design the API contract:**
   - For REST: Generate endpoint listing with HTTP methods, URL patterns, request/response schemas, and status codes following resource-oriented design from `proagent/roles/backend-engineer/skills/api-design.md`
   - For GraphQL: Generate schema with types, queries, mutations, subscriptions, and Relay-style pagination following patterns from `agents/plugins/backend-development/skills/api-design-principles/SKILL.md` and `agents/plugins/api-scaffolding/agents/graphql-architect.md`
   - For gRPC: Generate Protocol Buffer service definitions with message types and streaming patterns following patterns from `agents/plugins/backend-development/agents/backend-architect.md`
   - For Fastify+tRPC: Generate type-safe API with Zod validation following patterns from `ralph-orchestrator/backend/ralph-web-server/package.json`
3. **Generate implementation code:**
   - Route handlers with input validation (Pydantic for FastAPI, Joi/Zod for Node.js)
   - Structured error responses with proper HTTP status codes
   - Pagination with cursor-based or offset pagination
   - Request/response serialization and deserialization
   - Middleware for authentication, logging, and rate limiting
4. **Generate documentation:**
   - OpenAPI/Swagger specification for REST APIs
   - GraphQL SDL with descriptions for GraphQL APIs
   - Proto file with comments for gRPC services
   - Example requests and responses for each endpoint
5. **Add supporting infrastructure:**
   - Health check endpoint (`GET /health`)
   - Readiness check endpoint (`GET /ready`)
   - Metrics endpoint for Prometheus scraping
   - CORS configuration
   - Request logging middleware

### `design-schema` - Design a Database Schema

Create a production-ready database schema with proper normalization, constraints, indexes, and migrations.

**Steps:**
1. **Analyze data requirements:**
   - Entities and their attributes
   - Relationships between entities (one-to-one, one-to-many, many-to-many)
   - Data volume expectations and growth projections
   - Query patterns and access patterns
   - Consistency requirements (strong vs eventual)
2. **Choose database type:**
   - Relational (PostgreSQL, MySQL) for structured data with complex relationships and ACID requirements
   - Document (MongoDB, DynamoDB) for flexible schemas and hierarchical data
   - Key-Value (Redis) for caching, sessions, and simple lookups
   - Graph (Neo4j) for complex relationship traversal
   - Apply selection criteria from `proagent/roles/backend-engineer/skills/database-schema.md`
3. **Generate schema definition:**
   - For SQL: CREATE TABLE statements with data types, constraints, foreign keys, and indexes following patterns from `proagent/roles/backend-engineer/skills/database-schema.md`
   - For MongoDB: Collection schemas with validation rules and index definitions
   - Include: primary keys (UUID or auto-increment), NOT NULL constraints, CHECK constraints, DEFAULT values, timestamps (created_at, updated_at), and auto-update triggers
4. **Create indexes:**
   - Indexes on all foreign key columns
   - Composite indexes for multi-column query patterns
   - Partial indexes for filtered queries
   - Unique indexes for business rule enforcement
   - Present index strategy with EXPLAIN ANALYZE examples
5. **Generate migration files:**
   - Alembic migration for Python/SQLAlchemy
   - Prisma migration for Node.js/TypeScript
   - Django migration for Django projects
   - Raw SQL migration with both up and down scripts
   - Include safety checks for production (no DROP without confirmation, DEFAULT for new NOT NULL columns)

### `build-service` - Create a Microservice

Scaffold a new microservice with a complete project structure, API layer, data layer, and infrastructure configuration.

**Steps:**
1. **Define service scope:**
   - Service name and domain responsibility
   - API style (REST, GraphQL, gRPC) and public endpoints
   - Database requirements (PostgreSQL, MongoDB, Redis)
   - Message queue integration (RabbitMQ, SQS, Kafka)
   - External service dependencies
2. **Generate project structure:**
   - Application entry point with dependency injection
   - Route/controller layer with input validation
   - Service/business logic layer
   - Repository/data access layer with connection pooling
   - Configuration management with environment variables
   - Dockerfile with multi-stage build (non-root user, health check, pinned base image)
   - Docker Compose for local development with database and Redis
3. **Implement resilience patterns:**
   - Circuit breaker for external service calls (following patterns from `agents/plugins/backend-development/agents/backend-architect.md`)
   - Retry with exponential backoff and jitter
   - Timeout configuration for all external calls
   - Graceful degradation with fallback responses
   - Health check endpoints (liveness and readiness)
4. **Add observability:**
   - Structured logging with correlation IDs
   - Prometheus metrics (request rate, error rate, duration)
   - OpenTelemetry tracing integration
   - Error tracking and reporting
5. **Generate tests:**
   - Unit test stubs for service layer
   - Integration test stubs for API endpoints
   - Database test fixtures
   - Test configuration with in-memory database option

### `setup-auth` - Implement Authentication and Authorization

Add authentication and authorization to an existing or new API.

**Steps:**
1. **Assess requirements:**
   - Authentication method: JWT, OAuth2, session-based, API keys
   - Authorization model: RBAC, ABAC, resource-based
   - User registration flow (email verification, phone verification)
   - Password policy (minimum length, complexity, history)
   - MFA requirements (TOTP, SMS, email)
   - Token lifetime and refresh strategy
2. **Implement authentication:**
   - Password hashing with bcrypt or Argon2 (following patterns from `proagent/roles/backend-engineer/skills/security-hardening.md`)
   - JWT token generation with access and refresh tokens
   - Token validation middleware with expiration and signature checks
   - Account lockout after failed login attempts (5 attempts, 30-minute lockout)
   - Timing-safe response to prevent user enumeration
   - Session management with secure cookie configuration (HttpOnly, Secure, SameSite)
3. **Implement authorization:**
   - Permission model definition (roles, permissions, resource policies)
   - Authorization middleware/decorators
   - Resource ownership verification (users access only their own data)
   - Admin override with audit logging
   - CORS configuration for allowed origins
4. **Add security hardening:**
   - Rate limiting on authentication endpoints (5 per minute)
   - CSRF protection for session-based auth
   - Input validation on all authentication fields
   - Secure secret management with environment variables
   - Security event logging (login attempts, permission denials, token refresh)
5. **Generate configuration:**
   - Environment variables for secrets (JWT_SECRET_KEY, JWT_REFRESH_SECRET)
   - OAuth2 provider configuration (if applicable)
   - RBAC role and permission seed data
   - Security headers middleware (X-Frame-Options, X-Content-Type-Options, CSP)

### `optimize-queries` - Analyze and Optimize Database Queries

Profile and optimize database queries for improved performance.

**Steps:**
1. **Profile current performance:**
   - Identify slow endpoints using application logs or APM data
   - Run EXPLAIN ANALYZE on slow queries
   - Check for N+1 query patterns in ORM usage
   - Review connection pool configuration
   - Measure baseline response times
2. **Analyze query plans:**
   - Identify sequential scans that should be index scans
   - Find missing indexes on JOIN and WHERE columns
   - Detect unnecessary full table scans
   - Identify suboptimal JOIN order
   - Check for lock contention on heavily written tables
3. **Recommend optimizations:**
   - Add missing indexes (composite, partial, covering)
   - Fix N+1 queries with eager loading or DataLoaders (following patterns from `proagent/roles/backend-engineer/skills/performance-optimization.md`)
   - Replace SELECT * with specific column lists
   - Add LIMIT to unbounded queries
   - Implement cursor-based pagination for large datasets
   - Denormalize for read-heavy access patterns
4. **Implement caching layer:**
   - Add Redis caching for frequently accessed, slow queries
   - Configure TTL based on data freshness requirements
   - Implement cache invalidation on write operations
   - Add HTTP caching headers for GET endpoints
5. **Verify improvements:**
   - Re-run EXPLAIN ANALYZE to confirm index usage
   - Compare response times before and after optimization
   - Load test with realistic traffic patterns
   - Monitor for regressions after deployment

### `implement-cqrs` - Implement CQRS and Event Sourcing

Set up a CQRS architecture with separate command and query models, event store, and saga orchestration.

**Steps:**
1. **Assess domain complexity:**
   - Identify aggregates and their commands (write operations)
   - Identify read models and their query patterns
   - Determine if event sourcing is needed (audit trail, temporal queries, event replay)
   - Map distributed transaction boundaries for saga orchestration
2. **Implement command side:**
   - Command objects with validation following `agents/plugins/backend-development/skills/cqrs-implementation/SKILL.md`
   - Command handlers with domain logic
   - Event store for persisting domain events (append-only)
   - Aggregate root pattern with event application
3. **Implement query side:**
   - Denormalized read model projections optimized for query patterns
   - Event handlers that update projections when domain events occur
   - Eventually consistent read models with projection versioning
4. **Implement saga orchestration (if distributed):**
   - Saga orchestrator for multi-service transactions following `agents/plugins/backend-development/skills/saga-orchestration/SKILL.md`
   - Compensating actions for each saga step
   - Saga state persistence and recovery
   - Dead letter handling for failed compensation
5. **Add infrastructure:**
   - Event bus for publishing domain events (in-process or message broker)
   - Snapshot strategy for aggregates with many events
   - Projection rebuild mechanism
   - Monitoring for event lag and projection freshness

### `create-mcp-server` - Build an MCP Server

Create a Model Context Protocol server that exposes backend tools, resources, and prompts to Claude and other LLM clients.

**Steps:**
1. **Define server scope:**
   - Server name and purpose
   - Language: Python or TypeScript (following `taches-cc-resources/skills/create-mcp-servers/SKILL.md`)
   - Tools to expose (database queries, API calls, health checks, deployments)
   - Resources to expose (configuration, schemas, documentation)
   - Prompts to expose (code generation templates, review checklists)
2. **Generate server scaffold:**
   - For Python: MCP server using `mcp` SDK with `stdio` transport
   - For TypeScript: MCP server using `@modelcontextprotocol/sdk` with `StdioServerTransport`
   - Tool handlers with input schema validation (JSON Schema)
   - Resource handlers for exposing backend data
   - Error handling with structured MCP error responses
3. **Implement tools:**
   - Define tool input schemas with JSON Schema validation
   - Implement tool handlers with proper error handling
   - Add safety guards (read-only database access, input sanitization)
   - Include timeout handling for external service calls
4. **Add configuration:**
   - Environment variable configuration for database URLs, API keys
   - MCP server manifest for client registration
   - Integration instructions for `.mcp.json` in Claude Code projects
5. **Generate tests:**
   - Tool handler unit tests
   - Integration tests with mock MCP client
   - Input validation edge case tests

## Error Handling

If the requested operation is not recognized, display the list of available operations with descriptions and usage examples. If required context is missing (such as the programming language, framework, or database type), ask the user for the missing information before proceeding.
