# proagent-delivery

A Claude Code plugin for project delivery management. Covers sprint planning, milestone tracking, stakeholder updates, status reports, risk assessment, retrospectives, resource allocation, and agile/scrum ceremony facilitation.

**Version:** 0.2.0
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

## Components

| Component | Name | Purpose |
|-----------|------|---------|
| Skill | `proagent-delivery:delivery-assistant` | Core skill covering all delivery phases |
| Command | `proagent-delivery:proagent-delivery-hub` | Command hub and routing |
| Command | `proagent-delivery:proagent-delivery-run` | Execute delivery workflows (5 modes) |
| Command | `proagent-delivery:proagent-delivery-review` | Delivery health reviews (4 modes) |
| Agent | `proagent-delivery:delivery-specialist` | Subagent for assessments and reports |
| Hook | Status update reminder | 3-day freshness check, milestone proximity alert |
| Hook | Milestone check | Acceptance criteria and stakeholder notification before release |
| Hook | Sprint boundary notification | Follow-up actions after planning and retrospective |

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| Atlassian | `@modelcontextprotocol/server-atlassian` | Jira sprint management, backlog, Confluence documentation |
| Rube | `rube.app/mcp` | SaaS automation gateway (Jira, Linear, Asana, Trello, etc.) |

Set the environment variables for the services your team uses. Unused servers will not be started.

## Source Repositories

This plugin synthesizes patterns and content from 8 source repositories:

- **proagent** -- Project-manager role with 5 delivery skills (meeting facilitation, risk assessment, status reporting, stakeholder management, spec creation), weekly standup command, and project charter template
- **awesome-claude-skills** -- Internal communications skill with 3P update format, company newsletter templates, FAQ response patterns, and general communications guidelines
- **taches-cc-resources** -- Prioritization and analysis frameworks (Eisenhower matrix for urgent/important classification, Pareto 80/20 analysis, 5 Whys root cause drilling, SWOT mapping, inversion thinking, first principles decomposition), plus todo capture and resume workflows
- **awos** -- Product definition command and template, product roadmap command and template for milestone-based planning
- **proagent-repo GUI** -- KPI framework for measuring delivery effectiveness, planning command for generating implementation plans from specifications
- **ralph-orchestrator** -- Code task listing with status metadata for progress tracking
- **skills** -- Third-party update templates for external stakeholder communications
- **specs** -- Business role implementation patterns for delivery practice definition
