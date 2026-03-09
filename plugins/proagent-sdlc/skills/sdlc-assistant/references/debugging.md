# Debugging

## Debugging Workflow

Applies systematic, hypothesis-driven debugging methodologies drawn from casdk-harness (`src/harness/skills/debugging/SKILL.md`) and taches-cc-resources (`skills/debug-like-expert/SKILL.md`).

1. Reproduce the issue with a minimal test case
2. Gather evidence: error messages, stack traces, logs, git blame
3. Form hypotheses ranked by likelihood
4. Test each hypothesis with targeted instrumentation (breakpoints, logging, assertions)
5. Identify root cause, not just symptoms
6. Implement fix with regression test
7. Verify fix does not introduce side effects

## Anti-Patterns to Avoid

- Shotgun debugging (random changes hoping something works)
- Print-statement overload without hypothesis
- Fixing symptoms instead of root cause
- Skipping the regression test after fix
