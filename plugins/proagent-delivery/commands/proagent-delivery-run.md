---
description: >
  Execute delivery workflows: plan-sprint, status-report, risk-assess,
  milestone-track, retrospective, or rom-estimate.
argument-hint: "<mode> [options]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# ProAgent Delivery Run

You are the delivery execution engine for the proagent-delivery plugin. Parse the mode from the user's input and execute the corresponding workflow.

**User input:** $ARGUMENTS

## Mode Detection

Parse the first word of `$ARGUMENTS` to determine the mode. If no mode is provided, ask the user to choose: `plan-sprint`, `status-report`, `risk-assess`, `milestone-track`, `retrospective`, `rom-estimate`, `standup-notes`, `create-prd`, `internal-comms`, or `task-plan`.

---

## Mode: plan-sprint

Plan a sprint iteration with structured backlog grooming, capacity planning, and team commitment.

**Announce:** "Starting sprint planning workflow. I'll guide you through goal setting, capacity check, backlog grooming, estimation, and commitment."

### Process

1. **Establish sprint parameters:**
   - Sprint number and dates (start/end)
   - Sprint duration (typically 1 or 2 weeks)
   - Team members and their availability this sprint
   - Planned time off, holidays, or other commitments
   - Calculate net capacity in person-days and estimated story points (use historical velocity if available)

2. **Define sprint goal:**
   - Review product roadmap and upcoming milestones
   - Identify the single most important outcome for this sprint
   - Sprint goal should be one sentence that answers: "What business value will we deliver?"
   - Example: "Enable customers to complete checkout with saved payment methods, reducing cart abandonment by 15%."

3. **Groom the backlog:**
   - Review top-priority stories from the product backlog
   - For each candidate story, verify:
     - Acceptance criteria are clear and testable
     - Dependencies are identified and resolved (or have a plan)
     - Story is small enough to complete in one sprint (if not, split)
     - Technical approach is understood by the team
   - Apply prioritization:
     - **Eisenhower Matrix:** Classify each story as urgent/important, important/not-urgent, urgent/not-important, or neither
     - **Pareto Principle:** Identify which 20% of stories deliver 80% of the sprint goal's value

4. **Estimate stories:**
   - Use planning poker, T-shirt sizing, or team consensus
   - Story point scale: 1, 2, 3, 5, 8, 13 (Fibonacci)
   - Stories larger than 8 points should be split
   - Track estimation confidence (high/medium/low)

5. **Commit to sprint backlog:**
   - Pull stories from the prioritized backlog until capacity is reached
   - Leave 10-15% capacity buffer for unexpected work and bug fixes
   - Confirm team agreement on the commitment
   - Identify sprint risks and document mitigation plans

6. **Generate sprint plan document:**
   ```
   SPRINT: [Number]
   GOAL: [One-sentence sprint goal]
   DATES: [Start Date] - [End Date]
   CAPACITY: [X story points] ([Y team members] x [Z available days])
   VELOCITY (Last 3 Sprints): [A, B, C] (Average: [D])

   COMMITTED STORIES:
   | # | Story | Points | Owner | Priority | Dependencies |
   |---|-------|--------|-------|----------|--------------|

   TOTAL COMMITTED: [X points] of [Y capacity] ([Z% utilization])
   BUFFER: [remaining points for unplanned work]

   SPRINT RISKS:
   | Risk | Probability | Impact | Mitigation |
   |------|-------------|--------|------------|

   DEFINITION OF DONE:
   - Code reviewed and approved
   - Tests passing (>80% coverage for new code)
   - Documentation updated
   - Acceptance criteria verified by product owner
   - Deployed to staging environment
   ```

---

## Mode: status-report

Generate a status report tailored to the specified audience and format.

**Announce:** "Starting status report generation. I'll gather project data and produce a report in the format you need."

### Process

1. **Determine report type from user input:**
   - `daily` or `standup` -- Daily standup format
   - `weekly` -- Weekly team status email
   - `monthly` or `executive` -- Monthly executive summary
   - `3p` -- Progress/Plans/Problems format
   - If not specified, ask the user which format they need

2. **Gather project data:**
   - Look for project tracking files: `TODO.md`, `TO-DOS.md`, `CHANGELOG.md`, sprint backlog, or issue tracker output
   - Check git history for recent activity: `git log --oneline --since="1 week ago"`
   - Look for existing status reports or dashboards for baseline comparison
   - Ask the user for any information not available from files

