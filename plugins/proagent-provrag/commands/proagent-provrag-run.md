---
description: >
  Execute ProRAG operations: bootstrap, init, customize-ingestion, customize-rag,
  add-step, ingest, serve, or operate (status/list/clean/connect/disconnect).
argument-hint: "<operation> [options]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /proagent-provrag-run - Execute ProRAG Operations

Parse the operation from the user's input and execute the corresponding workflow.

## Usage

```
/proagent-provrag-run <operation> [options]
```

## Before Any Operation

> **CONTEXT GUARD**: ONLY read the files below when you are about to execute
> the operation. Do NOT pre-load them at command start.

1. Read `skills/provrag-developer/SKILL.md` for core architecture reference
2. If the project has a `.venv`, read the installed provrag source for current signatures (see `references/cli-reference.md` for discovery commands)

## Operations

| Operation | Description | Mode File |
|-----------|-------------|-----------|
| `bootstrap` | Check/install prerequisites | `commands/modes/bootstrap.md` |
| `init` | Scaffold new project with status monitoring | `commands/modes/init.md` |
| `customize-ingestion` | Modify ingestion pipeline | `commands/modes/customize-ingestion.md` |
| `customize-rag` | Modify RAG pipeline | `commands/modes/customize-rag.md` |
| `add-step` | Add custom pipeline step | `commands/modes/add-step.md` |
| `ingest` | Run ingestion pipeline | `commands/modes/ingest.md` |
| `serve` | Query the deployed API via tunnels | `commands/modes/serve.md` |
| `operate` | Status, list, clean, connect, disconnect | `commands/modes/operate.md` |

Read the corresponding mode file and follow its workflow. If the operation is not recognized, display the table above and ask the user which operation they need.

## Error Handling

- If a prerequisite is missing, suggest running `bootstrap` first
- If `task setup` hasn't been run, suggest running it first
- If Docker isn't running, suggest starting Docker Desktop
- If AWS SSO is expired, suggest `aws sso login --profile provectus-demos`
- If CodeArtifact token is expired, suggest `task ca:login`
