# Provectus Documentation Practice Plugin

This plugin provides the Documentation practice context for the Provectus agentic coding platform. It focuses on automated documentation generation from GitHub/GitLab repositories and publishing to Confluence.

## Practice Scope

1. **Repository Analysis** — Scan GitHub and GitLab repos to extract structure, tech stack, API endpoints, dependencies, and CI/CD configuration
2. **Document Generation** — Generate README, architecture docs, API reference, onboarding guides, and runbooks from repo analysis
3. **Confluence Publishing** — Create, update, and manage Confluence pages with proper Storage Format, macros, labels, and page hierarchy
4. **Documentation Sync** — Detect repo changes and update stale Confluence pages, preserving manual edits
5. **Documentation Review** — Audit quality, coverage, and freshness across repos and Confluence spaces

## Key Conventions

### Repository Analysis
- Always perform a full scan before generating documentation
- Detect tech stack from config files, not assumptions
- Extract API endpoints from code, not just README claims
- Produce structured JSON analysis for reproducibility

### Document Generation
- Follow standard templates for each doc type (README, architecture, API, onboarding, runbook)
- Include working code examples — they must be copy-paste ready
- Mark uncertain or incomplete sections clearly
- Use consistent heading hierarchy and formatting

### Confluence Publishing
- Always convert Markdown to Confluence Storage Format (XHTML with macros)
- Apply standard labels: `auto-generated`, `auto-docs`, `repo:<name>`, `type:<doctype>`
- Create pages under specified parent in the target space
- Never overwrite pages without user confirmation
- Preserve manually-edited sections during sync updates

### Documentation Quality
- Score docs on completeness, accuracy, readability, freshness, and formatting
- Flag broken links, outdated code examples, and missing sections
- Track coverage across repos — identify undocumented modules and APIs

## Default Confluence Target

When publishing documentation, use these defaults unless the user specifies otherwise:

| Setting | Value |
|---------|-------|
| **Space Key** | `PGPM` |
| **Space ID** | `215056390` |
| **Space Name** | Punchbowl News AI |
| **Parent Page** | Technical Documents |
| **Parent Page ID** | `223445003` |

This means:
- `/proagent-documentation-run publish-confluence` will default to `--space PGPM --parent "Technical Documents"`
- New pages will be created as children of **Technical Documents** in the Punchbowl News AI space
- The page hierarchy under Technical Documents includes: Data Engineering, AI/ML, DevOps

## MCP Integrations

- **GitHub**: Repository access for file scanning, PR docs, Actions configuration analysis
- **GitLab**: Repository access for file scanning, MR docs, CI pipeline analysis
- **Confluence**: Page creation, update, publishing, label management, space navigation
- **Slack**: Notification of documentation updates and team communication
- **Google Drive**: Import/export documentation from Google Docs and Sheets
- **Google Workspace**: Calendar integration for documentation review scheduling

## Plugin Structure

```
proagent-documentation/
├── .claude-plugin/plugin.json
├── skills/documentation-assistant/SKILL.md
├── commands/
│   ├── proagent-documentation-hub.md
│   ├── proagent-documentation-run.md
│   └── proagent-documentation-review.md
├── agents/
│   ├── documentation-specialist.md
│   ├── repo-analyzer.md
│   └── confluence-publisher.md
├── hooks/hooks.json
├── .mcp.json
├── CLAUDE.md
└── README.md
```
