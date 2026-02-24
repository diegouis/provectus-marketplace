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
