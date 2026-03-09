# Pipeline Frameworks

## ProAgent 5-Stage SDLC Pipeline

The ProAgent orchestration engine (`proagent-repo/core/orchestration/sdlc/pipeline.py`) defines a 5-stage pipeline that maps to the core SDLC phases:

1. **Analyze** -- Gather requirements, read specs, understand the problem domain
2. **Design** -- Architecture decisions, technology selection, component design
3. **Implement** -- Code generation with TDD, following the plan task-by-task
4. **Validate** -- Code review, test execution, acceptance criteria verification
5. **Deliver** -- Versioning, changelog, release readiness, deployment preparation

Each stage produces artifacts that feed the next. The pipeline can be run end-to-end or entered at any stage for targeted workflows.

## PITER Framework

The PITER framework (`proagent-repo/core/skills/tac/piter.md`) provides a micro-cycle for individual task execution:

- **Plan** -- Understand the task, identify files to change, define the approach
- **Implement** -- Write the code following the plan
- **Test** -- Write and run tests to verify correctness
- **Evaluate** -- Assess quality, check edge cases, review against requirements
- **Refine** -- Improve based on evaluation feedback, optimize, clean up

Apply PITER within each task of a larger plan. It complements TDD by adding explicit evaluation and refinement phases.

## Ralph Orchestrator Presets

The ralph-orchestrator provides pre-configured workflow presets for common SDLC scenarios:

- **Bugfix preset** (`ralph-orchestrator/presets/bugfix.yml`): Reproduce issue, isolate root cause, implement fix with regression test, verify no side effects
- **Refactor preset** (`ralph-orchestrator/presets/refactor.yml`): Identify refactoring target, ensure test coverage exists, apply transformation, verify behavior preservation

These presets define step sequences, quality gates, and rollback conditions for orchestrated multi-agent workflows.

## AWOS Specification-to-Implementation Pipeline

The AWOS (Agentic Workflow Operating System) provides an 8-step pipeline for transforming ideas into production code:

### Pipeline Steps
1. **Product Vision** -> `context/product/product.md` -- Non-technical vision, audience, and rationale
2. **Feature Roadmap** -> `context/product/roadmap.md` -- Prioritized features and delivery phases
3. **System Architecture** -> `context/product/architecture.md` -- Tech stack, databases, infrastructure
4. **Functional Spec** -> `context/spec/{feature}/spec.md` -- What the feature does for users
5. **Technical Plan** -> `context/spec/{feature}/tech.md` -- How to build it
6. **Task Decomposition** -> `tasks.md` + `task_list.json` -- Step-by-step implementation checklist
7. **Implementation** -> Code changes with progress tracking
8. **Verification** -> Validate acceptance criteria are met

### AWOS Commands
The AWOS framework provides 7 commands that map to pipeline steps:
- `awos/commands/spec.md` -- Generate functional specifications from product vision
- `awos/commands/architecture.md` -- Interactive architecture design with alternatives
- `awos/commands/implement.md` -- Execute implementation with task decomposition and TDD

AWOS also provides reusable templates:
- `awos/templates/architecture-template.md` -- Structured architecture document scaffold
- `awos/templates/functional-spec-template.md` -- Functional specification scaffold with acceptance criteria sections

### Mandatory Confirmation Gates
After each step, the workflow STOPS and presents output for user review:
- **[A]pprove** -- Accept output, continue to next step
- **[E]dit** -- User modifies the file, then continues
- **[R]edo** -- Provide feedback, regenerate the step

Configurable via `AWOS_SPEC_REFINEMENT=1,4,6` to set which steps require confirmation.

### Session Persistence
The workflow persists state to `awos_session.json` with atomic writes, enabling reliable resume across sessions. Step detection uses file existence (e.g., if `architecture.md` exists, skip to step 4).

For long-running development workflows, persist workflow state to a JSON file (e.g., `session.json`) using atomic writes (write to temp file, then rename). Track current step, completed steps, and user confirmations. This enables reliable resume across sessions without relying on chat history.

## Mandatory Confirmation Pattern

For any multi-step autonomous development workflow, implement confirmation gates between phases:

1. **Execute** the current phase (e.g., requirements analysis, architecture design)
2. **Present** output artifacts to the user
3. **STOP** and wait for explicit approval: Approve / Edit / Redo
4. **Only proceed** after receiving confirmation

This pattern prevents autonomous runaway and ensures stakeholder alignment at critical decision points. Configure which steps require confirmation vs. auto-advance based on team trust and workflow maturity.

## Pipeline Frameworks Comparison

| Framework | Source | Scope | Stages |
|-----------|--------|-------|--------|
| ProAgent 5-stage | `proagent-repo/core/orchestration/sdlc/pipeline.py` | Full project | Analyze, Design, Implement, Validate, Deliver |
| AWOS 8-step | `awos/commands/*` | Feature development | Vision, Roadmap, Architecture, Spec, Plan, Tasks, Implement, Verify |
| PITER | `proagent-repo/core/skills/tac/piter.md` | Single task | Plan, Implement, Test, Evaluate, Refine |
| Ralph presets | `ralph-orchestrator/presets/*.yml` | Targeted workflows | Bugfix, Refactor (configurable step sequences) |
