---
name: sdlc-assistant
description: Use when managing any phase of the software development lifecycle -- architecture decisions, code review, testing strategy, release planning, documentation, versioning, or git workflows
---

# Managing Software Development Lifecycle

## Overview

This skill orchestrates the full software development lifecycle from architecture through release.

## When to Use

- Defining or updating system architecture for a project
- Conducting code reviews on pull requests or branches
- Planning a testing strategy (unit, integration, e2e)
- Preparing a release (versioning, changelog, readiness checks)
- Generating or updating project documentation
- Establishing or enforcing git workflow conventions
- Breaking requirements into implementation plans with TDD

## Capabilities

### 1. Architecture Decisions

Follows the AWOS collaborative architecture pattern: read product definition and roadmap, then work through architectural areas section-by-section with the user, proposing technologies with alternatives and justifications. Produces a structured `architecture.md` covering stack, databases, infrastructure, and integration points.

**Key steps:**
- Check prerequisites: product definition and roadmap must exist
- Detect mode: creation vs. update
- Interactive design: propose areas, suggest technologies with alternatives, clarify and confirm
- Finalize and save to `context/product/architecture.md`
- Review subagent coverage against chosen technologies

### 2. Code Review

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

### 3. Testing Strategy

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

### 4. Release Management

Combines changelog generation, semantic versioning with conventional commits, and verification workflows for acceptance criteria.

**Release workflow:**
1. Verify all acceptance criteria are met
2. Generate changelog from conventional commits since last release
3. Determine version bump (major/minor/patch) from commit types
4. Update version in project manifests
5. Create release branch or tag
6. Run release readiness checks (tests pass, no blocking issues, docs current)
7. Create PR or release draft

**Verification process:**
- Identify target specification
- Confirm all tasks are complete
- Verify each acceptance criterion against implementation
- Mark spec as Completed
- Review product context docs for needed updates

### 5. Documentation

Covers automated doc generation, user guide creation, information architecture, and collaborative authoring.

**Documentation types:**
- Architecture documents
- Functional and technical specifications
- API documentation (OpenAPI/Swagger)
- User guides and tutorials
- Codebase summaries
- Changelogs and release notes
- Migration guides for breaking changes

### 6. Versioning and Git Workflows

Follows conventional commit standards and branch management best practices.

**Conventional commit format:**
- `feat(scope):` - New feature (minor version bump)
- `fix(scope):` - Bug fix (patch version bump)
- `docs(scope):` - Documentation only
- `refactor(scope):` - Code restructure, no behavior change
- `test(scope):` - Test additions or corrections
- `chore(scope):` - Build, CI, dependency updates
- `feat!:` or `BREAKING CHANGE:` - Breaking change (major version bump)

**Branch workflow:**
- `main` - Production-ready code
- `feature/<name>` - New features
- `fix/<name>` - Bug fixes
- `release/<version>` - Release preparation
- PRs required for all merges to main
- CI must pass before merge

### Structured Requirements Elicitation
The `ask-me-questions` command pattern provides structured requirement gathering by asking the user targeted questions before beginning implementation. Use this pattern at the start of any development workflow to ensure requirements are clear before writing code.

### 7. Planning and Task Breakdown

Breaks requirements into bite-sized tasks (2-5 minutes each) with explicit file paths, complete code snippets, exact test commands, and expected outputs.

**Plan structure:**
- Header: goal, architecture summary, tech stack
- Tasks with numbered steps
- Each step: exact file paths, complete code, test commands with expected output
- TDD cycle per task: write failing test, verify fail, implement, verify pass, commit
- Execution handoff: subagent-driven (in-session) or parallel session

## Agent Teams for Code Review

For comprehensive code reviews, use Agent Teams parallel review patterns:

### Parallel Multi-Dimensional Review
Spawn specialized reviewers running simultaneously:
- **Security reviewer**: Vulnerabilities, auth bypass, input validation, SQL injection
- **Performance reviewer**: Query efficiency, memory leaks, caching opportunities
- **Architecture reviewer**: SOLID principles, coupling, design patterns
- **Testing reviewer**: Coverage gaps, edge cases, test quality