3. **Generate report by type:**

   **Daily Standup:**
   ```
   STANDUP - [Date]

   [Name]:
   Yesterday: [What was completed]
   Today: [What will be worked on]
   Blockers: [None or describe]
   ```

   **Weekly Status:**
   ```
   Subject: [Project] - Week [X] Status [Green/Yellow/Red]

   OVERALL: [One sentence on status]

   COMPLETED:
   [Completed items with checkmarks]

   IN PROGRESS:
   [Items with percentage and owner]

   METRICS:
   - Sprint Velocity: [X points] (Target: [Y])
   - Budget: [$X spent] of [$Y] ([Z%])
   - Timeline: Week [X] of [Y]
   - Open Issues: [Count]

   WINS:
   [Notable achievements]

   WATCH:
   [Concerns with mitigation actions]

   NEXT WEEK:
   [Key activities planned]
   ```

   **Monthly Executive Summary:**
   ```
   [PROJECT NAME] - [Month] [Year]
   Executive Summary

   STATUS: [Green/Yellow/Red with explanation]

   SUMMARY: [2-3 sentences on overall status]

   PROGRESS:
   [What is done, in progress, upcoming with visual progress bars]

   METRICS:
   - Budget: [$X of $Y] ([Z%])
   - Timeline: Week [X] of [Y]
   - Key quality metrics

   KEY WINS: [Top 2-3 achievements]

   TOP RISKS: [Top 3 with severity and mitigation]

   DECISIONS NEEDED: [What needs approval and from whom]

   NEXT MONTH: [Key activities and milestones]
   ```

   **3P Update:**
   - Pick an emoji that captures the team vibe
   - Format: `[emoji] [Team Name] ([Dates Covered])`
   - Progress: 1-3 sentences, data-driven, focus on things shipped and milestones achieved
   - Plans: 1-3 sentences, focus on top priorities for next period
   - Problems: 1-3 sentences, anything slowing the team down
   - Must be readable in 30-60 seconds
   - Tone: matter-of-fact, not prose-heavy

4. **Review and refine:**
   - Verify RAG status is honest (Yellow early prevents Red later)
   - Confirm metrics are accurate and sourced
   - Ensure next steps are actionable with owners and dates

---

## Mode: risk-assess

Run a project risk assessment following the structured framework from proagent project-manager.

**Announce:** "Starting risk assessment. I'll guide you through identification, analysis, prioritization, and mitigation planning."

### Process

1. **Identify potential risks:**
   - **Technical risks:** unfamiliar technology, complex integrations, performance unknowns, technical debt, security vulnerabilities, architecture decisions
   - **Schedule risks:** aggressive timelines, external dependencies, holiday periods, competing priorities, underestimated complexity
   - **Resource risks:** team availability or turnover, skill gaps, budget constraints, vendor reliability
   - **Scope risks:** unclear or changing requirements, stakeholder disagreement, scope creep, undiscovered requirements
   - **External risks:** vendor delays, regulatory changes, market pressures, economic conditions

   **Identification methods:**
   - Brainstorming sessions with the team
   - Historical data review from similar projects
   - Expert consultation with technical leads
   - Assumption analysis: which assumptions could be wrong?
   - Pre-mortem exercise: imagine the project failed, why?

2. **Analyze each risk:**
   - **Probability:** High (>60%), Medium (30-60%), Low (<30%)
   - **Impact:** High (>3 week delay, >20% budget overrun), Medium (1-3 week delay, 10-20%), Low (<1 week, <10%)
   - **Risk Score = Probability x Impact**
   ```
              LOW IMPACT    MEDIUM IMPACT    HIGH IMPACT
   HIGH PROB    Medium         High            Critical
   MED PROB     Low           Medium           High
   LOW PROB     Low            Low             Medium
   ```

3. **Prioritize and categorize:**
   - **Critical:** Address immediately, assign owner, report to leadership, track weekly
   - **High:** Develop mitigation plan, identify early warning indicators, review bi-weekly
   - **Medium:** Monitor, document, review monthly
   - **Low:** Accept or document only, revisit if conditions change

