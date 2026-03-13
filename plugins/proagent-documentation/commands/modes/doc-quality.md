# Assess Documentation Quality

**Input**: File path, directory, or repository URL
**Output**: Quality report with scores and recommendations

## Steps

1. **Discover docs** — find all documentation files (`.md`, `.rst`, `.adoc`, `.txt`)
2. **Assess completeness** — check for required sections (overview, setup, usage, API, contributing)
3. **Check accuracy** — verify code examples compile/run, links resolve, versions match
4. **Evaluate readability** — assess heading structure, paragraph length, use of examples
5. **Check freshness** — compare last-modified dates against recent code changes
6. **Score and report** — produce quality report with actionable recommendations

## Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Completeness | 30% | All essential sections present |
| Accuracy | 25% | Code examples work, links valid, versions current |
| Readability | 20% | Clear structure, concise prose, good examples |
| Freshness | 15% | Updated within reasonable timeframe |
| Formatting | 10% | Consistent style, proper Markdown, no broken rendering |
