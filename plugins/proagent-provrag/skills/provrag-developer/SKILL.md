---
name: provrag-developer
description: >
  Build and customize provrag RAG applications -- pipeline composition with @step/@pipeline decorators,
  data models (Document, Chunk, ScoredChunk), LLM protocols (BaseEmbedder, BaseLLM), OpenSearch retrieval,
  S3 document loading, Pydantic v2 settings, FastAPI serving, and CLI operations.
  Use when: scaffolding provrag projects, writing custom pipeline steps, modifying ingestion/RAG pipelines,
  configuring settings, writing tests, or operating the provrag lifecycle.
---

# provrag RAG Framework Developer Skill

Build, customize, and operate RAG applications using provrag -- Provectus's internal RAG accelerator.

## When Invoked Without Clear Intent

**MANDATORY**: You MUST call the `AskUserQuestion` tool — do NOT render these options as text:

AskUserQuestion(
  header: "provrag",
  question: "What provrag task do you need help with?",
  options: [
    { label: "Scaffold Project", description: "Create a new provrag project with provrag init" },
    { label: "Customize Pipelines", description: "Write or modify @step/@pipeline ingestion or RAG pipelines" },
    { label: "Configure & Operate", description: "Settings, LLM providers, OpenSearch, CLI operations" },
    { label: "Write Tests", description: "Unit and integration tests for provrag code" }
  ]
)

## When to Use This Skill

- Scaffolding a new provrag project (`provrag init`)
- Writing or modifying pipeline steps (`@step` decorated functions)
- Composing pipelines (`@pipeline` decorated functions)
- Working with provrag data models (Document, Chunk, ScoredChunk)
- Configuring LLM providers (Bedrock, OpenAI) via factory functions
- Setting up OpenSearch indices and retrieval (k-NN, hybrid)
- Customizing ingestion or RAG pipelines
- Writing tests for provrag code
- Operating the lifecycle (ingest, serve, status, list, clean, connect, disconnect)

## Reading the Live API

**Before writing any provrag code**, read the installed library source to get current signatures:

```
uv run python -c "import provrag.core.step; print(provrag.core.step.__file__)"
uv run python -c "import provrag.core.pipeline; print(provrag.core.pipeline.__file__)"
uv run python -c "import provrag.models.document; print(provrag.models.document.__file__)"
uv run python -c "import provrag.llm.factory; print(provrag.llm.factory.__file__)"
uv run python -c "import provrag.retrieval.opensearch_client; print(provrag.retrieval.opensearch_client.__file__)"
uv run python -c "import provrag.settings; print(provrag.settings.__file__)"
```

Use the Read tool on those file paths. If the project is not yet set up (no `.venv`), use `references/api-reference.md` as a fallback.

## Core Architecture

- `@step` = Prefect `@task` + Phoenix OpenTelemetry tracing span
- `@pipeline` = Prefect `@flow`
- Steps are plain Python functions called inside pipeline functions
- Data flows through Python variables -- no YAML, no DAG builder
- Settings are Pydantic v2 BaseSettings with `PROVRAG_*` env prefix

## Reference Files

Load these **at the point of need**, not at startup:

| File | Contents |
|---|---|
| `references/api-reference.md` | Package imports, decorators, data models, LLM abstractions, OpenSearch client, built-in steps, S3 loader, chunker, FastAPI factory, tracing, settings, generated project structure, testing patterns, code style |
| `references/cli-reference.md` | CLI commands, Taskfile operations, provrag installation, AWS connectivity |
| `references/settings-reference.md` | PROVRAG_* environment variables and configuration |
| `references/customization-cookbook.md` | Implementation recipes: PDF ingestion, cross-encoder reranking, hybrid search, custom system prompts |
