---
name: Building Agentic Systems
description: >
  Comprehensive skill for designing, building, orchestrating, and optimizing AI agent systems
  with Claude Code. Covers agent design patterns, multi-agent orchestration, skill/command/hook
  creation, MCP server development, prompt engineering, plugin architecture, agent evaluation,
  context engineering, autonomous coding loops, multi-backend orchestration, trust/autonomy
  frameworks, spec-driven development, and thinking model commands.

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
  - Autonomous coding loops (ralph, casdk-harness, Auto-Claude, gastown)
  - Multi-backend adapters (Claude, Kiro, Gemini, Codex)
  - Spec-driven development (AWOS spec/implement/verify, ProAgent SDLC pipeline)
  - Tool registry, plugin lifecycle, knowledge graph integration
  - Thinking models, first-principles reasoning, mental model commands
  - 3-file planning pattern, context handoff, session persistence

  Do NOT use for:
  - General software development without an agentic component (use sdlc or backend/frontend skills)
  - DevOps infrastructure without agent involvement (use devops skills)
  - Pure testing without agent evaluation (use qa skills)
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebFetch, WebSearch
---

# Building Agentic Systems

## Overview

This skill provides comprehensive guidance for building, orchestrating, and optimizing AI agent systems using Claude Code, covering the full lifecycle of agentic engineering: from designing individual agents to orchestrating complex multi-agent workflows.

## Core Domains

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

### Autonomous Coding Loop Frameworks

Four production-grade autonomous loop implementations exist in the ecosystem:

**ralph-orchestrator** (Rust):
- Core event loop engine (`crates/ralph-core/src/event_loop/mod.rs`) drives the explore-plan-code-commit cycle
- AI agent iteration loop runner (`crates/ralph-cli/src/loop_runner.rs`) manages multi-turn autonomous sessions
- Configurable orchestration presets (`presets/feature.yml`) define phase sequences, exit conditions, and tool permissions
- Multi-backend adapters supporting Claude, Kiro, Gemini, and Codex as interchangeable LLM backends

**casdk-harness** (Python):
- `AgentSession` (`src/harness/agent.py`) provides Claude SDK integration with MCP support and lifecycle management
- Autonomous mode orchestration (`src/harness/autonomous.py`) for self-directed task completion
- Plugin lifecycle management (`src/harness/plugin_manager.py`) with discovery, namespacing, and hot-reload
- Bundled plugins: context-engineering (context-engineer agent), research-team (lead-research-coordinator agent)

**Auto-Claude** (Python):
- Autonomous multi-agent coding framework with main agent pipeline (`apps/backend/agent.py`)
- Tool registry (`apps/backend/agents/tools_pkg/registry.py`) for dynamic agent capability management
- Graphiti knowledge graph integration (`apps/backend/context/graphiti_integration.py`) for persistent context across sessions

**gastown** (Go):
- Multi-agent orchestration CLI (`cmd/gt/main.go`) with molecule-based workflow composition
- Workflow molecules (`internal/beads/molecule.go`) as composable units of agent coordination
- Design workflow formulas (`.beads/formulas/design.formula.toml`) for declarative orchestration

### Context Engineering Patterns

**3-File Planning Pattern** (planning-with-files):
- `/plan` command (`commands/plan.md`) initiates structured planning sessions
- Planning skill (`skills/planning-with-files/SKILL.md`) uses three files: plan, progress tracker, and output log
- Hook-driven plan execution tracks progress automatically through file existence detection

**Context Priming** (awesome-claude-code):
- Context priming slash command (`resources/slash-commands/context-prime/context-prime.md`) loads relevant context at session start

**Context Engineering Plugin** (casdk-harness):
- Dedicated context-engineer agent (`src/harness/plugins/context-engineering/agents/context-engineer.md`) for managing context windows
- Research team coordinator (`src/harness/plugins/research-team/agents/lead-research-coordinator.md`) for multi-agent research workflows

