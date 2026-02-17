---
description: Review test quality - audit test suites, analyze coverage gaps, evaluate testing strategy and maturity
argument-hint: <test suites|coverage|test strategy> [target]
allowed-tools: Read, Grep, Glob, Bash
---

# proagent-qa Review

Review and assess testing quality, coverage, and strategy for the project.

## Variables

mode: $1 (one of: "test suites", "coverage", "test strategy")
target: $2 (optional - specific file, directory, or scope to review)

## Instructions

Read the `mode` variable and execute the corresponding review workflow below.

---

### Mode: review test suites

Audit existing test suites for completeness, correctness, and best practices.

1. **Discover Test Suites**
   - Locate all test files in the project (test_*.py, *.test.ts, *.spec.js, *_test.go, etc.)
   - If `target` is provided, scope the review to that specific file or directory
   - Identify the test frameworks in use and their configurations

2. **Analyze Test Quality**
   - Check for meaningful assertion coverage (not just "does not throw")
   - Identify tests that are testing implementation details rather than behavior
   - Flag overly complex tests that should be split into focused cases
   - Detect missing edge case coverage (null inputs, boundary values, error conditions)
   - Look for test anti-patterns:
     - Tests that depend on execution order
     - Shared mutable state between tests
     - Overly broad mocks that hide real bugs
     - Tests that test the framework rather than the application
     - Flaky tests with timing dependencies

3. **Evaluate Test Organization**
   - Check naming conventions follow project patterns
   - Verify test file structure mirrors source file structure
   - Assess setup/teardown patterns for proper isolation
   - Evaluate use of test fixtures, factories, and helpers

4. **Report**
   Provide a structured review:
   - Overall test suite health score (1-10)
   - List of identified issues with severity (critical, warning, suggestion)
   - Specific recommendations for improvement with code examples
   - Highlighted tests that serve as good examples of best practices

---

### Mode: coverage

Analyze current coverage metrics against project quality standards.

1. **Gather Coverage Data**
   - Run tests with coverage instrumentation enabled
   - Collect line, branch, function, and statement coverage metrics
   - Identify project-specific coverage thresholds from configuration

2. **Analyze Critical Paths**
   - Map source files by criticality (core business logic, API handlers, utilities, config)
   - Cross-reference coverage data with file criticality
   - Identify critical files with below-threshold coverage

3. **Gap Analysis**
   - List uncovered code blocks in critical files
   - Categorize gaps by type:
     - Error handling paths not tested
     - Edge cases not covered
     - Integration points not validated
     - Recently modified code without tests

4. **Report**
   Provide a coverage assessment:
   - Overall coverage summary (percentage by metric type)
   - Critical gap inventory with file paths and line ranges
   - Prioritized list of tests to write, ordered by risk reduction impact
   - Estimated effort to reach target coverage thresholds

---

### Mode: test strategy

Evaluate the overall testing strategy and recommend improvements.

1. **Assess Current State**
   - Count tests by type (unit, integration, E2E, performance, accessibility)
   - Evaluate the testing pyramid balance
   - Review CI/CD pipeline test configuration
   - Check for test automation gaps in the development workflow

2. **Risk Analysis**
   - Identify high-risk areas with insufficient test coverage
   - Evaluate dependency testing (external APIs, databases, third-party services)
   - Assess error scenario coverage across the application
   - Review security testing posture (SQL injection, XSS, auth bypass)

3. **Best Practices Comparison**
   - Compare against the validation pyramid model (unit base > integration middle > E2E top)
   - Evaluate test isolation and independence
   - Check for continuous testing integration (pre-commit hooks, PR gates)
   - Assess test data management strategy

4. **Strategic Recommendations**
   Provide a strategic assessment:
   - Current testing maturity level (ad-hoc, repeatable, defined, managed, optimized)
   - Testing pyramid balance analysis with recommended adjustments
   - Top 5 prioritized improvements ranked by risk reduction
   - Recommended tooling additions or changes
   - Suggested quality gates for the CI/CD pipeline
   - Timeline estimate for implementing recommendations
