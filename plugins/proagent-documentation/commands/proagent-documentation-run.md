---
description: Execute documentation operations — analyze repos, generate docs, publish to Confluence, sync content, batch process
argument-hint: <analyze-repo|generate-docs|publish-confluence|sync-docs|batch-docs> [options]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# /proagent-documentation-run - Execute Documentation Operations

Parse the operation argument and load the corresponding mode file.

## Usage

```
/proagent-documentation-run <operation> [options]
```

## Operations

| Operation | Mode File | Description |
|-----------|-----------|-------------|
| `analyze-repo` | `commands/modes/analyze-repo.md` | Scan a GitHub/GitLab repo — extract structure, tech stack, patterns |
| `generate-docs` | `commands/modes/generate-docs.md` | Generate documentation (README, architecture, API, onboarding, runbook) |
| `publish-confluence` | `commands/modes/publish-confluence.md` | Create or update Confluence pages from generated docs |
| `sync-docs` | `commands/modes/sync-docs.md` | Sync repo docs with Confluence, update stale content |
| `batch-docs` | `commands/modes/batch-docs.md` | Process multiple repos and generate a documentation index |

After identifying the operation, read the mode file and follow its instructions.

## Error Handling

- **Repository not accessible** — verify credentials and GitHub/GitLab PAT
- **Confluence auth failed** — verify ATLASSIAN_SITE_NAME, ATLASSIAN_USER_EMAIL, and ATLASSIAN_API_TOKEN
- **Page already exists** — offer to update existing page or create with disambiguated title
- **Rate limiting** — implement backoff; process repos sequentially if batch hits limits
- **Large repos** — use `--depth shallow` for repos with 1000+ files; warn user about analysis time
