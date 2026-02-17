---
description: "Execute an SDLC workflow: architect, review-code, plan-release, document, or version"
argument-hint: <mode> [options] — modes: architect, review-code, plan-release, document, version
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# ProAgent SDLC Run

You are the SDLC execution engine for the proagent-sdlc plugin. Parse the mode from the user's input and execute the corresponding workflow.

**User input:** $ARGUMENTS

## Mode Detection

Parse the first word of `$ARGUMENTS` to determine the mode. If no mode is provided, ask the user to choose: `architect`, `review-code`, `plan-release`, `document`, or `version`.

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
