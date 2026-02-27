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

---

## Workflow Coherence Checklist

Use after generating multi-artifact workflows to validate consistency:

- [ ] All cross-references resolve (file paths, variable names, slash command names)
- [ ] Tool permissions cover what each workflow step needs (no more, no less)
- [ ] Model selections match the reasoning in Design Decisions
- [ ] Report types match the Report Type Selection Guide
- [ ] Contracts are consistent: producer output format = consumer input format
- [ ] Error handling covers: missing input, empty output, malformed data, timeouts
- [ ] Hooks don't conflict with existing `.claude/settings.json` entries
- [ ] Naming follows codebase conventions (kebab-case files, UPPER_SNAKE variables)

## Expert System Checklist

Use when creating or reviewing Expert System trios (Plan/Build/Improve):

- [ ] All three commands present (_plan, _build, _improve)
- [ ] All three share identical `## Expertise` sections
- [ ] Only `_improve` modifies Expertise sections; `_plan` and `_build` consume them
- [ ] `_plan` outputs spec to `specs/experts/<domain>/`
- [ ] `_build` reads spec path from `$ARGUMENTS` and implements from it
- [ ] `_improve` reads `git diff` and updates Expertise in both _plan and _build
- [ ] `## Workflow` sections are never modified by _improve
- [ ] Report types: _plan uses Path-Only, _build uses Diff, _improve uses Summary
