---
description: Review agent systems, skills, prompts, commands, hooks, plugins, orchestration patterns, and MCP servers for quality and best practices
argument-hint: [path-or-component-type]
model: opus
---

# ProAgent Agentic Engineering -- Reviewer

Perform a comprehensive review of agentic engineering artifacts. Analyze $ARGUMENTS or, if no specific target is provided, scan the current project for Claude Code components and review them all.

## Review Scope

Scan and review all of the following component types found in the project:

### 1. Agent Definitions (`.claude/agents/*.md`, `agents/*.md`)

For each agent, evaluate:

- **Single Responsibility**: Does the agent have ONE clear, focused purpose? Flag overly broad agents (e.g., "backend-expert" covering all backend technologies).
- **Description Quality**: Does the description include:
  - Primary capability statement (1-2 sentences)
  - Specific activation scenarios
  - 2-4 concrete `<example>` blocks with `<commentary>`
  - Trigger terms for discovery
  - "Use PROACTIVELY when..." phrasing
- **Tool Restrictions**: Are tools restricted following least privilege? Flag agents with full tool access that should be read-only (e.g., review agents with Write access).
- **Model Selection**: Is the model appropriate? (opus for complex reasoning, sonnet for balanced, haiku for simple)
- **System Prompt Quality**: Does it include Core Responsibilities, Approach, and Constraints sections?


### 2. Skills (`skills/*/SKILL.md`, `.claude/skills/*/SKILL.md`)

For each skill, evaluate:

- **Frontmatter Completeness**: Does YAML frontmatter include `name` and `description`?
- **Description Quality**: Does description include:
  - Trigger terms for activation
  - "Activate when user mentions:" section
  - Scope boundaries ("Do NOT use for:")
  - Concrete usage scenarios
- **Writing Style**: Is imperative/infinitive form used throughout (not second person)?
- **Progressive Disclosure**: Is content organized for efficient token usage (metadata -> instructions -> supporting files)?
- **Supporting Files**: Are scripts/, references/, assets/ organized properly?
- **References**: Do all referenced files actually exist?


### 3. Commands (`.claude/commands/*.md`, `commands/*.md`)

For each command, evaluate:

- **Frontmatter**: Does it have `description` and `argument-hint` fields?
- **Argument Handling**: Are `$ARGUMENTS`, `$1`/`$2`, and `${1:-default}` used correctly?
- **Bash Security**: Are `!command` bash calls covered by `allowed-tools: Bash(...)`?
- **Scope**: Is the command appropriately simple (not trying to be an agent)?
- **Documentation**: Is usage clear from the command content?


### 4. Hooks (`.claude/settings.json`, `hooks/hooks.json`)

For each hook configuration, evaluate:

- **Event Selection**: Is the correct lifecycle event used?
- **Matcher Specificity**: Is the matcher appropriately scoped (not wildcard when specific tool names would work)?
- **Security**: Does the shell command:
  - Avoid logging sensitive data (credentials, tokens, env vars)?
  - Use `jq` correctly for stdin JSON processing?
  - Quote shell variables properly?
  - Avoid external API calls with sensitive data?
- **Timeout**: Is a reasonable timeout configured?
- **Exit Codes**: For PreToolUse hooks, are exit codes correct (0=allow, 2=block)?
- **Blocking Logic**: Is blocking used only on events that support it?


### 5. Plugins (`.claude-plugin/plugin.json`)

For each plugin, evaluate:

- **plugin.json**: Is it valid with required fields (name, version, description)?
- **Versioning**: Does it follow semver?
- **Component Organization**: Are agents, skills, commands organized in proper directories?
- **Naming Conflicts**: Could component names conflict with standard Claude Code components?
- **Documentation**: Does README.md include installation and usage instructions?
- **CLAUDE.md**: Does it provide context for Claude sessions?


### 6. MCP Configurations (`.mcp.json`)

For each MCP configuration, evaluate:

- **Server Definitions**: Are `command` and `args` properly specified?
- **Environment Variables**: Are secrets referenced via `${VAR}` (not hardcoded)?
- **Tool Design**: Are tools workflow-oriented (not raw API wrappers)?


### 7. Orchestration Patterns

If multi-agent workflows exist, evaluate:

- **Pattern Selection**: Is the orchestration pattern appropriate for the task?
- **Hand-off Clarity**: Are agent-to-agent hand-offs explicit?
- **Error Handling**: Are failure modes handled (rollback, retry, alert)?
- **Context Provision**: Does each agent receive complete context (not required to discover it)?
- **Token Budget**: Is token usage considered and budgeted?
- **Progress Tracking**: Is there logging and checkpoint support?


## Output Format

Generate a structured review report:

```markdown
# Agentic Engineering Review Report

## Summary
- Components found: [count by type]
- Overall score: [A/B/C/D/F]
- Critical issues: [count]
- Warnings: [count]
- Recommendations: [count]

## Component Reviews

### [Component Type]: [Component Name]
**Score**: [A-F]
**Issues**:
- [CRITICAL] Description of critical issue
- [WARNING] Description of warning
- [INFO] Description of recommendation

**Strengths**:
- What the component does well

**Recommendations**:
1. Specific, actionable improvement
2. Another improvement
```

## Review Priorities

1. **Security** -- Credential exposure, tool permissions, hook safety
2. **Discovery** -- Will Claude find and invoke components correctly?
3. **Quality** -- Follows Anthropic specifications and best practices?
4. **Completeness** -- All required fields present, supporting files exist?
5. **Efficiency** -- Token usage, progressive disclosure, appropriate model selection?
