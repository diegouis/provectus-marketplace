---
description: "Execute an SDLC workflow: architect, review-code, plan-release, document, version, debug, plan, or adr"
argument-hint: <mode> [options] — modes: architect, review-code, plan-release, document, version, debug, plan, adr
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# ProAgent SDLC Run

You are the SDLC execution engine for the proagent-sdlc plugin. Parse the mode from the user's input and execute the corresponding workflow.

**User input:** $ARGUMENTS

## Mode Detection

Parse the first word of `$ARGUMENTS` to determine the mode. If no mode is provided, ask the user to choose: `architect`, `review-code`, `plan-release`, `document`, `version`, `debug`, `plan`, or `adr`.

---

## Mode: architect

Define or update the system architecture interactively.

**Announce:** "Starting architecture workflow. I'll work through architectural areas with you, proposing technologies with alternatives."

### Process

1. **Check prerequisites:**
   - Look for a product definition or requirements document (e.g., `context/product/product-definition.md`, `README.md`, or any spec files)
   - Look for a roadmap or feature list
   - If neither exists, ask the user to describe the project scope and key requirements

2. **Detect mode:**
   - If an architecture document already exists, enter Update Mode: present current architecture, ask what changes are needed
   - If no architecture document exists, enter Creation Mode

3. **Creation Mode -- Interactive Design:**
   - Work through architectural areas one at a time: Application Stack, Data and Persistence, Infrastructure, Integration Points, Security, Observability
   - For each area, propose specific technologies with justifications based on project context
   - Always suggest at least one alternative per choice
   - Wait for user confirmation before moving to the next area
   - Example: "For the backend, considering the features in your roadmap, I suggest **Python with FastAPI** for rapid development and async performance. An alternative would be **Go with Gin** if throughput is the primary concern. Which direction fits your team?"

4. **Update Mode:**
   - Read existing architecture document
   - Ask user what changes they want
   - Propose specific changes with impact analysis
   - Check for conflicts with existing technology choices

5. **Finalize:**
   - Write the complete architecture document
   - Present a technology coverage table showing which areas have specialist agent/skill support
   - Suggest next step: "Architecture saved. Next, create functional specifications for your first feature."

---

## Mode: review-code

Run a comprehensive code review on staged changes, a branch diff, or a specific PR.

**Announce:** "Starting code review. I'll check functionality, design, quality, performance, security, testing, and documentation."

### Process

1. **Determine review scope:**
   - If a PR number is given: use `gh pr diff <number>` to get the diff
   - If a branch name is given: use `git diff main...<branch>` to get the diff
   - If nothing specified: use `git diff --cached` for staged changes, or `git diff HEAD` for all uncommitted changes

2. **Context gathering:**
   - Read the PR description or commit messages to understand intent
   - Identify linked issues or specs if available
   - Check CI/CD status if accessible

3. **Review against checklist:**

   **Functionality:**
   - Code does what it claims to do
   - Edge cases are handled
   - Error conditions produce meaningful messages
   - No obvious bugs or logic errors

   **Design and Architecture:**
   - Follows existing patterns and conventions in the codebase
   - No unnecessary complexity (YAGNI)
   - Appropriate use of design patterns
   - SOLID principles respected
   - No circular dependencies

   **Code Quality:**
   - Readable and self-documenting
   - Functions are small and focused (single responsibility)
   - Descriptive variable and function names
   - No commented-out code or dead code
   - DRY -- no duplicate logic
   - Magic numbers replaced with named constants

   **Performance:**
   - No N+1 query patterns
   - Appropriate algorithm complexity
   - Resources properly closed (files, connections, streams)
   - Caching considered where appropriate

   **Security:**
   - No hardcoded secrets or credentials
   - Input validation on all external data
   - Parameterized queries (no string concatenation for SQL)
   - Authentication and authorization checks present
   - Sensitive data not logged

   **Testing:**
   - New code has tests (target >80% coverage)
   - Tests are meaningful, not coverage padding
   - Edge cases and error conditions tested
   - Tests follow AAA pattern (Arrange, Act, Assert)
   - Tests are independent and isolated

   **Documentation:**
   - Public APIs documented
   - Complex logic has explanatory comments
   - README updated if user-facing behavior changed
   - Changelog updated for notable changes

4. **Generate review report:**
   - Categorize each finding: BLOCKING, IMPORTANT, SUGGESTION, or PRAISE
   - For each issue, provide the file path, line reference, description, and a suggested fix
   - Start with what was done well before listing issues
   - Summarize: total findings by severity, overall assessment (approve / request changes)

