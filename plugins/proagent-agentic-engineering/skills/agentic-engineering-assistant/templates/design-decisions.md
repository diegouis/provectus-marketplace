# Design Decisions Template

Produce this structured analysis BEFORE generating any artifact. Save as a comment block at the top of the first artifact or as a separate `specs/workflow-design-<name>.md` file for Complex workflows.

```
## Design Decisions

### Complexity: <simple | medium | complex>
Rationale: <why this classification>

### Artifact Plan
For each artifact to generate:

Artifact 1: <name>
  Type:    <command | skill | agent | hook | expert-system | team-config>
  Why this type: <justification -- why not the alternatives?>
  Model:   <opus | sonnet | haiku>
  Why this model: <opus = complex reasoning, sonnet = balanced, haiku = speed/cost>
  Tools:   [<list>]
  Why these tools: <each tool justified, principle of least privilege>
  Report type: <from Report Type System>
  Error pattern: <from Error Handling Patterns>

Artifact 2: <name>
  ...

### Workflow Pattern: <pattern name>
Why this pattern: <justification>

### Contracts (if multi-artifact)
<Contract definitions from Inter-Artifact Contracts>

### Failure Modes
- If <artifact 1> fails: <consequence and mitigation>
- If <artifact 2> fails: <consequence and mitigation>
- Worst case: <what happens if everything fails -- user should see X>
```
