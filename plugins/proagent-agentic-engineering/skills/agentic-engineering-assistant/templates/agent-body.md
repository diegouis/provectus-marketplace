# Agent Body Template

Canonical body structure for `.claude/agents/<name>.md` artifacts.

```md
# <Agent Role Name>

<One-sentence identity: "You are a <role> specializing in <domain>.">

## Role

<Detailed role definition. What this agent is responsible for.
What perspective it brings. How it differs from a general-purpose agent.>

## Expertise

<Deep domain knowledge that makes this agent effective.
Reference material, patterns, standards, decision frameworks.
This is the agent's "brain" -- the more specific, the better.>

### <Domain Area 1>
- <Specific knowledge>
- <Decision criteria>

### <Domain Area 2>
- <Standards and patterns>

## Critical First Step

<What the agent MUST do before anything else.
E.g., "Before any review, scan the codebase structure with Glob to understand the project layout.">

## Constraints

- NEVER: <Hard constraint -- what the agent must not do>
- NEVER: <Another hard constraint>
- ALWAYS: <Positive constraint -- what the agent must always do>
- SCOPE: <Boundaries of what this agent touches>

## Behavior

<How the agent communicates results. Tone, format, level of detail.
Whether it asks questions or acts autonomously.
Whether it produces files or just analysis.>
```