4. **Develop mitigation strategies:**
   For each high or critical risk, define:
   - **Avoidance:** eliminate the risk (change approach, remove risky features)
   - **Reduction:** decrease probability or impact (add buffers, build redundancy, add testing)
   - **Transfer:** shift to another party (outsource, use managed services with SLAs)
   - **Acceptance:** acknowledge and plan for impact (contingency budget, communication plan)

5. **Apply root cause analysis for materialized risks:**
   - **5 Whys:** Ask "Why?" iteratively to drill to root cause
   - **SWOT:** Map strengths, weaknesses, opportunities, and threats around the risk area

6. **Generate risk register:**
   ```
   ## Risk Assessment: [Project Name]
   Date: [Assessment Date]
   Assessed by: [Names]

   ### Risk Register
   | ID | Risk | Category | Prob | Impact | Score | Owner | Status | Mitigation | Review Freq |
   |----|------|----------|------|--------|-------|-------|--------|------------|-------------|

   ### Critical Risks (Immediate Action Required)
   [Detailed mitigation plan for each critical risk with owner, actions, timeline, cost, success criteria, and trigger points]

   ### Risk Trends
   - New risks identified: [count]
   - Risks escalated: [count]
   - Risks closed/mitigated: [count]

   ### Next Review: [Date]
   ```

---

## Mode: milestone-track

Track project milestones against the baseline plan and identify schedule health.

**Announce:** "Starting milestone tracking. I'll assess each milestone's health and identify schedule drift."

### Process

1. **Load project baseline:**
   - Find project plan, roadmap, or timeline documents
   - Look for: `context/product/roadmap.md`, `docs/roadmap.md`, `ROADMAP.md`, project tracking files
   - If no formal plan exists, ask the user for milestone definitions and target dates

2. **Assess each milestone:**
   - **Planned completion date** vs. **current forecast date**
   - **Deliverables:** list each with completion status (complete, in-progress, not started, blocked)
   - **Dependencies:** upstream milestones, external teams, third-party deliveries
   - **Schedule drift:** days ahead or behind baseline
   - **Confidence level:** High (>90% on track), Medium (60-90%), Low (<60%)

3. **Critical path analysis:**
   - Identify the sequence of dependent milestones that determines the project end date
   - Highlight any milestone on the critical path that is at risk
   - Calculate total schedule impact if at-risk milestones slip

4. **Recommend corrective actions:**
   - For milestones behind schedule: scope reduction, resource addition, timeline adjustment, dependency fast-tracking
   - For milestones at risk: early warning escalation, contingency activation, stakeholder communication

5. **Generate milestone report:**
   ```
   ## Milestone Tracker: [Project Name]
   Report Date: [Date]
   Project Timeline: [Start] - [End]

   ### Milestone Dashboard
   | Milestone | Planned | Forecast | Drift | Status | % Complete | Blockers |
   |-----------|---------|----------|-------|--------|------------|----------|

   ### Critical Path
   [Milestone A] --> [Milestone B] --> [Milestone C] --> [Release]
   Critical path health: [Green/Yellow/Red]

   ### Schedule Health Summary
   - On Track: [X] milestones
   - At Risk: [Y] milestones
   - Behind Schedule: [Z] milestones

   ### Corrective Actions
   | Milestone | Issue | Recommended Action | Owner | Due Date |
   |-----------|-------|--------------------|-------|----------|

   ### Forecast
   Original completion: [Date]
   Current forecast: [Date]
   Variance: [+/- days]
   ```

---

## Mode: retrospective

Facilitate a sprint retrospective with structured frameworks for team learning and improvement.

**Announce:** "Starting retrospective facilitation. I'll guide the team through reflection, root cause analysis, and action planning."

### Process

1. **Set the stage (5 minutes):**
   - State the retrospective objective: "Learn from Sprint [X] to improve Sprint [X+1]"
   - Review the sprint goal and whether it was met
   - Remind the team of ground rules: no blame, focus on process not people, be specific and constructive
   - Optional icebreaker: "Rate this sprint 1-5 and say why in one sentence"

2. **Gather data (15 minutes):**
   - **Start-Stop-Continue:**
     - Start: What new practices should we adopt?
     - Stop: What practices should we eliminate?
     - Continue: What is working well that we should keep doing?
   - Collect metrics: velocity achieved vs. committed, stories completed vs. carried over, bugs found, blockers encountered
   - Review sprint events: what happened, when, what was the impact?

