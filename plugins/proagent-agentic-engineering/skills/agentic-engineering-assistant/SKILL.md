---
name: Building Agentic Systems
description: >
  Comprehensive skill for designing, building, orchestrating, and optimizing AI agent systems
  with Claude Code. Covers agent design patterns, multi-agent orchestration, skill/command/hook
  creation, MCP server development, prompt engineering, plugin architecture, agent evaluation,
  and context engineering best practices.

  This skill should be used when the user mentions:
  - Creating agents, skills, commands, hooks, or plugins for Claude Code
  - Multi-agent orchestration, parallel agents, subagent workflows
  - MCP server development or integration
  - Prompt engineering, context engineering, or prompt-driven development
  - Agent evaluation, testing agent systems, or agent quality assurance
  - Claude Code extensions, customization, or configuration
  - Agentic development workflows (ADW), trust ladder, progressive autonomy
  - Subagent-driven development (SDD), dispatching parallel agents
  - File-based planning with hooks, plan execution with agents

  Do NOT use for:
  - General software development without an agentic component (use sdlc or backend/frontend skills)
  - DevOps infrastructure without agent involvement (use devops skills)
  - Pure testing without agent evaluation (use qa skills)
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebFetch, WebSearch
---

# Building Agentic Systems

## Overview

This skill provides comprehensive guidance for building, orchestrating, and optimizing AI agent systems using Claude Code. It synthesizes proven patterns from 19 source repositories containing 612 assets, covering the full lifecycle of agentic engineering: from designing individual agents to orchestrating complex multi-agent workflows.

## Core Domains

### 1. Agent Design and Creation

Create specialized AI agents following Anthropic's sub-agent architecture.

**Key Patterns** (from `casdk-harness/src/harness/plugins/context-engineering/skills/agent-definition-creation/SKILL.md`):

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

**Reference Agents** (from `casdk-harness/src/harness/agents/configs/`):
- `dev-python-expert.md` -- Python/FastAPI development expert
- `dev-typescript-expert.md` -- TypeScript development expert
- `dev-react-expert.md` -- React development expert
- `dev-code-review-expert.md` -- Automated code review expert
- `infra-docker-engineer.md` -- Docker infrastructure engineer
- `infra-k8s-engineer.md` -- Kubernetes engineer
- `test-sdet-expert.md` -- SDET agent for testing strategies

**Additional Agent References**:
- `ralph-orchestrator/.claude/agents/code-assist.md` -- Code assist agent with Explore-Plan-Code-Commit workflow
- `superpowers/agents/code-reviewer.md` -- Code review subagent
- `taches-cc-resources/agents/skill-auditor.md` -- Skill quality auditor
- `agents/plugins/conductor/agents/conductor.md` -- Workflow orchestration conductor

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

**Key Patterns** (from `awesome-claude-skills/skill-creator/SKILL.md` and `casdk-harness/src/harness/plugins/context-engineering/skills/skill-creation/SKILL.md`):

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

**Skill Creation Process** (from `awesome-claude-skills/skill-creator/SKILL.md`):

1. **Understand** -- Gather concrete usage examples and trigger scenarios
2. **Plan** -- Identify reusable resources (scripts, references, assets)
3. **Initialize** -- Create skill directory with proper structure
4. **Edit** -- Write SKILL.md with frontmatter and instructions
5. **Package** -- Validate and distribute
6. **Iterate** -- Refine based on real usage

**Reference Skills**:
- `superpowers/skills/writing-skills/SKILL.md` -- Meta-skill for creating new skills
- `taches-cc-resources/skills/create-agent-skills/SKILL.md` -- Build new agent skills from descriptions
- `superpowers/skills/brainstorming/SKILL.md` -- Socratic design refinement before coding
- `superpowers/skills/writing-plans/SKILL.md` -- Break work into 2-5 minute tasks
- `superpowers/skills/test-driven-development/SKILL.md` -- RED-GREEN-REFACTOR TDD cycle
- `superpowers/skills/verification-before-completion/SKILL.md` -- Evidence-based verification
- `planning-with-files/skills/planning-with-files/SKILL.md` -- Manus-style file-based planning with hooks
- `ralph-orchestrator/.claude/skills/pdd/SKILL.md` -- Prompt-Driven Development
- `ralph-orchestrator/.claude/skills/eval/SKILL.md` -- Conversational evaluation framework

