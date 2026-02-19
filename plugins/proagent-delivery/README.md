# proagent-delivery

A Claude Code plugin for project delivery management. Covers sprint planning, milestone tracking, stakeholder updates, status reports, risk assessment, retrospectives, resource allocation, agile/scrum ceremony facilitation, SOW generation and review, standup notes generation, PRD creation, internal communications, task planning, meeting insights analysis, agentic KPIs tracking, todo management, and Eisenhower matrix prioritization.

**Version:** 0.4.0
**Category:** Delivery
**License:** MIT

## Installation

Copy the `proagent-delivery` directory into your Claude Code plugins directory, or reference it from your project's `.claude/plugins/` configuration.

## Quick Start

Run `/proagent-delivery:proagent-delivery-hub` to see all available commands and pick the right workflow for your task.

### Common Workflows

**Plan a sprint:**
```
/proagent-delivery:proagent-delivery-run plan-sprint
```
Set sprint goal aligned to roadmap milestones, check team capacity against velocity history, groom and estimate backlog stories using Fibonacci scale, apply Eisenhower Matrix and Pareto prioritization, and commit to sprint backlog with risk summary.

**Generate a status report:**
```
/proagent-delivery:proagent-delivery-run status-report weekly
```
Produce a structured weekly status report with progress, metrics, wins, issues, and next steps. Also supports `daily`, `monthly`, `executive`, and `3p` (Progress/Plans/Problems) formats. Reports use RAG status indicators and are tailored to audience depth.

**Assess project risks:**
```
/proagent-delivery:proagent-delivery-run risk-assess
```
Identify risks across Technical, Schedule, Resource, Scope, and External categories. Analyze using Probability x Impact matrix, prioritize by severity, and develop mitigation strategies (Avoidance, Reduction, Transfer, Acceptance). Generates a complete risk register with owners and review cadence.

**Track milestones:**
```
/proagent-delivery:proagent-delivery-run milestone-track
```
Compare milestone progress against baseline plan, calculate schedule drift, perform critical path analysis, and recommend corrective actions for milestones that are behind or at risk.

**Run a retrospective:**
```
/proagent-delivery:proagent-delivery-run retrospective
```
Facilitate a structured retrospective using Start-Stop-Continue framework. Apply 5 Whys root cause analysis to top issues, define 2-3 improvement actions with owners, and set one experiment for the next sprint with measurable success criteria.

**Review sprint health:**
```
/proagent-delivery:proagent-delivery-review sprint-health
```
Assess velocity trends, burndown progress, active blockers, and scope stability. Produces a sprint health scorecard with RAG ratings across four dimensions.

**Check stakeholder alignment:**
```
/proagent-delivery:proagent-delivery-review stakeholder-alignment
```
Map stakeholders using Power/Interest Grid, audit communication cadence, review open decisions, and identify alignment gaps. Ensures the "No Surprises" rule is being followed.

**Generate standup notes:**
```
/proagent-delivery:proagent-delivery-run standup-notes
```
Generate AI-assisted daily standup notes by analyzing git history, Jira tickets, and calendar data. Supports daily, async, and 3P formats. Links commits to Jira tickets and transforms technical messages into business value statements.

**Create a PRD:**
```
/proagent-delivery:proagent-delivery-run create-prd
```
Generate a Product Requirements Document from feature ideas and JTBD analysis. Reads product context, feature specs, and JTBD documentation. Outputs structured PRD with problem statement, user stories, acceptance criteria, and success metrics.

**Draft internal communications:**
```
/proagent-delivery:proagent-delivery-run internal-comms <type>
```
Write internal communications using company-standard formats. Supports 3P updates, newsletters, FAQs, incident reports, leadership updates, and project updates.

**Create a task plan:**
```
/proagent-delivery:proagent-delivery-run task-plan
```
Create a phased task plan with progress tracking, decision logs, and error tracking. Breaks work into 3-7 phases with structured tracking sections.

**Generate a SOW:**
```
/proagent-delivery:proagent-delivery-run generate-sow --channel=proj-acme-delivery --drive=https://drive.google.com/... --with-rom
```
Generate a delivery-ready Statement of Work from client context. Reads Slack channel history and Google Drive documents via MCP, conducts a structured clarification interview with the Solution Owner (engagement model, pricing, phases, assumptions), generates all 9 SOW sections using Provectus templates, and outputs to Google Drive as a Google Doc. Optionally appends a ROM estimate via `--with-rom`.

**Review a SOW:**
```
/proagent-delivery:proagent-delivery-review sow-review path/to/sow.md
```
Audit an existing SOW for completeness, scope specificity, pricing alignment, timeline realism, team composition, and risk coverage. Produces a structured audit report with section-by-section quality scores and actionable recommendations.

## Components

| Component | Name | Purpose |
|-----------|------|---------|
| Skill | `proagent-delivery:delivery-assistant` | Core skill covering all delivery phases |
| Skill | `proagent-delivery:rom-estimate` | ROM effort estimation from project docs |
| Skill | `proagent-delivery:sow-generator` | SOW generation from Slack + Drive context |
| Command | `proagent-delivery:proagent-delivery-hub` | Command hub and routing |
| Command | `proagent-delivery:proagent-delivery-run` | Execute delivery workflows (11 modes) |
| Command | `proagent-delivery:proagent-delivery-review` | Delivery health reviews (8 modes) |
| Agent | `proagent-delivery:delivery-specialist` | Subagent for assessments and reports |
| Agent | `proagent-delivery:sow-context-extractor` | SOW context extraction from Slack + Drive |
| Hook | Status update reminder | 3-day freshness check, milestone proximity alert |
| Hook | Milestone check | Acceptance criteria and stakeholder notification before release |
| Hook | Sprint boundary notification | Follow-up actions after planning and retrospective |
| Hook | SOW output notification | Share SOW with stakeholders after generation |

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |
| Atlassian | `@modelcontextprotocol/server-atlassian` | Jira sprint management, backlog, Confluence documentation |
| Rube | `rube.app/mcp` | SaaS automation gateway (Jira, Linear, Asana, Trello, etc.) |

Set the environment variables for the services your team uses. Unused servers will not be started.