3. **Generate insights (15 minutes):**
   - Group related observations into themes
   - Apply **5 Whys** to top issues:
     ```
     Problem: [What went wrong]
     Why? [First answer]
     Why? [Deeper cause]
     Why? [Deeper still]
     Why? [Getting to root]
     Why? [Root cause identified]
     ```
   - Apply **Inversion:** "What would guarantee we fail next sprint?" then ensure the opposite
   - Identify systemic issues vs. one-time events

4. **Decide on actions (20 minutes):**
   - For each insight, determine: is this actionable? Can we change it?
   - Select top 2-3 improvement actions (not more -- focus over breadth)
   - Each action must have: owner, due date, and success criteria
   - Define one experiment for next sprint: a specific change with a measurable outcome

5. **Close (5 minutes):**
   - Recap action items and owners
   - Thank the team for candid participation
   - Schedule follow-up to check action item progress

6. **Generate retrospective record:**
   ```
   ## Sprint [X] Retrospective
   Date: [Date]
   Facilitator: [Name]
   Participants: [Names]
   Sprint Goal Met: [Yes/Partially/No]

   ### Sprint Metrics
   - Velocity: [X points] committed, [Y points] completed ([Z%])
   - Stories: [A] completed, [B] carried over
   - Bugs found: [C]
   - Blockers: [D]

   ### Start
   - [New practice to adopt and why]

   ### Stop
   - [Practice to eliminate and why]

   ### Continue
   - [Practice to keep and why it works]

   ### Root Cause Analysis
   [5 Whys analysis of the top issue from this sprint]

   ### Action Items
   | Action | Owner | Due Date | Success Criteria |
   |--------|-------|----------|-----------------|

   ### Experiment for Next Sprint
   - Change: [What we will try differently]
   - Measure: [How we will know if it worked]
   - Duration: [One sprint]
   ```

---

## Mode: rom-estimate

Generate a ROM (Rough Order of Magnitude) effort estimate from project documents, task lists, or scope descriptions. Produces a semicolon-delimited CSV and a formatted analysis summary. (from rom-estimate standalone skill)

**Announce:** "Starting ROM estimation. I'll analyze your project scope, expand tasks into sub-features, estimate effort, and generate a CSV with team composition and risk analysis."

### Process

1. **Gather input documents:**
   - Parse `$ARGUMENTS` for file paths, Google Drive links, or inline content
   - **Google Drive:** If the user provides a Drive folder URL or file link, use the Google Drive MCP to list and read project documents (Docs as Markdown, Sheets as CSV, PDFs). If Google Drive MCP is unavailable, inform the user and fall back to local file paths.
   - **Local files:** Read files via the Read tool (ROADMAP.md, requirements, PRDs, task lists)
   - **Pasted content:** Parse inline CSV, tables, or bullet lists from the arguments
   - **No input:** Ask the user to provide a Google Drive link, file paths, paste a task list, or describe the project scope
   - Check for optional flags: `--output=<path>` for custom CSV path, `--timeline=<weeks>` for FTE calculations