**Context Handoff** (taches-cc-resources):
- Setup-ralph skill (`skills/setup-ralph/SKILL.md`) for bootstrapping autonomous loop context
- First-principles thinking model (`commands/consider/first-principles.md`) for structured reasoning before implementation

### Spec-Driven Development Workflows

**AWOS** (spec-to-implementation pipeline):
- `/architecture` command (`claude/commands/architecture.md`) generates system architecture documentation
- `/spec` command (`claude/commands/spec.md`) produces functional specifications from requirements
- `/implement` command (`claude/commands/implement.md`) builds features from specs
- `/verify` command (`claude/commands/verify.md`) validates implementation against spec acceptance criteria

**ProAgent SDLC Pipeline** (proagent-repo):
- CLI entry point (`cli.py`) with TAC, SDLC, and ZTE command groups
- 5-stage pipeline orchestrator (`core/orchestration/sdlc/pipeline.py`): Requirements, Design, Implementation, Testing, Deployment
- ZTE trust ladder (`core/zte/trust_ladder.py`): 5 levels of progressive autonomy (Observer, Assistant, Collaborator, Delegator, Autonomous)

### Extended Skill Library

Skills discovered across external repositories:

| Skill | Source Repo | Description |
|-------|-------------|-------------|
| subagent-driven-development | superpowers | Fresh subagent per task with two-stage review |
| dispatching-parallel-agents | superpowers | One agent per independent domain, verify no conflicts |
| systematic-debugging | superpowers | Root cause tracing with hypothesis-driven investigation |
| artifacts-builder | awesome-claude-skills | Interactive artifacts builder for rich outputs |
| connect-apps | awesome-claude-skills | 500+ app integration via Composio SDK |
| mcp-builder | awesome-claude-skills | MCP server scaffolding and development |
| skill-creator | awesome-claude-skills | Meta-skill for creating new Claude skills |
| create-agent-skills | taches-cc-resources | Skill for creating new agent skills from descriptions |
| create-mcp-servers | taches-cc-resources | MCP server builder with best practices |
| setup-ralph | taches-cc-resources | Bootstrap ralph autonomous loop configuration |
| context-driven-development | agents (conductor) | Context-driven development patterns |
| workflow-patterns | agents (conductor) | Workflow orchestration pattern library |
| prompt-engineering-patterns | agents (llm-application-dev) | LLM prompt optimization techniques |
| langchain-architecture | agents (llm-application-dev) | LangChain architecture patterns for agent systems |
| planning-with-files | planning-with-files | 3-file planning pattern with hook-driven tracking |

### 7. Multi-Agent Orchestration

Design and implement multi-agent systems for complex workflows.

**Orchestration Patterns**:

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

**Subagent-Driven Development**:
- Fresh subagent per task (no context pollution)
- Two-stage review: spec compliance first, then code quality
- Implementer + spec reviewer + code quality reviewer per task
- Controller extracts all tasks upfront, provides full text to each subagent

**Parallel Agent Dispatch**:
- One agent per independent problem domain
- Focused prompts with specific scope, clear goals, constraints, and expected output
- Review and integrate results after all agents return
- Verify fixes do not conflict before running full test suite

**Orchestration Examples**:
- Multi-agent implementation orchestrator
- Lead implementation agent
- Explore-Plan-Code-Commit workflow

## Agent Teams Orchestration

Production-ready patterns for multi-agent coordination using Claude Code's native Task tool:

### Multi-Reviewer Code Review
Assign each reviewer a specific quality dimension (security, performance, architecture, testing, accessibility) and run them in parallel. Deduplicate findings using merge rules:
- Same file:line, same issue → merge, credit all reviewers
- Conflicting severity → use higher rating
- Conflicting recommendations → include both with attribution

