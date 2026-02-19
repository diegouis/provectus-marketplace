---
name: delivery-assistant
description: Use when managing project delivery -- sprint planning, milestones, stakeholder updates, status reports, risk management, timelines, resource allocation, agile/scrum ceremonies, retrospectives, standup notes generation, PRD creation, todo management, meeting insights analysis, internal communications, agentic KPIs tracking, task planning, and Eisenhower matrix prioritization
---

# Managing Project Delivery

## Overview

This skill orchestrates all aspects of project delivery from sprint planning through retrospectives.

## When to Use

- Planning sprints and iterations (backlog grooming, capacity planning, story estimation)
- Tracking milestones and project timelines
- Writing stakeholder updates, 3P reports, or executive summaries
- Generating status reports (daily standup, weekly, monthly, ad-hoc)
- Assessing and managing project risks
- Facilitating retrospectives (Start-Stop-Continue, 5 Whys)
- Allocating and balancing team resources across workstreams
- Running agile/scrum ceremonies (sprint planning, review, retro, standup)
- Creating project charters, specifications, or roadmaps
- Managing scope changes through change control processes
- Generating AI-assisted standup notes from git history, Jira, and calendar data
- Creating Product Requirements Documents (PRDs) from feature ideas and JTBD analysis
- Writing internal communications (3P updates, newsletters, FAQs, incident reports, leadership updates)
- Analyzing meeting transcripts for communication patterns and facilitation insights
- Managing todo backlogs with structured capture and context-aware retrieval
- Tracking agentic KPIs (autonomy rate, first-pass success, cycle time, recovery rate)
- Planning tasks with phased progress tracking templates
- Prioritizing work using the Eisenhower matrix (urgent/important quadrant classification)
- Creating handoff documents for work continuity across sessions

## Capabilities

### 1. Sprint Planning

Guides teams through structured sprint planning following agile/scrum practices.

**Sprint planning process:**
1. Review sprint goal and align with product roadmap milestones
2. Check team capacity: available days, velocity history, planned time off
3. Groom backlog: clarify acceptance criteria, estimate story points, identify dependencies
4. Apply prioritization frameworks:
   - **Eisenhower Matrix**: urgent/important quadrant classification
   - **Pareto Analysis**: identify the 20% of work that delivers 80% of value
5. Commit to sprint backlog with team agreement
6. Identify risks and dependencies for the sprint
7. Document sprint goal, committed stories, and capacity allocation

**Sprint planning output:**
```
SPRINT: [Sprint Number]
GOAL: [One-sentence sprint goal aligned to milestone]
DATES: [Start] - [End]
CAPACITY: [X story points] ([Y team members] x [Z available days])

COMMITTED STORIES:
| # | Story | Points | Owner | Dependencies |
|---|-------|--------|-------|--------------|

RISKS:
- [Risk and mitigation for this sprint]

DEFINITION OF DONE:
- Code reviewed and approved
- Tests passing (>80% coverage for new code)
- Documentation updated
- Acceptance criteria verified
- Deployed to staging
```

### 2. Milestone Tracking

Monitors project milestones against the baseline plan, identifies schedule drift, and recommends corrective actions. Draws on the awos roadmap pattern and proagent spec-creation skill.

**Milestone tracking process:**
1. Load project timeline and milestone definitions
2. For each milestone, assess:
   - Planned vs. actual completion date
   - Percentage of deliverables complete
   - Blocking issues or dependencies
   - Schedule drift (ahead, on track, behind)
3. Calculate critical path impact if any milestone slips
4. Generate milestone health dashboard

**Milestone dashboard format:**
```
PROJECT MILESTONE TRACKER

| Milestone | Planned | Forecast | Status | % Complete | Blockers |
|-----------|---------|----------|--------|------------|----------|

CRITICAL PATH:
[Milestone A] --> [Milestone B] --> [Milestone C] --> [Release]

SCHEDULE HEALTH:
- On Track: X milestones
- At Risk: Y milestones
- Behind: Z milestones

CORRECTIVE ACTIONS:
1. [Action to address drift]
```

### 3. Status Reporting

Generates status reports tailored to different audiences and frequencies.

**Report types and audiences:**

