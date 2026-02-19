---
name: sdlc-assistant
description: Use when managing any phase of the software development lifecycle -- architecture decisions, code review, testing strategy, release planning, documentation, versioning, git workflows, debugging, hierarchical planning, ADR generation, C4 diagrams, or multi-agent review pipelines
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
- Debugging issues systematically using hypothesis-driven root-cause analysis
- Generating Architecture Decision Records (ADRs) and C4 context diagrams
- Orchestrating multi-stage pipelines (ProAgent 5-stage, PITER framework)
- Creating and executing hierarchical project plans with progress tracking
- Finalizing development branches with pre-merge quality checks

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

**Enhanced commit workflow** (from awesome-claude-code `resources/slash-commands/commit/commit.md`):
- Analyze staged changes to auto-generate semantic commit messages
- Validate conventional commit format before committing
- Include scope detection from changed file paths

**AI-powered PR creation** (from awesome-claude-code `resources/slash-commands/create-pr/create-pr.md`):
- Auto-generate PR title and description from branch commits
- Link related issues automatically
- Populate review checklist based on change types

**Branch finalization** (from superpowers `skills/finishing-a-development-branch/SKILL.md`):
- Pre-merge quality checklist: all tests pass, no TODO/FIXME in diff, documentation updated
- Squash or rebase strategy recommendation based on commit history
- Final review dispatch before merge

### Structured Requirements Elicitation
The `ask-me-questions` command pattern provides structured requirement gathering by asking the user targeted questions before beginning implementation. Use this pattern at the start of any development workflow to ensure requirements are clear before writing code.

### 7. Planning and Task Breakdown

Breaks requirements into bite-sized tasks (2-5 minutes each) with explicit file paths, complete code snippets, exact test commands, and expected outputs. Integrates patterns from taches-cc-resources (hierarchical project planning) and superpowers (plan writing and execution).

**Plan structure:**
- Header: goal, architecture summary, tech stack
- Tasks with numbered steps
- Each step: exact file paths, complete code, test commands with expected output
- TDD cycle per task: write failing test, verify fail, implement, verify pass, commit
- Execution handoff: subagent-driven (in-session) or parallel session

**Hierarchical planning** (from taches-cc-resources `skills/create-plans/SKILL.md`):
- Decompose complex projects into epics, features, and tasks
- Each task includes clear acceptance criteria and dependencies
- Track progress with status markers (pending, in-progress, done, blocked)

**Plan execution** (from superpowers `skills/executing-plans/SKILL.md`):
- Read the plan file, identify the next uncompleted task
- Execute the task following TDD discipline
- Mark task complete with commit reference
- Auto-advance to next task or pause for confirmation at phase boundaries

### 8. Debugging

Applies systematic, hypothesis-driven debugging methodologies drawn from casdk-harness (`src/harness/skills/debugging/SKILL.md`) and taches-cc-resources (`skills/debug-like-expert/SKILL.md`).

**Debugging workflow:**
1. Reproduce the issue with a minimal test case
2. Gather evidence: error messages, stack traces, logs, git blame
3. Form hypotheses ranked by likelihood
4. Test each hypothesis with targeted instrumentation (breakpoints, logging, assertions)
5. Identify root cause, not just symptoms
6. Implement fix with regression test
7. Verify fix does not introduce side effects

**Debugging anti-patterns to avoid:**
- Shotgun debugging (random changes hoping something works)
- Print-statement overload without hypothesis
- Fixing symptoms instead of root cause
- Skipping the regression test after fix

### 9. Architecture Decision Records (ADRs)

Generates ADRs following the pattern from agents repo (`plugins/documentation-generation/skills/architecture-decision-records/SKILL.md`). Each ADR captures a single architectural decision with full context.

**ADR structure:**
- Title: short descriptive name
- Status: proposed, accepted, deprecated, superseded
- Context: what forces are at play, what is the problem
- Decision: what was decided and why
- Consequences: what becomes easier, what becomes harder
- Alternatives considered: with trade-off analysis

### 10. C4 Architecture Diagrams

Generates C4 model documentation following the pattern from agents repo (`plugins/c4-architecture/agents/c4-context.md`).

**C4 levels:**
- Context: system boundaries, external actors, and integrations
- Container: applications, data stores, and communication protocols
- Component: internal modules, services, and their responsibilities
- Code: class/module level detail (optional, for critical paths only)

