# Plugin Design Guidelines

Design principles for building efficient, reliable Claude Code plugins in the Provectus marketplace. These guidelines emerged from production experience and should be applied to all new and existing plugins.

---

## 1. Context Efficiency

Every token loaded into context has a cost. Minimize what the model sees at any given moment.

### 1.1 Split Monolithic Command Files

**Problem:** A single command file with 10+ modes forces the model to load all mode instructions when only one is needed.

**Rule:** When a command file exceeds ~200 lines or contains 4+ modes, split into a **thin dispatcher** that routes to per-mode files.

```
commands/
├── my-plugin-run.md          # Thin dispatcher: parse mode, load the right file
├── modes/
│   ├── mode-a.md             # Only loaded when mode-a is invoked
│   ├── mode-b.md             # Only loaded when mode-b is invoked
│   └── mode-c.md
```

The dispatcher should be <50 lines: parse the mode, announce which file to load, and instruct the agent to read and execute that file.

### 1.2 Lazy-Load Reference Material

**Problem:** Loading all reference files at command start wastes context on content that may not apply.

**Rule:** Reference files should be loaded **at the point of need**, not at startup. Use explicit instructions: "After the user selects [option], read `references/[relevant-file].md`."

Split large reference files by category when the user's choice determines which section applies:
```
references/
├── engagement-models/
│   ├── time-and-materials.md
│   ├── fixed-price.md
│   └── milestone-based.md
```

### 1.3 Separate Instructions from Reference

| Content Type | When to Load | Where to Put |
|---|---|---|
| **Orchestration instructions** (process steps, tool calls, decision logic) | At command start | Skill or mode file |
| **Reference material** (templates, examples, conventions) | At point of need | `references/` directory |
| **Output templates** (structural scaffolds for generated content) | At generation step | `templates/` directory |

### 1.4 Avoid Duplication Across Files

**Problem:** When a skill file and a command file both describe the same workflow, the model sees two slightly different versions and may blend them or follow the wrong one.

**Rule:** Single source of truth. The command file should **delegate** to the skill, not restate it:

```markdown
## Mode: generate-sow

Load and execute the `sow-generator` skill by reading `skills/sow-generator/SKILL.md`.
Pass these parsed arguments: [list flags].
```

If two files must reference the same concept, one should contain the full definition and the other should contain only a pointer.

---

## 2. Skill Safety — Preventing Context Explosion

When a skill is selected from the plugins picker (vs. a command with arguments), there is **no user-provided mode or argument**. The model sees the full SKILL.md and decides what to do. If the skill contains imperative instructions ("detect environment", "read these files", bash code blocks), the model executes all of them immediately, cascading into reference files, mode files, and shell commands that rapidly fill the context window and can make Claude Code unresponsive.

### 2.1 SKILL.md Must Be a Router, Not a Runbook

**Problem:** A SKILL.md that contains step-by-step instructions with embedded bash commands gets executed eagerly when invoked without arguments.

**Rule:** SKILL.md must open with an explicit "ask first, load later" instruction. When invoked, it should:
1. Greet the user and present available options
2. Wait for the user's choice
3. Only then load the relevant mode file

Include a prominent guard at the top:

```markdown
## CRITICAL: Ask First, Load Later

**DO NOT** read reference files, run environment detection commands, or load
mode files until the user has told you what they want to do.
```

### 2.2 No Executable Code Blocks in SKILL.md

**Problem:** Bash snippets in a skill file are treated as imperative instructions and get executed immediately on skill load.

**Rule:** SKILL.md must not contain bash code blocks. Move all executable snippets to mode files, which are only loaded after the user selects a path. SKILL.md should contain only: name, description, when-to-use, scope table, routing table, and condensed principles (prose only).

| Allowed in SKILL.md | NOT allowed in SKILL.md |
|---|---|
| Routing table mapping user intent to mode files | `bash` code blocks |
| Condensed principles (prose) | Inline verification commands |
| Scope / connector table | Token format tables with validation regexes |
| "When to use" criteria | Detailed troubleshooting steps |

### 2.3 Budget Rule: SKILL.md < 80 Lines

**Problem:** Long SKILL.md files signal that content is leaking in from mode/reference files.

**Rule:** SKILL.md should be under 80 lines. If it exceeds this, audit for content that belongs in mode files or references. The skill file should contain:
- YAML frontmatter (~5 lines)
- One-paragraph description (~3 lines)
- Ask-first guard (~5 lines)
- When-to-use list (~5 lines)
- Scope table (~8 lines)
- Routing table (~10 lines)
- Condensed principles (~15 lines)
- Reference file index with lazy-load instructions (~10 lines)

