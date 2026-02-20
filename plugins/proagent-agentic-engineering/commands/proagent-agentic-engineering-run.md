---
description: Execute agentic engineering workflows -- create agents, skills, commands, hooks, MCP servers, plugins, orchestrate multi-agent systems, and evaluate agents
argument-hint: <workflow> [options]
---

# ProAgent Agentic Engineering -- Task Runner

Execute the requested agentic engineering workflow based on $ARGUMENTS.

## Available Workflows

### create-agent
Create a new Claude Code sub-agent definition.

**Process**:
1. Ask for the agent's domain, specific capabilities, and usage scenarios
2. Determine tool requirements (Read-only? Edit? Bash? MCP tools?)
3. Select model (sonnet for balanced, opus for complex reasoning, haiku for simple tasks)
4. Generate agent definition with:
   - Lowercase hyphenated `name` in YAML frontmatter
   - Discovery-optimized `description` with 2-4 `<example>` blocks and `<commentary>`
   - Focused system prompt with Core Responsibilities, Approach, and Constraints sections
   - Appropriate `tools` restriction (principle of least privilege)
5. Save to `.claude/agents/agent-name.md` or plugin `agents/` directory
6. Test discovery with natural language queries


### create-skill
Create a new Claude Code skill (model-invoked autonomous capability).

**Process**:
1. Gather concrete usage examples and trigger scenarios
2. Identify reusable resources (scripts, references, assets)
3. Create skill directory with SKILL.md
4. Write YAML frontmatter:
   - `name` in lowercase-hyphenated format
   - `description` with trigger terms, activation scenarios, scope boundaries
   - Optional `allowed-tools` for restricted access
5. Write instructions in imperative/infinitive form
6. Add supporting files (scripts/, references/, assets/, examples/)
7. Test autonomous activation with natural language


### create-command
Create a new Claude Code slash command.

**Process**:
1. Determine the reusable task and expected arguments
2. Create markdown file with YAML frontmatter:
   - `description`: concise 1-sentence summary
   - `argument-hint`: `<required>` and `[optional]` args
   - `allowed-tools`: if using Bash execution
   - `model`: if overriding default
3. Write prompt template using:
   - `$ARGUMENTS` for all args, `$1`/`$2` for positional
   - `${1:-default}` for default values
   - `@file` for file content inclusion
   - `!command` for bash execution (requires allowed-tools)
4. Save to `.claude/commands/` or plugin `commands/` directory
5. Test with various argument combinations


### create-hook
Create a Claude Code lifecycle hook for deterministic automation.

**Process**:
1. Identify the automation goal (formatting, logging, blocking, notifications)
2. Select lifecycle event:
   - PreToolUse (can block with exit 2)
   - PostToolUse (format code, run linters)
   - SessionStart (load context)
   - Stop (run tests, update docs)
   - Notification (custom alerts)
3. Design matcher pattern (exact tool name, regex with `|`, or `*` for all)
4. Write shell command using `jq` to extract stdin JSON fields
5. Test security (no credential exposure, safe logging)
6. Add to `.claude/settings.json` hooks section or plugin `hooks/hooks.json`


### create-mcp
Create a new MCP (Model Context Protocol) server.

**Process**:
1. Study target API documentation exhaustively
2. Fetch MCP protocol spec: `https://modelcontextprotocol.io/llms-full.txt`
3. Load SDK docs (Python: FastMCP, TypeScript: MCP SDK)
4. Design workflow-oriented tools (not raw API wrappers):
   - Consolidate related operations
   - Optimize for limited context windows
   - Design actionable error messages
5. Implement:
   - Core infrastructure (request helpers, error handling, pagination)
   - Input validation (Pydantic for Python, Zod for TypeScript)
   - Response formatting (JSON and Markdown options)
   - Tool annotations (readOnlyHint, destructiveHint, etc.)
6. Test with evaluation harness
7. Create 10 evaluation questions (independent, read-only, complex, verifiable)


