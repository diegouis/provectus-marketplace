### 1. Agent Design and Creation

Create specialized AI agents following Anthropic's sub-agent architecture.

**Key Patterns**:

- **Single Responsibility**: One agent = one domain. Focused expertise, not general purpose.
- **Discovery-Optimized Descriptions**: Include concrete `<example>` dialogues with `<commentary>` in the YAML `description` field.
- **Tool Restriction Strategy**: Grant only necessary tools using principle of least privilege.
- **Model Selection**: `opus` for complex reasoning, `sonnet` for balanced (default), `haiku` for fast/simple tasks.

**Agent Archetypes**:

| Archetype | Tools | Example |
|-----------|-------|---------|
| Research/Analysis | Read, Grep, Glob | Code reviewer, security auditor |
| Development | Read, Write, Edit, MultiEdit, Bash | Python expert, React specialist |
| Infrastructure | Bash, Read, Write | Docker engineer, K8s expert |
| Orchestration | Task, Read, Write | Project planner, workflow coordinator |

**Agent Archetypes and Examples**:
- Python/FastAPI development expert
- TypeScript development expert
- React development expert
- Automated code review expert
- Docker infrastructure engineer
- Kubernetes engineer
- SDET agent for testing strategies
- Code assist agent with Explore-Plan-Code-Commit workflow
- Code review subagent
- Skill quality auditor
- Workflow orchestration conductor

**Agent Definition Structure**:

```yaml
---
name: agent-identifier
description: >
  Primary description with capabilities and use cases.
  Use PROACTIVELY when [specific scenarios].

  Examples:
  <example>
  Context: Situation description
  user: "User request example"
  assistant: "I'll use the agent-name to handle this task."
  <commentary>
  Explanation of why this agent is appropriate.
  </commentary>
  </example>

tools: Tool1, Tool2, Tool3
model: sonnet
---

System prompt content starts here.

You are a [role description] specializing in [domain].

## Core Responsibilities
- Concrete, actionable responsibilities

## Approach
- Methodology with examples

## Constraints
- Limitations and boundaries
```

### 2. Skill Creation

Create model-invoked autonomous capabilities that Claude activates based on context.

**Key Patterns**:

- **Progressive Disclosure**: Three-level loading -- metadata (~100 words), SKILL.md body (<5k words), bundled resources (unlimited).
- **Discovery Optimization**: The `description` field determines when Claude uses the skill. Include trigger terms, activation scenarios, and scope boundaries.
- **Imperative Writing Style**: Use verb-first instructions ("To accomplish X, do Y"), not second person.

**Skill Directory Structure**:

```
skill-name/
├── SKILL.md                 # Required: Skill definition
├── scripts/                 # Optional: Deterministic code
├── references/              # Optional: On-demand documentation
├── assets/                  # Optional: Output resources (templates, images)
└── examples/                # Optional: Usage examples
```

**Skill Creation Process**:

1. **Understand** -- Gather concrete usage examples and trigger scenarios
2. **Plan** -- Identify reusable resources (scripts, references, assets)
3. **Initialize** -- Create skill directory with proper structure
4. **Edit** -- Write SKILL.md with frontmatter and instructions
5. **Package** -- Validate and distribute
6. **Iterate** -- Refine based on real usage

**Skill Examples**:
- Meta-skill for creating new skills
- Build new agent skills from descriptions
- Socratic design refinement before coding
- Break work into 2-5 minute tasks
- RED-GREEN-REFACTOR TDD cycle
- Evidence-based verification
- Manus-style file-based planning with hooks
- Prompt-Driven Development
- Conversational evaluation framework

### 3. Command Creation

Create user-invoked slash commands as reusable prompt templates.

**Key Patterns**:

- **Argument Handling**: `$ARGUMENTS` (all args), `$1, $2` (positional), `${1:-default}` (defaults)
- **File References**: `@file` includes file contents in the prompt
- **Bash Execution**: `!command` runs shell commands (requires `allowed-tools: Bash(...)`)
- **Frontmatter**: `description`, `argument-hint`, `allowed-tools`, `model`, `disable-model-invocation`