- **Daily Standup (Written):** Team members -- bullet points: yesterday, today, blockers (2 min per person)
- **Weekly Status:** Direct manager, core team -- email or dashboard (1-2 pages): progress, metrics, issues, decisions needed (5-10 min read)
- **Monthly Executive Summary:** Executives, steering committee -- executive summary with visuals: high-level status, key wins, major risks, budget/timeline (2-3 min read)
- **3P Updates:** Leadership, cross-functional teams -- Progress, Plans, Problems format (30-60 seconds to read). Data-driven, matter-of-fact tone, 1-3 sentences per section.

**RAG Status indicators:**
- **Green:** On track, no concerns
- **Yellow/Amber:** Minor issues, being managed, may need attention
- **Red:** Significant problems, intervention needed

**Standard weekly status structure:**
```
PROJECT: [Project Name]
REPORTING PERIOD: [Date Range]
OVERALL STATUS: [Green/Yellow/Red]

## EXECUTIVE SUMMARY
[One sentence on overall status, one on key progress, one on concerns]

## PROGRESS THIS PERIOD
[Completed items and in-progress items with percentages]

## KEY METRICS
- Budget: $X spent of $Y (Z%)
- Timeline: Week X of Y
- Velocity: [sprint velocity vs target]
- Quality: [test coverage, defect rate]

## WINS & HIGHLIGHTS
[Notable achievements and milestones reached]

## ISSUES & RISKS (Top 3)
[Issue, status, owner, impact, mitigation]

## DECISIONS NEEDED
[Decision required, by when, from whom]

## UPCOMING NEXT PERIOD
[Key activities, milestones, deliverables]
```

### 4. Risk Management

Systematically identifies, analyzes, prioritizes, and mitigates project risks.

**Risk assessment process:**

1. **Identify risks** across categories:
   - Technical: unfamiliar technology, complex integrations, performance unknowns, technical debt
   - Schedule: aggressive timelines, external dependencies, holiday periods, competing priorities
   - Resource: team availability, skill gaps, budget constraints, vendor reliability
   - Scope: unclear requirements, stakeholder disagreement, scope creep
   - External: vendor delays, regulatory changes, market pressures

2. **Analyze each risk** using Probability x Impact matrix:
   ```
              LOW IMPACT    MEDIUM IMPACT    HIGH IMPACT
   HIGH PROB    Medium         High            Critical
   MED PROB     Low           Medium           High
   LOW PROB     Low            Low             Medium
   ```

3. **Develop mitigation strategies:**
   - **Avoidance:** eliminate the risk entirely (change approach, remove risky scope)
   - **Reduction:** decrease probability or impact (add buffers, build redundancy)
   - **Transfer:** shift to another party (outsource, use managed services)
   - **Acceptance:** acknowledge and plan for impact (contingency budget, communication plan)

4. **Apply root cause analysis** when risks materialize:
   - **5 Whys**: drill to root cause by asking "Why?" iteratively
   - **SWOT**: map strengths, weaknesses, opportunities, and threats

5. **Maintain risk register:**
   ```
   | ID | Risk | Prob | Impact | Score | Owner | Status | Mitigation | Review |
   ```

### 5. Stakeholder Management

Identifies, analyzes, and engages stakeholders using the Power/Interest Grid framework. Implements the full stakeholder-management skill from proagent project-manager.

**Stakeholder engagement:**

- **Power/Interest Grid:** classify stakeholders as Manage Closely, Keep Satisfied, Keep Informed, or Monitor
- **RACI Matrix:** define Responsible, Accountable, Consulted, Informed for key decisions
- **Communication cadence:** daily (critical team), weekly (active contributors), bi-weekly (interested parties), monthly (executives)
- **No Surprises rule:** share bad news early, provide context and options, never hide problems
- **Conflict resolution:** understand each perspective, find common ground, present options with trade-offs, escalate when needed

### 6. Meeting Facilitation and Agile Ceremonies

Runs effective meetings following the meeting-facilitation skill from proagent project-manager, with specific templates for agile ceremonies.

**Supported ceremony types:**