### 2.4 Agent Definitions Must Delegate, Not Duplicate

**Problem:** When an agent definition restates detailed knowledge from reference files, the model loads both — doubling context for the same information.

**Rule:** Agent `.md` files should describe the agent's identity and behavioral guidelines, then **point to** mode files and references for technical details. Replace knowledge sections with delegation pointers:

```markdown
## Technical Knowledge

Detailed setup steps live in mode files and reference docs — delegate to:
- **Slack setup** → `commands/modes/setup-slack.md` + `references/slack-setup.md`
- **Google Drive setup** → `commands/modes/setup-google-drive.md`

Load these at point-of-need, not upfront.
```

### 2.5 Context-Load Guards on Reference-Reading Steps

**Problem:** Mode files that instruct "Read file X" without qualification get pre-loaded when the model scans ahead.

**Rule:** Every step that reads a reference file must include an explicit guard:

```markdown
> **CONTEXT GUARD**: ONLY read the reference file below when the user
> reaches this step. Do NOT pre-load it during earlier steps or at
> skill initialization.
```

### 2.6 Guard External Tool Dependencies in Hooks

**Problem:** Hooks that shell out to tools like `jq`, `python3`, or `node` fail or hang when the tool isn't installed, potentially blocking the session.

**Rule:** Every hook command must check for tool existence before executing. Use an early exit so the hook is a silent no-op when the tool is missing:

```json
{
  "command": "which jq >/dev/null 2>&1 || exit 0; jq -r '.field' | ..."
}
```

---

## 3. Prompt Design

### 3.1 North Star Statement

Every skill and command must open with a concrete, verifiable description of what it produces. Not "a delivery-ready document" but "a Google Doc with 7 numbered sections following the Provectus SOW template, ready for client signature."

### 3.2 Show, Don't Tell

**Rule:** For every critical output format, provide at least one concrete example. Examples anchor model behavior more effectively than prose instructions.

| Tell (weak) | Show (strong) |
|---|---|
| "Write a specific scope item" | `"Implement 12 REST API endpoints for user management with JWT authentication and rate limiting"` |
| "Include acceptance criteria" | `"Accepted when: all 47 test cases pass, response latency < 200ms at 100 concurrent users"` |

**Target ratio:** At least 30% of skill content should be examples, templates, or worked demonstrations. Pure instruction text ("tell") should not exceed 70%.

### 3.3 Structural Output Templates

When the model must generate structured documents, provide a **skeleton template** — a complete document scaffold with headers, placeholder tables, and `<!-- guidance -->` comments. This eliminates structural variation across runs.

Templates belong in `templates/` and should be based on **real production examples**, not invented formats.

### 3.4 Do/Don't Pairs Over Abstract Principles

Replace vague quality principles with concrete Do/Don't pairs:

| Principle | Do | Don't |
|---|---|---|
| Specific | "Develop REST API with 12 endpoints for user management" | "Build backend API" |
| Measurable | "Accepted when all 47 test cases in the acceptance plan pass" | "Accepted when client approves" |

### 3.5 Cite-Your-Work Constraints Over Self-Verification Checklists

**Problem:** A checklist asking the model to verify its own output ("verify all sections are present") will always self-report as passing.

**Rule:** Replace with cite-your-work constraints: "Before proceeding, cite the specific text from your draft that satisfies each criterion. If you cannot cite text for a criterion, complete that section first."

---

## 4. Task Decomposition

### 4.1 One Complex Task Per Turn

If a phase requires generating 2,000+ words of content, decompose it:
1. Generate outline / structure → pause for validation
2. Generate content sections in batches
3. Run quality verification

### 4.2 Subagents for Isolated Data Gathering

Use subagents (Task tool) when:
- The task is data-gathering that produces a structured artifact
- The gathered data would bloat the main conversation context
- The task can run independently without user interaction

The subagent's output contract (schema/template of what it returns) must be explicit in the agent definition.

### 4.3 Adequacy Gates

Before a generation-heavy phase, verify that prerequisites are met. Define minimum required inputs:

```markdown
**Context adequacy gate:** Before proceeding to draft generation, verify:
- Client name is identified
- At least 3 stated requirements exist
- Project purpose is clear
If any are missing, collect them in the clarification interview before generating.
```

### 4.4 Bounded Iteration

Any loop (edit/retry cycles) must have a termination condition:
```markdown
After 3 rounds of Edit without Approve, present a summary of all changes
and ask: "Continue editing, start fresh, or pause and resume later?"
```

