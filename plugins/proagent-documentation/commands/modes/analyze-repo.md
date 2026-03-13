# Analyze Repository

**Input**: Repository URL (GitHub or GitLab) or local path
**Output**: Structured analysis JSON with project metadata

## Steps

1. **Clone or access** the repository via GitHub/GitLab MCP server
2. **Scan directory structure** — identify source dirs, test dirs, docs dirs, config files
3. **Detect tech stack** — parse `package.json`, `requirements.txt`, `go.mod`, `Cargo.toml`, `pom.xml`, etc.
4. **Extract entry points** — find `main.*`, `app.*`, `index.*`, `cmd/` patterns
5. **Map API endpoints** — scan route definitions, controllers, OpenAPI specs
6. **Catalog dependencies** — list direct and dev dependencies with versions
7. **Analyze CI/CD** — parse `.github/workflows/`, `.gitlab-ci.yml`, `Jenkinsfile`
8. **Identify existing docs** — check for README, CHANGELOG, CONTRIBUTING, docs/ directory
9. **Produce analysis JSON** — structured output for downstream operations

> **CONTEXT GUARD**: For detailed analysis schemas, artifact tables, and JSON output format, read `skills/documentation-assistant/references/repo-analysis.md` at this point.

## Options

- `--depth <shallow|full>` — shallow scans top-level only, full recurses into all modules (default: full)
- `--output <path>` — write analysis JSON to file (default: stdout)
