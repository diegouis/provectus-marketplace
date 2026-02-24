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
