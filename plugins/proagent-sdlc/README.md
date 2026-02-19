# proagent-sdlc

A Claude Code plugin for end-to-end software development lifecycle management. Covers architecture decisions, code review, testing strategy, release management, documentation, semantic versioning, git workflow enforcement, systematic debugging, hierarchical planning, ADR generation, C4 architecture diagrams, and multi-agent review pipelines.

**Version:** 0.3.0
**Category:** SDLC
**License:** MIT

## Installation

Copy the `proagent-sdlc` directory into your Claude Code plugins directory, or reference it from your project's `.claude/plugins/` configuration.

## Quick Start

Run `/proagent-sdlc:hub` to see all available commands and pick the right workflow for your task.

### Common Workflows

**Design system architecture:**
```
/proagent-sdlc:run architect
```
Interactively define your technology stack, data layer, infrastructure, and integration points. The agent proposes technologies with alternatives and justifications, working through each area collaboratively.

**Review a pull request:**
```
/proagent-sdlc:review pr 42
```
Runs a comprehensive review against the PR's linked spec and coding standards. Checks functionality, design, code quality, performance, security, testing, and documentation. Produces a structured report with findings classified as BLOCKING, IMPORTANT, SUGGESTION, or PRAISE.

**Plan a release:**
```
/proagent-sdlc:run plan-release
```
Verifies acceptance criteria, analyzes commits since the last release tag, determines the semantic version bump, and generates a changelog grouped by category.

**Check release readiness:**
```
/proagent-sdlc:review release-readiness
```
Runs all quality gates: acceptance criteria, test suite, code review status, documentation currency, dependency vulnerabilities, and version correctness. Outputs a pass/fail table with blockers.

**Review test coverage:**
```
/proagent-sdlc:review test-coverage
```
Runs coverage analysis, identifies uncovered critical paths, reviews test quality, and detects anti-patterns (The Liar, The Giant, The Mockery, The Inspector, The Slow Poke, The Dead Tree).

**Bump version:**
```
/proagent-sdlc:run version
```
Reads conventional commits since the last tag, recommends a version bump (major/minor/patch), updates manifest files, generates changelog, and creates a version commit and tag.

**Generate documentation:**
```
/proagent-sdlc:run document architecture
```
Analyzes the codebase and generates the specified documentation type: architecture, api, spec, guide, summary, or changelog.

**Debug an issue:**
```
/proagent-sdlc:run debug
```
Applies hypothesis-driven root-cause analysis: reproduce, gather evidence, rank hypotheses, test systematically, implement fix with regression test. Based on casdk-harness and taches-cc-resources debugging patterns.

**Create an implementation plan:**
```
/proagent-sdlc:run plan
```
Decomposes requirements into a hierarchical plan (epics, features, tasks) with exact file paths, code snippets, test commands, and dependency tracking. Each task follows the PITER micro-cycle.

**Generate an ADR:**
```
/proagent-sdlc:run adr
```
Creates an Architecture Decision Record with status, context, decision, consequences, and alternatives considered. Saves to the project's ADR directory with sequential numbering.

**Review an implementation plan:**
```
/proagent-sdlc:review plan
```
Assesses plan completeness, task granularity, dependency correctness, spec alignment, and risk areas. Outputs a structured report with coverage table and verdict.

## Components

| Component | Name | Purpose |
|-----------|------|---------|
| Skill | `proagent-sdlc:sdlc-assistant` | Core skill covering all SDLC phases |
| Command | `proagent-sdlc:hub` | Command hub and routing |
| Command | `proagent-sdlc:run` | Execute SDLC workflows (8 modes) |
| Command | `proagent-sdlc:review` | Quality reviews (5 modes) |
| Agent | `proagent-sdlc:sdlc-specialist` | Subagent for reviews and assessments |
| Hook | Pre-commit quality gate | Conventional commits, TODO check, test file check |
| Hook | Post-review notification | Structured review summary with severity counts |
| Hook | Pre-push validation | No WIP commits, branch up-to-date check |

## MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |
| GitLab | `@modelcontextprotocol/server-gitlab` | Merge requests, CI/CD pipelines |
| Jira | `@modelcontextprotocol/server-atlassian` | Issue tracking, sprint management |
| Confluence | `@modelcontextprotocol/server-atlassian` | Documentation publishing, ADRs |

Set the environment variables for the services your team uses. Unused servers will not be started.

## Pipeline Frameworks

| Framework | Source | Scope |
|-----------|--------|-------|
| ProAgent 5-stage | `proagent-repo/core/orchestration/sdlc/pipeline.py` | Full project lifecycle |
| AWOS 8-step | `awos/commands/*` | Feature spec-to-implementation |
| PITER | `proagent-repo/core/skills/tac/piter.md` | Per-task micro-cycle |
| Ralph presets | `ralph-orchestrator/presets/*.yml` | Bugfix and refactoring orchestration |

## Source Repositories

> Built from Provectus internal engineering practices and 14 source repositories: agents, Auto-Claude, awesome-claude-code, awesome-claude-skills, awos, casdk-harness, gastown, planning-with-files, proagent-repo, provectus-marketplace, ralph-orchestrator, skills, superpowers, taches-cc-resources.
