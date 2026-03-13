# Documentation Coverage Analysis

**Input**: Organization, repository list, or Confluence space
**Output**: Coverage report identifying gaps

## Steps

1. **Inventory repos** — list all repos in scope
2. **Check for docs** — verify each repo has README, CONTRIBUTING, architecture docs
3. **Map to Confluence** — check which repos have corresponding Confluence pages
4. **Identify API gaps** — find endpoints without documentation
5. **Check module coverage** — identify undocumented packages/modules
6. **Produce coverage matrix** — repo x doc-type matrix showing gaps

## Coverage Matrix Example

| Repository | README | Architecture | API Docs | Onboarding | Runbook | Confluence |
|-----------|--------|-------------|----------|-----------|---------|------------|
| service-a | Yes | Yes | Partial | No | No | Yes |
| service-b | Yes | No | No | No | No | No |
| service-c | Outdated | No | Yes | Yes | No | Partial |
