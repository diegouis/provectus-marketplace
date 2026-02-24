---
name: documentation-assistant
description: Cross-platform repository documentation and Confluence publishing — analyze GitHub/GitLab repos, generate docs (README, architecture, API, onboarding, runbooks), format as Confluence pages, publish and sync content. Use when performing any documentation generation, repo analysis for docs, Confluence publishing, or documentation review task.
---

# Cross-Platform Repository Documentation & Confluence Publishing

Comprehensive documentation engineering skill covering the full lifecycle from repository analysis through document generation to Confluence publishing and synchronization. Built for teams that maintain documentation across GitHub, GitLab, and Confluence.

## When to Use This Skill

Activate when the user mentions:
- **Documentation generation**: "generate docs", "create README", "write architecture docs", "document this repo"
- **Repository analysis**: "analyze repo structure", "what does this repo do", "extract API docs"
- **Confluence publishing**: "publish to Confluence", "create Confluence page", "update wiki"
- **Documentation sync**: "sync docs", "update stale docs", "keep Confluence in sync"
- **Documentation review**: "review docs", "doc quality", "coverage gaps"

## Environment Setup

This plugin uses direct git and API calls (no MCP servers required). Credentials are stored in the plugin's `.env` file.

> **CONTEXT GUARD**: Do NOT source credentials, clone repos, or make API calls until the user has specified what they want to do. The credential loading, GitHub API, and Confluence API patterns are documented in the plugin's CLAUDE.md — refer to them at the point of need, not upfront.

## Repository Analysis

### Workflow
1. **Clone the repo** using `git clone --depth 1` with token auth
2. **Scan directory structure** using `find`, `ls`, file reading
3. **Detect tech stack** from config files (package.json, requirements.txt, go.mod, etc.)
4. **Extract entry points** — find main.*, app.*, index.*, cmd/ patterns
5. **Map API endpoints** — scan route definitions, controllers, OpenAPI specs
6. **Catalog dependencies** — list direct and dev dependencies with versions
7. **Analyze CI/CD** — parse .github/workflows/, .gitlab-ci.yml, Jenkinsfile
8. **Identify existing docs** — check for README, CHANGELOG, CONTRIBUTING, docs/ directory
9. **Produce analysis JSON** — structured output for downstream operations

### Key Artifacts to Extract
| Artifact | Source Files | Purpose |
|----------|-------------|---------|
| Tech Stack | `package.json`, `requirements.txt`, `go.mod`, `Cargo.toml` | Identify languages, frameworks, dependencies |
| Entry Points | `main.*`, `app.*`, `index.*`, `cmd/` | Understand application startup |
| API Endpoints | `routes/`, `controllers/`, `api/`, OpenAPI specs | Document public interfaces |
| Database Schema | `migrations/`, `models/`, `schema.*` | Document data layer |
| CI/CD Pipeline | `.github/workflows/`, `.gitlab-ci.yml`, `Jenkinsfile` | Document build/deploy process |
| Configuration | `.env.example`, `config/`, `settings.*` | Document environment setup |
| Tests | `test/`, `tests/`, `__tests__/`, `*_test.*` | Understand test coverage |

### Analysis Output Format
```json
{
  "project_name": "example-service",
  "description": "Extracted from README or package.json",
  "tech_stack": {
    "language": "TypeScript",
    "framework": "NestJS",
    "database": "PostgreSQL",
    "cache": "Redis"
  },
  "structure": {
    "source_dir": "src/",
    "test_dir": "test/",
    "docs_dir": "docs/",
    "entry_point": "src/main.ts"
  },
  "api_endpoints": [],
  "dependencies": {},
  "ci_cd": {}
}
```

## Document Generation

### README Generation
A generated README should include:
1. **Project title and description** — extracted from package metadata
2. **Tech stack badges** — language, framework, CI status
3. **Prerequisites** — runtime versions, tools required
4. **Installation** — step-by-step setup instructions
5. **Configuration** — environment variables from `.env.example`
6. **Usage** — how to run, common commands
7. **API Reference** — endpoint summary if applicable
8. **Testing** — how to run tests
9. **Deployment** — CI/CD pipeline overview
10. **Contributing** — guidelines extracted from CONTRIBUTING.md or inferred

