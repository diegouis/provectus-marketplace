---
description: Execute QA operations - run tests, generate test automation, measure coverage, check regressions, run E2E tests
argument-hint: <test|automate|coverage-report|regression-check|e2e-test> [target]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# proagent-qa Run

Execute testing and quality assurance operations based on the specified mode.

## Variables

mode: $1
target: $2 (optional - file path, test name, or URL depending on mode)
options: $3 (optional - additional configuration)

## Instructions

Read the `mode` variable and execute the corresponding workflow below.

---

### Mode: test

Execute the comprehensive project test suite, validating both backend and frontend components.

1. **Discover Project Structure**
   - Identify the project type (Python, Node.js, Go, Rust, or mixed)
   - Locate test directories, test configuration files (pytest.ini, jest.config, vitest.config, etc.)
   - Identify available test runners and their configurations

2. **Execute Backend Tests**
   - Run syntax/compile checks for the primary backend language
   - Run linting and static analysis (ruff, eslint, golangci-lint as appropriate)
   - Execute the full backend test suite with verbose output and short tracebacks
   - Example: `cd app/server && uv run pytest tests/ -v --tb=short`

3. **Execute Frontend Tests**
   - Run TypeScript type checking: `tsc --noEmit`
   - Run frontend build validation: `npm run build` or `bun run build`
   - Run frontend unit tests if configured (vitest, jest)

4. **Report Results**
   - Return results exclusively as a JSON array
   - Sort with failed tests at the top
   - Include test_name, passed (boolean), execution_command, test_purpose, and error (if failed)
   - Stop execution on first failure and return results collected so far

```json
[
  {
    "test_name": "string",
    "passed": true,
    "execution_command": "string",
    "test_purpose": "string",
    "error": "optional string"
  }
]
```

---

### Mode: automate

Generate automated tests for specified code or specifications.

1. **Analyze Target**
   - If `target` is a file path, read the source code and identify testable functions, classes, and behaviors
   - If `target` is a spec file (specs/*.md), extract acceptance criteria and user stories
   - Identify edge cases, error conditions, and boundary values

2. **Apply Validation Pyramid**
   - Generate unit tests for individual functions and methods (base layer)
   - Generate integration tests for component interactions (middle layer)
   - Suggest E2E test scenarios for user-facing workflows (top layer)

3. **Generate Test Code**
   - Use the project's existing test framework and conventions
   - Follow existing naming patterns and directory structure
   - Include setup/teardown, mocking, and assertion patterns consistent with the codebase
   - Add descriptive test names that explain the behavior being validated

4. **Validate Generated Tests**
   - Run the generated tests to ensure they compile and execute
   - Verify assertions are meaningful (not trivially passing)
   - Report which tests pass and which require manual review

---

### Mode: coverage-report

Measure and report code coverage metrics.

1. **Configure Coverage Instrumentation**
   - Python: `pytest --cov=<source_dir> --cov-report=term-missing --cov-report=html`
   - Node.js: `npx c8 npm test` or `npx jest --coverage`
   - Go: `go test -coverprofile=coverage.out ./...`

2. **Execute Tests with Coverage**
   - Run the full test suite with coverage collection enabled
   - Capture line, branch, and function coverage percentages

3. **Analyze Coverage Gaps**
   - Identify files with coverage below project thresholds
   - List specific uncovered lines and branches
   - Prioritize gaps by file criticality (core business logic > utilities > configuration)

4. **Generate Report**
   - Output a summary table with per-file coverage metrics
   - Highlight files below threshold in the report
   - Recommend specific test cases to close the most impactful gaps
   - If HTML report was generated, provide the output path

---

### Mode: regression-check

Analyze recent changes and execute targeted regression tests.

1. **Identify Changes**
   - Run `git diff origin/main --stat --name-only` to list modified files
   - Categorize changes by component (backend, frontend, shared, config)
   - Assess change risk level based on file type and modification scope

2. **Map Changes to Tests**
   - Identify test files that correspond to modified source files
   - Find tests that import or depend on modified modules
   - Prioritize tests closest to the change (direct tests > integration > E2E)

3. **Execute Targeted Tests**
   - Run identified regression tests in priority order
   - Stop on first failure if in fast-fail mode
   - Capture full error output for any failures

4. **Report Regression Status**
   - List all changes analyzed and their risk assessment
   - Report test results for each change area
   - Flag any regressions introduced by recent changes
   - Recommend additional test coverage for high-risk changes without tests

---

### Mode: e2e-test

Execute end-to-end tests using Playwright browser automation.

1. **Setup**
   - Verify the application is running at the target URL (default: http://localhost:5173)
   - If an application startup command is available, execute it
   - Initialize Playwright browser via MCP server

2. **Execute Test**
   - If `target` is a test file path, read and execute the test steps defined in it
   - Navigate to the application URL using Playwright
   - Execute each test step: click elements, fill forms, navigate pages
   - Wait for async operations and element visibility before assertions
   - Capture screenshots at critical validation points

3. **Validate Results**
   - Check each success criterion defined in the test file
   - Mark steps as passed or failed with specific error details
   - On failure, capture the current page state and error context

4. **Save Evidence**
   - Save screenshots with descriptive names (01_initial_load.png, 02_form_submitted.png)
   - Organize by test name in structured directories
   - Include screenshot paths in the result output

5. **Report**
   Return results as structured JSON:
```json
{
  "test_name": "string",
  "status": "passed|failed",
  "screenshots": ["path/to/screenshot1.png", "path/to/screenshot2.png"],
  "error": null
}
```

## Error Handling

- If a command returns a non-zero exit code, mark the test as failed and capture stderr
- Timeout commands after 5 minutes unless otherwise specified
- If a test fails, report all results collected so far and stop
- For E2E tests, always capture a screenshot of the failure state before stopping
