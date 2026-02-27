# Skill Body Template

Canonical body structure for `.claude/skills/<name>/SKILL.md` artifacts.

```md
# <Skill Name>

<Purpose statement: what this skill enables and when it activates.>

## Context

<WHY this skill exists. The problem it solves. When Claude should auto-load it.
Describe the trigger conditions that match the `description` field.>

## Expertise

<Domain knowledge the skill brings. This is the section that makes the skill
valuable -- patterns, standards, conventions, decision trees, reference data.
This section should be substantial for medium/complex skills.>

### <Knowledge Area 1>
- <Pattern or standard>
- <Decision criteria>

### <Knowledge Area 2>
- <Reference data>
- <Best practices>

## Instructions

- <Behavioral rule>
- <Scope constraint>
- <Quality standard>
- IMPORTANT: <Critical guardrail>

## Workflow

1. **<Step Name>**
   - <Action with tool reference>
   - If <failure> -> <fallback>

2. **<Step Name>**
   - <Action>

## Error Handling

- If <condition> -> <response>

## Report

<Appropriate report type template>
```
