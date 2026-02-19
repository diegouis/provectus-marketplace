---
description: Execute QA operations - run tests, generate test automation, measure coverage, check regressions, run E2E tests, TDD cycles, accessibility audits, LLM judge evaluation
argument-hint: <test|automate|coverage-report|regression-check|e2e-test|tdd-cycle|accessibility-audit|llm-judge|verify> [target]
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

---

### Mode: tdd-cycle

Execute a full TDD red/green/refactor cycle for the specified target.

Based on patterns from `agents/plugins/tdd-workflows/commands/tdd-cycle.md` and `superpowers/skills/test-driven-development/SKILL.md`.

1. **Red Phase** (Write Failing Test)
   - Read the target file or specification to understand the behavior to implement
   - Write a focused test that describes the expected behavior
   - Run the test and confirm it fails with a clear, expected error message
   - If the test passes unexpectedly, the behavior already exists — skip to refactor

2. **Green Phase** (Minimal Implementation)
   - Write the minimum code required to make the failing test pass
   - Apply YAGNI discipline — do NOT add functionality beyond what the test requires
   - Run the test and confirm it passes
   - If it fails, iterate on the implementation until it passes

3. **Refactor Phase** (Improve Quality)
   - Review the implementation for code smells, duplication, and clarity issues
   - Refactor while keeping all tests green
   - Run the full related test suite to confirm no regressions
   - Report the cycle outcome: test written, code implemented, refactorings applied

4. **Report**
   Return results as structured JSON:
```json
{
  "cycle": "tdd",
  "test_file": "string",
  "implementation_file": "string",
  "red_phase": {"test_name": "string", "initial_failure": "string"},
  "green_phase": {"passed": true, "lines_added": 0},
  "refactor_phase": {"changes": ["string"], "all_tests_pass": true}
}
```

---

### Mode: accessibility-audit

Run a WCAG accessibility audit on the specified target URL or component.

Based on patterns from `agents/plugins/accessibility-compliance/commands/accessibility-audit.md`.

1. **Setup**
   - Verify the target URL is accessible or identify the component to audit
   - Initialize Playwright browser via MCP for page rendering

2. **Execute Audit**
   - Navigate to the target URL using Playwright
   - Run axe-core accessibility checks against WCAG 2.1 AA standards
   - Check color contrast ratios across all visible text elements
   - Validate keyboard navigation paths (tab order, focus management, skip links)
   - Test screen reader compatibility for headings, landmarks, and ARIA labels

3. **Analyze Results**
   - Categorize violations by severity: critical, serious, moderate, minor
   - Group violations by WCAG success criterion (e.g., 1.4.3 Contrast, 2.1.1 Keyboard)
   - Identify quick wins (fixes that resolve multiple violations)

4. **Report**
   Return a structured accessibility audit report:
```json
{
  "url": "string",
  "wcag_level": "AA",
  "violations": [{"rule": "string", "severity": "string", "elements": 0, "fix": "string"}],
  "passes": 0,
  "score": "string"
}
```

---

### Mode: llm-judge

Evaluate AI-generated outputs using the LLM judge pattern for quality assessment.

Based on the LLM judge pattern from `ralph-orchestrator/tools/e2e/helpers/llm_judge.py`.

1. **Define Evaluation Criteria**
   - If `target` is a rubric file, read the evaluation criteria from it
   - If no rubric, use default criteria: accuracy, completeness, format compliance, relevance
   - Establish pass/fail thresholds for each criterion

2. **Collect Outputs**
   - Read the AI-generated output(s) to evaluate
   - If comparing multiple outputs, collect all candidates

3. **Evaluate**
   - Score each output against the defined rubric dimensions
   - Provide specific evidence for each score (quote relevant passages)
   - Flag outputs that fail any critical criterion
   - Rank outputs if comparing multiple candidates

4. **Report**
   Return structured evaluation results:
```json
{
  "evaluations": [
    {
      "output_id": "string",
      "scores": {"accuracy": 0, "completeness": 0, "format": 0, "relevance": 0},
      "overall": 0,
      "pass": true,
      "evidence": "string"
    }
  ]
}
```

---

### Mode: verify

Verify that an implementation meets its specification and acceptance criteria before completion.

Based on patterns from `superpowers/skills/verification-before-completion/SKILL.md` and `awos/commands/verify.md`.

1. **Gather Requirements**
   - Read the specification or user story that defines the expected behavior
   - Extract explicit acceptance criteria and success conditions
   - Identify implicit requirements (error handling, edge cases, performance)

2. **Check Implementation**
   - Read the implementation code and compare against each acceptance criterion
   - Run existing tests to confirm they pass
   - Identify any acceptance criteria without corresponding test coverage

3. **Validate**
   - For each acceptance criterion, mark as: verified, partial, or missing
   - Generate targeted tests for any unverified criteria
   - Run newly generated tests to confirm the implementation satisfies them

4. **Report**
   Return a verification summary:
```json
{
  "spec": "string",
  "criteria_total": 0,
  "verified": 0,
  "partial": 0,
  "missing": 0,
  "details": [{"criterion": "string", "status": "verified|partial|missing", "evidence": "string"}]
}
```

## Error Handling

- If a command returns a non-zero exit code, mark the test as failed and capture stderr
- Timeout commands after 5 minutes unless otherwise specified
- If a test fails, report all results collected so far and stop
- For E2E tests, always capture a screenshot of the failure state before stopping