- **Daily Standup (15 min):** Yesterday, today, blockers. Anti-patterns to avoid: status report to manager, too much detail, problem-solving during standup, running over time.
- **Sprint Planning (90 min):** Sprint goal review, velocity/capacity check, backlog refinement, story estimation, sprint commitment.
- **Sprint Review (60 min):** Demo completed work, gather stakeholder feedback, update product backlog.
- **Sprint Retrospective (60 min):** Start-Stop-Continue framework. Set the stage (5 min), gather data (15 min), generate insights (15 min), decide actions (20 min), close (5 min).
- **Backlog Grooming (60 min):** Refine upcoming stories, add acceptance criteria, estimate, split large stories.

**Meeting facilitation best practices:**
- Send agenda 24 hours in advance with objectives, topics, time allocations, and pre-reading
- Start on time, confirm note-taker and timekeeper
- Time-box each topic, use parking lot for tangents
- Encourage quiet voices, manage dominant speakers
- Close with recap of decisions, action items (who/what/when), and next meeting

### 7. Resource Allocation

Balances team capacity across workstreams and projects to optimize delivery throughput.

**Resource allocation process:**
1. Map team skills and availability (capacity planning)
2. Identify workstream demands and priorities
3. Detect over-allocation or idle capacity
4. Apply Pareto analysis: focus team energy on highest-impact work
5. Flag key-person dependencies (bus factor risks)
6. Recommend rebalancing with trade-off analysis

### 8. Retrospective Analysis

Facilitates team learning through structured retrospective practices.

**Retrospective frameworks:**
- **Start-Stop-Continue**: What should we start, stop, and continue doing?
- **5 Whys Root Cause**: Drill to root cause of recurring problems
- **Inversion**: "What would guarantee failure?" then do the opposite
- **First Principles**: Break down process assumptions to fundamentals

**Retrospective output:**
```
SPRINT [X] RETROSPECTIVE

START:
- [New practice to adopt]

STOP:
- [Practice to eliminate]

CONTINUE:
- [Practice that is working well]

ACTION ITEMS:
| Action | Owner | Due Date |
|--------|-------|----------|

ROOT CAUSES IDENTIFIED:
- [5 Whys analysis of top issue]

EXPERIMENT FOR NEXT SPRINT:
- [One improvement to try and measure]
```

### 9. Standup Notes Generation

Generates AI-assisted daily standup notes by analyzing multiple data sources. Based on the standup-notes command from the `agents` repo (`plugins/team-collaboration/commands/standup-notes.md`).

**Data source orchestration:**
1. **Git commit history:** Parse recent commits (last 24-48h) using `git log --author="<user>" --since="yesterday"` to extract accomplishments grouped by feature area
2. **Jira tickets:** Query assigned tickets for status updates (`assignee = currentUser() AND status CHANGED TO "Done" DURING (-1d, now())`)
3. **Calendar events:** Include meeting context and time commitments via `mcp-gsuite`
4. **Local files:** Check `TO-DOS.md`, `CHANGELOG.md`, sprint backlog documents for task completions and meeting outcomes

**Standup note structure:**
```
# Standup - YYYY-MM-DD

## Yesterday / Last Update
- [Completed task] - [Jira ticket link if applicable]
- [Shipped feature/fix] - [PR link]
- [Meeting outcomes or decisions made]

## Today / Next
- [Continue work on X] - [Jira ticket] - [Expected completion]
- [Start new feature Y] - [Goal for today]
- [Code review for Z] - [PR link]

## Blockers / Notes
- [Blocker description] - **Needs:** [Help needed] - **From:** [Person/team]
- [Dependency] - **ETA:** [Expected resolution]
```

**Async standup patterns:**
- Written-only standups posted to Slack `#standup` channel at consistent daily times
- Thread-based standups with emoji reactions for acknowledgment
- Rolling 24-hour standup windows for distributed teams across timezones
- Auto-generated follow-up tasks from standup notes (blockers, deliverables, dependencies)

**Accomplishment quality criteria:**
- Focus on delivered value, not activity ("Shipped user auth" vs "Worked on auth")
- Include impact when known ("Fixed bug affecting 20% of users")
- Connect to team goals or sprint objectives

### 10. PRD Creation

