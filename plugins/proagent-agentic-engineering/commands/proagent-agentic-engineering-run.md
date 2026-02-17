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

Reference: `casdk-harness/src/harness/plugins/context-engineering/skills/agent-definition-creation/SKILL.md`

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

Reference: `awesome-claude-skills/skill-creator/SKILL.md`, `casdk-harness/src/harness/plugins/context-engineering/skills/skill-creation/SKILL.md`

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

Reference: `casdk-harness/src/harness/plugins/context-engineering/skills/command-creation/SKILL.md`

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

Reference: `casdk-harness/src/harness/plugins/context-engineering/skills/hook-configuration/SKILL.md`

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

Reference: `awesome-claude-skills/mcp-builder/SKILL.md`

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

Reference: `casdk-harness/src/harness/plugins/context-engineering/skills/plugin-development/SKILL.md`

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

Reference: `casdk-harness/src/harness/plugins/context-engineering/patterns/multi-agent-orchestration.md`, `superpowers/skills/subagent-driven-development/SKILL.md`

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

Reference: `ralph-orchestrator/.claude/skills/eval/SKILL.md`, `superpowers/skills/verification-before-completion/SKILL.md`

---

If no workflow is specified, display this menu and ask which workflow to execute.