### create-plugin
Create a complete Claude Code plugin bundling multiple components.

**Process**:
1. Define plugin theme, domain, and included components
2. Create directory structure:
   ```
   plugin-name/
   ├── .claude-plugin/plugin.json
   ├── agents/
   ├── skills/skill-name/SKILL.md
   ├── commands/
   ├── hooks/hooks.json
   ├── .mcp.json
   ├── CLAUDE.md
   └── README.md
   ```
3. Generate plugin.json with name, version (semver), description, author, keywords
4. Create each component following its respective workflow
5. Write CLAUDE.md with context for Claude sessions
6. Write README.md with installation and usage instructions
7. Test locally with `/plugin install /path/to/plugin`


### orchestrate
Design and implement a multi-agent orchestration workflow.

**Process**:
1. Decompose the task into sub-tasks
2. Identify dependencies between sub-tasks
3. Select orchestration pattern:
   - **Sequential Pipeline**: clear phase dependencies (A -> B -> C)
   - **Parallel Fan-Out/Fan-In**: independent analyses in parallel
   - **Hierarchical Delegation**: complex systems with sub-orchestrators
   - **State Machine**: conditional transitions with error recovery
4. Define agent responsibilities and hand-offs explicitly
5. Provide complete context to each agent
6. Implement error handling and recovery paths
7. Track progress with logging and checkpoints
8. Budget token usage across agents


### evaluate
Evaluate an agent system's effectiveness.

**Process**:
1. Define evaluation dimensions:
   - Accuracy: Does the agent produce correct results?
   - Completeness: Does it cover all required scenarios?
   - Efficiency: Token usage, response time, tool call count
   - Discovery: Does it activate/invoke appropriately?
   - Safety: Are tool restrictions effective?
2. Create test scenarios matching real usage patterns
3. Run agent against test scenarios
4. Measure results against success criteria
5. Generate evaluation report with scores and recommendations
6. Iterate on agent design based on findings


### bootstrap-loop
Bootstrap an autonomous coding loop using one of the ecosystem frameworks.

**Process**:
1. Assess project requirements: language, complexity, backend preference
2. Recommend framework:
   - **ralph-orchestrator** for Rust projects or multi-backend LLM needs (Claude, Kiro, Gemini, Codex)
   - **casdk-harness** for Python projects with Claude SDK and plugin lifecycle needs
   - **Auto-Claude** for projects needing persistent knowledge graph context (Graphiti)
   - **gastown** for Go projects or molecule-based workflow composition
3. Configure orchestration preset or autonomous mode settings
4. Set up tool registry with required capabilities
5. Define exit conditions (test pass, build success, coverage threshold)
6. Configure ZTE trust level (Observer through Autonomous) from `proagent-repo core/zte/trust_ladder.py`
7. Add confirmation gates at critical decision points
8. Set up context persistence (session files, knowledge graph, or checkpoint files)
9. Test loop execution with a small, scoped task


### spec-driven
Run a spec-driven development workflow from architecture to verified implementation.

**Process**:
1. Generate architecture documentation (following AWOS `/architecture` pattern)
2. Produce functional specification with acceptance criteria (following AWOS `/spec` pattern)
3. Present spec for user approval (confirmation gate)
4. Route through implementation stages (following ProAgent SDLC 5-stage pipeline)
5. Implement features from approved specs (following AWOS `/implement` pattern)
6. Verify implementation against spec acceptance criteria (following AWOS `/verify` pattern)
7. Generate verification report with pass/fail status per acceptance criterion


### context-plan
Create a structured planning session using the 3-file planning pattern.

**Process**:
1. Create plan file with task decomposition and dependencies
2. Create progress tracker for status monitoring
3. Create output log for artifact tracking
4. Set up hooks for automatic progress tracking via file existence detection
5. Execute plan phases with confirmation gates between major stages
6. Update progress tracker as tasks complete


---

If no workflow is specified, display this menu and ask which workflow to execute.
