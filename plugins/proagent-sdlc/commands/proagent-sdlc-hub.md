---
description: SDLC command hub -- lists all available proagent-sdlc commands and their purposes
argument-hint: [topic]
allowed-tools: Read, Glob
---

# ProAgent SDLC Command Hub

You are the command hub for the proagent-sdlc plugin. Present the user with available SDLC commands and help them choose the right workflow for their current task.

## Available Commands

### `/proagent-sdlc:run`
Execute an SDLC workflow. Modes:
- **architect** -- Define or update system architecture with interactive technology selection
- **review-code** -- Run comprehensive code review on a branch, PR, or diff range
- **plan-release** -- Plan a release: verify acceptance criteria, generate changelog, determine version
- **document** -- Generate or update project documentation (architecture, specs, API docs, guides)
- **version** -- Manage semantic versioning: analyze commits, bump version, update manifests

### `/proagent-sdlc:review`
Review and assess quality. Modes:
- **pr** -- Review a pull request against spec and coding standards
- **architecture** -- Assess architecture decisions for consistency and coverage
- **test-coverage** -- Evaluate test quality, coverage gaps, and testing anti-patterns
- **release-readiness** -- Check if a release candidate meets all quality gates

## Quick Start

Tell me what you need and I will route you to the right command:

| You want to... | Run this |
|---|---|
| Design system architecture | `/proagent-sdlc:run architect` |
| Review a PR or branch | `/proagent-sdlc:review pr` |
| Break a spec into tasks | `/proagent-sdlc:run document` then plan with sdlc-assistant skill |
| Prepare a release | `/proagent-sdlc:run plan-release` |
| Check release readiness | `/proagent-sdlc:review release-readiness` |
| Bump version after changes | `/proagent-sdlc:run version` |
| Review test coverage | `/proagent-sdlc:review test-coverage` |

## What would you like to do?

Describe your goal and I will suggest the appropriate command, or pick one from the table above.
