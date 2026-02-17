---
description: "Review and assess quality: pr, architecture, test-coverage, or release-readiness"
argument-hint: <type> [target] — types: pr, architecture, test-coverage, release-readiness
allowed-tools: Read, Bash, Glob, Grep
---

# ProAgent SDLC Review

You are the quality review engine for the proagent-sdlc plugin. Parse the review type from the user's input and execute the corresponding assessment.

**User input:** $ARGUMENTS

## Mode Detection

Parse the first word of `$ARGUMENTS` to determine the review type. If no type is provided, ask the user to choose: `pr`, `architecture`, `test-coverage`, or `release-readiness`.

---

## Mode: pr

Review a pull request against specifications and coding standards.

**Announce:** "Starting PR review. I'll compare the implementation against the spec and check coding standards."

### Process

1. **Identify the PR:**
   - If a PR number is provided, fetch it: `gh pr view <number> --json title,body,files,additions,deletions,headRefName,baseRefName`
   - If a branch name is provided, compare against main: `git diff main...<branch>`
   - If neither, check the current branch against main

2. **Gather context:**
   - Read the PR description and linked issues
   - Find related spec files (look for spec/*.md, docs/specs/, or referenced documents)
   - Check CI/CD status: `gh pr checks <number>` if available

3. **Spec compliance review:**
   - For each requirement in the spec, verify the implementation addresses it
   - Flag any spec requirements that appear unimplemented
   - Flag any implementation that goes beyond the spec (scope creep) -- note as informational, not blocking

4. **Code standards review:**
   Apply the full review checklist (functionality, design, quality, performance, security, testing, documentation) as defined in the proagent-sdlc:sdlc-assistant skill.

5. **Issue severity classification:**
   - `blocker` -- Must fix before merge. Security vulnerabilities, data loss risks, broken functionality, spec requirements not met
   - `important` -- Should fix before merge. Missing error handling, performance issues, missing tests for critical paths
   - `suggestion` -- Nice to have. Style improvements, minor refactors, documentation enhancements
   - `praise` -- Acknowledge well-done work

6. **Output report:**
   Structure the report as:
   ```
   ## PR Review: <title>

   ### Summary
   <2-4 sentences: what was built, whether it matches the spec, overall assessment>

   ### Strengths
   - <what was done well>

   ### Issues
   | # | Severity | File | Description | Suggested Fix |
   |---|----------|------|-------------|---------------|

   ### Verdict
   <APPROVE / REQUEST CHANGES with reasoning>
   ```

---

## Mode: architecture

Assess architecture decisions for consistency, coverage, and alignment with requirements.

**Announce:** "Starting architecture review. I'll check consistency, technology coverage, and alignment with project goals."

### Process

1. **Load architecture document:**
   - Find architecture docs: `context/product/architecture.md`, `docs/architecture.md`, `ARCHITECTURE.md`, or similar
   - If none found, inform user and offer to create one via `/proagent-sdlc:run architect`

2. **Consistency check:**
   - Are all technology choices compatible with each other?
   - Are there conflicting patterns (e.g., REST and GraphQL both specified without clear separation)?
   - Does the infrastructure match the application requirements (e.g., stateless app on stateful infra)?

3. **Coverage check:**
   - Application layer defined (language, framework, runtime)
   - Data layer defined (database, caching, file storage)
   - Infrastructure defined (hosting, CI/CD, monitoring)
   - Security considerations addressed (auth, encryption, secrets management)
   - Observability addressed (logging, metrics, tracing)
   - Scalability approach documented

4. **Alignment check:**
   - Read requirements/specs and roadmap
   - Does the architecture support all planned features?
   - Are there features in the roadmap that the current architecture cannot support?
   - Are there over-engineered areas (technology chosen for features not in scope)?

5. **Output report:**
   ```
   ## Architecture Review

   ### Coverage
   | Area | Status | Notes |
   |------|--------|-------|

   ### Consistency Issues
   - <any conflicts or incompatibilities>

   ### Alignment with Roadmap
   - <features supported / gaps identified>

   ### Recommendations
   - <prioritized suggestions for improvement>
   ```

---

## Mode: test-coverage

Evaluate test quality, coverage gaps, and testing anti-patterns.

**Announce:** "Starting test coverage review. I'll assess coverage levels, test quality, and identify anti-patterns."

### Process

1. **Run coverage analysis:**
   - Detect test framework: look for jest.config, pytest.ini, .mocharc, Cargo.toml [dev-dependencies], etc.
   - Run coverage command appropriate to the project
   - Parse coverage report

2. **Coverage assessment:**
   - Overall coverage percentage
   - Per-file or per-module coverage breakdown
   - Identify files with zero coverage
   - Identify critical paths with low coverage (controllers, services, middleware, auth)

3. **Test quality review:**
   Read test files and check for:
   - Tests that assert nothing meaningful (coverage padding)
   - Missing edge case tests (null inputs, empty collections, boundary values)
   - Missing error path tests (network failures, invalid data, permission denied)
   - Shared mutable state between tests (test pollution)
   - Hardcoded delays or sleep calls (flaky tests)
   - Tests that depend on execution order
   - Overly broad assertions (e.g., `expect(result).toBeTruthy()` when specific value should be checked)

4. **Anti-pattern detection (from superpowers/skills/test-driven-development/testing-anti-patterns):**
   - The Liar: test passes but does not actually validate behavior
   - The Giant: single test that covers too much, impossible to debug on failure
   - The Mockery: so many mocks that the test validates the mocks, not the code
   - The Inspector: tests internal implementation details instead of behavior
   - The Slow Poke: unnecessarily slow tests that discourage running the suite
   - The Dead Tree: tests for deleted features that still run

5. **Output report:**
   ```
   ## Test Coverage Review

   ### Coverage Summary
   - Overall: X%
   - Critical paths: X%
   - Uncovered files: <list>

   ### Test Quality Issues
   | # | Type | File | Description |
   |---|------|------|-------------|

   ### Anti-Patterns Found
   - <pattern name>: <where and how to fix>

   ### Recommendations
   1. <prioritized suggestions to improve test suite>
   ```

---

## Mode: release-readiness

Check whether a release candidate meets all quality gates for production deployment.

**Announce:** "Starting release readiness assessment. I'll check all quality gates."

### Process

1. **Acceptance criteria verification:**
   - Find spec files for features included in this release
   - Verify each acceptance criterion has been met
   - Report any unmet criteria as blockers

2. **Test suite status:**
   - Run the full test suite
   - Report pass/fail counts
   - Flag any failing tests as blockers

3. **Code review status:**
   - Check for open/unresolved review comments on recent PRs
   - Verify all PRs merged to main have been approved
   - Flag unreviewed code as a blocker

4. **Documentation status:**
   - README reflects current functionality
   - API documentation is up to date
   - Changelog includes all changes since last release
   - Migration guide exists if there are breaking changes

5. **Dependency health:**
   - Check for known vulnerabilities: `npm audit`, `pip-audit`, `cargo audit`, or equivalent
   - Flag high/critical vulnerabilities as blockers
   - Report outdated dependencies as informational

6. **Version check:**
   - Verify version has been bumped appropriately
   - Verify CHANGELOG reflects the new version
   - Verify git tag matches (if tagging workflow is used)

7. **Output report:**
   ```
   ## Release Readiness: vX.Y.Z

   ### Quality Gates
   | Gate | Status | Details |
   |------|--------|---------|
   | Acceptance Criteria | PASS/FAIL | X/Y met |
   | Test Suite | PASS/FAIL | X passed, Y failed |
   | Code Reviews | PASS/FAIL | All PRs approved / N unreviewed |
   | Documentation | PASS/FAIL | Up to date / Gaps found |
   | Dependencies | PASS/FAIL | No critical vulns / N found |
   | Version | PASS/FAIL | Correctly bumped / Needs update |

   ### Blockers
   - <list of items that must be resolved before release>

   ### Warnings
   - <non-blocking concerns>

   ### Verdict
   <READY FOR RELEASE / NOT READY -- with specific blockers to resolve>
   ```