Generates Product Requirements Documents from feature ideas and Jobs to be Done analysis. Based on the create-prd command from the `awesome-claude-code` repo (`resources/slash-commands/create-prd/create-prd.md`).

**PRD creation process:**
1. Read product documentation (`product-development/resources/product.md`) to understand product context
2. Read feature documentation (`product-development/current-feature/feature.md`) for the feature idea
3. Read JTBD documentation (`product-development/current-feature/JTBD.md`) for Jobs to be Done analysis
4. Apply PRD template to generate a structured requirements document capturing what, why, and how
5. Output PRD to `product-development/current-feature/PRD.md`

**Key principles:**
- Focus on product requirements and user needs, not technical implementation
- Do not include time estimates in the PRD
- Capture user stories, acceptance criteria, and success metrics
- Define scope boundaries and out-of-scope items

### 11. Internal Communications

Writes internal communications using company-standard formats. Based on the internal-comms skill from the `awesome-claude-skills` repo (`internal-comms/SKILL.md`).

**Supported communication types:**
- **3P updates:** Progress/Plans/Problems format for team updates -- 30-60 second read, data-driven, matter-of-fact tone
- **Company newsletters:** Company-wide updates with highlights, announcements, and recognition
- **FAQ responses:** Structured answers to frequently asked questions
- **Incident reports:** Post-incident documentation with timeline, impact, root cause, and remediation
- **Leadership updates:** Executive-level status and strategic alignment updates
- **Project updates:** Detailed project progress reports for active contributors

**Usage pattern:**
1. Identify the communication type from the request
2. Load the appropriate guideline (3P updates, newsletter, FAQ, or general comms format)
3. Follow specific formatting, tone, and content-gathering instructions for that type

### 12. Meeting Insights Analysis

Analyzes meeting transcripts to uncover communication patterns, behavioral insights, and actionable feedback. Based on the meeting-insights-analyzer skill from the `awesome-claude-skills` repo (`meeting-insights-analyzer/SKILL.md`).

**Analysis capabilities:**
- **Conflict avoidance detection:** Hedging language, indirect phrasing, subject changes when tension arises
- **Speaking ratios:** Percentage of meeting time speaking, interruption counts, turn-taking balance
- **Filler word tracking:** Frequency of "um", "uh", "like", "you know" per minute or per speaking turn
- **Active listening indicators:** Questions referencing others' points, paraphrasing, building on contributions
- **Leadership facilitation:** Decision-making approach, disagreement handling, inclusion of quieter participants

**Output format:**
```
# Meeting Insights Summary

Analysis Period: [Date range]
Meetings Analyzed: [X meetings]

## Key Patterns Identified
### 1. [Pattern]
- Observed: [What was seen]
- Impact: [Why it matters]
- Recommendation: [How to improve]

## Communication Strengths
## Growth Opportunities
## Speaking Statistics
## Next Steps
```

### 13. Todo Management

Captures and retrieves structured todo items with full context for later resumption. Based on the taches-cc todo commands from the `taches-cc-resources` repo (`commands/add-to-todos.md`, `commands/check-todos.md`, `commands/whats-next.md`).

**Add todo (`add-to-todos` pattern):**
1. Read `TO-DOS.md` in working directory (create if absent)
2. Check for duplicate todos before adding
3. Extract context from conversation: problem, file paths with line numbers, technical details, root cause
4. Append structured entry: `## Brief Context Title - YYYY-MM-DD HH:MM` with `- **[Action verb] [Component]** - Description. **Problem:** What's wrong. **Files:** path:line-range. **Solution:** Approach hints.`

**Check todos (`check-todos` pattern):**
1. Parse `TO-DOS.md` and display compact numbered list with dates
2. User selects a todo by number
3. Load full context: Problem, Files, Solution fields
4. Check for project workflows in `CLAUDE.md` and `.claude/skills/`
5. Present options: invoke matching skill, work directly, brainstorm approach, or put back

**Handoff documents (`whats-next` pattern):**
- Generates comprehensive handoff documents capturing: original task, work completed, work remaining, attempted approaches, critical context, and current state
- Enables continuing work in a fresh context with zero information loss
- Writes to `whats-next.md` in the current working directory

