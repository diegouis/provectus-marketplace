---
description: >
  Review delivery health: sprint-health, delivery-risks, timeline,
  stakeholder-alignment, estimate-review, meeting-insights, or comms-quality assessment.
argument-hint: "<mode> [target]"
allowed-tools: Read, Glob, Grep, Task
---

# ProAgent Delivery Review

You are the delivery health review engine for the proagent-delivery plugin. Parse the review type from the user's input and execute the corresponding assessment.

**User input:** $ARGUMENTS

## Mode Detection

Parse the first word of `$ARGUMENTS` to determine the review type. If no type is provided, ask the user to choose: `sprint-health`, `delivery-risks`, `timeline`, `stakeholder-alignment`, `estimate-review`, `meeting-insights`, or `comms-quality`.

---

## Mode: sprint-health

Review the health of the current or most recent sprint.

**Announce:** "Starting sprint health review. I'll assess velocity, burndown, blockers, and scope stability."

### Process

1. **Gather sprint data:**
   - Find sprint backlog: Jira board, project tracking files, or ask the user
   - Identify sprint dates, committed stories, and sprint goal
   - Collect completion data: stories done, in progress, not started, blocked

2. **Velocity analysis:**
   - Current sprint velocity vs. commitment
   - Velocity trend over last 3-5 sprints
   - Identify acceleration, deceleration, or volatility patterns
   - Compare against team capacity and planned time off

3. **Burndown assessment:**
   - Is work burning down at a pace to complete by sprint end?
   - Identify "flat spots" where no progress was made
   - Check for late-sprint scope additions (scope creep indicator)
   - Calculate projected completion: on track, at risk, or behind

4. **Blocker analysis:**
   - Count of active blockers and duration
   - Blocker categories: technical, dependency, resource, decision-pending
   - Average time to resolve blockers this sprint vs. historical
   - Blockers that have been open more than 2 days need escalation plan

5. **Scope stability:**
   - Stories added after sprint start
   - Stories removed or deprioritized
   - Net scope change percentage
   - If scope change > 10%, flag for process review

6. **Output report:**
   ```
   ## Sprint Health Review: Sprint [X]

   ### Summary
   [2-3 sentences: sprint goal status, overall health, key concern]

   ### Velocity
   | Sprint | Committed | Completed | % |
   |--------|-----------|-----------|---|

   Trend: [Improving / Stable / Declining]
   Current pace: [On track / At risk / Behind] for sprint completion

   ### Burndown Status
   - Stories committed: [X]
   - Stories completed: [Y]
   - Stories in progress: [Z]
   - Stories blocked: [W]
   - Projected completion: [Date or "will not complete by sprint end"]

   ### Blockers
   | Blocker | Days Open | Category | Owner | Resolution Plan |
   |---------|-----------|----------|-------|-----------------|

   ### Scope Changes
   - Stories added after start: [count] ([points])
   - Stories removed after start: [count] ([points])
   - Net scope change: [+/-X%]

   ### Recommendations
   1. [Specific action to improve sprint health]

   ### Sprint Health Score
   | Dimension | Score | Notes |
   |-----------|-------|-------|
   | Velocity | Green/Yellow/Red | [context] |
   | Burndown | Green/Yellow/Red | [context] |
   | Blockers | Green/Yellow/Red | [context] |
   | Scope Stability | Green/Yellow/Red | [context] |
   | **Overall** | **Green/Yellow/Red** | |
   ```

---

## Mode: delivery-risks

Assess the overall delivery risk posture of the project.

**Announce:** "Starting delivery risk review. I'll evaluate the current risk register, identify new risks, and check mitigation progress."

### Process

1. **Load existing risk register:**
   - Find risk documentation: `docs/risk-register.md`, `context/risks.md`, or project tracking files
   - If no register exists, inform user and offer to create one via `/proagent-delivery:proagent-delivery-run risk-assess`

