## Composition Patterns

Patterns for wiring artifacts together into larger workflows. Select based on the workflow's orchestration needs.

### Pattern 1: Linear Pipeline
```
Input -> Step A -> Step B -> Step C -> Report
```
Single command, sequential steps. Use for: builds, plans, focused tasks.
**Report type:** Summary or Diff.

### Pattern 2: Parallel Fan-Out / Fan-In
```
Input -> Spawn N agents (Task tool) -> Collect -> Merge -> Report
```
Use for: multi-source research, codebase scanning, documentation scraping.
**Report type:** Comparison (merge step), then Summary (final).

### Pattern 3: Chained Slash Commands
```
/command-a -> output_a -> /command-b output_a -> output_b -> /command-c output_b
```
Use for: multi-phase pipelines (scout -> plan -> build).
**Report types:** Handoff or Path-Only (intermediate steps), Diff or Summary (final step).
**Requires:** Inter-Artifact Contracts between each pair.

### Pattern 4: Fire-and-Forget Background
```
Launch headless agent -> Write progress to file -> Rename on complete/fail
```
Use for: long-running autonomous tasks, parallel workstreams.
**Report type:** Progress.

### Pattern 5: Self-Improving Expert Loop
```
Plan -> Build -> Improve (analyze git diff -> update expertise sections)
```
Use for: domain expert systems that accumulate knowledge over time.
**Report types:** Path-Only (plan), Diff (build), Summary (improve).
**Requires:** Expert System artifact template.

### Pattern 6: Agent Team Orchestration
```
Lead decomposes task -> Assigns to teammates -> Teammates self-coordinate -> Lead synthesizes
```
Use for: complex multi-file features, competing approaches, review panels.
**Report type:** Summary (lead's synthesis).

### Pattern 7: Skill + Agent Composition
```
Skill defines the capability -> Custom agent executes it -> Hook validates output
```
Use for: reusable, safe, domain-specific automation.
**Report type:** Varies by skill purpose.

---

## Creation Workflows

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
