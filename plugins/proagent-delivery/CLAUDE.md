# ProAgent Delivery Plugin

This plugin provides comprehensive project delivery management for Claude Code. It was synthesized from 8 source repositories including proagent (project-manager roles), awesome-claude-skills (internal-comms), taches-cc-resources (prioritization frameworks), and awos (product/roadmap commands).

## Plugin Structure

```
proagent-delivery/
├── .claude-plugin/plugin.json                  # Plugin manifest (name, version, category)
├── .mcp.json                                   # MCP server configs (Atlassian, Slack, Google Calendar)
├── skills/
│   ├── delivery-assistant/SKILL.md             # Core skill: Managing Project Delivery
│   └── rom-estimate/                           # ROM estimation skill: effort estimates from project docs
│       ├── SKILL.md                            # Skill definition with Google Drive MCP support
│       ├── references/effort-levels.md         # Effort sizing guide (XS/S/M/L/XL)
│       ├── references/epic-categories.md       # Epic taxonomy with sub-category guidance
│       └── examples/apex-vendor-platform-rom.csv  # Sample 89-feature ROM output
├── commands/
│   ├── proagent-delivery-hub.md                # Command hub: list and route to delivery commands
│   ├── proagent-delivery-run.md                # Execute: plan-sprint, status-report, risk-assess, milestone-track, retrospective, rom-estimate
│   └── proagent-delivery-review.md             # Review: sprint-health, delivery-risks, timeline, stakeholder-alignment, estimate-review
├── agents/
│   └── delivery-specialist.md                  # Delivery specialist subagent for assessments and reports
├── hooks/
│   └── hooks.json                              # Status update reminders, milestone checks, sprint boundary notifications
├── CLAUDE.md                                   # This file
└── README.md                                   # User-facing documentation
```

## Usage

### Skills
Use the `proagent-delivery:delivery-assistant` skill when managing any aspect of project delivery. It covers sprint planning, milestone tracking, status reporting, risk management, stakeholder communication, meeting facilitation, resource allocation, and retrospective analysis.

Use the `proagent-delivery:rom-estimate` skill when generating ROM (Rough Order of Magnitude) effort estimates. It analyzes project documents, task lists, or scope descriptions and produces a semicolon-delimited CSV with effort levels, duration ranges, and team specialties. Supports reading project files directly from Google Drive via the Google Drive MCP server.

### Commands
- `/proagent-delivery:proagent-delivery-hub` -- See all available commands and choose the right workflow
- `/proagent-delivery:proagent-delivery-run <mode>` -- Execute a workflow (plan-sprint, status-report, risk-assess, milestone-track, retrospective, rom-estimate)
- `/proagent-delivery:proagent-delivery-review <type>` -- Run a delivery health review (sprint-health, delivery-risks, timeline, stakeholder-alignment, estimate-review)

### Agent
The `proagent-delivery:delivery-specialist` agent can be dispatched as a subagent for sprint planning, risk assessments, status report generation, and stakeholder alignment checks. It produces structured reports with findings organized by priority and RAG status.

### Hooks
Three hooks support delivery discipline:
1. **Milestone check:** Before deploy/release commands, validates that milestone acceptance criteria are met and stakeholders have been notified.
2. **Status update reminder:** After git commits, suggests running a status report to update stakeholders.
3. **Sprint boundary notification:** After sprint planning or retrospective sessions, suggests follow-up actions (create Jira sprint, schedule ceremonies, share summary).

### MCP Servers

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **Atlassian**: Jira sprint management, backlog grooming, issue tracking, velocity metrics, burndown charts, and Confluence documentation publishing via `@modelcontextprotocol/server-atlassian`
- **Rube (Composio)**: SaaS automation gateway providing access to Jira, Linear, Asana, ClickUp, Monday.com, Confluence, and Trello via `RUBE_SEARCH_TOOLS`, `RUBE_MANAGE_CONNECTIONS`, and `RUBE_MULTI_EXECUTE_TOOL`

## ROM Estimation

The `rom-estimate` run mode analyzes project documents (local files, pasted content, or Google Drive via MCP) and generates effort estimates following a 6-step process: accept input, analyze scope and identify epics, expand tasks into sub-features, estimate effort levels (XS/S/M/L/XL), generate semicolon-delimited CSV, and display an analysis summary with FTE estimates, epic breakdown, and risk factors.

Key features:
- Reads input from local files, pasted content, or **Google Drive** via MCP
- Expands high-level tasks into 2-5 granular sub-features per epic
- Effort levels with optimistic/pessimistic duration ranges
- Specialty mapping across 10 team roles
- Outputs semicolon-delimited CSV to `docs/rom-estimation/{slug}-rom.csv`
- Executive summary with FTE estimates, epic breakdown, and risk factors

The `estimate-review` review mode audits existing ROM CSVs for completeness, sizing accuracy, and team balance.

## Source Attribution

Key patterns and content were drawn from:
- **proagent** -- Project-manager role skills (meeting facilitation, risk assessment, status reporting, stakeholder management, spec creation), weekly standup command, project charter template
- **awesome-claude-skills** -- Internal communications skill (3P updates, newsletters, FAQ responses, general comms)
- **taches-cc-resources** -- Prioritization frameworks (Eisenhower matrix, Pareto analysis, 5 Whys root cause, SWOT mapping, inversion, first principles), todo management workflows
- **awos** -- Product definition and roadmap commands, product definition template, roadmap template
- **proagent-repo GUI** -- KPI framework for measuring agentic coding effectiveness, planning from specifications
- **ralph-orchestrator** -- Code task listing with status and metadata
- **skills** -- Third-party update templates
- **specs** -- Business role implementation patterns
- **rom-estimate** -- ROM estimation skill with effort sizing guide, epic taxonomy, and sample output
