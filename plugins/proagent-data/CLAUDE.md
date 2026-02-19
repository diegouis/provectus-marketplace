# Provectus Data Practice Plugin

This plugin provides the Data practice context for the Provectus agentic coding platform. It equips Claude with production-tested data engineering and analytics patterns drawn from actual Provectus engineering repositories.

## Practice Scope

The Data practice covers nine operational domains:

1. **Data Pipeline Engineering** - ETL/ELT pipeline design with Airflow DAGs, dbt models, and Spark jobs including incremental loading, retry policies, and idempotent operations. Reference assets in `agents/plugins/data-engineering/` (data-engineer agent, data-pipeline command, Airflow DAG patterns, dbt transformation patterns, Spark optimization skills)
2. **Data Warehousing** - Dimensional modeling with star schema, snowflake schema, and Data Vault 2.0 patterns including SCD Type 2, partitioning, and materialized views
3. **dbt Analytics Engineering** - Model layers (staging, intermediate, marts), source freshness monitoring, testing, macros, and incremental strategies (merge, delete+insert, insert_overwrite). Reference: `agents/plugins/data-engineering/skills/dbt-transformation-patterns/SKILL.md`
4. **SQL Optimization** - Query performance analysis with EXPLAIN ANALYZE, index strategies (B-tree, GIN, BRIN, partial, covering), PostgreSQL tuning, and monitoring. Reference: `casdk-harness/src/harness/agents/configs/db-postgres-expert.md` and `db-sql-expert.md`
5. **Data Quality** - Validation frameworks with Great Expectations and dbt tests, volume anomaly detection, freshness monitoring, and referential integrity checks
6. **Analytics and EDA** - Exploratory data analysis, statistical summaries, correlation analysis, data visualization, window functions, and sessionization queries
7. **Business Analytics** - KPI dashboard design, data storytelling, and visualization for business stakeholders. Reference assets in `agents/plugins/business-analytics/` (business-analyst agent, KPI dashboard design skill, data storytelling skill)
8. **Bioinformatics Data Pipelines** - Nextflow pipeline development for genomics and life sciences, instrument data conversion to Allotrope format. Reference: `provectus-marketplace/testing/knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md` and `nextflow-development/SKILL.md`
9. **Analytics Infrastructure** - Usage tracking, KPI reporting, and analytics SQL queries for internal tooling. Reference: `proagent-repo/infrastructure/analytics/` (tracker.py, reporter.py, queries.py)

## Key Conventions

When performing data engineering tasks, follow these standards:

### Data Pipelines
- All pipelines must be idempotent (safe to re-run without creating duplicates)
- Use upsert (INSERT ON CONFLICT) or MERGE patterns for incremental loads
- Configure retry policies with exponential backoff and execution timeouts
- Include data quality checks between pipeline stages
- Never hardcode credentials; use environment variables or secret managers

### dbt Models
- Organize models into staging (stg_), intermediate (int_), and marts (dim_, fct_) layers
- Staging models are 1:1 with source tables, performing only renaming and light type casting
- Every model must have at least unique and not_null tests on its primary key
- Use incremental models for tables exceeding 1 million rows
- Configure source freshness monitoring with warn_after and error_after thresholds

### SQL Standards
- Use explicit JOIN syntax (never comma-separated FROM clauses)
- Specify column lists explicitly (never SELECT *)
- Use CTEs for readability instead of nested subqueries
- Apply consistent formatting: lowercase keywords, one column per line, trailing commas
- Document business logic in SQL comments for complex transformations

### Schema Design
- Add created_at and updated_at timestamps to all tables
- Use UUIDs for distributed systems, BIGSERIAL for single-database applications
- Always create indexes on foreign key columns
- Apply CHECK constraints for business rules (valid status values, positive amounts)
- Plan partitioning strategy for tables expected to exceed 100 million rows

### Data Quality
- Test not_null and unique on every primary key
- Test relationships between fact and dimension tables
- Test accepted_values on all enum/categorical columns
- Monitor source freshness and alert on stale data
- Track volume trends and alert on anomalies beyond 2 standard deviations

### Business Analytics
- Design KPI dashboards with clear metric hierarchies (leading vs lagging indicators)
- Apply data storytelling principles: context, narrative arc, actionable insight
- Use the business-analyst agent for stakeholder-facing deliverables
- Reference `agents/plugins/business-analytics/skills/kpi-dashboard-design/SKILL.md` for dashboard patterns
- Reference `agents/plugins/business-analytics/skills/data-storytelling/SKILL.md` for visualization and narrative patterns

### Bioinformatics Pipelines
- Use Nextflow for genomics and life-sciences pipeline development
- Convert instrument data to Allotrope ASM format for standardized lab data exchange
- Reference `provectus-marketplace/testing/knowledge-work-plugins/bio-research/skills/nextflow-development/SKILL.md` for Nextflow patterns
- Reference `provectus-marketplace/testing/knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md` for instrument data conversion

### Excel and Spreadsheet Operations
- Use the xlsx skill for reading, writing, and transforming Excel spreadsheets
- Reference `skills/skills/xlsx/SKILL.md` for spreadsheet patterns

## MCP Integrations

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **Rube (Composio)**: SaaS automation gateway providing access to Google Sheets, Airtable, Supabase, Amplitude, Mixpanel, PostHog, and Segment via `RUBE_SEARCH_TOOLS`, `RUBE_MANAGE_CONNECTIONS`, and `RUBE_MULTI_EXECUTE_TOOL`

## Plugin Structure

```
proagent-data/
  .claude-plugin/plugin.json
  skills/data-assistant/SKILL.md
  commands/proagent-data-hub.md
  commands/proagent-data-run.md
  commands/proagent-data-review.md
  agents/data-specialist.md
  hooks/hooks.json
  .mcp.json
  CLAUDE.md
  README.md
```
