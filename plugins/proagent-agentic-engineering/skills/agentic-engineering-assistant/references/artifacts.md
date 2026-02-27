# Artifact Reference

Knowledge base for all Claude Code workflow artifact types. Each type includes its purpose, frontmatter schema, and key characteristics. Canonical body templates are in `../templates/`.

---

## A. Slash Commands (`.claude/commands/<name>.md`)

The original workflow primitive. A markdown file with YAML frontmatter that becomes a `/command-name` the user can invoke.

**When to use:** Task-specific instructions, step-by-step workflows, orchestrating other commands.
**When NOT to use:** When the artifact needs to be portable across Claude.ai/Code/API (use Skill). When the artifact needs to auto-trigger without user invocation (use Agent). When the artifact needs to intercept lifecycle events (use Hook).

**Full frontmatter fields:**

```yaml
---
name: command-name                    # Becomes the /command-name invocation
description: What this command does   # Shown in / menu and used for auto-matching
argument-hint: [arg1] [arg2]          # Autocomplete guidance
allowed-tools: Read, Write, Bash      # Comma-separated tool allowlist (temporary, expires on completion)
model: sonnet                         # Model override: opus | sonnet | haiku | full-model-id
---
```

**Variable patterns:**
- `$ARGUMENTS` -- entire input string
- `$1`, `$2`, `$3` -- positional arguments (index-based)
- Static variables defined inline with defaults

**Body template:** See `../templates/command-body.md`

---

## B. Skills (`.claude/skills/<skill-name>/SKILL.md`)

The evolved, portable successor to slash commands. A folder containing a `SKILL.md` plus optional support files (scripts, references, templates).

**When to use:** Reusable capabilities, auto-loadable domain expertise, portable packages that work across Claude.ai/Code/API. When Claude should auto-detect and invoke without user typing a command.
**When NOT to use:** One-off task workflows (use Command). When you need lifecycle interception (use Hook).

**Full frontmatter fields:**

```yaml
---
name: skill-name                      # Slash command identifier (lowercase, hyphens, max 64 chars)
description: When to auto-load        # Claude uses this to decide when to invoke automatically
argument-hint: [filename]             # Shown in autocomplete menu
allowed-tools: Read, Grep, Bash       # Temporary tool permissions during execution
model: sonnet                         # Model override
context: fork                         # Run in isolated subagent with separate context window
agent: Explore                        # Subagent type when context=fork: Explore | Plan | general-purpose
disable-model-invocation: false       # true = only user can invoke (prevents Claude auto-triggering)
user-invocable: true                  # false = hidden from / menu; Claude can still auto-load
hooks:                                # Skill-scoped lifecycle hooks
  PreToolUse:
    - matcher: Bash
      command: ".claude/hooks/validate.sh"
  Stop:
    - command: ".claude/hooks/cleanup.sh"
      once: true                      # Execute only once per session
mode: null                            # Categorizes as a "mode command" for behavioral modification
license: MIT                          # Metadata
version: 1.0.0                        # Metadata
---
```

**Invocation control matrix:**

| disable-model-invocation | user-invocable | Who can invoke |
|---|---|---|
| false (default) | true (default) | Both user and Claude |
| true | true | User only |
| false | false | Claude only (background knowledge) |
| true | false | Neither (disabled) |

**Folder structure:**
```
.claude/skills/skill-name/
  SKILL.md           # Required -- main definition
  PATTERNS.md        # Optional -- reference patterns and examples
  scripts/           # Optional -- executable helper scripts
  references/        # Optional -- detailed domain docs
  assets/            # Optional -- templates, binaries
```

**String substitution:** `${CLAUDE_SESSION_ID}` available in skill content (v2.1.9+).

**Body template:** See `../templates/skill-body.md`

---

## C. Custom Agents (`.claude/agents/<agent-name>.md`)

Specialized subagent definitions. Claude auto-delegates work when the task matches the agent's `description`. Agents run in isolated context windows and return distilled results.

**When to use:** Domain experts (security reviewer, test writer, doc generator), specialized roles in multi-agent workflows, when work should be auto-delegated based on task description.
**When NOT to use:** Simple sequential tasks (use Command). When portability matters (use Skill).

**Full frontmatter fields:**

```yaml
---
name: agent-name                      # Unique identifier (lowercase, hyphens)
description: Expert at X. Use PROACTIVELY when Y happens.  # Triggers auto-delegation
tools: Read, Grep, Glob, Bash         # CSV tool allowlist (inherits all if omitted)
disallowedTools: Write, Edit           # Explicit denylist
model: opus                           # opus | sonnet | haiku
color: orange                         # Visual indicator: red|blue|green|yellow|purple|orange|pink|cyan
permissionMode: plan                  # plan = read-only analysis mode
maxTurns: 20                          # Max agentic turns before stopping
mcpServers: []                        # MCP server access
hooks: {}                             # Agent-scoped hooks
skills: []                            # Skills to inject at startup
memory: project                       # Persistent memory scope: user | project | local
---
```

**Key characteristics:**
- Isolated context window -- keeps main thread clean
- Auto-delegated when description matches task
- Up to 10 subagents can run in parallel
- Can be sent to background with `Ctrl+B`
- `permissionMode: plan` makes them read-only analysts

**Built-in agent types for Task tool:**

| Type | Model | Access | Purpose |
|---|---|---|---|
| `Explore` | Haiku | Read-only | Fast codebase scanning |
| `general-purpose` | Sonnet | Full | Research and modification |
| `Plan` | Sonnet/Opus | Read-only | Planning and analysis |