---

## 5. Error Handling & Fallbacks

### 5.1 MCP Unavailability

When a workflow depends on an MCP server (Slack, Google Drive, Atlassian), always define:
- What happens when the MCP is unavailable
- How to proceed with partial data
- What the user should be told

### 5.2 Output Fallbacks

When writing to external services (Google Drive, Slack, Confluence), always define a local fallback:
```markdown
If Google Drive write fails:
1. Write to local file at `docs/{type}/{name}-{date}.md`
2. Output the full content in the conversation as a code block
3. Inform the user and suggest manual upload
```

### 5.3 Subagent Error Propagation

When a subagent returns partial or empty results, the main workflow must have explicit handling:
```markdown
If the subagent returns a partial brief (one source failed):
  → Continue with available data, flag the gap
If the subagent returns an empty brief:
  → Switch to manual input mode
```

---

## 6. Tool Configuration

### 6.1 Tool Lists Must Match Actual Requirements

The `tools:` field in agent frontmatter must include every tool the agent needs to execute its primary function. Common mistakes:
- Listing `Read, Glob, Grep` when the agent needs MCP server tools
- Omitting `Write` when the agent creates files
- Listing tools the agent never uses

### 6.2 Model Selection

| Agent Purpose | Recommended Model | Rationale |
|---|---|---|
| Data extraction, summarization | `sonnet` | Good comprehension, fast, cost-effective |
| Complex reasoning, generation | `opus` | Highest quality for nuanced output |
| Simple routing, classification | `haiku` | Fastest, cheapest for simple tasks |

---

## 7. File Organization

### 7.1 Standard Plugin Structure

```
plugin-name/
├── .claude-plugin/plugin.json      # Manifest
├── .mcp.json                       # MCP server configs
├── skills/
│   └── skill-name/
│       ├── SKILL.md                # Orchestration + examples
│       ├── references/             # Loaded at point of need
│       └── templates/              # Output scaffolds
├── commands/
│   ├── plugin-hub.md               # Command router (<50 lines)
│   ├── plugin-run.md               # Thin dispatcher (<50 lines)
│   ├── plugin-review.md            # Thin dispatcher (<50 lines)
│   └── modes/                      # Per-mode instruction files
│       ├── mode-a.md
│       └── mode-b.md
├── agents/                         # Subagent definitions
├── hooks/
│   └── hooks.json                  # Event hooks
├── CLAUDE.md                       # Plugin documentation
└── README.md                       # User-facing docs
```

### 7.2 Naming Conventions

- Skills: `kebab-case/SKILL.md`
- Commands: `plugin-name-{hub|run|review}.md`
- Mode files: `modes/{mode-name}.md`
- Agents: `kebab-case.md`
- References: `references/{topic}.md`
- Templates: `templates/{template-name}.md`

---

## 8. Documentation

### 8.1 CLAUDE.md

Must include:
- Directory tree showing all components
- One-line description of each skill, command, agent
- MCP server list with purpose
- Hook descriptions

### 8.2 README.md

Must include:
- Plugin description and version
- Installation instructions
- Usage examples for every command mode
- Component inventory table

---

## 9. New Plugin Registration Checklist

When adding a new plugin to the marketplace, complete ALL of the following:

### Plugin Components
- [ ] `.claude-plugin/plugin.json` — manifest with name, version, description, author
- [ ] `.mcp.json` — MCP server configurations (or empty `{}` if none)
- [ ] `skills/<name>/SKILL.md` — core skill with YAML frontmatter
- [ ] `commands/<plugin>-hub.md` — capabilities overview (<50 lines)
- [ ] `commands/<plugin>-run.md` — execution dispatcher
- [ ] `commands/<plugin>-review.md` — review/audit command
- [ ] `agents/<practice>-specialist.md` — specialist subagent
- [ ] `hooks/hooks.json` — lifecycle hooks
- [ ] `CLAUDE.md` — developer documentation
- [ ] `README.md` — user-facing documentation

### Marketplace Registration
- [ ] `marketplace.json` — add plugin entry + update statistics
- [ ] `.claude-plugin/marketplace.json` — add plugin entry
- [ ] `README.md` (root) — add to plugins table + update statistics + add to project structure tree

### Router Integration
- [ ] `proagent-router/skills/proagent-router/SKILL.md` — add to routing table + specialist agents table + available practices list
- [ ] `proagent-router/commands/proagent.md` — add to Available Practices table
- [ ] `proagent-router/CLAUDE.md` — add to practices list + update count
