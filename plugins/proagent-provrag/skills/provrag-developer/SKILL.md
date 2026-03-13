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

## CRITICAL: Ask First, Load Later

**DO NOT** read reference files, run environment detection commands, or load
mode files until the user has told you what they want to do.

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

## Routing

After the user selects an option, load the corresponding mode file:

| User Intent | Mode File |
|---|---|
| Scaffold Project | `commands/modes/init.md` |
| Customize ingestion (PDF, chunking) | `commands/modes/customize-ingestion.md` |
| Customize RAG (reranking, hybrid, prompts) | `commands/modes/customize-rag.md` |
| Add a pipeline step | `commands/modes/add-step.md` |
| Configure & Operate (ingest, serve, status) | `commands/modes/operate.md` |
| Write Tests | Read `references/api-reference.md` testing patterns section |
| Bootstrap / prerequisites | `commands/modes/bootstrap.md` |

## Core Architecture

- `@step` = Prefect `@task` + Phoenix OpenTelemetry tracing span
- `@pipeline` = Prefect `@flow`
- Steps are plain Python functions called inside pipeline functions
- Data flows through Python variables -- no YAML, no DAG builder
- Settings are Pydantic v2 BaseSettings with `PROVRAG_*` env prefix

## Reference Files

> **CONTEXT GUARD**: ONLY read these files when the user reaches a step
> that requires them. Do NOT pre-load at skill initialization.

| File | Contents |
|---|---|
| `references/api-reference.md` | Package imports, decorators, data models, LLM abstractions, OpenSearch client, built-in steps, S3 loader, chunker, FastAPI factory, tracing, settings, project structure, testing patterns, code style |
| `references/cli-reference.md` | CLI commands, Taskfile operations, provrag installation, AWS connectivity |
| `references/settings-reference.md` | PROVRAG_* environment variables and configuration |
| `references/customization-cookbook.md` | Implementation recipes: PDF ingestion, cross-encoder reranking, hybrid search, custom system prompts |

## Live API Reading

When writing provrag code in a project with `.venv`, mode files will instruct you to read the installed library source for current signatures. See `references/cli-reference.md` for the discovery commands. If no `.venv` exists, use `references/api-reference.md` as fallback.
