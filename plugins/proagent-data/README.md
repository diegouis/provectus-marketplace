# proagent-data

Provectus Data practice plugin for Claude Code. Provides production-tested data pipeline engineering, analytics, data warehousing, dbt transformations, SQL optimization, data quality, schema design, business analytics (KPI dashboards, data storytelling), bioinformatics pipelines (Nextflow, Allotrope), analytics infrastructure, and Excel spreadsheet patterns drawn from actual Provectus engineering repositories.

## Installation

### Option 1: Copy to your project

Copy the `proagent-data/` directory into your project's `.claude/plugins/` directory:

```bash
cp -r proagent-data/ /path/to/your-project/.claude/plugins/proagent-data/
```

### Option 2: Reference from the marketplace

If your project uses the Provectus marketplace plugin loader, add the plugin to your configuration:

```json
{
  "plugins": ["proagent-data"]
}
```

### Option 3: Symlink for development

```bash
ln -s /path/to/provectus-marketplace/plugins/proagent-data /path/to/your-project/.claude/plugins/proagent-data
```

## Prerequisites

Depending on which operations you use, install the following CLI tools:

| Tool | Required For | Install |
|------|-------------|---------|
| `psql` | PostgreSQL operations | [postgresql.org](https://www.postgresql.org/download/) |
| `dbt` | dbt transformations | [docs.getdbt.com](https://docs.getdbt.com/docs/installation) |
| `python` | Airflow DAGs, Spark jobs, EDA | [python.org](https://www.python.org/downloads/) |
| `sqlfluff` | SQL linting | `pip install sqlfluff` |
| `aws` | AWS S3, Redshift, Glue, Athena | [aws.amazon.com](https://aws.amazon.com/cli/) |
| `gcloud` / `bq` | GCP BigQuery, Cloud SQL, GCS | [cloud.google.com](https://cloud.google.com/sdk/docs/install) |
| `gh` | GitHub integration | [cli.github.com](https://cli.github.com/) |
| `snowsql` | Snowflake operations | [snowflake.com](https://docs.snowflake.com/en/user-guide/snowsql) |

## Usage

### Hub Command

View all available Data capabilities:

```
/proagent-data-hub
```

### Run Commands

Execute data operations:

```
/proagent-data-run build-pipeline       # Build an ETL/ELT pipeline with Airflow, dbt, or Spark
/proagent-data-run design-schema        # Design a database or warehouse schema
/proagent-data-run optimize-queries     # Analyze and optimize SQL query performance
/proagent-data-run setup-warehouse      # Set up a data warehouse with dimensional modeling
/proagent-data-run data-quality-check   # Run data quality checks and generate a report
/proagent-data-run build-dashboard      # Design a KPI dashboard with metrics and visualizations
/proagent-data-run build-bio-pipeline   # Build a Nextflow bioinformatics pipeline
/proagent-data-run analytics-infra      # Set up analytics tracking and reporting infrastructure
```

### Review Command

Review data engineering artifacts for best practices, performance, and quality:

```
/proagent-data-review                   # Auto-detect and review all data artifacts
/proagent-data-review models/           # Review dbt models
/proagent-data-review slow_query.sql    # Review a specific SQL query
```

The review command checks:
- dbt models for naming conventions, test coverage, and materialization strategy
- SQL queries for anti-patterns, performance issues, and correctness
- Database schemas for missing constraints, indexes, and design issues
- Airflow DAGs for retry policies, idempotency, and observability
- Data quality configurations for coverage and alerting
- Spark jobs for partitioning, caching, and memory management
- Nextflow pipelines for DSL2 patterns, containers, and resource configuration
- KPI dashboards for metric definitions, thresholds, and time comparisons
- Analytics infrastructure for event tracking schemas and reporting pipelines

### Using the Data Specialist Agent

The plugin includes a data specialist agent that can be invoked for complex data engineering tasks:

```
Ask the data-specialist to design a star schema for e-commerce analytics
```

### Using the Skill Directly

The data assistant skill is available for any data task:

```
Use the data-assistant skill to build an incremental dbt model for order events
```

## What This Plugin Provides

### Patterns and Templates
- Airflow DAG with sensors, SQL operators, quality checks, and retry configuration
- dbt project structure with staging, intermediate, and marts layers
- Incremental model patterns (merge, delete+insert, insert_overwrite)
- PostgreSQL schema with indexes, constraints, triggers, and partitioning
- Star schema data warehouse with fact tables, dimension tables, and date dimension
- Window function queries for running totals, rankings, and sessionization
- PySpark ETL job with adaptive execution and partition optimization
- Great Expectations validation suite for comprehensive data quality
- SQL-based data quality checks for row counts, nulls, integrity, and volume anomalies
- KPI dashboard design with metric hierarchies, thresholds, and time comparisons
- Data storytelling framework for presenting insights to business stakeholders
- Nextflow DSL2 bioinformatics pipelines with containerized processes
- Allotrope ASM instrument data conversion patterns
- Analytics infrastructure (event tracking, KPI reporting, SQL query libraries)
- Excel spreadsheet read/write/transform operations

### External Reference Assets
- `agents/plugins/data-engineering/` - Data engineer agent, pipeline command, Airflow/dbt/Spark skills
- `agents/plugins/business-analytics/` - Business analyst agent, KPI dashboard and storytelling skills
- `casdk-harness/src/harness/agents/configs/` - PostgreSQL expert and SQL expert subagents
- `proagent-repo/infrastructure/analytics/` - Usage tracker, reporter, and analytics queries
- `provectus-marketplace/testing/knowledge-work-plugins/bio-research/skills/` - Nextflow and Allotrope skills
- `skills/skills/xlsx/SKILL.md` - Excel spreadsheet skill

### Automated Checks
- Schema validation hooks that prevent destructive operations (DROP, TRUNCATE without confirmation)
- SQL linting hooks that catch anti-patterns (SELECT *, implicit joins, unnecessary UNION)
- dbt test coverage checks that verify models have adequate quality assertions
- Migration safety checks for lock contention, rollback reversibility, and NOT NULL safety
- Post-query analysis for long-running operations and failed dbt tests

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |
| Rube | `rube.app/mcp` | SaaS automation gateway (Google Sheets, Airtable, Supabase, etc.) |

## Version

- Plugin version: 0.3.0
- Category: data
- Author: Provectus
