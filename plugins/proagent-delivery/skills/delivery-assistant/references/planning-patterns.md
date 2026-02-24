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
