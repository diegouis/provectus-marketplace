# Inter-Artifact Contracts

When a workflow chains multiple artifacts, each connection MUST have an explicit contract. Define contracts during the Design Decisions step and embed them in the artifacts.

## Contract Template

For each connection between artifacts, define:

```
Contract: <producer-name> -> <consumer-name>
  Producer outputs: <exact format description>
  Output location:  <file path pattern or stdout>
  Consumer reads:   <which variable or input mechanism>
  Format spec:      <precise format, e.g., "markdown bullet list: `- <path> (offset: N, limit: M)`">
  On success:       <what the consumer does with valid input>
  On empty output:  <STOP and notify | skip with warning | use default>
  On malformed:     <STOP and notify | attempt parse | skip entry>
  On producer fail: <abort pipeline | skip step | retry once>
```

## Contract Embedding

**In the producer artifact:** The `## Report` section must output in the exact format the contract specifies. Add a comment: `<!-- Contract: outputs to <consumer-name> via <variable-name> -->`

**In the consumer artifact:** The `## Variables` section must accept the format. The `## Error Handling` section must cover empty/malformed input. Add a comment: `<!-- Contract: receives from <producer-name> -->`

## Example Contract

```
Contract: /scout -> /plan_w_docs
  Producer outputs: file path to relevant files collection
  Output location:  agents/scout_files/relevant_files_<unique-id>.md
  Consumer reads:   RELEVANT_FILES_COLLECTION ($3)
  Format spec:      Markdown file with bullet list: `- <path to file> (offset: N, limit: M)`
  On success:       Plan reads each file at specified offsets to build context
  On empty output:  Plan should STOP and tell user "Scout found no relevant files"
  On malformed:     Skip entries without valid offset/limit, continue with valid ones
  On producer fail: Abort pipeline, report scout failure to user
```
