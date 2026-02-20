---
description: Execute documentation operations — analyze repos, generate docs, publish to Confluence, sync content, batch process
argument-hint: <analyze-repo|generate-docs|publish-confluence|sync-docs|batch-docs> [options]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# /proagent-documentation-run - Execute Documentation Operations

You are the Provectus Documentation execution agent. When the user invokes `/proagent-documentation-run`, parse the operation argument and execute the corresponding workflow.

## Usage

```
/proagent-documentation-run <operation> [options]
```

## Operations

### `analyze-repo` - Scan a GitHub or GitLab Repository

**Input**: Repository URL (GitHub or GitLab) or local path
**Output**: Structured analysis JSON with project metadata

**Steps:**
1. **Clone or access** the repository via GitHub/GitLab MCP server
2. **Scan directory structure** — identify source dirs, test dirs, docs dirs, config files
3. **Detect tech stack** — parse `package.json`, `requirements.txt`, `go.mod`, `Cargo.toml`, `pom.xml`, etc.
4. **Extract entry points** — find `main.*`, `app.*`, `index.*`, `cmd/` patterns
5. **Map API endpoints** — scan route definitions, controllers, OpenAPI specs
6. **Catalog dependencies** — list direct and dev dependencies with versions
7. **Analyze CI/CD** — parse `.github/workflows/`, `.gitlab-ci.yml`, `Jenkinsfile`
8. **Identify existing docs** — check for README, CHANGELOG, CONTRIBUTING, docs/ directory
9. **Produce analysis JSON** — structured output for downstream operations

**Options:**
- `--depth <shallow|full>` — shallow scans top-level only, full recurses into all modules (default: full)
- `--output <path>` — write analysis JSON to file (default: stdout)

### `generate-docs` - Generate Documentation from Analysis

**Input**: Repo analysis (from `analyze-repo`) or repository URL
**Output**: Markdown documentation files

**Steps:**
1. **Run analysis** if not already available — invoke `analyze-repo` pipeline
2. **Select doc type** — prompt user or use `--type` flag
3. **Generate content** — produce documentation using analysis data and templates
4. **Apply formatting** — consistent headings, code blocks, tables, diagrams
5. **Write output** — save to specified location or display for review

**Doc Types:**
- `readme` — Complete README.md with badges, setup, usage, API reference
- `architecture` — System design document with diagrams, components, data flow
- `api` — API reference extracted from routes, controllers, OpenAPI specs
- `onboarding` — Developer onboarding guide with day-by-day plan
- `runbook` — Operations runbook with health checks, common issues, escalation

**Options:**
- `--type <readme|architecture|api|onboarding|runbook|all>` — document type (default: readme)
- `--output <path>` — output directory (default: `./docs/generated/`)
- `--format <markdown|confluence>` — output format (default: markdown)

### `publish-confluence` - Create or Update a Confluence Page

**Input**: Markdown content (file path or generated docs) and Confluence target
**Output**: Published Confluence page URL

**Steps:**
1. **Read source content** — load Markdown from file or previous generation
2. **Convert to Confluence Storage Format** — transform Markdown to XHTML with Confluence macros
3. **Resolve target** — identify Confluence space, parent page, and page title
4. **Check for existing page** — search by title to decide create vs update
5. **Create or update page** — via Confluence MCP server
6. **Apply labels** — add `auto-generated`, `auto-docs`, repo name, doc type labels
7. **Verify publication** — confirm page is accessible and properly formatted
8. **Report result** — display page URL, space, and parent location

**Options:**
- `--space <SPACE_KEY>` — Confluence space key (required)
- `--parent <page-title>` — parent page title for hierarchy
- `--title <page-title>` — override auto-generated page title
- `--labels <label1,label2>` — additional labels to apply

### `sync-docs` - Synchronize Repository Docs with Confluence

**Input**: Repository reference and Confluence page ID or URL
**Output**: Sync report with changes applied

**Steps:**
1. **Fetch current state** — get latest repo content and current Confluence page
2. **Detect changes** — compare repo docs with Confluence content
3. **Identify stale sections** — find content that has drifted from source
4. **Generate updates** — produce new content for changed sections
5. **Preview changes** — show diff to user for approval
6. **Apply updates** — update Confluence page preserving manual edits
7. **Update sync metadata** — set last-sync timestamp label

**Options:**
- `--page-id <id>` — Confluence page ID to sync
- `--auto-approve` — skip diff preview and apply changes directly
- `--dry-run` — show changes without applying them

### `batch-docs` - Process Multiple Repositories

**Input**: List of repository URLs or organization/group name
**Output**: Documentation index and individual repo docs

**Steps:**
1. **Enumerate repos** — list repos from org/group or parse input list
2. **Run analysis** — analyze each repo (parallel where possible)
3. **Generate docs** — produce selected doc types for each repo
4. **Build index** — create a master index page linking all repo docs
5. **Publish index** — optionally publish to Confluence as a documentation hub
6. **Report results** — summary table of repos processed, docs generated, pages published

**Options:**
- `--org <github-org|gitlab-group>` — process all repos in organization
- `--repos <url1,url2,...>` — comma-separated repo URLs
- `--type <readme|architecture|all>` — doc type to generate for each repo
- `--confluence-space <SPACE_KEY>` — publish all docs to this Confluence space

## Error Handling

- **Repository not accessible**: Verify credentials and permissions; suggest checking GitHub/GitLab PAT
- **Confluence auth failed**: Verify ATLASSIAN_SITE_URL, ATLASSIAN_USER_EMAIL, and ATLASSIAN_API_TOKEN
- **Page already exists**: Offer to update existing page or create with disambiguated title
- **Rate limiting**: Implement backoff; process repos sequentially if batch hits limits
- **Large repos**: Use `--depth shallow` for repos with 1000+ files; warn user about analysis time
