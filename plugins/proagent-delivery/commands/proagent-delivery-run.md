---
description: >
  Execute delivery workflows: plan-sprint, status-report, risk-assess,
  milestone-track, or retrospective.
argument-hint: "<mode> [options]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# ProAgent Delivery Run

You are the delivery execution engine for the proagent-delivery plugin. Parse the mode from the user's input and execute the corresponding workflow.

**User input:** $ARGUMENTS

## Mode Detection

Parse the first word of `$ARGUMENTS` to determine the mode. If no mode is provided, ask the user to choose: `plan-sprint`, `status-report`, `risk-assess`, `milestone-track`, or `retrospective`.

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
   - `3p` -- Progress/Plans/Problems format (from awesome-claude-skills/internal-comms)
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

   **Weekly Status (from proagent/roles/project-manager/skills/status-reporting):**
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

   **3P Update (from awesome-claude-skills/internal-comms/examples/3p-updates):**
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

1. **Identify potential risks (from proagent/roles/project-manager/skills/risk-assessment):**
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
   - **5 Whys (from taches-cc-resources):** Ask "Why?" iteratively to drill to root cause
   - **SWOT (from taches-cc-resources):** Map strengths, weaknesses, opportunities, and threats around the risk area

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
   - **Start-Stop-Continue (from proagent/roles/project-manager/skills/meeting-facilitation):**
     - Start: What new practices should we adopt?
     - Stop: What practices should we eliminate?
     - Continue: What is working well that we should keep doing?
   - Collect metrics: velocity achieved vs. committed, stories completed vs. carried over, bugs found, blockers encountered
   - Review sprint events: what happened, when, what was the impact?

3. **Generate insights (15 minutes):**
   - Group related observations into themes
   - Apply **5 Whys (from taches-cc-resources/commands/consider/5-whys)** to top issues:
     ```
     Problem: [What went wrong]
     Why? [First answer]
     Why? [Deeper cause]
     Why? [Deeper still]
     Why? [Getting to root]
     Why? [Root cause identified]
     ```
   - Apply **Inversion (from taches-cc-resources/commands/consider/inversion):** "What would guarantee we fail next sprint?" then ensure the opposite
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
