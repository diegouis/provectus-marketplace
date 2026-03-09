---
name: sdlc-assistant
description: >
  Use when managing any phase of the software development lifecycle -- architecture
  decisions, code review, testing strategy, release planning, changelog generation,
  versioning, git workflows, debugging, hierarchical planning, task breakdown, ADR
  generation, C4 diagrams, multi-agent review pipelines, or orchestrated development
  workflows (ProAgent, AWOS, PITER, Ralph). Do NOT use for domain-specific work like
  frontend development (use frontend-assistant), backend APIs (use backend-assistant),
  or AWS infrastructure (use aws-ai-assistant).
---

# Managing Software Development Lifecycle

This skill orchestrates the full software development lifecycle from architecture through release, including planning, TDD, code review, debugging, and multi-stage pipeline execution.

## When to Use

- Defining or updating system architecture for a project
- Conducting code reviews on pull requests or branches
- Planning a testing strategy (unit, integration, e2e)
- Preparing a release (versioning, changelog, readiness checks)
- Generating or updating project documentation
- Establishing or enforcing git workflow conventions
- Breaking requirements into implementation plans with TDD
- Debugging issues systematically using hypothesis-driven root-cause analysis
- Generating Architecture Decision Records (ADRs) and C4 context diagrams
- Orchestrating multi-stage pipelines (ProAgent 5-stage, PITER framework)
- Creating and executing hierarchical project plans with progress tracking
- Finalizing development branches with pre-merge quality checks

## CRITICAL: Ask First, Load Later

**DO NOT** read reference files, run environment detection commands, or load
mode files until the user has told you what they want to do.

## Reference Routing

> **CONTEXT GUARD**: Load reference files only when the user's request
> matches a specific topic below. Do NOT load all references upfront.

| User Intent | Reference File |
|---|---|
| Architecture design, ADRs, C4 diagrams | `references/architecture-decisions.md` |
| Code review, PR review, multi-agent review | `references/code-review.md` |
| TDD, test strategy, test quality | `references/testing-strategy.md` |
| Release planning, changelogs, versioning | `references/release-management.md` |
| Git workflows, conventional commits, branches | `references/versioning-git.md` |
| Planning, task breakdown, requirements | `references/planning-tasks.md` |
| Debugging, root-cause analysis | `references/debugging.md` |
| SDLC pipelines (ProAgent, AWOS, PITER, Ralph) | `references/pipeline-frameworks.md` |

## Core Principles

- Follow TDD red-green-refactor for every implementation task
- Use conventional commits and semantic versioning
- Implement confirmation gates between autonomous workflow phases
- Apply hypothesis-driven debugging — never shotgun debug

## Integration Points

GitHub/GitLab (PRs, issues, CI/CD), Jira (sprint tracking), Confluence (docs), Slack (notifications).

## Visual Diagramming

Use Excalidraw MCP for system architecture diagrams, release pipeline flows, code review workflows, and sprint planning layouts.
