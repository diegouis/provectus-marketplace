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

---

## Additional Composition Patterns

These patterns from the Workflow Factory complement the orchestration patterns above. They focus on wiring artifacts together with explicit data passing.

### Chained Slash Commands
```
/command-a -> output_a -> /command-b output_a -> output_b -> /command-c output_b
```
Use for: multi-phase pipelines (scout -> plan -> build).
**Report types:** Handoff or Path-Only (intermediate steps), Diff or Summary (final step).
**Requires:** Inter-Artifact Contracts between each pair. See `references/contracts.md`.

### Fire-and-Forget Background
```
Launch headless agent -> Write progress to file -> Rename on complete/fail
```
Use for: long-running autonomous tasks, parallel workstreams.
**Report type:** Progress.

### Self-Improving Expert Loop
```
Plan -> Build -> Improve (analyze git diff -> update expertise sections)
```
Use for: domain expert systems that accumulate knowledge over time.
**Report types:** Path-Only (plan), Diff (build), Summary (improve).
**Requires:** Expert System artifact template. See `references/artifacts.md` Section E.

### Skill + Agent Composition
```
Skill defines the capability -> Custom agent executes it -> Hook validates output
```
Use for: reusable, safe, domain-specific automation.
**Report type:** Varies by skill purpose.

### Inter-Artifact Contracts for Multi-Artifact Orchestration

When any orchestration pattern chains multiple artifacts, each connection MUST have an explicit contract defining:
- Exact output format from the producer
- Exact input variable in the consumer
- Behavior for empty, malformed, and failed outputs

See `references/contracts.md` for the full contract template and examples.
