---
description: Review documentation quality, Confluence page health, and documentation coverage across repos
argument-hint: [doc-quality|confluence-audit|coverage] [target-path-or-url]
allowed-tools: Read, Grep, Glob, Bash
---

# /proagent-documentation-review - Review Documentation Quality & Coverage

Parse the review mode and load the corresponding mode file.

## Usage

```
/proagent-documentation-review <mode> [target]
```

## Review Modes

| Mode | Mode File | Description |
|------|-----------|-------------|
| `doc-quality` | `commands/modes/doc-quality.md` | Assess documentation completeness, accuracy, and readability |
| `confluence-audit` | `commands/modes/confluence-audit.md` | Audit Confluence pages for staleness, broken links, outdated content |
| `coverage` | `commands/modes/coverage.md` | Identify undocumented repos, modules, or APIs |

After identifying the mode, read the mode file and follow its instructions.

## Output Format

```markdown
## Documentation Review: <target>

### Summary
- **Files reviewed**: N
- **Overall score**: X/10
- **Critical issues**: N
- **Warnings**: N

### Issues Found

#### Critical
- [ ] Missing README.md in `service-b/`
- [ ] API endpoint `/users` undocumented

#### Warnings
- [ ] Architecture docs last updated 120 days ago
- [ ] Confluence page "Service A" has 3 broken links

#### Suggestions
- [ ] Add code examples to API reference
- [ ] Create onboarding guide for new team members

### Coverage: X% (documented repos / total repos)

### Score: X/10
```