After all reviewers complete, consolidate findings:
1. Same file:line with same issue → merge findings, credit all reviewers
2. Conflicting severity → use the higher severity rating
3. Conflicting recommendations → include both with reviewer attribution

### Severity Calibration
- **Critical**: Data loss, security breach, complete failure
- **High**: Significant functionality impact (memory leak, missing validation)
- **Medium**: Partial impact, workaround exists (N+1 query, missing edge case)
- **Low**: Minimal impact, cosmetic (style, minor optimization)

## AWOS Specification-to-Implementation Pipeline

The AWOS (Agentic Workflow Operating System) provides an 8-step pipeline for transforming ideas into production code:

### Pipeline Steps
1. **Product Vision** → `context/product/product.md` — Non-technical vision, audience, and rationale
2. **Feature Roadmap** → `context/product/roadmap.md` — Prioritized features and delivery phases
3. **System Architecture** → `context/product/architecture.md` — Tech stack, databases, infrastructure
4. **Functional Spec** → `context/spec/{feature}/spec.md` — What the feature does for users
5. **Technical Plan** → `context/spec/{feature}/tech.md` — How to build it
6. **Task Decomposition** → `tasks.md` + `task_list.json` — Step-by-step implementation checklist
7. **Implementation** → Code changes with progress tracking
8. **Verification** → Validate acceptance criteria are met

### Mandatory Confirmation Gates
After each step, the workflow STOPS and presents output for user review:
- **[A]pprove** — Accept output, continue to next step
- **[E]dit** — User modifies the file, then continues
- **[R]edo** — Provide feedback, regenerate the step

Configurable via `AWOS_SPEC_REFINEMENT=1,4,6` to set which steps require confirmation.

### Session Persistence
The workflow persists state to `awos_session.json` with atomic writes, enabling reliable resume across sessions. Step detection uses file existence (e.g., if `architecture.md` exists, skip to step 4).

For long-running development workflows, persist workflow state to a JSON file (e.g., `session.json`) using atomic writes (write to temp file, then rename). Track current step, completed steps, and user confirmations. This enables reliable resume across sessions without relying on chat history.

## Mandatory Confirmation Pattern

For any multi-step autonomous development workflow, implement confirmation gates between phases:

1. **Execute** the current phase (e.g., requirements analysis, architecture design)
2. **Present** output artifacts to the user
3. **STOP** and wait for explicit approval: Approve / Edit / Redo
4. **Only proceed** after receiving confirmation

This pattern prevents autonomous runaway and ensures stakeholder alignment at critical decision points. Configure which steps require confirmation vs. auto-advance based on team trust and workflow maturity.

## Integration Points

- **GitHub/GitLab:** PR creation, review comments, issue tracking, CI/CD status
- **Jira:** Issue linking, sprint tracking, status transitions
- **Confluence:** Architecture docs, decision records, runbooks
- **Slack:** Review notifications, release announcements

## Workflow Summary

```
Requirements --> Architecture --> Specs --> Plan --> Implement (TDD) --> Review --> Release
     |              |              |          |           |               |          |
     v              v              v          v           v               v          v
  Brainstorm   Tech choices   Func+Tech   Bite-sized   Red-green    Multi-layer  Changelog
  refinement   with alts      specs       tasks        refactor     checklist    + version
```

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate interactive diagrams directly in the conversation. Describe what you need in natural language and Excalidraw renders it as an interactive canvas with hand-drawn style.

### When to Use

- System architecture and component dependency diagrams
- Release pipeline and branching strategy flows
- Code review workflow visualizations
- Sprint planning and feature roadmap layouts

### Workflow

1. Describe the diagram you need — be specific about components, relationships, and layout
2. Review the rendered interactive diagram in the chat
3. Request refinements by describing what to change (add/remove/rearrange elements)
4. Use fullscreen mode for detailed editing when needed

### Tips for Effective Diagrams

- Name specific components and their connections (e.g., "API Gateway connects to Auth Service and User Service")
- Specify layout direction when it matters (e.g., "left-to-right flow" or "top-down hierarchy")
- Request specific diagram types (architecture diagram, flowchart, sequence diagram, ER diagram)
- Iterate — start with the overall structure, then refine details
