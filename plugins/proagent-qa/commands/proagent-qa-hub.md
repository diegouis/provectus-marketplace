# proagent-qa Hub

Welcome to the Provectus QA plugin. This hub provides access to all quality assurance and test automation capabilities.

## Available Commands

### /proagent-qa-run
Execute testing operations. Accepts a mode argument:

- **test** - Run the full project test suite (unit, integration, and build validation). Executes backend and frontend tests in sequence, returning structured JSON results with pass/fail status and error details.
- **automate** - Generate automated tests from specifications or code. Analyzes the target code, identifies testable behaviors, and creates comprehensive test cases following the validation pyramid (unit > integration > E2E).
- **coverage-report** - Measure and report code coverage. Runs tests with coverage instrumentation and generates reports showing line, branch, and function coverage with identified gaps.
- **regression-check** - Analyze recent changes and run targeted regression tests. Uses git diff to identify impacted areas, prioritizes tests by change proximity, and reports any regressions introduced.
- **e2e-test** - Execute end-to-end tests using Playwright browser automation. Navigates the application, performs user interactions, captures screenshots, and validates against success criteria.

### /proagent-qa-review
Review and assess quality. Accepts a mode argument:

- **review test suites** - Audit existing test suites for completeness, correctness, and adherence to best practices. Identifies missing edge cases, redundant tests, and anti-patterns.
- **coverage** - Analyze current coverage metrics against project thresholds. Highlight untested critical paths and recommend targeted tests to close gaps.
- **test strategy** - Evaluate the overall testing strategy for the project. Assess the balance of unit/integration/E2E tests, identify risk areas with insufficient coverage, and recommend improvements.

## Quick Start

1. Run `/proagent-qa-run test` to execute the project test suite
2. Run `/proagent-qa-run coverage-report` to see current coverage
3. Run `/proagent-qa-review test strategy` to get a strategic assessment
4. Run `/proagent-qa-run e2e-test <test_file>` to execute E2E tests with Playwright

## Configuration

This plugin integrates with:
- **Playwright MCP** for browser automation and E2E testing
- **GitHub/GitLab** for CI/CD pipeline integration and PR test gates
- **Jira** for linking test results to stories and defects

See `.mcp.json` for MCP server configuration and `hooks/hooks.json` for automated quality gates.