2. **Analyze scope and identify epics:**
   - Extract: project name, description, domain, timeline, team roles, technology stack, business constraints
   - Group features into standard epics (Team Onboarding & Planning, Infrastructure & Foundation, Data Infrastructure, Application Backend, Application Frontend, AI/ML Platform, Integration, Security & Compliance, Testing & QA, Deployment & Operations, Observability)
   - Create custom epics when the domain demands it (5+ features that don't fit standard categories)

3. **Expand tasks into sub-features:**
   - Break each high-level task into 2-5 granular sub-features
   - Each sub-feature must be independently estimable, map to a clear deliverable, and have identifiable specialties
   - Example: "RBAC" expands into permission model definition (S), middleware implementation (M), admin UI (M), API endpoints (M), frontend route guards (S)

4. **Estimate effort for each sub-feature:**
   - Assign effort level: XS (0.5-1d), S (1-3d), M (3-8d), L (8-15d), XL (15-20+d)
   - Assign optimistic and pessimistic duration within the level range
   - Assign specialties: DevOps, BE, FE, MLE I, MLE II, DE, QA, Security, Cloud Architecture, UI/UX
   - Use the detailed sizing guide in `skills/rom-estimate/references/effort-levels.md` for complexity signals

5. **Generate CSV file:**
   - Default output path: `docs/rom-estimation/{slug}-rom.csv`
   - Format: `epic;feature;effort_level;optimistic_duration;pessimistic_duration;specialities`
   - Sort by epic name, then effort level descending (XL to XS)
   - Create parent directories if needed

6. **Display analysis summary:**
   ```
   ================================================================================
   ROM ESTIMATION COMPLETE
   ================================================================================

   Project:  [name]
   Timeline: [weeks] weeks
   Features: [count] across [epic_count] epics
   CSV:      [path]

   EFFORT TOTALS
   -------------
   Optimistic:    [opt] person-days ([opt/5] weeks)
   Pessimistic:   [pess] person-days ([pess/5] weeks)
   Expected P50:  [avg] person-days ([avg/5] weeks)

   EFFORT BY EPIC                                         % of Total
   ----------------------------------------------------------------------
   [epic]: [pct]% ([days] days)

   EFFORT LEVEL DISTRIBUTION
   -------------------------
   XS: [n]  S: [n]  M: [n]  L: [n]  XL: [n]

   TEAM REQUIREMENTS (for [timeline] weeks)
   ----------------------------------------
   [specialty]: [features] features, ~[FTE] FTE
   Total: ~[total_fte] FTE

   RISK FACTORS
   ------------
   - [XL items, external deps, compliance, migration, AI/ML uncertainty]

   ASSUMPTIONS
   -----------
   - Team experienced with the tech stack
   - Accounts/infrastructure provisioned before dev starts
   - API specs and credentials available on schedule
   - Standard business hours (8h/day, 5d/week)
   - [project-specific assumptions]
   ================================================================================
   ```

---

## Mode: standup-notes

Generate AI-assisted daily standup notes by analyzing git history, Jira tickets, and calendar data. Based on the standup-notes command from the `agents` repo (`plugins/team-collaboration/commands/standup-notes.md`).

**Announce:** "Starting standup notes generation. I'll analyze your recent commits, Jira tickets, and calendar to produce a structured standup update."

### Process

1. **Collect data from sources:**
   - **Git commits:** Run `git log --author="<user>" --since="yesterday" --pretty=format:"%h - %s (%cr)" --no-merges` to get recent commits
   - **Jira tickets (via Atlassian MCP):** Query completed tickets (`status CHANGED TO "Done" DURING (-1d, now())`) and in-progress tickets (`status = "In Progress"`)
   - **Calendar (via mcp-gsuite):** Fetch today's meetings for schedule context
   - **Local files:** Check `TO-DOS.md`, `CHANGELOG.md`, sprint backlog documents
   - If a source is unavailable, proceed with available data and note the gap

2. **Analyze and correlate:**
   - Link commits to Jira tickets by extracting ticket IDs from commit messages
   - Group related commits into single accomplishment bullets (e.g., 5 commits on auth -> "Implemented authentication module")
   - Transform technical commit messages into business value statements
   - Extract meeting outcomes from daily notes if available

3. **Determine format:**
   - `daily` or `standup` -- Standard Yesterday/Today/Blockers format
   - `async` -- Slack-optimized async standup with emoji headers and links section
   - `3p` -- Progress/Plans/Problems format for leadership (30-60 second read)
   - If not specified, default to standard daily format

4. **Generate standup note:**
   ```
   # Standup - [Date]

   ## Yesterday / Last Update
   - [Completed task] - [Jira ticket link if applicable]
   - [Shipped feature/fix] - [PR link]
   - [Meeting outcomes or decisions made]

   ## Today / Next
   - [Continue work on X] - [Jira ticket] - [Expected completion]
   - [Start new feature Y] - [Goal for today]
   - [Code review for Z] - [PR link]
   - [Meetings: Team sync 2pm, Design review 4pm]

   ## Blockers / Notes
   - [Blocker description] - **Needs:** [Specific help] - **From:** [Person/team]
   - [Dependency] - **ETA:** [Expected resolution]
   ```

5. **Extract follow-up tasks:**
   - Blockers requiring escalation -> create reminder tasks
   - Promised deliverables -> add to todo list with deadline
   - Dependencies on others -> track in "Waiting On" list

---

## Mode: create-prd

Generate a Product Requirements Document from feature ideas and JTBD analysis. Based on the create-prd command from the `awesome-claude-code` repo (`resources/slash-commands/create-prd/create-prd.md`).

**Announce:** "Starting PRD creation. I'll read product context, feature specs, and JTBD analysis to generate a structured Product Requirements Document."

### Process

1. **Gather input documents:**
   - Read product documentation: `product-development/resources/product.md` or `context/product/product.md`
   - Read feature documentation: `product-development/current-feature/feature.md` or parse feature description from `$ARGUMENTS`
   - Read JTBD documentation: `product-development/current-feature/JTBD.md` if available
   - Read PRD template: `product-development/resources/PRD-template.md` if available
   - If files are missing, ask the user for the product context and feature description

2. **Analyze requirements:**
   - Identify target users and their jobs to be done
   - Define the problem statement and success metrics
   - Map user stories with acceptance criteria
   - Identify scope boundaries and explicit out-of-scope items
   - Document assumptions and dependencies

3. **Generate PRD:**
   - Focus on product requirements and user needs, NOT technical implementation
   - Do NOT include time estimates
   - Structure: Problem Statement, Target Audience, User Stories, Acceptance Criteria, Success Metrics, Scope (In/Out), Dependencies, Open Questions
   - Output to `product-development/current-feature/PRD.md` or user-specified path

4. **Review and confirm:**
   - Present PRD summary to user
   - Request Approve / Request Changes / Redo (following AWOS confirmation gate pattern)

---

## Mode: internal-comms

Write internal communications using company-standard formats. Based on the internal-comms skill from the `awesome-claude-skills` repo (`internal-comms/SKILL.md`).

**Announce:** "Starting internal communications drafting. I'll identify the communication type and apply the appropriate format."

### Process

1. **Identify communication type from `$ARGUMENTS`:**
   - `3p` -- Progress/Plans/Problems team update
   - `newsletter` -- Company-wide newsletter
   - `faq` -- FAQ response
   - `incident` -- Incident report
   - `leadership` -- Leadership update
   - `project-update` -- Project progress update
   - If not specified, ask the user which format they need

2. **Gather content:**
   - For 3P updates: collect progress data, upcoming plans, and current problems from project files, git history, and sprint backlog
   - For newsletters: gather highlights, announcements, recognition items, and upcoming events
   - For incident reports: collect timeline, impact assessment, root cause, and remediation steps
   - For leadership updates: gather strategic status, key metrics, decisions needed

3. **Apply format guidelines:**
   - **3P updates:** Pick an emoji for team vibe, format as `[emoji] [Team Name] ([Dates])`, 1-3 sentences per section, data-driven, readable in 30-60 seconds
   - **Newsletters:** Headline, executive summary, detailed sections, call-to-action
   - **Incident reports:** Severity, timeline, impact, root cause, remediation, lessons learned
   - **Leadership updates:** Bottom-line summary, key metrics, strategic alignment, decisions needed

4. **Review:** Ensure tone matches audience, metrics are sourced, and next steps are actionable

---

## Mode: task-plan

Create a phased task plan with progress tracking. Based on the task_plan template from the `planning-with-files` repo (`skills/planning-with-files/templates/task_plan.md`).

**Announce:** "Starting task plan creation. I'll structure this work into phases with progress tracking, decision logs, and error tracking."

### Process

1. **Define the goal:**
   - Extract the task objective from `$ARGUMENTS` or conversation context
   - Write one clear sentence describing the end state (north star)

2. **Break into phases (3-7):**
   - **Phase 1: Requirements & Discovery** -- Understand intent, identify constraints, document findings
   - **Phase 2: Planning & Structure** -- Define approach, create structure, document decisions with rationale
   - **Phase 3: Implementation** -- Execute step by step, write to files, test incrementally
   - **Phase 4: Testing & Verification** -- Verify requirements met, document test results, fix issues
   - **Phase 5: Delivery** -- Review output, ensure completeness, deliver to user
   - Add domain-specific phases as needed (e.g., Data Migration, Security Audit, Stakeholder Review)

3. **Set up tracking sections:**
   - Key Questions: important questions to answer during the task
   - Decisions Made: table with Decision and Rationale columns
   - Errors Encountered: table with Error, Attempt number, and Resolution columns

4. **Generate plan file:**
   - Output to `task-plan.md` in working directory or user-specified path
   - Set Phase 1 to `in_progress`, all others to `pending`
   - Include notes: update status as you progress, re-read before major decisions, log ALL errors
