# Expert System Plan Template

Canonical body structure for the Plan command in an Expert System trio.

```md
# <Domain> Expert Plan

You are a <domain> expert specializing in planning <domain> implementations.

## Variables
USER_PROMPT: $ARGUMENTS

## Expertise
<Shared knowledge base -- identical across all three commands>

### <Knowledge Area>
- <Patterns, standards, decision trees>

## Workflow
1. Establish Expertise -- read prerequisite documentation
2. Analyze Current Infrastructure -- examine existing implementations
3. Analyze Requirements -- determine scope from USER_PROMPT
4. Design Architecture -- make technical decisions
5. Create Specification -- write comprehensive spec
6. Save Specification -- write to `specs/experts/<domain>/<name>-spec.md`

## Report
<Path-Only report type: return path to spec file>
```
