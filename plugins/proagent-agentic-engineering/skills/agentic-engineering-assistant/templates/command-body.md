# Slash Command Body Template

Canonical body structure for `.claude/commands/<name>.md` artifacts.

```md
# <Command Name>

<One-paragraph purpose statement. Reference key sections: "Follow the `Workflow` to accomplish X, then follow the `Report` section.">

## Variables

<DYNAMIC_VAR_1>: $1
<DYNAMIC_VAR_2>: $2
<STATIC_VAR>: <default value>

## Instructions

- <Behavioral guardrail: what the command MUST do>
- <Behavioral guardrail: what the command MUST NOT do>
- <Data handling rule: how to pass variables between steps>
- <Scope constraint: boundaries of what this command touches>
- IMPORTANT: <The single most critical rule, capitalized for emphasis>

## Workflow

1. **<Step Name>**
   - <Specific action with tool name>
   - <Expected output or side effect>
   - If <failure condition> -> <fallback action from Error Handling Patterns>

2. **<Step Name>**
   - <Specific action>
   - <Validation check>

<continue with numbered steps>

## Error Handling

- If no <required input> is provided -> STOP and ask the user
- If <step N> returns empty/fails -> <specific fallback>
- If <step N> times out -> <skip with note | retry once | abort with report>

## Report

<Select and fill the appropriate template from the Report Type System>
```
