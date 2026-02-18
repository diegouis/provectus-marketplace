# proagent-qa

Provectus QA plugin for Claude Code. Comprehensive quality assurance and test automation for software projects.

## Overview

proagent-qa provides a complete testing toolkit that integrates with Claude Code to automate test creation, execution, coverage analysis, regression detection, and E2E browser testing. It follows the validation pyramid model and enforces quality gates through pre-commit hooks and CI/CD integration.

## Installation

1. Copy the `proagent-qa/` directory into your project's `.claude/plugins/` directory
2. Configure MCP servers by setting environment variables:
   - Set `GITHUB_PERSONAL_ACCESS_TOKEN` for GitHub integration
   - Set `GITLAB_PERSONAL_ACCESS_TOKEN` and `GITLAB_API_URL` for GitLab integration
   - Set `ATLASSIAN_API_TOKEN`, `ATLASSIAN_EMAIL`, and `ATLASSIAN_DOMAIN` for Jira integration
3. Install Playwright for E2E testing: `npm install -D @playwright/test`

## Commands

| Command | Description |
|---------|-------------|
| `/proagent-qa-hub` | View all available commands and quick start guide |
| `/proagent-qa-run test` | Execute full project test suite |
| `/proagent-qa-run automate <target>` | Generate automated tests for code or specs |
| `/proagent-qa-run coverage-report` | Measure code coverage with gap analysis |
| `/proagent-qa-run regression-check` | Run targeted regression tests on recent changes |
| `/proagent-qa-run e2e-test <test_file>` | Execute E2E tests with Playwright |
| `/proagent-qa-review test suites` | Audit test quality and best practices |
| `/proagent-qa-review coverage` | Analyze coverage against thresholds |
| `/proagent-qa-review test strategy` | Evaluate testing maturity and strategy |

## Quality Gates

The plugin includes automated quality gates via `hooks/hooks.json`:

- **Pre-commit**: Blocks commits that fail syntax checks, linting, or unit tests
- **Post-test**: Warns or blocks when coverage drops below configured thresholds (default: 80% line, 70% branch, 85% function)
- **Pre-merge**: Requires full test suite pass and regression check before merging

## Supported Technologies

### Test Frameworks
- Python: pytest, unittest
- JavaScript/TypeScript: jest, vitest, mocha
- Go: go test
- Rust: cargo test

### E2E and Browser Testing
- Playwright (via MCP server)
- Cypress

### Coverage Tools
- pytest-cov (Python)
- c8, istanbul/nyc (Node.js)
- go tool cover (Go)

### Static Analysis
- ruff (Python)
- eslint (JavaScript/TypeScript)
- golangci-lint (Go)
- tsc (TypeScript type checking)

### Performance and Accessibility
- k6, Artillery (load testing)
- Lighthouse (performance auditing)
- axe-core (accessibility testing)

## Architecture

The plugin is built around these components:

- **SKILL.md**: Defines the QA assistant's core competencies across test automation, Playwright/Cypress integration, regression testing, coverage analysis, E2E testing, performance testing, and accessibility auditing
- **Commands**: Three command files (Hub, Run, Review) that provide the user-facing interface for all QA operations
- **Agent**: A QA specialist subagent with SDET expertise for autonomous test design, execution, and analysis
- **Hooks**: Automated quality gates that enforce standards at commit, test, and merge time
- **MCP Config**: Integration with Playwright, GitHub, GitLab, Jira, Slack, Google Drive, and Google Workspace for end-to-end workflow automation

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |
| GitLab | `@modelcontextprotocol/server-gitlab` | Merge request test enforcement, pipeline monitoring |
| Playwright | `@playwright/mcp` | Browser automation for E2E testing |
| Jira | `@modelcontextprotocol/server-atlassian` | Test-to-story linking, defect ticket creation |

## Source Attribution

This plugin synthesizes patterns and practices from the following Provectus repositories:

- **tac**: Test suite execution, E2E testing with Playwright MCP, test failure resolution workflows
- **superpowers**: TDD red-green-refactor enforcement, evidence-based verification, testing anti-patterns reference
- **proagent**: QA engineer role definition, automated testing skills, E2E and API testing strategies
- **proagent-repo GUI**: Validation pyramid, quality gate generation, test generation workflows
- **casdk-harness**: SDET agent configuration, testing strategy orchestration
- **ralph-orchestrator**: Behavior verification, TDD presets, smoke test runners
- **skills**: Playwright-based webapp testing, server lifecycle management for tests
- **Auto-Claude**: Pre-commit hook configuration with pytest and ESLint
- **taches-cc-resources**: Skill and command auditing patterns
- **agents**: TDD workflow plugin patterns

## License

MIT
