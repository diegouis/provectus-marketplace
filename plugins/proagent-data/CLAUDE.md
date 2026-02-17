# Provectus Data Practice Plugin

This plugin provides the Data practice context for the Provectus agentic coding platform. It equips Claude with production-tested data engineering and analytics patterns drawn from actual Provectus engineering repositories.

## Practice Scope

The Data practice covers six operational domains:

1. **Data Pipeline Engineering** - ETL/ELT pipeline design with Airflow DAGs, dbt models, and Spark jobs including incremental loading, retry policies, and idempotent operations
2. **Data Warehousing** - Dimensional modeling with star schema, snowflake schema, and Data Vault 2.0 patterns including SCD Type 2, partitioning, and materialized views
3. **dbt Analytics Engineering** - Model layers (staging, intermediate, marts), source freshness monitoring, testing, macros, and incremental strategies (merge, delete+insert, insert_overwrite)
4. **SQL Optimization** - Query performance analysis with EXPLAIN ANALYZE, index strategies (B-tree, GIN, BRIN, partial, covering), PostgreSQL tuning, and monitoring
5. **Data Quality** - Validation frameworks with Great Expectations and dbt tests, volume anomaly detection, freshness monitoring, and referential integrity checks
6. **Analytics and EDA** - Exploratory data analysis, statistical summaries, correlation analysis, data visualization, window functions, and sessionization queries

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

## Source Repositories

This plugin draws patterns from: proagent, casdk-harness, agents, awesome-claude-skills, specs, tac, claude-ui, and skills.

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
  mcp.json
  CLAUDE.md
  README.md
```
