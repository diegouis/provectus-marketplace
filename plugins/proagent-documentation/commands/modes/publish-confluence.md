# Publish to Confluence

**Input**: Markdown content (file path or generated docs) and Confluence target
**Output**: Published Confluence page URL

## Steps

1. **Read source content** — load Markdown from file or previous generation
2. **Convert to Confluence Storage Format** — transform Markdown to XHTML with Confluence macros
3. **Resolve target** — identify Confluence space, parent page, and page title
4. **Check for existing page** — search by title to decide create vs update
5. **Create or update page** — via Confluence MCP server
6. **Apply labels** — add `auto-generated`, `auto-docs`, repo name, doc type labels
7. **Verify publication** — confirm page is accessible and properly formatted
8. **Report result** — display page URL, space, and parent location

> **CONTEXT GUARD**: For Markdown-to-Confluence conversion rules and Storage Format reference, read `skills/documentation-assistant/references/confluence-publishing.md` at this point.

## Options

- `--space <SPACE_KEY>` — Confluence space key (required)
- `--parent <page-title>` — parent page title for hierarchy
- `--title <page-title>` — override auto-generated page title
- `--labels <label1,label2>` — additional labels to apply