### 3. Command Creation

Create user-invoked slash commands as reusable prompt templates.

**Key Patterns** (from `casdk-harness/src/harness/plugins/context-engineering/skills/command-creation/SKILL.md`):

- **Argument Handling**: `$ARGUMENTS` (all args), `$1, $2` (positional), `${1:-default}` (defaults)
- **File References**: `@file` includes file contents in the prompt
- **Bash Execution**: `!command` runs shell commands (requires `allowed-tools: Bash(...)`)
- **Frontmatter**: `description`, `argument-hint`, `allowed-tools`, `model`, `disable-model-invocation`

**Command File Location**:
- Project: `.claude/commands/command-name.md`
- Personal: `~/.claude/commands/command-name.md`
- Plugin: `plugin-name/commands/command-name.md`

**Reference Commands**:
- `taches-cc-resources/commands/create-agent-skill.md` -- Invoke skill creation
- `taches-cc-resources/commands/create-slash-command.md` -- Build custom slash commands
- `taches-cc-resources/commands/create-subagent.md` -- Build specialized Claude instances
- `taches-cc-resources/commands/create-hook.md` -- Build event-driven hooks
- `taches-cc-resources/commands/create-prompt.md` -- Generate optimized prompts
- `superpowers/commands/brainstorm.md` -- Socratic design refinement
- `superpowers/commands/write-plan.md` -- Write detailed implementation plans
- `superpowers/commands/execute-plan.md` -- Execute plans with human checkpoints
- `awos/commands/implement.md` -- Lead implementation agent
- `awos/commands/verify.md` -- Verify implementation against acceptance criteria
- `casdk-harness/src/harness/plugins/context-engineering/commands/create-agent.md` -- Create new agent definitions interactively

### 4. Hook Configuration

Create lifecycle event automation for deterministic control.

**Key Patterns** (from `casdk-harness/src/harness/plugins/context-engineering/skills/hook-configuration/SKILL.md`):

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

**Reference Hooks**:
- `superpowers/hooks/hooks.json` -- SessionStart hook for loading context
- `planning-with-files/.cursor/hooks.json` -- PreToolUse/PostToolUse/Stop hooks for file-based planning
- `tac/Code/tac-6/.claude/hooks/pre_tool_use.py` -- Pre-validation guardrails
- `tac/Code/tac-6/.claude/hooks/post_tool_use.py` -- Post-processing and logging
- `tac/Code/tac-6/.claude/hooks/stop.py` -- Graceful session termination

### 5. Plugin Development

Bundle agents, skills, commands, hooks, and MCP servers into distributable plugins.

**Key Patterns** (from `casdk-harness/src/harness/plugins/context-engineering/skills/plugin-development/SKILL.md`):

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

**Reference Plugins**:
- `casdk-harness/src/harness/plugins/context-engineering/` -- Context engineering plugin (5 skills, 1 agent, 1 command)
- `casdk-harness/src/harness/plugins/research-team/` -- Research team plugin (3 agents, 1 skill, 1 command)

### 6. MCP Server Development

Build Model Context Protocol servers to connect Claude to external services.

**Key Patterns** (from `awesome-claude-skills/mcp-builder/SKILL.md`):

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

**Reference MCP Configs**:
- `casdk-harness/src/harness/config/.mcp.json` -- Playwright and Puppeteer MCP servers
- `tac/Code/tac-6/.mcp.json` -- Playwright MCP for E2E testing
- `proagent-repo GUI/mcp_servers/gdrive/server.py` -- Google Drive MCP server

### 7. Multi-Agent Orchestration

Design and implement multi-agent systems for complex workflows.

**Orchestration Patterns** (from `casdk-harness/src/harness/plugins/context-engineering/patterns/multi-agent-orchestration.md`):

| Pattern | When to Use | Example |
|---------|-------------|---------|
| Sequential Pipeline | Clear phase dependencies | Feature development: PRD -> Backend -> Frontend -> Tests |
| Parallel Fan-Out/Fan-In | Independent analyses | Code review: Security + Performance + Style in parallel |
| Hierarchical Delegation | Complex systems with sub-domains | Microservices: Service A Orchestrator -> Build/Test/Deploy |
| State Machine / Graph | Conditional transitions, error recovery | Deployment with rollback paths |