### Hypothesis-Driven Debugging
Use the Analysis of Competing Hypotheses (ACH) methodology across failure mode categories: Logic Error, Data Issue, State Problem, Integration Failure, Resource Issue, Environment. Each investigator gathers evidence classified as Direct (strong), Correlational (medium), Testimonial (weak), or Absence (variable). Arbitrate by confidence level, then evidence count, then causal chain strength.

### Parallel Feature Development
The cardinal rule: **one owner per file**. When files must be shared, designate a single owner — other implementers request changes via messages. Use interface contract files (read-only) to define boundaries between implementers.

### Agent Roles
- **team-lead**: Orchestrator that decomposes work and synthesizes results
- **team-reviewer**: Multi-dimensional code reviewer (assigned a specific dimension)
- **team-debugger**: Hypothesis investigator that gathers evidence
- **team-implementer**: Parallel builder respecting file ownership boundaries

### Marketplace Orchestration Commands

Commands from the agents marketplace for multi-agent coordination:
- **multi-agent-optimize** (`plugins/agent-orchestration/commands/multi-agent-optimize.md`): Optimize multi-agent workflow performance
- **team-spawn** (`plugins/agent-teams/commands/team-spawn.md`): Spawn agent teams for parallel work
- **team-delegate** (`plugins/agent-teams/commands/team-delegate.md`): Delegate tasks across agent teams
- **prompt-optimize** (`plugins/llm-application-dev/commands/prompt-optimize.md`): Optimize LLM prompts for agent systems
- **context-manager agent** (`plugins/agent-orchestration/agents/context-manager.md`): Manage context across multi-agent orchestration
- **conductor-validator** (`plugins/conductor/agents/conductor-validator.md`): Validate conductor workflow definitions

### 8. Prompt Engineering and Context Engineering

Design effective prompts and manage context for optimal agent performance.

**Agentic Development Workflow (ADW)**:
- Structured workflow for agent-assisted development
- Phases: Explore, Plan, Code, Commit
- Progressive context building

**Trust Ladder** (ProAgent ZTE -- `proagent-repo core/zte/trust_ladder.py`):
- Progressive agent autonomy model with 5 levels
- Levels: Observer -> Assistant -> Collaborator -> Delegator -> Autonomous
- Increase trust as agent demonstrates competence
- Each level unlocks additional tool permissions and reduces confirmation gates
- Gastown escalation system provides complementary trust management for multi-agent teams

**Core Four TAC Principles**:
- Task framing, autonomy calibration, context management, review cadence

**Prompt-Driven Development**:
- Treat prompts as first-class engineering artifacts
- Version control, review, and iterate on prompts
- Evaluate prompt effectiveness with structured criteria

**Session Handoff**:
- Context preservation between sessions
- State serialization and recovery
- Checkpoint management
- Setup-ralph skill (`taches-cc-resources skills/setup-ralph/SKILL.md`) for bootstrapping loop context

**Thinking Model Commands** (taches-cc-resources):
- First-principles reasoning (`commands/consider/first-principles.md`) for structured decomposition before implementation
- Apply mental models to agent design decisions, architecture tradeoffs, and debugging strategies
- Use structured thinking before committing to orchestration patterns or agent architectures

### 9. Agent Evaluation

Test and evaluate agent system effectiveness.

**Evaluation Approaches**:
- Conversational evaluation framework
- Task-based assessment with clear success criteria
- Multi-dimensional scoring (accuracy, completeness, efficiency)

**MCP Server Evaluations**:
- Create 10 evaluation questions per MCP server
- Requirements: independent, read-only, complex, realistic, verifiable, stable
- XML output format with `<qa_pair>` elements

**Verification Before Completion**:
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

### Bootstrap an Autonomous Coding Loop

