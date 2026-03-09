# Testing Strategy

## TDD Discipline

Applies TDD discipline. Every implementation task follows the red-green-refactor cycle with explicit test-first steps.

**Testing approach:**
- Write the failing test first (red)
- Run to confirm failure with expected error
- Write minimal implementation to pass (green)
- Run to confirm pass
- Refactor if needed, re-run tests
- Commit with semantic message

**Test quality standards:**
- Tests must be meaningful, not coverage padding
- Edge cases and error conditions covered
- Tests are independent and isolated (no shared mutable state)
- Follow AAA pattern: Arrange, Act, Assert
- No flaky tests introduced
- Integration tests for critical paths
- E2e tests for user-facing workflows
