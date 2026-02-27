# Report Type System

Every artifact's `## Report` section MUST use one of these templates. Select based on the artifact's role in the workflow.

## Type 1: Summary Report

**When to use:** End of a standalone task, final step in a pipeline, general-purpose completion.

```md
## Report

Summarize the completed work:
- <What was accomplished -- bullet points>
- <Key decisions made>
- <Anything the user should know or review>
```

## Type 2: YAML Structured Report

**When to use:** When downstream agents or scripts will parse the output. Machine-readable results.

```md
## Report

Report your work in the following format:
<format>
work_changes:
  - file: <file-path>
    action: <created|modified|deleted>
    description: <one-sentence description>
  - ...
status: <success|partial|failed>
summary: <one-sentence overall summary>
</format>
```

## Type 3: Diff Report

**When to use:** After code changes. Build commands, implementation steps.

```md
## Report

- Run `git diff --stat` then `git diff` to capture all changes
- Summarize the work in concise bullet points
- Report files changed and lines modified
```

## Type 4: Progress Report

**When to use:** Long-running tasks, background agents. Updated continuously as work progresses.

```md
## Report

IMPORTANT: Update this report file continuously as you work -- after every major step.

Structure:
## Task Understanding
<What was requested, broken into numbered items>

## Progress
<Bullet points updated as you work: action taken, finding, next action>

## Results
<Concrete outcomes with file paths and metrics>

## Task Completed (or Task Failed)
<Final summary>

When finished:
- Success: Rename report file to `<name>.complete.md`
- Failure: Rename report file to `<name>.failed.md`
```

## Type 5: Handoff Report

**When to use:** Chained commands where this artifact's output IS the next artifact's input. The format MUST match the consumer's variable schema exactly.

```md
## Report

IMPORTANT: Return ONLY the <output type> in the exact format the next step expects.
- Output: `<exact format matching the consumer's input variable>`
- No additional commentary -- this output is consumed programmatically.
- Example: `/scout` returns only a file path that `/plan_w_docs` reads as its RELEVANT_FILES_COLLECTION variable.
```

## Type 6: Comparison Report

**When to use:** Fan-out patterns where multiple agents produce competing/complementary results that need merging.

```md
## Report

Collect outputs from all agents and synthesize:
- Deduplicate overlapping results
- Merge complementary findings
- Flag contradictions between agent outputs
- Rank results by relevance/confidence
- Skip agent outputs that failed or returned invalid format

Format:
## Merged Results
<Deduplicated, ranked findings>

## Agent Concordance
- Agreed: <findings all agents produced>
- Diverged: <findings where agents disagreed, with each position noted>
- Unique: <findings only one agent produced>
```

## Type 7: Audit Report

**When to use:** Security hooks, compliance checks, permission decisions. Timestamped decision log.

```md
## Report

Log every decision to `<audit-log-path>` in JSONL format:
{"timestamp": "<ISO-8601>", "event": "<hook-event>", "decision": "<allow|block>", "reason": "<why>", "context": {"tool": "<tool-name>", "input_summary": "<brief>"}}
- One JSON object per line (JSONL format for efficient append)
- NEVER log sensitive values (secrets, tokens, full file contents)
- Log to session-specific directory: `agents/<feature>/<session_id>/`
```

## Type 8: Path-Only Report

**When to use:** Intermediate pipeline steps that produce a file for the next step. Scout results, plan files, spec documents.

```md
## Report

IMPORTANT: Return exclusively the path to the file created.
- Format: `<directory>/<filename>.md`
- No additional text, explanation, or formatting.
```

---

## Report Type Selection Guide

| Artifact Role | Report Type |
|---|---|
| Final step, standalone task | Summary |
| Build step with code changes | Diff |
| Produces machine-readable output | YAML Structured |
| Background / long-running task | Progress |
| Intermediate pipeline step producing a file | Path-Only |
| Intermediate pipeline step producing data for next command | Handoff |
| Fan-out with multiple agents | Comparison |
| Security / compliance hook | Audit |