### 14. Agentic KPIs

Tracks AI effectiveness metrics for human-AI collaboration in delivery workflows. Based on the agentic-kpis framework from the `proagent-repo` (`core/skills/tac/agentic-kpis.md`).

**Core KPIs:**

| KPI | Definition | Target |
|-----|-----------|--------|
| Autonomy Rate | Tasks completed without human intervention | > 80% routine tasks |
| First-Pass Success | Tasks correct on first attempt | > 90% |
| Human Touch Points | Average human interventions per task | < 0.5 for standard tasks |
| Cycle Time | Average time from task start to completion | Simple fix < 5 min, Feature < 2 hours |
| Recovery Rate | Failures successfully self-corrected | > 80% |
| Code Quality Score | Composite of lint, coverage, maintainability, security | > 85/100 |

**Secondary KPIs:** Context Efficiency, Token Efficiency, Escalation Rate, Trust Progression Rate

**KPI-driven actions:**
- When Autonomy Rate drops: analyze intervention causes, identify missing context patterns, update agent prompts
- When First-Pass drops: review recent failures, identify requirement gaps, strengthen validation
- When Cycle Time increases: identify bottlenecks, check for blockers, optimize slow stages

**KPI targets by trust level:**
| KPI | Level 1 | Level 3 | Level 5 |
|-----|---------|---------|---------|
| Autonomy | 20% | 70% | 95% |
| First-Pass | 70% | 90% | 98% |
| HTP | 2.0 | 0.5 | 0.05 |

### 15. Task Planning with Phased Progress Tracking

Structures complex delivery tasks into phased plans with progress tracking. Based on the task_plan template from the `planning-with-files` repo (`skills/planning-with-files/templates/task_plan.md`).

**Task plan structure:**
1. **Goal:** One clear sentence describing the end state (north star reference)
2. **Current Phase:** Quick reference for active phase
3. **Phases** (3-7 logical phases):
   - Phase 1: Requirements & Discovery (understand intent, identify constraints, document findings)
   - Phase 2: Planning & Structure (define approach, create structure, document decisions)
   - Phase 3: Implementation (execute plan, write to files, test incrementally)
   - Phase 4: Testing & Verification (verify requirements, document results, fix issues)
   - Phase 5: Delivery (review output, ensure completeness, deliver)
4. **Key Questions:** Guide research and decision-making
5. **Decisions Made:** Table with Decision and Rationale columns
6. **Errors Encountered:** Table with Error, Attempt, and Resolution columns

**Phase status tracking:** `pending` -> `in_progress` -> `complete`

**Best practices:**
- Create the plan FIRST before starting any work
- Update phase status after each phase completes
- Re-read the plan before major decisions (attention manipulation)
- Log ALL errors to avoid repeating failed approaches

### 16. Eisenhower Matrix Prioritization

Applies the Eisenhower urgent/important matrix to prioritize tasks, backlogs, or decisions. Based on the eisenhower-matrix thinking model from the `taches-cc-resources` repo (`commands/consider/eisenhower-matrix.md`).

**Quadrant classification:**
- **Q1: Do First** (Important + Urgent) -- Items with deadline pressure that contribute to long-term goals. Include specific next action and deadline.
- **Q2: Schedule** (Important + Not Urgent) -- Strategic work without immediate pressure. Specify when to do it and why it matters long-term.
- **Q3: Delegate** (Not Important + Urgent) -- Time-sensitive but not goal-aligned. Identify who can handle it or how to minimize time spent.
- **Q4: Eliminate** (Not Important + Not Urgent) -- Noise items. Explicitly mark as droppable with rationale.

**Application to delivery:**
- Sprint backlog prioritization: classify stories across quadrants before commitment
- Risk register triage: map risks by urgency of mitigation vs. importance of impact
- Stakeholder request management: sort incoming requests to protect team focus
- Meeting agenda optimization: ensure ceremony time is spent on Q1/Q2 items

## AWOS Delivery Planning Patterns

The AWOS framework provides structured artifact templates for delivery planning:

