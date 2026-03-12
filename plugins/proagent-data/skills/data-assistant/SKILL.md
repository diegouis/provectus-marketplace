---
name: data-assistant
description: Engineering Data Pipelines & Analytics - ETL/ELT design, dbt transformation patterns, data warehousing, SQL optimization, Airflow orchestration, Spark processing, data quality frameworks, data modeling, exploratory data analysis, business analytics (KPI dashboards, data storytelling), bioinformatics pipelines (Nextflow, Allotrope), analytics infrastructure, and Excel spreadsheet operations. Use when performing any data engineering, analytics, or database task.
---

# Engineering Data Pipelines & Analytics

Comprehensive data engineering skill covering pipeline development, warehouse design, dbt transformations, SQL optimization, data quality assurance, and analytics.

## When to Use This Skill

- Building ETL/ELT data pipelines with Airflow, dbt, or Spark
- Designing data warehouse schemas (star schema, snowflake schema, Data Vault)
- Writing and optimizing SQL queries for PostgreSQL, Snowflake, or BigQuery
- Implementing dbt transformation layers (staging, intermediate, marts)
- Setting up data quality checks and validation frameworks
- Performing exploratory data analysis on datasets
- Designing database schemas for analytics and reporting
- Creating KPI dashboards and data storytelling visualizations
- Building bioinformatics pipelines or analytics infrastructure

## When Invoked Without Clear Intent

**MANDATORY**: You MUST call the `AskUserQuestion` tool — do NOT render these options as text:

AskUserQuestion(
  header: "Data",
  question: "What data engineering topic do you need help with?",
  options: [
    { label: "Data Pipelines", description: "ETL/ELT, Airflow DAGs, pipeline stages" },
    { label: "dbt Models", description: "Staging/intermediate/marts, incremental, macros, testing" },
    { label: "SQL Optimization", description: "EXPLAIN ANALYZE, indexes, window functions, tuning" },
    { label: "Data Quality", description: "Great Expectations, dbt tests, freshness, anomaly detection" }
  ]
)

If the user selects "Other", present: Schema Design (star schema, warehousing), EDA & Analytics, Domain-Specific (KPI dashboards, bioinformatics, Excel).

## Reference Routing

> **CONTEXT GUARD**: Load reference files only when the user's request matches a specific topic below. Do NOT load all references upfront.

| User Intent | Reference File |
|---|---|
| ETL/ELT pipelines, Airflow DAGs, pipeline stages, extract/transform/load | `references/pipeline-patterns.md` |
| dbt models, staging/intermediate/marts, incremental, macros, sources, testing | `references/dbt-patterns.md` |
| PostgreSQL schemas, star schema, data warehouse design, dimensional modeling, SCD | `references/schema-design.md` |
| SQL optimization, EXPLAIN ANALYZE, indexes, window functions, PostgreSQL tuning, partitioning | `references/sql-optimization.md` |
| Data quality, Great Expectations, dbt tests, freshness, volume anomaly detection | `references/quality-framework.md` |
| EDA, pandas analysis, Spark/PySpark, correlation analysis, data profiling | `references/eda-analytics.md` |
| KPI dashboards, data storytelling, bioinformatics, Nextflow, Allotrope, analytics infra, Excel | `references/domain-specific.md` |

## External Subagent References

> **CONTEXT GUARD**: Do NOT read these external agent files unless the user specifically needs deep database expertise beyond what this skill provides.

- **db-postgres-expert** (`casdk-harness/src/harness/agents/configs/db-postgres-expert.md`)
- **db-sql-expert** (`casdk-harness/src/harness/agents/configs/db-sql-expert.md`)

## Composio App Automations

Integrates with Google Sheets, Airtable, Supabase, Amplitude, Mixpanel, PostHog, and Segment via the Rube MCP server (`RUBE_SEARCH_TOOLS` → `RUBE_MANAGE_CONNECTIONS` → `RUBE_MULTI_EXECUTE_TOOL`).

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate pipeline flow diagrams, warehouse schema maps, Airflow DAG visualizations, and data quality checkpoint flows. Describe what you need in natural language.
