# Provectus provrag RAG Framework Plugin

This plugin gives Claude Code full knowledge of the provrag RAG accelerator framework. It enables scaffolding new provrag projects, customizing ingestion and RAG pipelines, and operating the project lifecycle.

## Practice Scope

1. **Bootstrap** -- Verify and install prerequisites (git, Docker, mise, Python 3.13, uv, go-task, AWS CLI, AWS SSO, Pulumi, glab)
2. **Scaffold** -- Create new projects via `provrag init` with lifecycle monitoring
3. **Customize Pipelines** -- Modify ingestion (PDF, chunking, preprocessing) and RAG (reranking, hybrid search, system prompts) pipelines
4. **Operate** -- Run ingestion, serve API, check status, manage indices, connect/disconnect SSM tunnels to AWS
5. **Review** -- Audit pipeline architecture, step implementations, settings, and test coverage

## Key Conventions

### provrag Installation
- Distributed via AWS CodeArtifact, NOT PyPI
- Run `task ca:login` to authenticate, then `task setup` to install
- CodeArtifact: domain `provrag`, account `257394491982`, region `us-east-2`

### Reading Live API
- After setup, read installed provrag source directly for current signatures
- Use `uv run python -c "import provrag.{module}; print(provrag.{module}.__file__)"` to locate
- This ensures the plugin stays current with provrag updates

### Code Style
- Python 3.13: `str | None`, `StrEnum`, `from __future__ import annotations`
- `TYPE_CHECKING` guards for protocol types
- Ruff (line-length 120), mypy strict
- No unnecessary comments or docstrings
- TDD: write failing test first, then implement
- `.fn()` to bypass Prefect wrappers in tests

### Pipeline Architecture
- `@step` wraps Prefect `@task` + Phoenix OTEL span
- `@pipeline` wraps Prefect `@flow`
- Plain Python function composition -- no YAML, no DAG builders
- Factory functions for LLM providers: `create_embedder()`, `create_llm()`

### Settings
- Prefix: `PROVRAG_`, nested delimiter: `__`
- Environment: `local` (OpenAI, MinIO) or `aws` (Bedrock, S3, SSM tunnels)
- Provider auto-derived from environment unless explicitly set

## Plugin Structure

```
proagent-provrag/
├── .claude-plugin/plugin.json
├── skills/provrag-developer/
│   ├── SKILL.md                      # Core API reference + patterns
│   └── references/
│       ├── cli-reference.md          # CLI commands + Taskfile commands
│       ├── settings-reference.md     # PROVRAG_* env vars
│       └── customization-cookbook.md  # PDF, cross-encoder, hybrid search recipes
├── commands/
│   ├── proagent-provrag-hub.md       # Overview + routing
│   ├── proagent-provrag-run.md       # Execution dispatcher
│   ├── proagent-provrag-review.md    # Project review
│   └── modes/                        # Operation-specific workflows
│       ├── bootstrap.md
│       ├── init.md
│       ├── customize-ingestion.md
│       ├── customize-rag.md
│       ├── add-step.md
│       ├── ingest.md
│       ├── serve.md
│       └── operate.md
├── agents/provrag-specialist.md      # Specialist subagent
├── hooks/hooks.json                  # Safety hooks
├── .mcp.json                         # MCP config (empty -- uses CLI tooling)
├── CLAUDE.md                         # This file
└── README.md                         # User-facing docs
```
