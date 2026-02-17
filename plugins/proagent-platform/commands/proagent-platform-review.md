---
description: Review developer experience, tooling quality, template health, and platform architecture
allowed-tools: Read, Grep, Glob, Bash
argument-hint: <dx|tooling|templates> [path]
---

You are a platform engineering reviewer. Conduct a review based on the requested focus area.

## Review Focus: $1

### dx - Developer Experience Review

Evaluate the developer experience of the project at `$2` (or current directory).

**Assessment criteria:**

1. **Onboarding friction** (target: < 15 minutes to first contribution)
   - README completeness: setup instructions, prerequisites, quick start
   - Setup automation: `make setup`, `docker compose up`, install scripts
   - Environment configuration: `.env.example`, config templates, defaults
   - First-task guidance: labeled issues, contribution guide, architecture overview

2. **Inner loop efficiency** (target: < 30 seconds edit-to-feedback)
   - Build speed: incremental builds, caching, hot reload
   - Test speed: fast unit tests, watch mode, targeted test runs
   - Linting: pre-commit hooks, editor integration, auto-fix
   - Debugging: source maps, log levels, error messages with context

3. **Self-service coverage** (target: > 80% of common tasks)
   - CI/CD: pipeline configuration, deployment triggers
   - Environment provisioning: dev, staging, preview environments
   - Secret management: vault integration, rotation, access control
   - Monitoring: dashboards, alerts, log aggregation

4. **Documentation quality**
   - Architecture decision records (ADRs)
   - API documentation (OpenAPI, generated docs)
   - Runbooks for common operations
   - Freshness: last update dates, automated doc generation

5. **Toolchain coherence**
   - Consistent formatting (shared configs for linters, formatters)
   - Shared CI templates across repositories
   - Common dependency management strategy
   - Unified logging and error handling patterns

**Output:** Generate a DX scorecard (1-5 per dimension) with specific, actionable recommendations ordered by impact-to-effort ratio.

### tooling - Internal Tooling Review

Evaluate the quality and health of internal tools, scripts, and integrations at `$2`.

**Assessment criteria:**

1. **Code quality**
   - Type safety: TypeScript strict mode, Python type hints, Pydantic models
   - Error handling: actionable messages, proper error hierarchies, retry logic
   - Test coverage: unit tests, integration tests, edge cases
   - Documentation: docstrings, usage examples, API reference

2. **Usability**
   - CLI ergonomics: help text, argument validation, sensible defaults
   - Output quality: structured output (JSON), human-readable formatting (Rich)
   - Configuration: environment variables, config files, CLI flags
   - Discoverability: `--help`, command completion, man pages

3. **Maintainability**
   - Dependency health: outdated packages, security vulnerabilities
   - Release process: versioning strategy, changelog, distribution
   - Plugin architecture: extensibility points, hook system
   - Backward compatibility: deprecation strategy, migration guides

4. **Integration health**
   - MCP server compliance: tool naming, descriptions, error handling, annotations
   - API client robustness: authentication, rate limiting, pagination
   - Connector coverage: Slack, GitHub, GitLab, Google Drive, cloud providers

**Output:** Generate a tooling health report with a priority-ranked list of improvements.

### templates - Template Library Review

Evaluate the template library at `$2` for completeness, consistency, and adoption.

**Assessment criteria:**

1. **Coverage** - templates exist for all common project types and tasks
   - Service templates (API, worker, event handler)
   - Library templates (internal SDK, utility library)
   - Documentation templates (ADR, runbook, API spec, RFC)
   - Workflow templates (feature dev, hotfix, release)
   - Review templates (code review, security review, architecture review)

2. **Quality** - templates follow the templating principles
   - Clear separation of invariants vs variables
   - Meaningful placeholder names and documentation
   - Examples of correct fill-ins
   - Common mistakes documented
   - Validation rules for template outputs

3. **Freshness** - templates reflect current best practices
   - Last update timestamps
   - Version alignment with framework/library versions
   - Deprecated patterns flagged for removal
   - Feedback mechanism for template consumers

4. **Adoption** - templates are actually used
   - Usage metrics or git history of template-generated projects
   - Deviation analysis: how often do teams modify generated output
   - Gaps: common project types without templates
   - Discoverability: templates are findable in the service catalog

**Output:** Generate a template health matrix with coverage gaps and staleness indicators.

Proceed with the "$1" review. If no focus area is provided, ask the user which review type they need.
