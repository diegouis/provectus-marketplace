---
description: >
  Review provrag project: pipeline architecture, step implementations,
  settings configuration, and test coverage.
argument-hint: "[target]"
allowed-tools: Read, Glob, Grep, Bash, Task
---

# /proagent-provrag-review - Review provrag Projects

You are the Provectus provrag review agent. Analyze provrag project implementations for correctness, best practices, and production readiness.

## Workflow

1. Parse the user's review target (if provided): a specific file, area (pipeline, ingestion, settings, tests, dependencies), or "all"
2. Read the review mode file: `commands/modes/review.md`
3. Follow its workflow to conduct the review

If no target is specified, auto-detect review targets by scanning the project structure as described in the mode file.
