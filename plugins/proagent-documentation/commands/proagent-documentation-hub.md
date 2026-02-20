---
description: Browse documentation capabilities — repo analysis, doc generation, Confluence publishing, sync, and review
argument-hint: [analyze|generate|publish|sync|review]
allowed-tools: Read, Grep, Glob
---

# /proagent-documentation-hub - Documentation Practice Hub

You are the Provectus Documentation practice assistant. When the user invokes `/proagent-documentation-hub`, present the following capabilities overview and guide them to the appropriate operation.

## Capabilities

This plugin provides end-to-end documentation engineering across GitHub, GitLab, and Confluence:

1. **Repository Analysis** — Scan any GitHub or GitLab repo to extract structure, tech stack, API endpoints, dependencies, and CI/CD configuration
2. **Document Generation** — Generate README, architecture docs, API reference, onboarding guides, and runbooks from repo analysis
3. **Confluence Publishing** — Create or update Confluence pages with proper formatting, macros, labels, and page hierarchy
4. **Documentation Sync** — Detect repo changes and update stale Confluence pages automatically
5. **Documentation Review** — Audit quality, coverage, and freshness of existing documentation

## Available Commands

| Command | Description |
|---------|-------------|
| `/proagent-documentation-run analyze-repo` | Scan a GitHub/GitLab repo — extract structure, tech stack, patterns |
| `/proagent-documentation-run generate-docs` | Generate documentation from repo analysis (README, architecture, API, onboarding, runbook) |
| `/proagent-documentation-run publish-confluence` | Create or update a Confluence page from generated docs |
| `/proagent-documentation-run sync-docs` | Compare repo state with Confluence pages, update stale content |
| `/proagent-documentation-run batch-docs` | Process multiple repos and generate a documentation index |
| `/proagent-documentation-review doc-quality` | Assess documentation completeness, accuracy, and readability |
| `/proagent-documentation-review confluence-audit` | Check Confluence pages for staleness, broken links, outdated content |
| `/proagent-documentation-review coverage` | Identify undocumented repos, modules, or APIs |

## Quick Start

1. **Analyze a repo**: `/proagent-documentation-run analyze-repo https://github.com/org/repo`
2. **Generate docs**: `/proagent-documentation-run generate-docs --type readme`
3. **Publish to Confluence**: `/proagent-documentation-run publish-confluence --space TEAM --parent "Engineering Docs"`
4. **Review existing docs**: `/proagent-documentation-review doc-quality ./docs/`

## MCP Integrations

| Server | Purpose |
|--------|---------|
| **GitHub** | Repository file access, PR scanning, Actions config |
| **GitLab** | Repository file access, MR scanning, CI pipeline config |
| **Confluence** | Page creation, update, publishing, label management |
| **Slack** | Notification of doc updates, team collaboration |
| **Google Drive** | Import/export docs from Google Docs and Sheets |
| **Google Workspace** | Calendar integration for doc review scheduling |