### Project Artifacts
- **Product Vision** (`product.md`) — Problem statement, target audience, success metrics, and project rationale
- **Feature Roadmap** (`roadmap.md`) — Prioritized feature list with delivery phases, dependencies, and milestones
- **Architecture Decision** (`architecture.md`) — Technology stack selection, infrastructure design, and scaling considerations

### Milestone-Based Confirmation
The AWOS pattern of mandatory confirmation gates (Approve/Edit/Redo after each step) is recommended for any delivery planning workflow where stakeholder alignment is required between phases. This prevents autonomous runaway and ensures collaborative decision-making.

## Milestone-Based Confirmation Gates

For delivery planning workflows where stakeholder approval is required between phases, implement the mandatory confirmation pattern:

After each milestone deliverable (project charter, roadmap, architecture decision, sprint plan):
1. Present the deliverable to stakeholders
2. Explicitly request: **Approve** / **Request Changes** / **Redo**
3. Only proceed to the next phase after receiving approval

This ensures alignment at critical handoff points and creates a documented audit trail of planning decisions.

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate interactive diagrams directly in the conversation. Describe what you need in natural language and Excalidraw renders it as an interactive canvas with hand-drawn style.

### When to Use

- Project timeline and milestone diagrams
- Sprint flow and ceremony visualizations
- Stakeholder communication and RACI maps
- Risk and dependency matrix layouts

### Workflow

1. Describe the diagram you need — be specific about components, relationships, and layout
2. Review the rendered interactive diagram in the chat
3. Request refinements by describing what to change (add/remove/rearrange elements)
4. Use fullscreen mode for detailed editing when needed

### Tips for Effective Diagrams

- Name specific components and their connections (e.g., "API Gateway connects to Auth Service and User Service")
- Specify layout direction when it matters (e.g., "left-to-right flow" or "top-down hierarchy")
- Request specific diagram types (architecture diagram, flowchart, sequence diagram, ER diagram)
- Iterate — start with the overall structure, then refine details

## Composio App Automations

This plugin integrates with Composio-powered SaaS automation skills via the Rube MCP server. These skills connect to real external services for end-to-end workflow automation.

### Available Automations

| Skill | Service | Key Capabilities |
|-------|---------|-----------------|
| jira-automation | Jira | Sprint management, issue creation, backlog grooming, velocity tracking, burndown charts |
| linear-automation | Linear | Issue tracking, project management, cycle planning, team workflows |
| asana-automation | Asana | Task management, project tracking, timeline planning, workload balancing |
| clickup-automation | ClickUp | Task management, sprint planning, time tracking, goal setting |
| monday-automation | Monday.com | Work management, project tracking, dashboard creation, automations |
| confluence-automation | Confluence | Documentation publishing, meeting notes, retrospective records, knowledge base |
| trello-automation | Trello | Board management, card creation, workflow automation, checklist tracking |

### Usage Pattern

All Composio automations follow a three-step workflow:

1. **Discover tools**: Use `RUBE_SEARCH_TOOLS` with a use case description to find available tools and their schemas
2. **Connect service**: Use `RUBE_MANAGE_CONNECTIONS` to activate the toolkit connection (handles OAuth automatically)
3. **Execute actions**: Use `RUBE_MULTI_EXECUTE_TOOL` with the discovered tool slug and schema-compliant arguments

### Configuration

Add the Rube MCP server to your `.mcp.json`:
```json
"rube": {
  "url": "https://rube.app/mcp"
}
```

## Integration Points

- **Jira:** Sprint management, backlog grooming, issue tracking, velocity metrics, burndown charts
- **Confluence:** Meeting notes, project charters, risk registers, retrospective records, status dashboards
- **Slack:** Daily standups, 3P updates, blocker alerts, milestone notifications, stakeholder communications
- **Google Calendar:** Sprint ceremony scheduling, milestone due dates, stakeholder review cadence

## Workflow Summary

```
Charter --> Roadmap --> Sprint Plan --> Execute --> Track --> Report --> Review --> Retro
   |           |            |             |          |          |          |         |
   v           v            v             v          v          v          v         v
 Scope     Milestones    Backlog      Daily       Risk      Status    Stakeholder  Start-Stop
 define    & timeline    commit     standups    monitor    reports    feedback    Continue
```
