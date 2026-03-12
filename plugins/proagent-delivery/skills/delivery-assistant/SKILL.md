---
name: delivery-assistant
description: Use when managing project delivery -- sprint planning, milestones, stakeholder updates, status reports, risk management, timelines, resource allocation, agile/scrum ceremonies, retrospectives, standup notes generation, PRD creation, todo management, meeting insights analysis, internal communications, agentic KPIs tracking, task planning, and Eisenhower matrix prioritization
---

# Managing Project Delivery

Comprehensive delivery skill covering sprint planning, milestone tracking, status reporting, risk management, stakeholder engagement, and agile ceremonies.

## When to Use

- Planning sprints and iterations
- Tracking milestones and project timelines
- Writing status reports and stakeholder updates
- Assessing and managing project risks
- Facilitating retrospectives and agile ceremonies
- Generating standup notes and internal communications
- Creating PRDs and managing todo backlogs
- Tracking agentic KPIs and planning tasks

## When Invoked Without Clear Intent

**Use `AskUserQuestion`** to present options as a selector widget:

```
AskUserQuestion(
  header: "Delivery",
  question: "What project delivery task do you need help with?",
  options: [
    { label: "Sprint Planning", description: "Sprint planning, milestone tracking, resource allocation, retrospectives" },
    { label: "Status & Reporting", description: "Status reports, risk management, standup notes, 3P updates" },
    { label: "Stakeholder Mgmt", description: "Meeting facilitation, agile ceremonies, meeting insights" },
    { label: "Planning & PRDs", description: "PRD creation, todo management, task planning, AWOS pipeline" }
  ]
)
```

## Reference Routing

> **CONTEXT GUARD**: Load reference files only when the user's request matches a specific topic below. Do NOT load all references upfront.

| User Intent | Reference File |
|---|---|
| Sprint planning, milestone tracking, resource allocation, retrospectives, capacity | `references/sprint-patterns.md` |
| Status reports, risk management, standup notes, internal communications, 3P updates | `references/reporting-patterns.md` |
| Stakeholder management, meeting facilitation, agile ceremonies, meeting insights | `references/stakeholder-patterns.md` |
| PRD creation, todo management, agentic KPIs, task planning, Eisenhower matrix, AWOS, confirmation gates | `references/planning-patterns.md` |

## Composio App Automations

Integrates with Jira, Linear, Asana, ClickUp, Monday.com, Confluence, and Trello via the Rube MCP server (`RUBE_SEARCH_TOOLS` → `RUBE_MANAGE_CONNECTIONS` → `RUBE_MULTI_EXECUTE_TOOL`).

## Integration Points

- **Jira**: Sprint management, backlog grooming, issue tracking, velocity metrics
- **Confluence**: Meeting notes, project charters, risk registers, retrospectives
- **Slack**: Daily standups, 3P updates, blocker alerts, milestone notifications
- **Google Calendar**: Sprint ceremony scheduling, milestone due dates

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate project timeline diagrams, sprint flows, stakeholder RACI maps, and risk matrix layouts. Describe what you need in natural language.
