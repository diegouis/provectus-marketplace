# Creation Report Template

After generating all artifacts, provide this structured output.

```
Workflow Created: <one-line description>

Complexity: <simple | medium | complex>

Design Decisions:
- Pattern: <pattern name> -- <one-line rationale>
- Model strategy: <e.g., "opus for planning, sonnet for building, haiku for scanning">
- Key tradeoff: <the most important design choice and why>

Artifacts Generated:
- <type>: `<file-path>` -- <purpose> [Report: <report-type>]
- <type>: `<file-path>` -- <purpose> [Report: <report-type>]
- ...

Contracts:
- <producer> -> <consumer>: <format summary>
- ...
(or "None -- single artifact, no chaining")

Data Flow:
<step 1> -> <output> -> <step 2> -> <output> -> ...

Error Handling:
- Missing input: <what happens>
- Step failure: <what happens>
- Pipeline abort: <what the user sees>

How to Use:
<exact invocation command, e.g., /command-name "args">

Configuration Changes Required:
- <any settings.json updates needed -- show exact JSON to add>
- <any environment variables to set>
- (or "None -- all artifacts are self-contained")
```