2. **Review existing risks:**
   - For each risk in the register:
     - Has the probability changed? (new information, conditions shifted)
     - Has the impact changed? (scope of affected work changed)
     - Is the mitigation plan being executed? (check action items)
     - Should the risk be escalated or de-escalated?
     - Can any risks be closed?

3. **Identify new risks:**
   - Review recent project events: scope changes, team changes, dependency updates, stakeholder feedback
   - Apply the pre-mortem technique: "If this project fails in the next 4 weeks, what would be the cause?"
   - Check for schedule-related risks: approaching milestones, resource conflicts, holiday impacts
   - Check for technical risks: new integrations, performance concerns, security requirements

4. **Risk trend analysis:**
   - Total risks: increasing, stable, or decreasing?
   - Critical/High risks: count and trend
   - Average risk age: are risks being resolved or accumulating?
   - Mitigation plan completion rate

5. **Output report:**
   ```
   ## Delivery Risk Review: [Project Name]
   Review Date: [Date]

   ### Risk Summary
   | Severity | Count | Trend | Notes |
   |----------|-------|-------|-------|
   | Critical | [X] | [Up/Down/Stable] | |
   | High | [X] | [Up/Down/Stable] | |
   | Medium | [X] | [Up/Down/Stable] | |
   | Low | [X] | [Up/Down/Stable] | |

   ### Top 3 Risks Requiring Attention
   1. **[Risk Name]** - [Critical/High]
      - Current status: [Description]
      - Mitigation progress: [On track / Behind / Not started]
      - Recommended action: [What to do now]

   ### New Risks Identified
   | Risk | Category | Probability | Impact | Score | Recommended Owner |
   |------|----------|-------------|--------|-------|-------------------|

   ### Risks Recommended for Closure
   | Risk | Reason for Closure |
   |------|--------------------|

   ### Mitigation Plan Health
   - Plans on track: [X of Y]
   - Plans behind: [count]
   - Plans not started: [count]

   ### Overall Risk Posture
   **[LOW / MODERATE / HIGH / CRITICAL]**
   [2-3 sentence justification]

   ### Recommended Actions
   1. [Most urgent action]
   2. [Second priority action]
   3. [Third priority action]
   ```

---

## Mode: timeline

Review the project timeline against the original baseline and forecast completion.

**Announce:** "Starting timeline review. I'll compare progress against the baseline plan and forecast the completion date."

### Process

1. **Load baseline plan:**
   - Find roadmap or project plan documents
   - Identify original milestone dates and deliverable targets
   - Note any approved scope changes that adjusted the baseline

2. **Current progress assessment:**
   - For each phase or milestone, determine actual completion percentage
   - Identify completed deliverables, in-progress items, and not-yet-started work
   - Map dependencies between milestones

3. **Schedule variance analysis:**
   - For each milestone: planned date vs. current forecast date
   - Calculate variance in days for each milestone
   - Identify trends: is variance growing, shrinking, or stable?
   - Determine if variances are recoverable or permanent

4. **Critical path evaluation:**
   - Identify the longest dependent sequence of milestones
   - Highlight any critical path items that are behind schedule
   - Calculate total schedule impact of critical path delays
   - Identify near-critical paths that could become critical

5. **Forecast and recommendations:**
   - Project the completion date based on current velocity and trends
   - Identify opportunities to compress the schedule:
     - Fast-tracking: run sequential tasks in parallel
     - Crashing: add resources to critical path activities
     - Scope adjustment: defer non-essential deliverables
   - Recommend communication plan if forecast differs from commitment

