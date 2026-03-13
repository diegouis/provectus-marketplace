# Synchronize Docs with Confluence

**Input**: Repository reference and Confluence page ID or URL
**Output**: Sync report with changes applied

## Steps

1. **Fetch current state** — get latest repo content and current Confluence page
2. **Detect changes** — compare repo docs with Confluence content
3. **Identify stale sections** — find content that has drifted from source
4. **Generate updates** — produce new content for changed sections
5. **Preview changes** — show diff to user for approval
6. **Apply updates** — update Confluence page preserving manual edits
7. **Update sync metadata** — set last-sync timestamp label

> **CONTEXT GUARD**: For change detection patterns and sync workflow details, read `skills/documentation-assistant/references/doc-sync.md` at this point.

## Options

- `--page-id <id>` — Confluence page ID to sync
- `--auto-approve` — skip diff preview and apply changes directly
- `--dry-run` — show changes without applying them
