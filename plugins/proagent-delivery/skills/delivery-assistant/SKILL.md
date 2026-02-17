---
name: delivery-assistant
description: Use when managing project delivery -- sprint planning, milestones, stakeholder updates, status reports, risk management, timelines, resource allocation, agile/scrum ceremonies, and retrospectives
---

# Managing Project Delivery

## Overview

This skill orchestrates all aspects of project delivery from sprint planning through retrospectives. It draws on proven patterns from proagent project-manager roles (meeting facilitation, risk assessment, status reporting, stakeholder management, spec creation), awesome-claude-skills internal-comms (3P updates, newsletters, leadership communications), taches-cc-resources (Eisenhower matrix prioritization, Pareto analysis, 5 Whys root cause, SWOT mapping, todo management), and awos (product definition, roadmap planning).

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

## Capabilities

### 1. Sprint Planning

Guides teams through structured sprint planning following agile/scrum practices. Combines the proagent project-manager meeting-facilitation skill with taches-cc-resources prioritization frameworks.

**Sprint planning process:**
1. Review sprint goal and align with product roadmap milestones
2. Check team capacity: available days, velocity history, planned time off
3. Groom backlog: clarify acceptance criteria, estimate story points, identify dependencies
4. Apply prioritization frameworks:
   - **Eisenhower Matrix** (from taches-cc-resources/commands/consider/eisenhower-matrix): urgent/important quadrant classification
   - **Pareto Analysis** (from taches-cc-resources/commands/consider/pareto): identify the 20% of work that delivers 80% of value
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

Generates status reports tailored to different audiences and frequencies. Implements the full status-reporting skill from proagent project-manager and the 3P update format from awesome-claude-skills internal-comms.

**Report types and audiences (from proagent/roles/project-manager/skills/status-reporting):**

- **Daily Standup (Written):** Team members -- bullet points: yesterday, today, blockers (2 min per person)
- **Weekly Status:** Direct manager, core team -- email or dashboard (1-2 pages): progress, metrics, issues, decisions needed (5-10 min read)
- **Monthly Executive Summary:** Executives, steering committee -- executive summary with visuals: high-level status, key wins, major risks, budget/timeline (2-3 min read)
- **3P Updates (from awesome-claude-skills/internal-comms/examples/3p-updates):** Leadership, cross-functional teams -- Progress, Plans, Problems format (30-60 seconds to read). Data-driven, matter-of-fact tone, 1-3 sentences per section.

**RAG Status indicators:**
- **Green:** On track, no concerns
- **Yellow/Amber:** Minor issues, being managed, may need attention
- **Red:** Significant problems, intervention needed

**Standard weekly status structure (from proagent/roles/project-manager/skills/status-reporting):**
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

Systematically identifies, analyzes, prioritizes, and mitigates project risks. Implements the full risk-assessment skill from proagent project-manager with the 5 Whys root cause analysis and SWOT mapping from taches-cc-resources.

**Risk assessment process (from proagent/roles/project-manager/skills/risk-assessment):**

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
   - **5 Whys** (from taches-cc-resources/commands/consider/5-whys): drill to root cause by asking "Why?" iteratively
   - **SWOT** (from taches-cc-resources/commands/consider/swot): map strengths, weaknesses, opportunities, and threats

5. **Maintain risk register:**
   ```
   | ID | Risk | Prob | Impact | Score | Owner | Status | Mitigation | Review |
   ```

### 5. Stakeholder Management

Identifies, analyzes, and engages stakeholders using the Power/Interest Grid framework. Implements the full stakeholder-management skill from proagent project-manager.

**Stakeholder engagement (from proagent/roles/project-manager/skills/stakeholder-management):**

- **Power/Interest Grid:** classify stakeholders as Manage Closely, Keep Satisfied, Keep Informed, or Monitor
- **RACI Matrix:** define Responsible, Accountable, Consulted, Informed for key decisions
- **Communication cadence:** daily (critical team), weekly (active contributors), bi-weekly (interested parties), monthly (executives)
- **No Surprises rule:** share bad news early, provide context and options, never hide problems
- **Conflict resolution:** understand each perspective, find common ground, present options with trade-offs, escalate when needed

### 6. Meeting Facilitation and Agile Ceremonies

Runs effective meetings following the meeting-facilitation skill from proagent project-manager, with specific templates for agile ceremonies.

**Supported ceremony types (from proagent/roles/project-manager/skills/meeting-facilitation):**

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

Facilitates team learning through structured retrospective practices, drawing on both the meeting-facilitation skill and the inversion mental model from taches-cc-resources.

**Retrospective frameworks:**
- **Start-Stop-Continue** (from proagent/roles/project-manager/skills/meeting-facilitation): What should we start, stop, and continue doing?
- **5 Whys Root Cause** (from taches-cc-resources/commands/consider/5-whys): Drill to root cause of recurring problems
- **Inversion** (from taches-cc-resources/commands/consider/inversion): "What would guarantee failure?" then do the opposite
- **First Principles** (from taches-cc-resources/commands/consider/first-principles): Break down process assumptions to fundamentals

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
