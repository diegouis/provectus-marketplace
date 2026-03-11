# Code Review

## Review Pipeline

Implements a comprehensive code review pipeline. Reviews assess functionality, design, code quality, performance, security, testing, documentation, and dependencies.

**Review checklist categories:**
- Functionality: correctness, edge cases, error handling, concurrency
- Design and Architecture: patterns, SOLID principles, modularity, dependency management
- Code Quality: readability, naming, DRY, no dead code, style consistency
- Performance: algorithm complexity, N+1 queries, caching, memory leaks
- Security: no hardcoded secrets, input validation, SQL injection prevention, CSRF, auth checks
- Testing: >80% coverage for new code, meaningful tests, AAA pattern, no flaky tests
- Documentation: public API docs, complex logic comments, README updates, changelog
- Dependencies: justified additions, no vulnerabilities, license compatibility

**Feedback severity levels:**
- BLOCKING (must fix): security vulnerabilities, data loss risks, broken functionality
- IMPORTANT (should fix): design issues, missing error handling, performance concerns
- SUGGESTION (nice to have): style nits, minor refactors, documentation improvements
- QUESTION: seeking clarification on design choices
- PRAISE: acknowledging well-written code

**Code review dispatch:**
1. Get git SHAs for the range under review
2. Dispatch the proagent-sdlc:sdlc-specialist agent with the review context
3. Act on feedback: fix BLOCKING immediately, fix IMPORTANT before proceeding, note SUGGESTION for later

## Agent Teams for Code Review

For comprehensive code reviews, use Agent Teams parallel review patterns. Draws on specialized agents from the agents repo:
- `plugins/code-review-ai/agents/architect-review.md` -- AI-powered architect-level review
- `plugins/git-pr-workflows/agents/code-reviewer.md` -- PR-focused code reviewer
- `plugins/debugging-toolkit/agents/debugger.md` -- Debugging specialist for root-cause analysis
- `plugins/code-refactoring/agents/legacy-modernizer.md` -- Legacy code modernization assessment

### Parallel Multi-Dimensional Review
Spawn specialized reviewers running simultaneously:
- **Security reviewer**: Vulnerabilities, auth bypass, input validation, SQL injection
- **Performance reviewer**: Query efficiency, memory leaks, caching opportunities
- **Architecture reviewer**: SOLID principles, coupling, design patterns
- **Testing reviewer**: Coverage gaps, edge cases, test quality

After all reviewers complete, consolidate findings:
1. Same file:line with same issue -> merge findings, credit all reviewers
2. Conflicting severity -> use the higher severity rating
3. Conflicting recommendations -> include both with reviewer attribution

### Severity Calibration
- **Critical**: Data loss, security breach, complete failure
- **High**: Significant functionality impact (memory leak, missing validation)
- **Medium**: Partial impact, workaround exists (N+1 query, missing edge case)
- **Low**: Minimal impact, cosmetic (style, minor optimization)
