# Planning and Task Breakdown

## Structured Requirements Elicitation

The `ask-me-questions` command pattern provides structured requirement gathering by asking the user targeted questions before beginning implementation. Use this pattern at the start of any development workflow to ensure requirements are clear before writing code.

## Plan Structure

Breaks requirements into bite-sized tasks (2-5 minutes each) with explicit file paths, complete code snippets, exact test commands, and expected outputs. Integrates patterns from taches-cc-resources (hierarchical project planning) and superpowers (plan writing and execution).

- Header: goal, architecture summary, tech stack
- Tasks with numbered steps
- Each step: exact file paths, complete code, test commands with expected output
- TDD cycle per task: write failing test, verify fail, implement, verify pass, commit
- Execution handoff: subagent-driven (in-session) or parallel session

## Hierarchical Planning

From taches-cc-resources `skills/create-plans/SKILL.md`:
- Decompose complex projects into epics, features, and tasks
- Each task includes clear acceptance criteria and dependencies
- Track progress with status markers (pending, in-progress, done, blocked)

## Plan Execution

From superpowers `skills/executing-plans/SKILL.md`:
- Read the plan file, identify the next uncompleted task
- Execute the task following TDD discipline
- Mark task complete with commit reference
- Auto-advance to next task or pause for confirmation at phase boundaries
