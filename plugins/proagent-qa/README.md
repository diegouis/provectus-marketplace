# proagent-qa

Provectus QA plugin for Claude Code. Comprehensive quality assurance and test automation for software projects.

## Overview

proagent-qa provides a complete testing toolkit that integrates with Claude Code to automate test creation, execution, coverage analysis, regression detection, E2E browser testing, TDD workflows, LLM-based test evaluation, and implementation verification. It follows the validation pyramid model and enforces quality gates through pre-commit hooks and CI/CD integration. Version 0.3.0 incorporates 72 newly discovered assets from 14 scanned repositories.

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
| `/proagent-qa-run tdd-cycle <target>` | Execute full TDD red/green/refactor cycle |
| `/proagent-qa-run accessibility-audit <url>` | Run WCAG 2.1 AA accessibility audit |
| `/proagent-qa-run llm-judge <target>` | Evaluate AI outputs with LLM judge scoring |
| `/proagent-qa-run verify <spec>` | Verify implementation meets acceptance criteria |
| `/proagent-qa-review test suites` | Audit test quality and best practices |
| `/proagent-qa-review coverage` | Analyze coverage against thresholds |
| `/proagent-qa-review test strategy` | Evaluate testing maturity and strategy |
| `/proagent-qa-review test plan` | Review or generate structured test plans |
| `/proagent-qa-review skill audit` | Audit QA skill quality and completeness |

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

### Deterministic and AI Testing
- Mock backends for service simulation (ralph-orchestrator pattern)
- Replay backends for deterministic API call reproduction (ralph-orchestrator pattern)
- LLM judge for evaluating AI-generated outputs (ralph-orchestrator pattern)

### TDD and Verification
- Red/green/refactor cycle workflows (agents, superpowers patterns)
- Implementation verification against acceptance criteria (superpowers, awos patterns)
- Test plan generation from specifications (awesome-claude-code pattern)
- Validation pyramid enforcement (proagent-repo pattern)

## Architecture

The plugin is built around these components:

- **SKILL.md**: Defines the QA assistant's core competencies across test automation, TDD workflows, Playwright/Cypress integration, regression testing, coverage analysis, E2E testing, LLM-based evaluation, mock/replay backends, performance testing, accessibility auditing, and implementation verification
- **Commands**: Three command files (Hub, Run, Review) providing 15 modes for QA operations including TDD cycles, accessibility audits, LLM judge evaluation, verification, test plan review, and skill auditing
- **Agent**: A QA specialist subagent with SDET expertise for autonomous test design, execution, TDD guidance, LLM evaluation, and verification
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

> Built from Provectus internal engineering practices and 100 assets discovered across 14 repositories: agents, Auto-Claude, awesome-claude-code, awesome-claude-skills, awos, casdk-harness, claude-ui, gastown, proagent-repo, provectus-marketplace, ralph-orchestrator, skills, superpowers, taches-cc-resources.

## License

MIT
