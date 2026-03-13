---
name: documentation-assistant
description: Cross-platform repository documentation and Confluence publishing — analyze GitHub/GitLab repos, generate docs (README, architecture, API, onboarding, runbooks), format as Confluence pages, publish and sync content. Use when performing any documentation generation, repo analysis for docs, Confluence publishing, or documentation review task.
---

# Cross-Platform Repository Documentation & Confluence Publishing

Comprehensive documentation engineering covering the full lifecycle from repository analysis through document generation to Confluence publishing and synchronization.

## When to Use This Skill

- Generating documentation (README, architecture, API, onboarding, runbooks) from repositories
- Analyzing repo structure for documentation purposes
- Publishing or syncing content to Confluence
- Reviewing documentation quality or coverage
- Batch-processing multiple repos for documentation

## When Invoked Without Clear Intent

**MANDATORY**: You MUST call the `AskUserQuestion` tool — do NOT render these options as text:

AskUserQuestion(
  header: "Docs",
  question: "What documentation task do you need help with?",
  options: [
    { label: "Generate Docs", description: "Generate README, architecture, API, onboarding, or runbook docs from a repo" },
    { label: "Analyze Repo", description: "Scan a repository to extract structure, tech stack, and API endpoints" },
    { label: "Publish to Confluence", description: "Create or update Confluence pages from Markdown documentation" },
    { label: "Sync & Review", description: "Detect stale docs, sync changes, or audit documentation quality" }
  ]
)

## Reference Routing

> **CONTEXT GUARD**: Load reference files only when the user's request matches a specific topic below. Do NOT load all references upfront.

| User Intent | Reference File |
|---|---|
| Repo analysis, structure scanning, tech stack detection, API extraction | `references/repo-analysis.md` |
| README, architecture docs, API docs, onboarding guide, runbook generation | `references/doc-generation.md` |
| Confluence publishing, Storage Format, page creation, labels, hierarchy | `references/confluence-publishing.md` |
| Doc sync, change detection, stale content, freshness checking | `references/doc-sync.md` |

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate architecture diagrams, system component maps, data flow diagrams, and documentation coverage visualizations. Describe what you need in natural language.