**Command File Location**:
- Project: `.claude/commands/command-name.md`
- Personal: `~/.claude/commands/command-name.md`
- Plugin: `plugin-name/commands/command-name.md`

**Command Examples**:
- Invoke skill creation
- Build custom slash commands
- Build specialized Claude instances
- Build event-driven hooks
- Generate optimized prompts
- Socratic design refinement
- Write detailed implementation plans
- Execute plans with human checkpoints
- Lead implementation agent
- Verify implementation against acceptance criteria
- Create new agent definitions interactively

### 4. Hook Configuration

Create lifecycle event automation for deterministic control.

**Key Patterns**:

**Ten Lifecycle Events**:

| Event | Blocking | Use Cases |
|-------|----------|-----------|
| PreToolUse | Yes (exit 2) | Block edits, validate commands, log usage |
| PostToolUse | No | Format code, run linters, sync changes |
| UserPromptSubmit | Yes | Inject context, validate prompts |
| PermissionRequest | Yes | Auto-approve/deny operations |
| Notification | No | Custom alerts (macOS, Linux, Slack) |
| Stop | Yes | Run tests, update docs, commit changes |
| SubagentStop | Yes | Log results, validate outputs |
| PreCompact | Yes | Save conversation state |
| SessionStart | No | Load context, display status |
| SessionEnd | No | Cleanup, export logs |

**Hook Configuration Structure** (in `.claude/settings.json` or `hooks/hooks.json` for plugins):

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "shell command",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**Hook Input**: JSON via stdin. Use `jq` to extract: `.tool_input.file_path`, `.tool_input.command`, `.tool_name`, `.session_id`, `.cwd`.

**Hook Examples**:
- SessionStart hook for loading context
- PreToolUse/PostToolUse/Stop hooks for file-based planning
- Pre-validation guardrails
- Post-processing and logging
- Graceful session termination

### 5. Plugin Development

Bundle agents, skills, commands, hooks, and MCP servers into distributable plugins.

**Key Patterns**:

**Plugin Structure**:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json              # Required: metadata
├── agents/                      # Sub-agent definitions
├── skills/                      # Skill definitions
│   └── skill-name/
│       └── SKILL.md
├── commands/                    # Slash commands
├── hooks/
│   └── hooks.json               # Hook configurations
├── .mcp.json                    # MCP server configs
├── CLAUDE.md                    # Context documentation
└── README.md                    # User documentation
```

**plugin.json Fields**: `name`, `version` (semver), `description`, `author`, `license`, `keywords`, `engines`, `dependencies`.

**Installation Methods**:
- `/plugin install plugin-name` -- From marketplace
- `/plugin install /path/to/plugin` -- From local path
- `/plugin install https://github.com/user/plugin.git` -- From Git
- `.claude/settings.json` plugins config -- Project-level auto-install

**Plugin Examples**:
- Context engineering plugin (5 skills, 1 agent, 1 command)
- Research team plugin (3 agents, 1 skill, 1 command)

### 6. MCP Server Development

Build Model Context Protocol servers to connect Claude to external services.

**Key Patterns**:

**Four-Phase Process**:

1. **Research and Planning**: Study API docs, MCP protocol (`https://modelcontextprotocol.io/llms-full.txt`), SDK docs
2. **Implementation**: Set up project, implement core infrastructure, add tools systematically
3. **Review and Refine**: DRY, composability, consistency, error handling, type safety
4. **Create Evaluations**: 10 complex, realistic, verifiable evaluation questions

**Agent-Centric Design Principles**:
- Build for workflows, not just API endpoints
- Optimize for limited context (high-signal responses, concise/detailed modes)
- Design actionable error messages
- Follow natural task subdivisions
- Use evaluation-driven development

**Tool Annotations**: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`

**Python**: Use FastMCP with Pydantic v2 models, `@mcp.tool` decorator
**TypeScript**: Use MCP TypeScript SDK with Zod schemas, `server.registerTool`

**MCP Configuration Examples**:
- Playwright and Puppeteer MCP servers
- Playwright MCP for E2E testing
- Google Drive MCP server
