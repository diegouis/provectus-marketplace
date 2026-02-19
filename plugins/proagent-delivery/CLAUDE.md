# ProAgent Delivery Plugin

This plugin provides comprehensive project delivery management for Claude Code.

## Plugin Structure

```
proagent-delivery/
├── .claude-plugin/plugin.json                  # Plugin manifest (name, version, category)
├── .mcp.json                                   # MCP server configs (Atlassian, Slack, Google Calendar)
├── skills/
│   ├── delivery-assistant/SKILL.md             # Core skill: Managing Project Delivery
│   ├── rom-estimate/                           # ROM estimation skill: effort estimates from project docs
│   │   ├── SKILL.md                            # Skill definition with Google Drive MCP support
│   │   ├── references/effort-levels.md         # Effort sizing guide (XS/S/M/L/XL)
│   │   ├── references/epic-categories.md       # Epic taxonomy with sub-category guidance
│   │   └── examples/apex-vendor-platform-rom.csv  # Sample 89-feature ROM output
│   └── sow-generator/                          # SOW generation skill: create delivery-ready SOWs
│       ├── SKILL.md                            # 6-phase SOW generation workflow
│       ├── references/sow-sections.md          # Section-by-section SOW writing guidance
│       ├── references/engagement-models.md     # T&M, Fixed-Price, Milestone, Discovery+Delivery patterns
│       ├── references/pricing-guidance.md      # Rate card structure and pricing conventions
│       └── templates/                          # Directory for user-provided sample SOW templates
├── commands/
│   ├── proagent-delivery-hub.md                # Command hub: list and route to delivery commands
│   ├── proagent-delivery-run.md                # Execute: plan-sprint, status-report, risk-assess, milestone-track, retrospective, rom-estimate, generate-sow
│   └── proagent-delivery-review.md             # Review: sprint-health, delivery-risks, timeline, stakeholder-alignment, estimate-review, sow-review
├── agents/
│   ├── delivery-specialist.md                  # Delivery specialist subagent for assessments and reports
│   └── sow-context-extractor.md               # SOW context extraction from Slack + Google Drive
├── hooks/
│   └── hooks.json                              # Status update reminders, milestone checks, sprint boundary notifications, SOW output notifications
├── CLAUDE.md                                   # This file
└── README.md                                   # User-facing documentation
```

## Usage

### Skills
Use the `proagent-delivery:delivery-assistant` skill when managing any aspect of project delivery. It covers sprint planning, milestone tracking, status reporting, risk management, stakeholder communication, meeting facilitation, resource allocation, and retrospective analysis.

Use the `proagent-delivery:rom-estimate` skill when generating ROM (Rough Order of Magnitude) effort estimates. It analyzes project documents, task lists, or scope descriptions and produces a semicolon-delimited CSV with effort levels, duration ranges, and team specialties. Supports reading project files directly from Google Drive via the Google Drive MCP server.

Use the `proagent-delivery:sow-generator` skill when creating Statements of Work. It reads client context from Slack channels and Google Drive documents, conducts a clarification interview with the Solution Owner, generates a delivery-ready SOW using templates, and outputs to Google Drive. Optionally generates a ROM estimate as an appendix.

### Commands
- `/proagent-delivery:proagent-delivery-hub` -- See all available commands and choose the right workflow
- `/proagent-delivery:proagent-delivery-run <mode>` -- Execute a workflow (plan-sprint, status-report, risk-assess, milestone-track, retrospective, rom-estimate, generate-sow, standup-notes, create-prd, internal-comms, task-plan)
- `/proagent-delivery:proagent-delivery-review <type>` -- Run a delivery health review (sprint-health, delivery-risks, timeline, stakeholder-alignment, estimate-review, meeting-insights, comms-quality, sow-review)

### Agents
The `proagent-delivery:delivery-specialist` agent can be dispatched as a subagent for sprint planning, risk assessments, status report generation, and stakeholder alignment checks. It produces structured reports with findings organized by priority and RAG status.

The `proagent-delivery:sow-context-extractor` agent is dispatched by the SOW generator to read Slack channel history and Google Drive documents. It produces a structured Client Context Brief with requirements, stakeholders, timeline signals, budget signals, and a document inventory.

### Hooks
Four hooks support delivery discipline:
1. **Milestone check:** Before deploy/release commands, validates that milestone acceptance criteria are met and stakeholders have been notified.
2. **Status update reminder:** After git commits, suggests running a status report to update stakeholders.
3. **Sprint boundary notification:** After sprint planning or retrospective sessions, suggests follow-up actions (create Jira sprint, schedule ceremonies, share summary).
4. **SOW output notification:** After writing a SOW file, suggests sharing it with stakeholders via Slack and uploading to the client Google Drive folder.

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

## SOW Generation

The `generate-sow` run mode creates delivery-ready Statements of Work from client context gathered via Slack and Google Drive. It follows a 6-phase process: source collection (via sow-context-extractor subagent), context synthesis, clarification interview with the SO, SOW draft generation, review gate, and output to Google Drive.

Key features:
- Reads client context from Slack channels via Slack MCP and Google Drive documents via Google Drive MCP
- Dispatches `sow-context-extractor` subagent for isolated data gathering
- Conducts structured clarification interview with the Solution Owner using `AskUserQuestion`
- Supports multiple engagement models: T&M, Fixed-Price, Milestone-Based, Discovery+Delivery
- Generates all 9 required SOW sections with Provectus conventions
- Mandatory review gate before output (Approve / Edit / Redo)
- Outputs directly to Google Drive as a Google Doc
- Optional ROM estimate as appendix via `--with-rom` flag

The `sow-review` review mode audits existing SOWs for section completeness, scope specificity, pricing alignment, timeline realism, team composition, and risk coverage.

## Source Repositories

Built from Provectus internal repositories: `agents`, `awesome-claude-code`, `awesome-claude-skills`, `awos`, `planning-with-files`, `proagent-repo`, `provectus-marketplace`. Key external assets include standup-notes and team collaboration commands from `agents`, PRD creation from `awesome-claude-code`, internal comms skill from `awesome-claude-skills`, and task planning templates from `planning-with-files`.