**Coordination Mechanisms**:
- **Explicit Hand-offs** (recommended): Orchestrator invokes each agent via Task tool
- **Shared Context**: Agents communicate through shared files
- **Message Passing**: Orchestrator maintains message queue

**Subagent-Driven Development** (from `superpowers/skills/subagent-driven-development/SKILL.md`):
- Fresh subagent per task (no context pollution)
- Two-stage review: spec compliance first, then code quality
- Implementer + spec reviewer + code quality reviewer per task
- Controller extracts all tasks upfront, provides full text to each subagent

**Parallel Agent Dispatch** (from `superpowers/skills/dispatching-parallel-agents/SKILL.md`):
- One agent per independent problem domain
- Focused prompts with specific scope, clear goals, constraints, and expected output
- Review and integrate results after all agents return
- Verify fixes do not conflict before running full test suite

**Reference Orchestration Patterns**:
- `root-claude-config/.claude/commands/implement_mul-agent.md` -- Multi-agent implementation orchestrator
- `awos/commands/implement.md` -- Lead implementation agent
- `ralph-orchestrator/.claude/skills/code-assist/SKILL.md` -- Explore-Plan-Code-Commit workflow

### 8. Prompt Engineering and Context Engineering

Design effective prompts and manage context for optimal agent performance.

**Agentic Development Workflow (ADW)** (from `proagent-repo GUI/core/skills/tac/adw.md`):
- Structured workflow for agent-assisted development
- Phases: Explore, Plan, Code, Commit
- Progressive context building

**Trust Ladder** (from `proagent-repo GUI/core/skills/tac/trust-ladder.md`):
- Progressive agent autonomy model
- Levels: Observer -> Assistant -> Collaborator -> Delegator -> Autonomous
- Increase trust as agent demonstrates competence

**Core Four TAC Principles** (from `proagent-repo GUI/core/skills/tac/core-four.md`):
- Task framing, autonomy calibration, context management, review cadence

**Prompt-Driven Development** (from `ralph-orchestrator/.claude/skills/pdd/SKILL.md`):
- Treat prompts as first-class engineering artifacts
- Version control, review, and iterate on prompts
- Evaluate prompt effectiveness with structured criteria

**Session Handoff** (from `gastown/.claude/skills/handoff/SKILL.md`):
- Context preservation between sessions
- State serialization and recovery
- Checkpoint management

### 9. Agent Evaluation

Test and evaluate agent system effectiveness.

**Evaluation Approaches** (from `ralph-orchestrator/.claude/skills/eval/SKILL.md`):
- Conversational evaluation framework
- Task-based assessment with clear success criteria
- Multi-dimensional scoring (accuracy, completeness, efficiency)

**MCP Server Evaluations** (from `awesome-claude-skills/mcp-builder/SKILL.md`):
- Create 10 evaluation questions per MCP server
- Requirements: independent, read-only, complex, realistic, verifiable, stable
- XML output format with `<qa_pair>` elements

**Verification Before Completion** (from `superpowers/skills/verification-before-completion/SKILL.md`):
- Evidence-based verification before declaring success
- Run tests, check outputs, validate against requirements
- Never rely on assumptions about what was done

## Workflow Patterns

### Create a New Agent

1. Define the agent's single responsibility and domain
2. Write a discovery-optimized description with 2-4 concrete examples
3. Select minimal tool set (principle of least privilege)
4. Choose appropriate model (sonnet/opus/haiku)
5. Write focused system prompt with responsibilities, approach, and constraints
6. Place in `.claude/agents/agent-name.md` or plugin `agents/` directory
7. Test discovery with natural language queries

### Create a New Skill

1. Gather concrete usage examples and trigger scenarios
2. Plan reusable resources (scripts, references, assets)
3. Create skill directory with SKILL.md
4. Write YAML frontmatter with name, description (include trigger terms), and allowed-tools
5. Write instructions in imperative form
6. Add supporting files as needed
7. Test autonomous activation with natural language

### Create a New Command

