## Framework-Specific Patterns

### Fastify + tRPC + SQLite Stack

Reference: `ralph-orchestrator/backend/ralph-web-server/package.json`

Type-safe API layer combining Fastify's performance with tRPC's end-to-end type safety:

```typescript
import Fastify from "fastify";
import { fastifyTRPCPlugin } from "@trpc/server/adapters/fastify";
import { initTRPC } from "@trpc/server";
import { z } from "zod";
import Database from "better-sqlite3";

const db = new Database("app.db");
const t = initTRPC.create();

const appRouter = t.router({
  getUser: t.procedure.input(z.object({ id: z.string() })).query(({ input }) => {
    return db.prepare("SELECT * FROM users WHERE id = ?").get(input.id);
  }),
  createUser: t.procedure
    .input(z.object({ name: z.string(), email: z.string().email() }))
    .mutation(({ input }) => {
      const stmt = db.prepare("INSERT INTO users (name, email) VALUES (?, ?)");
      return stmt.run(input.name, input.email);
    }),
});

const server = Fastify();
server.register(fastifyTRPCPlugin, { prefix: "/trpc", trpcOptions: { router: appRouter } });
await server.listen({ port: 3000 });
```

### Express Reference Patterns

Reference: `claude-ui/server/index.js`, `claude-ui/server/routes/auth.js`

Production Express patterns from the claude-ui server for authentication routes and middleware composition.

### Go Backend Patterns

Reference: `casdk-harness/src/harness/agents/configs/dev-go-expert.md`

Go-specific backend patterns including Gin/Echo/Chi routing, sqlx for database access, and goroutine-based concurrency for high-throughput services.

### Rust Streaming Adapters

Reference: `ralph-orchestrator/crates/ralph-adapters/src/claude_stream.rs`

Rust-based streaming adapters for Claude API integration, demonstrating async stream processing with tokio for high-performance backend services.

## Python 3.12+ Best Practices

When building Python backends, leverage modern Python 3.12+ features:

### Language Features
- **Improved error messages**: More precise tracebacks with fine-grained error locations
- **ExceptionGroup and except***: Handle multiple concurrent exceptions from async tasks
- **TaskGroup**: Structured concurrency with `async with asyncio.TaskGroup() as tg:` for managing parallel async operations
- **Type parameter syntax**: `def foo[T](x: T) -> T:` instead of `TypeVar` boilerplate
- **f-string improvements**: Nested quotes and backslashes now allowed in f-string expressions

### FastAPI Modern Patterns
- Use `Annotated` types for dependency injection: `Annotated[User, Depends(get_current_user)]`
- Prefer `lifespan` context manager over `@app.on_event("startup")` / `@app.on_event("shutdown")`
- Use `APIRouter` with `tags` and `prefix` for modular route organization
- Return Pydantic v2 models directly (automatic serialization with `model_dump()`)

### Django 5.x Patterns
- Use `GeneratedField` for computed database columns
- Leverage `Field.db_default` for database-level defaults
- Use `aiterator()` for async ORM iteration
- Prefer `async` views with `@sync_to_async` for I/O-bound operations
