# ProAgent SDLC Plugin

This plugin provides end-to-end software development lifecycle management for Claude Code. It was synthesized from 17 open-source repositories including AWOS, superpowers, casdk-harness, tac, ralph-orchestrator, and proagent.

## Plugin Structure

```
proagent-sdlc/
├── .claude-plugin/plugin.json    # Plugin manifest (name, version, category)
├── .mcp.json                     # MCP server configs (GitHub, GitLab, Jira, Confluence)
├── skills/
│   └── sdlc-assistant/SKILL.md   # Core skill: Managing Software Development Lifecycle
├── commands/
│   ├── hub.md                    # Command hub: list and route to SDLC commands
│   ├── run.md                    # Execute: architect, review-code, plan-release, document, version
│   └── review.md                 # Review: pr, architecture, test-coverage, release-readiness
├── agents/
│   └── sdlc-specialist.md        # SDLC specialist subagent for code review and assessments
├── hooks/
│   └── hooks.json                # Pre-commit quality gates, post-review notifications, pre-push validation
├── CLAUDE.md                     # This file
└── README.md                     # User-facing documentation
```

## Usage

### Skill
Use the `proagent-sdlc:sdlc-assistant` skill when managing any SDLC phase. It covers architecture decisions, code review, testing strategy, release management, documentation, versioning, and git workflows.

### Commands
- `/proagent-sdlc:hub` -- See all available commands and choose the right workflow
- `/proagent-sdlc:run <mode>` -- Execute a workflow (architect, review-code, plan-release, document, version)
- `/proagent-sdlc:review <type>` -- Run a quality review (pr, architecture, test-coverage, release-readiness)

### Agent
The `proagent-sdlc:sdlc-specialist` agent can be dispatched as a subagent for code reviews, architecture assessments, and release readiness checks. It produces structured reports with findings categorized by severity.

### Hooks
Three hooks enforce quality gates:
1. **Pre-commit:** Validates conventional commit format, checks for TODO/FIXME in staged changes, verifies test files exist for new source files
2. **Post-review:** Formats review findings into a structured summary with severity counts and next steps
3. **Pre-push:** Prevents pushing WIP/fixup commits and warns if the branch is behind the remote

### MCP Servers
Configure the following environment variables to enable integrations:
- `GITHUB_PERSONAL_ACCESS_TOKEN` -- GitHub PR management and issue tracking
- `GITLAB_PERSONAL_ACCESS_TOKEN` / `GITLAB_API_URL` -- GitLab merge requests and CI/CD
- `ATLASSIAN_API_TOKEN` / `ATLASSIAN_EMAIL` / `ATLASSIAN_DOMAIN` -- Jira issues and Confluence docs

## Source Attribution

Key patterns and content were drawn from:
- **awos** -- Architecture command, spec/verify workflows, document hierarchy templates
- **casdk-harness** -- Code review checklist, automated review pipeline, documentation skills
- **superpowers** -- TDD planning (writing-plans), code review dispatch (requesting-code-review), testing anti-patterns, branch completion workflows
- **tac** -- Semantic commits, automated PR creation, review command with spec compliance, SDLC pipeline orchestration
- **ralph-orchestrator** -- Spec-driven development, TDD SOP, codebase summary skill
- **awesome-claude-skills** -- Changelog generation from git commits
- **proagent** -- Technical writer roles (user guide creation, information architecture, spec creation)
- **planning-with-files** -- File-based planning with hooks and task templates