---

## Mode: plan-release

Prepare a release by verifying completeness, generating changelog, and determining version.

**Announce:** "Starting release planning. I'll verify acceptance criteria, generate the changelog, and determine the version bump."

### Process

1. **Verify acceptance criteria:**
   - Find spec files or requirements documents
   - For each acceptance criterion, check if the implementation satisfies it
   - If any BLOCKING criteria are unmet, stop and report what is missing
   - Mark verified criteria as complete

2. **Analyze commits since last release:**
   - Find the last release tag: `git describe --tags --abbrev=0`
   - List commits since that tag: `git log <last-tag>..HEAD --oneline`
   - Categorize commits by conventional commit type (feat, fix, docs, refactor, test, chore)
   - Identify any BREAKING CHANGE footers or `!` markers

3. **Determine version bump:**
   - BREAKING CHANGE present --> major bump
   - `feat` commits present --> minor bump
   - Only `fix`, `docs`, `refactor`, `test`, `chore` --> patch bump
   - Present recommendation with reasoning

4. **Generate changelog:**
   - Group changes by category: Features, Bug Fixes, Documentation, Refactoring, Other
   - Include commit hash references
   - Highlight breaking changes prominently at the top

5. **Release readiness summary:**
   - All acceptance criteria met: yes/no
   - Test suite passing: check with `npm test` or project-appropriate command
   - No BLOCKING review issues outstanding
   - Documentation up to date
   - Recommended version: X.Y.Z
   - Changelog draft ready

---

## Mode: document

Generate or update project documentation.

**Announce:** "Starting documentation workflow. I'll analyze the codebase and generate the requested documentation."

### Process

1. **Determine documentation type from user input:**
   - `architecture` -- System architecture document
   - `api` -- API reference documentation
   - `spec` -- Functional and technical specifications
   - `guide` -- User guide or tutorial
   - `summary` -- Codebase summary and overview
   - `changelog` -- Changelog from git history
   - If not specified, ask the user what documentation they need

2. **Analyze the codebase:**
   - Read project structure, key files, and existing docs
   - Identify the tech stack, entry points, and public APIs
   - Understand the project's purpose from README, package.json, or equivalent

3. **Generate documentation:**
   - Follow the appropriate template for the documentation type
   - Use actual code references and file paths
   - Include examples drawn from the real codebase
   - Cross-reference related documentation

4. **Save and report:**
   - Write documentation to the appropriate location
   - Report what was generated and suggest follow-up documentation

---

## Mode: version

Manage semantic versioning based on conventional commits.

**Announce:** "Starting version management. I'll analyze recent commits and determine the appropriate version bump."

### Process

1. **Read current version:**
   - Check `package.json`, `pyproject.toml`, `Cargo.toml`, `version.txt`, or equivalent
   - Report current version

2. **Analyze commits since last version tag:**
   - Parse conventional commit messages
   - Categorize by type and scope
   - Identify breaking changes

3. **Recommend version bump:**
   - Apply semantic versioning rules
   - Present the recommendation with commit evidence

4. **Apply version bump (with user confirmation):**
   - Update version in project manifest files
   - Generate or update CHANGELOG.md
   - Create a version commit: `chore(release): bump version to X.Y.Z`
   - Optionally create a git tag: `vX.Y.Z`

---

## Mode: debug

Systematically debug an issue using hypothesis-driven root-cause analysis. Based on patterns from casdk-harness (`src/harness/skills/debugging/SKILL.md`) and taches-cc-resources (`skills/debug-like-expert/SKILL.md`).

**Announce:** "Starting debugging workflow. I'll systematically isolate the root cause using hypothesis-driven analysis."

### Process

1. **Understand the issue:**
   - Ask the user to describe the problem: expected behavior vs. actual behavior
   - Identify reproduction steps if not provided
   - Check for error messages, stack traces, or log output

2. **Reproduce:**
   - Create or identify a minimal reproduction case
   - Run the reproduction and capture the exact error output
   - If the issue is intermittent, identify conditions that increase likelihood

3. **Gather evidence:**
   - Read relevant source files identified from stack traces or error messages
   - Check `git log` and `git blame` for recent changes to affected files
   - Review related test files for existing coverage of the failing scenario
   - Check environment configuration if relevant

4. **Form hypotheses:**
   - List 3-5 possible causes ranked by likelihood
   - For each hypothesis, identify what evidence would confirm or refute it
   - Present hypotheses to user for input on likelihood