Output as structured markdown with Excalidraw or Mermaid diagram descriptions.

## Changelog Generation

Automated changelog generation follows the pattern from awesome-claude-skills (`changelog-generator/SKILL.md`):

1. Parse conventional commits since last release tag
2. Group by type: Features, Bug Fixes, Performance, Breaking Changes, Documentation, Chores
3. Include commit hash, scope, and description
4. Highlight breaking changes at the top with migration notes
5. Output as CHANGELOG.md entry with release date and version

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
1. Same file:line with same issue → merge findings, credit all reviewers
2. Conflicting severity → use the higher severity rating
3. Conflicting recommendations → include both with reviewer attribution

### Severity Calibration
- **Critical**: Data loss, security breach, complete failure
- **High**: Significant functionality impact (memory leak, missing validation)
- **Medium**: Partial impact, workaround exists (N+1 query, missing edge case)
- **Low**: Minimal impact, cosmetic (style, minor optimization)

## ProAgent 5-Stage SDLC Pipeline

The ProAgent orchestration engine (`proagent-repo/core/orchestration/sdlc/pipeline.py`) defines a 5-stage pipeline that maps to the core SDLC phases:

1. **Analyze** -- Gather requirements, read specs, understand the problem domain
2. **Design** -- Architecture decisions, technology selection, component design
3. **Implement** -- Code generation with TDD, following the plan task-by-task
4. **Validate** -- Code review, test execution, acceptance criteria verification
5. **Deliver** -- Versioning, changelog, release readiness, deployment preparation

Each stage produces artifacts that feed the next. The pipeline can be run end-to-end or entered at any stage for targeted workflows.

## PITER Framework

The PITER framework (`proagent-repo/core/skills/tac/piter.md`) provides a micro-cycle for individual task execution:

- **Plan** -- Understand the task, identify files to change, define the approach
- **Implement** -- Write the code following the plan
- **Test** -- Write and run tests to verify correctness
- **Evaluate** -- Assess quality, check edge cases, review against requirements
- **Refine** -- Improve based on evaluation feedback, optimize, clean up

Apply PITER within each task of a larger plan. It complements TDD by adding explicit evaluation and refinement phases.

## Ralph Orchestrator Presets

The ralph-orchestrator provides pre-configured workflow presets for common SDLC scenarios:

- **Bugfix preset** (`ralph-orchestrator/presets/bugfix.yml`): Reproduce issue, isolate root cause, implement fix with regression test, verify no side effects
- **Refactor preset** (`ralph-orchestrator/presets/refactor.yml`): Identify refactoring target, ensure test coverage exists, apply transformation, verify behavior preservation

These presets define step sequences, quality gates, and rollback conditions for orchestrated multi-agent workflows.

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

### AWOS Commands
The AWOS framework provides 7 commands that map to pipeline steps:
- `awos/commands/spec.md` -- Generate functional specifications from product vision
- `awos/commands/architecture.md` -- Interactive architecture design with alternatives
- `awos/commands/implement.md` -- Execute implementation with task decomposition and TDD

AWOS also provides reusable templates:
- `awos/templates/architecture-template.md` -- Structured architecture document scaffold
- `awos/templates/functional-spec-template.md` -- Functional specification scaffold with acceptance criteria sections

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
  Brainstorm   Tech choices   Func+Tech   Hierarchical  PITER cycle  Multi-agent  Changelog
  refinement   C4 + ADRs     specs+AWOS   task plans   per task     parallel     + version
               templates     templates    + tracking   red-green    review       + branch
                                                       refactor     pipeline     finalize
```

### Pipeline Frameworks

| Framework | Source | Scope | Stages |
|-----------|--------|-------|--------|
| ProAgent 5-stage | `proagent-repo/core/orchestration/sdlc/pipeline.py` | Full project | Analyze, Design, Implement, Validate, Deliver |
| AWOS 8-step | `awos/commands/*` | Feature development | Vision, Roadmap, Architecture, Spec, Plan, Tasks, Implement, Verify |
| PITER | `proagent-repo/core/skills/tac/piter.md` | Single task | Plan, Implement, Test, Evaluate, Refine |
| Ralph presets | `ralph-orchestrator/presets/*.yml` | Targeted workflows | Bugfix, Refactor (configurable step sequences) |

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