**Body template:** See `../templates/agent-body.md`

---

## D. Hooks (`.claude/hooks/<hook-name>.py` + `settings.json`)

Event-driven scripts that intercept Claude's lifecycle. Two flavors: file-based (settings.json) for global hooks, and inline (SDK) for programmatic hooks.

**When to use:** Validation gates, auto-formatting, logging, security enforcement, context injection, quality gates.
**When NOT to use:** Workflow orchestration (use Command/Skill). Domain expertise (use Agent).

**All 13 hook events:**

| Event | Trigger | Supports matcher |
|---|---|---|
| `Setup` | Before session initialization | No |
| `SessionStart` | Session begins | No |
| `SessionEnd` | Session ends | No |
| `UserPromptSubmit` | User submits prompt | No |
| `PreToolUse` | Before tool executes | Yes |
| `PermissionRequest` | Permission dialog needed | Yes |
| `PostToolUse` | After tool succeeds | Yes |
| `PostToolUseFailure` | After tool fails | Yes |
| `Stop` | Agent finishes response | No |
| `SubagentStart` | Subagent starts | No |
| `SubagentStop` | Subagent stops | No |
| `Notification` | Alert sent | No |
| `PreCompact` | Before compaction | Yes (`auto` or `manual`) |

**Handler types:**

```json
{"type": "command", "command": "path/to/script.py", "timeout": 10}
{"type": "command", "command": "script.sh", "async": true}
{"type": "prompt", "prompt": "Evaluate if task is complete..."}
{"type": "agent", "...": "spawns subagent with tools"}
```

**Matcher syntax:** `"Write"`, `"Write|Edit"`, `"*"`, `"Bash(npm test*)"`, `"mcp__memory__.*"`

**Exit codes:** 0 = allow, 2 = block (stderr sent to Claude), 1/3+ = non-blocking error

**JSON response fields:**
```json
{
  "decision": "approve|block|allow|deny|ask",
  "reason": "explanation",
  "continue": true,
  "updatedInput": {},
  "additionalContext": "injected into model context"
}
```

**Agent team hooks:**
- `TeammateIdle` -- exit code 2 provides feedback and re-engages idle teammates
- `TaskCompleted` -- exit code 2 prevents completion (quality gates)

**Body template:** See `../templates/hook-body.py` and `../templates/hook-settings.json`

---

## E. Expert Systems (Plan/Build/Improve Trio)

A pattern combining three commands into a self-improving domain expert. Each command shares an `## Expertise` section that the Improve command updates over time.

**When to use:** Specialized domains where accumulated knowledge matters (hooks, security, testing, infrastructure). When you need a plan -> build -> learn feedback loop.
**When NOT to use:** One-off tasks. Simple CRUD workflows.

**Structure:**
```
.claude/commands/experts/<domain>/
  <domain>_plan.md       # Analyzes requirements, creates specifications
  <domain>_build.md      # Implements from specifications
  <domain>_improve.md    # Reviews git diffs, updates Expertise sections
```

**Shared characteristics:**
- All three commands share identical `## Expertise` sections (the knowledge base)
- Only `_improve` modifies the Expertise sections -- `_plan` and `_build` consume them
- `_plan` outputs a spec file to `specs/experts/<domain>/`
- `_build` reads that spec file and implements it
- `_improve` reads git diffs and enriches the Expertise sections in `_plan` and `_build`

**Body templates:** See `../templates/expert-plan.md`, `../templates/expert-build.md`, `../templates/expert-improve.md`

---

## F. Agent Teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)

Multi-instance orchestration where a team lead delegates to independent teammates with shared task lists and peer messaging.

**When to use:** Parallel workstreams, competing hypothesis debugging, full-stack features, architecture decisions, review panels.
**When NOT to use:** Sequential tasks. Tasks that fit in a single context window. Token-sensitive environments.

**Enable via settings.json:**
```json
{
  "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" },
  "teammateMode": "auto"
}
```

**Architecture:**
- **Team Lead** -- plans, delegates, synthesizes (does NOT implement in delegate mode)
- **Teammates** -- independent Claude instances with own context windows
- **Shared Task List** -- pending/in-progress/completed states with dependency chains
- **Mailbox System** -- direct peer-to-peer messaging

**Delegate Mode:** `Shift+Tab` restricts lead to coordination-only tools.

**Task sharing across sessions:** `CLAUDE_CODE_TASK_LIST_ID` env var points multiple instances at the same task list.

**Cost consideration:** 3-teammate team for 30 minutes uses ~3-4x single session tokens. Use Sonnet for implementation teammates, Opus for leads.

---

## G. Headless Automation (`claude -p`)

Non-interactive mode for CI/CD, background agents, and automated pipelines.

**When to use:** Background agents, CI/CD integration, agent-in-agent architectures, automated batch processing.

**Key flags:**
```bash
claude -p "prompt"                          # Non-interactive
  --model opus                              # Model selection
  --output-format json|text                 # Output format
  --append-system-prompt "instructions"     # Injected into system prompt (not user message)
  --system-prompt-file path/to/file.md      # System prompt from file
  --allowedTools "Bash,Read"                # Tool restriction
  --add-dir /path/to/dir                    # Additional context directories
  --agents '{"name":"x","description":"y"}' # Inline agent definitions
  --dangerously-skip-permissions            # Bypass all permission prompts
```

**Key distinction:** `CLAUDE.md` content is injected as a user message. `--append-system-prompt` content is appended to the system prompt itself. Use system prompt for identity/rules, user message for task context.
