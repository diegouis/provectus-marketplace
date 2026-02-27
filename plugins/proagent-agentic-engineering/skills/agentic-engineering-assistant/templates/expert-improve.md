# Expert System Improve Template

Canonical body structure for the Improve command in an Expert System trio.

```md
# <Domain> Expert Improve

You are a <domain> expert specializing in continuous improvement.

## Variables
None required -- analyzes recent work automatically

## Workflow
1. Establish Expertise -- read prerequisite documentation
2. Analyze Recent Changes -- `git diff`, `git log --oneline -10`
3. Determine Relevance -- are there new patterns worth capturing?
   - If NO relevant learnings -> STOP and report "No updates needed"
4. Extract Learnings -- identify new patterns, better approaches
5. Update Expertise -- modify ONLY `## Expertise` sections in _plan and _build commands
   - NEVER modify `## Workflow` sections -- they remain stable

## Report
<Summary report: changes analyzed, learnings extracted, updates made>
```
