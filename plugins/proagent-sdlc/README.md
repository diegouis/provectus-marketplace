# proagent-sdlc

A Claude Code plugin for end-to-end software development lifecycle management. Covers architecture decisions, code review, testing strategy, release management, documentation, semantic versioning, and git workflow enforcement.

**Version:** 0.2.0
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

## Components

| Component | Name | Purpose |
|-----------|------|---------|
| Skill | `proagent-sdlc:sdlc-assistant` | Core skill covering all SDLC phases |
| Command | `proagent-sdlc:hub` | Command hub and routing |
| Command | `proagent-sdlc:run` | Execute SDLC workflows (5 modes) |
| Command | `proagent-sdlc:review` | Quality reviews (4 modes) |
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

## Source Repositories

> Built from Provectus internal engineering practices.