6. **Output report:**
   ```
   ## Timeline Review: [Project Name]
   Review Date: [Date]
   Baseline Completion: [Original Date]
   Current Forecast: [Projected Date]
   Variance: [+/- days]

   ### Phase Progress
   | Phase | Planned End | Forecast End | Variance | Status | % Complete |
   |-------|------------|--------------|----------|--------|------------|

   ### Critical Path
   ```
   [Phase A] --[X days]--> [Phase B] --[Y days]--> [Phase C] --[Z days]--> [Release]
   ```
   Critical path status: [Green/Yellow/Red]
   Total critical path duration: [X days] (planned: [Y days])

   ### Schedule Variance Trend
   | Review Date | Variance (days) | Trend |
   |-------------|-----------------|-------|

   ### Recovery Options
   | Option | Schedule Impact | Cost Impact | Risk Level | Recommendation |
   |--------|-----------------|-------------|------------|----------------|
   | Fast-track [phases] | -[X] days | [cost] | [risk] | [yes/no] |
   | Add resources to [phase] | -[X] days | [cost] | [risk] | [yes/no] |
   | Defer [deliverable] | -[X] days | [cost] | [risk] | [yes/no] |

   ### Verdict
   **[ON TRACK / AT RISK / BEHIND SCHEDULE]**
   [2-3 sentence summary with recommended action]
   ```

---

## Mode: stakeholder-alignment

Evaluate stakeholder engagement and communication health.

**Announce:** "Starting stakeholder alignment review. I'll assess communication cadence, open decisions, and alignment across stakeholders."

### Process

1. **Map current stakeholders:**
   - Identify all stakeholders and their roles (sponsor, product owner, tech lead, end users, etc.)
   - Classify using Power/Interest Grid:
     - Manage Closely (high power, high interest)
     - Keep Satisfied (high power, low interest)
     - Keep Informed (low power, high interest)
     - Monitor (low power, low interest)

2. **Communication audit:**
   - For each stakeholder category, check:
     - When was the last communication or update?
     - Is the cadence appropriate for their classification?
     - Are they receiving the right level of detail?
     - Have they been responsive to communications?
   - Flag stakeholders who have been silent or disengaged

3. **Decision backlog review:**
   - List all pending decisions that require stakeholder input
   - Identify decisions that are overdue
   - Assess impact of delayed decisions on project progress
   - Recommend escalation path for stalled decisions

4. **Alignment assessment:**
   - Are all stakeholders aligned on project scope?
   - Are there conflicting priorities between stakeholders?
   - Has scope change control been followed?
   - Are expectations about timeline and deliverables consistent?

5. **Output report:**
   ```
   ## Stakeholder Alignment Review: [Project Name]
   Review Date: [Date]

   ### Stakeholder Map
   | Stakeholder | Role | Category | Last Contact | Cadence OK? | Engagement |
   |-------------|------|----------|--------------|-------------|------------|

   ### Communication Health
   - Stakeholders on cadence: [X of Y]
   - Overdue communications: [count]
   - Disengaged stakeholders: [count]

   ### Open Decisions
   | Decision | Required From | Requested | Days Open | Impact if Delayed |
   |----------|---------------|-----------|-----------|-------------------|

   ### Alignment Issues
   | Issue | Stakeholders Involved | Impact | Recommended Resolution |
   |-------|-----------------------|--------|------------------------|

   ### RACI Gaps
   [Any decisions or activities without clear R/A/C/I assignments]

   ### Recommendations
   1. [Most urgent stakeholder action]
   2. [Second priority]
   3. [Third priority]

   ### Overall Stakeholder Health
   **[ALIGNED / MINOR GAPS / SIGNIFICANT MISALIGNMENT]**
   [2-3 sentence summary]
   ```

---

## Mode: estimate-review

Audit an existing ROM estimate CSV for completeness, sizing accuracy, epic coverage, team composition balance, and risk identification. (from rom-estimate standalone skill)

**Announce:** "Starting ROM estimate review. I'll audit the CSV for sizing accuracy, missing coverage, team balance, and risk factors."

### Process

1. **Load the ROM estimate:**
   - If `$ARGUMENTS` includes a file path or Google Drive link, read the CSV from that location
   - Otherwise, search for ROM files: `docs/rom-estimation/*-rom.csv`, or ask the user for the file path
   - Parse the semicolon-delimited CSV: `epic;feature;effort_level;optimistic_duration;pessimistic_duration;specialities`

