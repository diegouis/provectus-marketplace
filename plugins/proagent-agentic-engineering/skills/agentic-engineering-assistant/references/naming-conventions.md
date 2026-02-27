# Naming Conventions

Rules for naming and placing workflow artifacts.

## File Naming

- **kebab-case** for all file names: `my-command.md`, `code-review-agent.md`
- **UPPER_SNAKE_CASE** for variables inside artifacts: `USER_PROMPT`, `PATH_TO_SPEC`
- **lowercase-with-hyphens** for skill and agent names: `skill-name`, `agent-name`

## File Placement

| Artifact Type | Location | Example |
|---|---|---|
| Slash Commands | `.claude/commands/<name>.md` | `.claude/commands/review-code.md` |
| Namespaced Commands | `.claude/commands/<namespace>/<name>.md` | `.claude/commands/review/code.md` |
| Skills | `.claude/skills/<name>/SKILL.md` | `.claude/skills/code-review/SKILL.md` |
| Custom Agents | `.claude/agents/<name>.md` | `.claude/agents/security-reviewer.md` |
| Hooks | `.claude/hooks/<name>.py` | `.claude/hooks/block-rm-rf.py` |
| Expert Systems | `.claude/commands/experts/<domain>/` | `.claude/commands/experts/hooks/` |

## Frontmatter Conventions

- `name` field: matches file name without extension
- `description` field: starts with a verb ("Generates...", "Reviews...", "Validates...")
- `argument-hint` field: uses `[brackets]` for optional args, `<angle>` for required
- `allowed-tools` field: principle of least privilege -- only what the workflow needs

## Variable Conventions

- Prefer `$1`, `$2` over `$ARGUMENTS` when multiple arguments are expected
- Define static variables with defaults inline in the `## Variables` section
- Use descriptive names: `PATH_TO_SPEC` not `P`, `USER_PROMPT` not `UP`

## Spacing and Formatting

- Follow existing codebase conventions (check `.claude/commands/` for patterns)
- Use `---` horizontal rules between major sections
- Use triple-backtick code blocks for templates and examples
- Indent nested content consistently (2 spaces for YAML, 3 spaces for markdown lists)
