---
description: Review test quality - audit test suites, analyze coverage gaps, evaluate testing strategy and maturity, review test plans, audit skill quality
argument-hint: <test suites|coverage|test strategy|test plan|skill audit> [target]
allowed-tools: Read, Grep, Glob, Bash
---

# proagent-qa Review

Review and assess testing quality, coverage, and strategy for the project.

## Variables

mode: $1 (one of: "test suites", "coverage", "test strategy", "test plan", "skill audit")
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

---

### Mode: test plan

Review and assess an existing test plan or generate a structured test plan from specifications.

Based on patterns from `awesome-claude-code/resources/slash-commands/testing_plan_integration/testing_plan_integration.md` and `proagent-repo/core/templates/validation_workflows/qa-engineer.yaml`.

1. **Analyze Input**
   - If `target` is a test plan document, read and assess its completeness
   - If `target` is a specification or feature description, identify testable behaviors
   - Extract acceptance criteria, edge cases, and non-functional requirements

2. **Evaluate Validation Pyramid Coverage**
   - Check that the plan includes unit, integration, and E2E test scenarios
   - Verify the pyramid balance (unit tests should outnumber integration, integration should outnumber E2E)
   - Identify missing test levels for critical behaviors

3. **Assess Test Data and Environment**
   - Review test data requirements and fixtures
   - Check for mock/stub requirements for external dependencies
   - Evaluate environment configuration needs (mock backends, replay servers)

4. **Report**
   Provide a test plan assessment:
   - Completeness score (percentage of acceptance criteria with corresponding tests)
   - Pyramid balance analysis
   - List of missing test scenarios by priority
   - Recommended test data fixtures and mock configurations
   - Effort estimate for full test plan implementation

---

### Mode: skill audit

Audit the quality and completeness of QA-related skills, commands, and agents.

Based on patterns from `taches-cc-resources/agents/skill-auditor.md` and `taches-cc-resources/commands/audit-skill.md`.

1. **Discover QA Assets**
   - Locate all QA-related skill files, command files, and agent definitions
   - If `target` is provided, scope the audit to that specific skill or directory
   - Check for proper frontmatter, description, and activation triggers

2. **Evaluate Quality**
   - Verify each skill has clear, actionable instructions
   - Check for concrete examples rather than generic guidance
   - Confirm integration points reference real tools and MCP servers
   - Validate that commands have proper argument hints and error handling

3. **Cross-Reference Coverage**
   - Compare discovered skills against the QA manifest asset inventory
   - Identify patterns from source repos not yet captured in skills
   - Check for redundancy or conflicting guidance between skills

4. **Report**
   Provide a skill audit report:
   - Total skills/commands/agents audited
   - Quality score per asset (1-10)
   - List of gaps where known patterns lack corresponding skill coverage
   - Specific recommendations for improvement with priority ranking
