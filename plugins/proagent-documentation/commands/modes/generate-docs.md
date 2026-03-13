# Generate Documentation

**Input**: Repo analysis (from `analyze-repo`) or repository URL
**Output**: Markdown documentation files

## Steps

1. **Run analysis** if not already available — invoke `analyze-repo` pipeline
2. **Select doc type** — prompt user or use `--type` flag
3. **Generate content** — produce documentation using analysis data and templates
4. **Apply formatting** — consistent headings, code blocks, tables, diagrams
5. **Write output** — save to specified location or display for review

> **CONTEXT GUARD**: For document templates (README, architecture, API, onboarding, runbook), read `skills/documentation-assistant/references/doc-generation.md` at this point.

## Doc Types

- `readme` — Complete README.md with badges, setup, usage, API reference
- `architecture` — System design document with diagrams, components, data flow
- `api` — API reference extracted from routes, controllers, OpenAPI specs
- `onboarding` — Developer onboarding guide with day-by-day plan
- `runbook` — Operations runbook with health checks, common issues, escalation

## Options

- `--type <readme|architecture|api|onboarding|runbook|all>` — document type (default: readme)
- `--output <path>` — output directory (default: `./docs/generated/`)
- `--format <markdown|confluence>` — output format (default: markdown)