1. Determine the reusable task and argument pattern
2. Create markdown file with optional YAML frontmatter
3. Use `$ARGUMENTS`, `$1`/`$2` for arguments, `@file` for file references, `!command` for bash
4. Declare `allowed-tools` for any bash execution
5. Place in `.claude/commands/` or plugin `commands/` directory
6. Test with various argument combinations

### Create a New Hook

1. Identify the automation goal and lifecycle event
2. Design matcher pattern (tool name, regex, or wildcard)
3. Write shell command with `jq` for stdin JSON processing
4. Test security implications (no credential exposure)
5. Add to `.claude/settings.json` or plugin `hooks/hooks.json`
6. Verify event triggers and blocking behavior

### Build a Plugin

1. Create directory structure with `.claude-plugin/plugin.json`
2. Add agents, skills, commands, hooks as needed
3. Configure MCP servers in `.mcp.json`
4. Write CLAUDE.md for context and README.md for documentation
5. Test locally with `/plugin install /path/to/plugin`
6. Verify all components load and no naming conflicts
7. Version with semver and distribute via marketplace or Git

### Build an MCP Server

1. Study target API documentation exhaustively
2. Read MCP protocol spec from `https://modelcontextprotocol.io/llms-full.txt`
3. Design workflow-oriented tools (not raw API wrappers)
4. Implement with FastMCP (Python) or MCP TypeScript SDK
5. Add input validation (Pydantic/Zod), error handling, response formatting
6. Add tool annotations (readOnlyHint, destructiveHint, etc.)
7. Create 10 evaluation questions
8. Test with evaluation harness

### Orchestrate Multi-Agent Workflow

1. Decompose task into independent sub-tasks
2. Select orchestration pattern (sequential, parallel, hierarchical, state machine)
3. Define agent responsibilities and hand-offs explicitly
4. Provide complete context to each agent (do not require agents to discover context)
5. Implement error handling and recovery paths
6. Track progress with logging and checkpoints
7. Budget token usage across agents

## Quality Standards

### Agent Quality Checklist

- [ ] Single, focused responsibility
- [ ] Discovery-optimized description with 2+ concrete examples
- [ ] Appropriate tool restrictions (least privilege)
- [ ] Clear system prompt with responsibilities, approach, and constraints
- [ ] Model selection matches task complexity
- [ ] Tested with natural language queries for discovery

### Skill Quality Checklist

- [ ] YAML frontmatter with name and description
- [ ] Trigger terms included in description
- [ ] Scope boundaries defined (what NOT to use for)
- [ ] Imperative writing style throughout
- [ ] Supporting files organized properly (scripts/, references/, assets/)
- [ ] Progressive disclosure implemented (metadata -> instructions -> details)

### Command Quality Checklist

- [ ] Clear argument pattern with defaults
- [ ] argument-hint in frontmatter
- [ ] Bash commands declared in allowed-tools
- [ ] Tested with edge cases (missing args, extra args)

### Hook Quality Checklist

- [ ] Correct lifecycle event selected
- [ ] Matcher pattern scoped appropriately
- [ ] Shell command tested independently
- [ ] No credential exposure in commands or logs
- [ ] Timeout configured
- [ ] Exit codes handled correctly (0 = success, 2 = block)

### Plugin Quality Checklist

- [ ] .claude-plugin/plugin.json present with valid semver
- [ ] All components follow individual quality checklists
- [ ] No naming conflicts with standard components
- [ ] README.md with installation and usage instructions
- [ ] CLAUDE.md with context for Claude sessions
- [ ] Tested with local installation

### MCP Server Quality Checklist

- [ ] Workflow-oriented tools (not raw API wrappers)
- [ ] Input validation with Pydantic/Zod
- [ ] Actionable error messages
- [ ] Response format options (concise/detailed)
- [ ] Tool annotations set correctly
- [ ] 10 evaluation questions created
- [ ] Character limits and truncation handled

## Decision Matrix

| Need | Component |
|------|-----------|
| Autonomous capability triggered by context | **Skill** |
| User-invoked reusable prompt with arguments | **Command** |
| Specialized AI assistant for a domain | **Agent** |
| Deterministic automation at lifecycle events | **Hook** |
| Bundle of related components | **Plugin** |
| External service integration | **MCP Server** |
| Complex multi-step task decomposition | **Multi-Agent Orchestration** |