1. Choose framework: ralph-orchestrator (Rust, multi-backend), casdk-harness (Python, Claude SDK native), Auto-Claude (Python, knowledge graph), or gastown (Go, molecule workflows)
2. Configure orchestration preset (ralph `presets/feature.yml`) or autonomous mode (casdk `autonomous.py`)
3. Set up tool registry with required capabilities and permissions
4. Define exit conditions (test pass, build success, coverage threshold)
5. Configure trust level (ZTE trust ladder) to control autonomous scope
6. Set up context persistence (Graphiti knowledge graph for Auto-Claude, session files for casdk)
7. Add confirmation gates at critical decision points (spec approval, deployment)
8. Monitor loop execution with logging and checkpoint files

### Run Spec-Driven Development

1. Generate architecture documentation (`/architecture` command pattern from AWOS)
2. Produce functional specification with acceptance criteria (`/spec` command pattern)
3. Route through SDLC pipeline stages (ProAgent `core/orchestration/sdlc/pipeline.py`)
4. Implement features from specs (`/implement` command pattern)
5. Verify implementation against spec acceptance criteria (`/verify` command pattern)
6. Use confirmation gates between stages (AWOS `AWOS_SPEC_REFINEMENT` pattern)

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

## AWOS Plugin Architecture Reference

The AWOS workflow plugin demonstrates production-ready multi-agent plugin design:

### Key Patterns
- **Shared `lib/` module**: Common utilities (`session.py`, `step_detector.py`) consolidated into a reusable library used by all 8 agents
- **Session persistence**: JSON-based state file (`awos_session.json`) with atomic writes (write to temp, then rename) for crash-safe resume
- **File-based step detection**: Determine workflow progress by checking output file existence rather than relying on chat history
- **Configurable confirmation gates**: `AWOS_SPEC_REFINEMENT=1,4,6` controls which steps require user approval vs. auto-advance

### Session State Structure
```json
{
  "started_at": "ISO-8601",
  "spec_hash": "sha256_prefix",
  "current_step": 4,
  "completed_steps": [1, 2, 3],
  "interactive_confirmations": {"step_1": "approved"},
  "step_outputs": {"step_1": "context/product/product.md"},
  "status": "in_progress"
}
```

## Mandatory Confirmation Pattern

For multi-step autonomous workflows, implement mandatory user confirmation gates to prevent autonomous runaway:

### Pattern
After each significant step in an autonomous workflow:
1. **Execute** the step
2. **Present** the output to the user
3. **STOP** and ask for explicit approval
4. **Process** the response before continuing

### Confirmation Options
- **[A]pprove** — Accept output, proceed to next step
- **[E]dit** — User modifies the output, then signals readiness
- **[R]edo** — User provides feedback, agent regenerates the step

### Configuration
Make confirmation gates configurable per step (e.g., `REFINEMENT_STEPS=1,4,6`) so teams can choose which steps need human review vs. auto-advance. Critical specification steps (product vision, functional spec, task decomposition) should always require confirmation.

This pattern is essential for any workflow that produces artifacts requiring stakeholder alignment.

## Composio SDK Integration

The Composio SDK provides two production-ready patterns for building AI agents that connect to 200+ external services:

### Tool Router Pattern (for AI Agents)
- **Session-based isolation** per user with unique MCP URLs
- **Dynamic toolkit configuration** per session
- **Automatic OAuth authentication** with `manageConnections: true`
- Framework integration with Vercel AI, LangChain, and OpenAI Agents

### Direct Execution Pattern (for Traditional Apps)
- Manual tool execution with `composio.tools.execute()`
- CRUD operations on connected accounts and auth configs
- Custom tool creation with authentication
- Version pinning via `toolkitVersions`

### Configuration
Add the Rube MCP server for Composio tool access:
```json
"rube": {
  "url": "https://rube.app/mcp"
}
```

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

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate interactive diagrams directly in the conversation. Describe what you need in natural language and Excalidraw renders it as an interactive canvas with hand-drawn style.

### When to Use

- Agent orchestration flows and multi-agent topology diagrams
- MCP server architecture and plugin component relationships
- Prompt chain and workflow visualizations
- Fan-out/fan-in patterns and parallel agent coordination

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
