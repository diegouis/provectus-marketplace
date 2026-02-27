# Error Handling Patterns

Every generated artifact must include error guards. Select the appropriate pattern based on the artifact's role.

## Pattern A: Gate Guard (for input validation)

```md
- If no `<REQUIRED_VAR>` is provided -> STOP immediately and ask the user to provide it
- If `<REQUIRED_VAR>` points to a file that doesn't exist -> STOP and report "File not found: <path>"
```

Use at the top of every `## Workflow` for commands and skills that take arguments.

## Pattern B: Step Fallback (for pipeline steps)

```md
- If <step N> returns empty -> <skip to next step with note | abort with report>
- If <step N> produces malformed output -> <attempt to parse what's available | skip and continue>
- If <step N> times out -> <skip with warning and continue | retry once then abort>
```

Use within `## Workflow` for each step that could fail.

## Pattern C: Graceful Degradation (for hooks)

```python
# Primary function -- must work
try:
    # core logic
    result = validate(data)
except Exception as e:
    # For blocking hooks: fail open (allow) rather than breaking Claude
    sys.exit(0)

# Auxiliary function -- nice to have
try:
    # logging, audit trail
    log_decision(result)
except Exception:
    pass  # Never let logging break primary function
```

Use in every hook script. Blocking hooks should fail open unless explicitly designed as security gates.

## Pattern D: Pipeline Abort (for coordinator commands)

```md
- Execute steps in order. After each step, verify the output before proceeding.
- If any step returns an unexpected result -> STOP the pipeline and report:
  - Which step failed
  - What was expected vs. what was received
  - Suggested remediation
- Do NOT continue to the next step with bad data.
```

Use in coordinator commands that chain slash commands together.

## Pattern E: Retry with Ceiling (for external operations)

```md
- If <operation> fails -> retry once after 5 seconds
- If retry also fails -> skip this operation and note it in the report
- NEVER retry more than once -- avoid infinite loops
```

Use for operations that depend on external services (web fetches, API calls, MCP servers).
