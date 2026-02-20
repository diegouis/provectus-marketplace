# proagent-qa

This is the Provectus QA plugin for Claude Code. It provides comprehensive quality assurance and test automation capabilities for software projects.

## Plugin Structure

```
proagent-qa/
  .claude-plugin/plugin.json   - Plugin metadata and configuration (v0.3.0)
  skills/qa-assistant/SKILL.md - Core QA skill: test automation, TDD, E2E, coverage, regression, LLM judge, mock/replay
  commands/
    proagent-qa-hub.md          - Plugin hub with command overview and quick start
    proagent-qa-run.md          - Execute: test, automate, coverage-report, regression-check, e2e-test, tdd-cycle, accessibility-audit, llm-judge, verify
    proagent-qa-review.md       - Review: test suites, coverage, test strategy, test plan, skill audit
  agents/qa-specialist.md       - QA specialist subagent with TDD, LLM evaluation, and verification capabilities
  hooks/hooks.json              - Pre-commit test gates and post-test coverage checks
  .mcp.json                     - MCP server configs: Playwright, GitHub, GitLab, Jira
```

## Commands

- `/proagent-qa-hub` - View all available QA commands and quick start guide
- `/proagent-qa-run test` - Execute the full project test suite with structured JSON output
- `/proagent-qa-run automate <target>` - Generate automated tests for a file or specification
- `/proagent-qa-run coverage-report` - Measure and report code coverage with gap analysis
- `/proagent-qa-run regression-check` - Analyze changes and run targeted regression tests
- `/proagent-qa-run e2e-test <test_file>` - Execute E2E tests with Playwright browser automation
- `/proagent-qa-run tdd-cycle <target>` - Execute a full TDD red/green/refactor cycle with YAGNI discipline
- `/proagent-qa-run accessibility-audit <url>` - Run WCAG 2.1 AA accessibility audit with remediation guidance
- `/proagent-qa-run llm-judge <target>` - Evaluate AI-generated outputs using LLM judge scoring rubrics
- `/proagent-qa-run verify <spec>` - Verify implementation meets specification and acceptance criteria
- `/proagent-qa-review test suites` - Audit test suites for quality and best practices
- `/proagent-qa-review coverage` - Analyze coverage against project thresholds
- `/proagent-qa-review test strategy` - Evaluate testing maturity and strategy
- `/proagent-qa-review test plan` - Review or generate structured test plans from specifications
- `/proagent-qa-review skill audit` - Audit QA skill quality and completeness against manifest

## Quality Gates

The hooks configuration enforces:
1. **Pre-commit**: Syntax checks, linting, and fast unit tests before every commit
2. **Post-test**: Coverage measurement and threshold enforcement after test runs
3. **Pre-merge**: Full test suite and regression analysis before merging to main

## MCP Integrations

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **GitLab**: Merge request test enforcement, pipeline monitoring via `@modelcontextprotocol/server-gitlab`
- **Playwright**: Browser automation for E2E testing, visual regression, and accessibility auditing via `@playwright/mcp@latest`
- **Jira**: Test-to-story linking, defect ticket creation, and sprint tracking via `@modelcontextprotocol/server-atlassian`

## Conventions

- All test results are returned as structured JSON for automated pipeline processing
- Test failures include root cause analysis, the fix applied, and confirmation of resolution
- E2E tests capture screenshot evidence organized by test run and test name
- Coverage thresholds default to 80% line, 70% branch, 85% function (configurable)
- The validation pyramid guides test strategy: unit (base) > integration (middle) > E2E (top)
- TDD cycles follow strict red/green/refactor phases with YAGNI enforcement
- LLM judge evaluations use multi-dimensional scoring rubrics (accuracy, completeness, format, relevance)
- Mock/replay backends enable deterministic testing without live service dependencies
- Implementations must be verified against acceptance criteria before marking complete

## Source Repos

This plugin integrates patterns from 14 scanned repositories (100 total assets, 72 newly discovered):
- `agents` - TDD workflow commands (tdd-cycle, tdd-red, tdd-green, tdd-refactor), unit test generation, accessibility audit
- `awesome-claude-code` - Test plan integration command
- `awesome-claude-skills` - Web app testing with browser automation
- `awos` - Implementation verification command
- `casdk-harness` - Testing strategies skill, 22-file unit test suite, 17-file integration test suite
- `proagent-repo` - QA engineer validation workflow, test generator meta-prompts, validation pyramid framework
- `ralph-orchestrator` - Mock backend, replay backend, LLM judge for AI output evaluation
- `superpowers` - TDD skill with YAGNI, verification-before-completion skill
- `taches-cc-resources` - Skill quality auditor agent, skill audit command