2. **Completeness check:**
   - Are all standard epics represented? Flag missing epics that are typically needed for the project type
   - Are there any epics with fewer than 2 features? (may indicate under-scoping)
   - Are there features without specialties assigned?
   - Are there features without duration ranges?
   - Check for "catch-all" epics with too many unrelated features

3. **Sizing accuracy review:**
   - Flag features where effort level doesn't match the duration range (e.g., M-level with 1-2d durations)
   - Identify features that may be under-estimated based on complexity signals:
     - Multi-service integrations at S or below
     - AI/ML features at M or below
     - Cross-account/migration features at L or below
   - Identify features that may be over-estimated:
     - Config changes or documentation at M or above
     - Single CRUD endpoints at L or above
   - Reference `skills/rom-estimate/references/effort-levels.md` for red flag signals

4. **Team composition analysis:**
   - Count features per specialty and calculate workload balance
   - Identify specialties with disproportionate load (>30% of total effort)
   - Flag specialties mentioned in features but not represented in the team
   - Calculate FTE requirements per specialty for the stated timeline
   - Identify bottleneck specialties (single-threaded work streams)

5. **Risk and dependency review:**
   - Count XL features (each is a risk factor)
   - Identify features with external dependencies
   - Flag compliance-related features that may require audit time
   - Check if testing effort is proportional to implementation effort (minimum 15-20%)
   - Identify sequential dependencies between epics

6. **Output audit report:**
   ```
   ## ROM Estimate Review: [Project Name]
   Review Date: [Date]
   Source CSV: [path]

   ### Summary
   - Total features: [count]
   - Total epics: [count]
   - Effort range: [opt]-[pess] person-days

   ### Completeness
   | Check | Status | Notes |
   |-------|--------|-------|
   | All standard epics covered | Pass/Warn | [missing epics] |
   | All features have sizing | Pass/Warn | [count missing] |
   | All features have specialties | Pass/Warn | [count missing] |
   | No catch-all epics | Pass/Warn | [flagged epics] |

   ### Sizing Concerns
   | Feature | Current Level | Suggested Level | Reason |
   |---------|---------------|-----------------|--------|

   ### Team Composition
   | Specialty | Features | % of Effort | FTE Needed | Status |
   |-----------|----------|-------------|------------|--------|

   ### Risk Factors
   - XL features: [count] ([list])
   - External dependencies: [count]
   - Compliance features: [count]
   - Testing coverage: [test effort]% of total ([adequate/insufficient])

   ### Recommendations
   1. [Most impactful improvement]
   2. [Second priority]
   3. [Third priority]

   ### Overall Estimate Health
   **[SOLID / NEEDS REFINEMENT / SIGNIFICANT GAPS]**
   [2-3 sentence summary with confidence level]
   ```

---

## Mode: meeting-insights

Analyze meeting transcripts or notes for communication patterns, decision quality, and facilitation effectiveness.

**Announce:** "Starting meeting insights review. I'll analyze communication patterns, decision tracking, and facilitation quality."

### Process

1. **Gather meeting data:**
   - Find meeting notes, transcripts, or recordings in project files
   - Check for meeting summaries in Confluence (via Atlassian MCP), Google Docs (via Google Drive MCP), or local files
   - Identify meeting type: standup, planning, review, retro, stakeholder sync, design review, or ad hoc

2. **Communication pattern analysis:**
   - **Participation balance:** Are all attendees contributing, or is one person dominating?
   - **Topic drift:** How often does the conversation diverge from the agenda?
   - **Decision velocity:** How quickly are decisions made vs. deferred?
   - **Action item clarity:** Are action items assigned with owners and deadlines?
   - **Follow-up rate:** What percentage of previous action items were completed?