### Architecture Documentation
```markdown
# Architecture: <Project Name>

## Overview
High-level system description and purpose.

## System Diagram
[Mermaid or PlantUML diagram]

## Components
### Component A
- **Purpose**: ...
- **Technology**: ...
- **Key Files**: ...

## Data Flow
1. Request enters via ...
2. Processed by ...
3. Stored in ...

## Infrastructure
- Hosting: ...
- Database: ...
- External Services: ...
```

### API Documentation
Extract from OpenAPI/Swagger specs, route definitions, or controller decorators:
```markdown
## API Reference

### GET /api/v1/users
**Description**: List all users
**Auth**: Bearer token required
**Query Params**: `page`, `limit`, `search`
**Response**: `200 OK` — Array of User objects

### POST /api/v1/users
**Description**: Create a new user
**Auth**: Admin role required
**Body**: `{ name, email, role }`
**Response**: `201 Created` — User object
```

### Onboarding Guide
```markdown
# Developer Onboarding: <Project Name>

## Day 1: Environment Setup
1. Clone the repository
2. Install dependencies
3. Configure environment variables
4. Run the application locally
5. Run the test suite

## Day 2: Codebase Tour
- Project structure overview
- Key modules and their responsibilities
- Data models and relationships

## Day 3: First Contribution
- Pick a "good first issue"
- Development workflow (branch, commit, PR)
- Code review process
```

### Runbook
```markdown
# Runbook: <Project Name>

## Service Overview
- **Service**: ...
- **Team**: ...
- **On-call**: ...

## Health Checks
- Endpoint: `GET /health`
- Expected: `200 OK`

## Common Issues
### Issue: High Latency
- **Symptoms**: Response times > 2s
- **Diagnosis**: Check database connections, cache hit rate
- **Resolution**: Scale replicas, flush cache

### Issue: OOM Errors
- **Symptoms**: Pod restarts, memory alerts
- **Diagnosis**: Check memory usage, heap dumps
- **Resolution**: Increase memory limit, check for leaks
```

## Confluence Publishing

### Markdown to Confluence Storage Format
Key conversions:
| Markdown | Confluence Storage Format |
|----------|--------------------------|
| `# Heading` | `<h1>Heading</h1>` |
| `**bold**` | `<strong>bold</strong>` |
| `` `code` `` | `<code>code</code>` |
| Code blocks | `<ac:structured-macro ac:name="code">` |
| Tables | `<table><tr><th>...</th></tr></table>` |
| Links | `<a href="...">text</a>` |
| Images | `<ac:image><ri:url ri:value="..." /></ac:image>` |
| Info boxes | `<ac:structured-macro ac:name="info">` |

### Page Creation Workflow
1. **Source credentials** — load .env file
2. **Identify target space** — ask user or use default
3. **Check for existing page** — search by title via API to avoid duplicates
4. **Convert content** — Markdown to Confluence Storage Format
5. **Create/update page** — via curl to Confluence REST API
6. **Add labels** — auto-generated, auto-docs, repo name, doc type
7. **Verify publication** — fetch page back and confirm formatting
8. **Report result** — display page URL, space, and parent location

### Page Update Strategy
- Compare content hash to detect changes
- Preserve existing page metadata (labels, watchers, restrictions)
- Increment version number for Confluence versioning
- Add update note: "Auto-updated from <repo> on <date>"

## Documentation Sync

### Change Detection

Use `git log --since="<last-sync-date>" --name-only` to detect repo changes since the last Confluence sync. Filter for doc-relevant paths (README, docs/, api/, schema, models, routes, controllers).

### Sync Workflow
1. Fetch current Confluence page content via API
2. Re-analyze repository for changes
3. Generate updated documentation sections
4. Diff old vs new content
5. Update only changed sections (preserve manual edits)
6. Update sync timestamp label

## Reference Assets
| Asset | Source | Description |
|-------|--------|-------------|
| README templates | Provectus repos | Standardized README structures |
| Architecture templates | `docs/architecture/` | System design document templates |
| API doc generators | OpenAPI specs | Automated API documentation |
| Confluence macros | Atlassian docs | Storage format reference |
| Runbook templates | SRE practices | Incident response documentation |