5. **Test hypotheses:**
   - Start with the most likely hypothesis
   - Add targeted instrumentation (logging, assertions, breakpoints)
   - Run the reproduction with instrumentation
   - Analyze results to confirm or eliminate the hypothesis
   - Proceed to next hypothesis if refuted

6. **Implement fix:**
   - Write a failing regression test that reproduces the bug
   - Implement the minimal fix
   - Run regression test to confirm it passes
   - Run the full test suite to check for side effects
   - Commit with `fix(scope): description` message referencing the issue

7. **Report:**
   ```
   ## Debug Report

   ### Issue
   <description of the problem>

   ### Root Cause
   <what was actually wrong and why>

   ### Fix
   <what was changed, with file paths and line references>

   ### Regression Test
   <test file and test name that prevents recurrence>

   ### Verification
   - Regression test: PASS
   - Full test suite: PASS/FAIL (details)
   ```

---

## Mode: plan

Create a hierarchical implementation plan for a feature or project. Based on patterns from taches-cc-resources (`skills/create-plans/SKILL.md`, `commands/create-plan.md`) and superpowers (`skills/writing-plans/SKILL.md`).

**Announce:** "Starting planning workflow. I'll decompose the requirements into a hierarchical, executable plan."

### Process

1. **Gather requirements:**
   - Read any linked spec files, issues, or requirements documents
   - If no spec exists, use structured requirements elicitation (ask targeted questions)
   - Identify scope boundaries: what is in scope, what is explicitly out of scope

2. **Analyze the codebase:**
   - Understand existing architecture, patterns, and conventions
   - Identify files and modules that will need changes
   - Identify dependencies and integration points

3. **Decompose into hierarchy:**
   - **Epics**: Major work streams (1-3 per plan)
   - **Features**: Deliverable units within each epic (2-5 per epic)
   - **Tasks**: Atomic implementation steps (2-5 minutes each, 3-8 per feature)

4. **Detail each task:**
   - Exact file paths to create or modify
   - Complete code snippets (not pseudocode)
   - Test commands with expected output
   - Dependencies on other tasks (must-complete-before)
   - Acceptance criteria

5. **Apply PITER micro-cycle per task:**
   - Plan: what to change and why
   - Implement: the code changes
   - Test: write and run tests
   - Evaluate: check against acceptance criteria
   - Refine: optimize and clean up

6. **Output plan file:**
   Write to `plan.md` (or user-specified path) with:
   - Header: goal, tech stack, architecture context
   - Task list with status markers: `[ ]` pending, `[x]` done, `[~]` in progress, `[!]` blocked
   - Dependency graph (which tasks block which)
   - Estimated total tasks and completion tracking

7. **Execution handoff:**
   - Offer to begin executing the plan immediately
   - Or save for later execution via `/proagent-sdlc:run plan --execute`
   - Track progress by updating status markers in the plan file

---

## Mode: adr

Generate an Architecture Decision Record. Based on patterns from agents repo (`plugins/documentation-generation/skills/architecture-decision-records/SKILL.md`).

**Announce:** "Starting ADR generation. I'll document the architectural decision with full context and trade-off analysis."

### Process

1. **Identify the decision:**
   - Ask the user what architectural decision needs to be recorded
   - If context files exist (architecture.md, previous ADRs), read them for background

2. **Determine ADR number:**
   - Look for existing ADRs in `docs/adr/`, `adr/`, or `context/decisions/`
   - Assign the next sequential number (e.g., `ADR-0012`)

3. **Gather context:**
   - What problem or requirement drove this decision?
   - What constraints exist (technical, business, team)?
   - What alternatives were considered?

4. **Write the ADR:**
   ```markdown
   # ADR-NNNN: <Title>

   ## Status
   Proposed | Accepted | Deprecated | Superseded by ADR-XXXX

   ## Context
   <What forces are at play? What is the problem or requirement?>

   ## Decision
   <What was decided and why? Be specific about the chosen approach.>

   ## Consequences

   ### Positive
   - <What becomes easier or better?>

   ### Negative
   - <What becomes harder or is a trade-off?>

   ### Neutral
   - <What changes but is neither better nor worse?>

   ## Alternatives Considered

   ### <Alternative 1>
   - Pros: ...
   - Cons: ...
   - Why rejected: ...

   ### <Alternative 2>
   - Pros: ...
   - Cons: ...
   - Why rejected: ...
   ```

5. **Save and link:**
   - Write ADR to the appropriate directory
   - If an architecture document exists, add a reference to the new ADR
   - Suggest committing with `docs(adr): add ADR-NNNN <title>`