3. **Decision quality assessment:**
   - Are decisions documented with context and rationale?
   - Are decision-makers identified (RACI clarity)?
   - Are alternatives discussed before deciding?
   - Are decisions reversible or one-way (and treated accordingly)?
   - Are open decisions tracked with deadlines?

4. **Facilitation effectiveness:**
   - Does the meeting start and end on time?
   - Is there a clear agenda shared in advance?
   - Are parking lot items captured and scheduled?
   - Is the meeting outcome proportional to the time invested?
   - Could this meeting have been an async update?

5. **Output report:**
   ```
   ## Meeting Insights Review
   Review Date: [Date]
   Meetings Analyzed: [count]

   ### Communication Health
   | Metric | Score | Notes |
   |--------|-------|-------|
   | Participation balance | Green/Yellow/Red | [context] |
   | Topic focus | Green/Yellow/Red | [context] |
   | Decision velocity | Green/Yellow/Red | [context] |
   | Action item clarity | Green/Yellow/Red | [context] |
   | Follow-up completion | Green/Yellow/Red | [X% of previous items completed] |

   ### Decision Log
   | Decision | Made By | Date | Alternatives Considered | Status |
   |----------|---------|------|------------------------|--------|

   ### Facilitation Recommendations
   1. [Most impactful improvement]
   2. [Second priority]
   3. [Third priority]

   ### Meetings That Could Be Async
   [List any meetings where an async update would be more efficient]

   ### Overall Meeting Health
   **[EFFECTIVE / NEEDS IMPROVEMENT / INEFFICIENT]**
   [2-3 sentence summary]
   ```

---

## Mode: comms-quality

Review the quality and consistency of team communications (status updates, 3P reports, stakeholder emails, Slack messages).

**Announce:** "Starting communications quality review. I'll assess clarity, consistency, tone, and completeness of team communications."

### Process

1. **Gather communications samples:**
   - Find recent status reports, 3P updates, stakeholder emails, and Slack messages
   - Check for communication templates and standards in project documentation
   - Identify the audience for each communication type

2. **Clarity assessment:**
   - Are updates readable in 30-60 seconds?
   - Is the bottom line stated upfront (not buried)?
   - Are metrics data-driven with specific numbers?
   - Are RAG statuses honest and consistent?
   - Are next steps actionable with owners and dates?

3. **Consistency check:**
   - Is the team using a consistent format across updates?
   - Are communication cadences being met (weekly, bi-weekly, monthly)?
   - Are all required stakeholders receiving their expected updates?
   - Is terminology consistent across communications?

4. **Tone and audience fit:**
   - Is the tone appropriate for the audience (executive vs. team vs. external)?
   - Are technical details abstracted for non-technical stakeholders?
   - Is the language matter-of-fact rather than overly optimistic or pessimistic?
   - Are concerns raised early rather than hidden?

5. **Completeness check:**
   - Do updates cover progress, plans, and problems?
   - Are blockers called out with specific asks?
   - Are wins and recognition included?
   - Are risks flagged before they become issues?

6. **Output report:**
   ```
   ## Communications Quality Review
   Review Date: [Date]
   Samples Reviewed: [count]

   ### Quality Scores
   | Dimension | Score | Notes |
   |-----------|-------|-------|
   | Clarity | Green/Yellow/Red | [context] |
   | Consistency | Green/Yellow/Red | [context] |
   | Tone/Audience Fit | Green/Yellow/Red | [context] |
   | Completeness | Green/Yellow/Red | [context] |
   | Timeliness | Green/Yellow/Red | [context] |

   ### Common Issues
   - [Most frequent issue across communications]
   - [Second most frequent]

   ### Best Practices Observed
   - [What the team is doing well]

   ### Recommendations
   1. [Most impactful improvement]
   2. [Second priority]
   3. [Third priority]

   ### Overall Comms Health
   **[STRONG / ADEQUATE / NEEDS IMPROVEMENT]**
   [2-3 sentence summary]
   ```
