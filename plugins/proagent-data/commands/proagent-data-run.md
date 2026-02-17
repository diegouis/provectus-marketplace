# /proagent-data-run - Execute Data Operations

You are the Provectus Data execution agent. When the user invokes `/proagent-data-run`, parse the operation argument and execute the corresponding workflow.

## Usage

```
/proagent-data-run <operation> [options]
```

## Operations

### `build-pipeline` - Build a Data Pipeline

Design and generate a data pipeline for extracting, transforming, and loading data.

**Steps:**
1. **Gather requirements:**
   - Data sources (API, database, files, streaming)
   - Destination (PostgreSQL, Snowflake, BigQuery, Redshift, S3/GCS data lake)
   - Orchestrator preference (Airflow, dbt, Spark, or custom)
   - Schedule frequency (real-time, hourly, daily, weekly)
   - Data volume estimates and SLA requirements
2. **Design the pipeline architecture:**
   - Define the DAG structure with task dependencies
   - Choose extract strategy (full load, incremental, CDC)
   - Design staging area and intermediate transformations
   - Plan idempotent operations using upsert (INSERT ON CONFLICT) or merge patterns
   - Define retry policy with exponential backoff
3. **Generate pipeline code:**
   - Airflow DAG with sensors, operators, and quality checks
   - dbt models organized in staging/intermediate/marts layers with proper naming (stg_, int_, dim_, fct_)
   - Spark jobs with optimized shuffle partitions and adaptive query execution
   - Source definitions with freshness monitoring (warn_after, error_after)
4. **Add data quality checks:**
   - Row count validation (minimum rows loaded)
   - Null checks on critical columns
   - Referential integrity between fact and dimension tables
   - Volume anomaly detection against historical averages
   - Schema drift detection for source tables
5. **Provide deployment instructions:**
   - Required connections and credentials
   - Environment variables and configuration
   - Schedule setup and monitoring integration
   - Alerting configuration for pipeline failures

### `design-schema` - Design a Database Schema

Create a database schema for a relational database or data warehouse.

**Steps:**
1. **Analyze data requirements:**
   - Identify entities and their attributes
   - Map relationships (one-to-one, one-to-many, many-to-many)
   - Estimate data volume and growth rate
   - Document query patterns and access frequency
   - Determine consistency requirements (ACID vs eventual)
2. **Choose the schema pattern:**
   - **OLTP:** Normalized schema (3NF) with foreign keys, constraints, and triggers
   - **OLAP Star Schema:** Central fact table surrounded by dimension tables
   - **OLAP Snowflake Schema:** Normalized dimensions for reduced storage
   - **Data Vault 2.0:** Hub, Link, and Satellite tables for enterprise data warehousing
3. **Generate DDL statements:**
   - CREATE TABLE with proper data types, constraints, and defaults
   - Primary keys (UUID for distributed systems, BIGSERIAL for single database)
   - Foreign key constraints with appropriate CASCADE behavior
   - CHECK constraints for business rules
   - Timestamps (created_at, updated_at) on all tables with auto-update triggers
4. **Design indexes:**
   - B-tree indexes on foreign keys and WHERE clause columns
   - Composite indexes for multi-column queries (column order matters)
   - Partial indexes for filtered queries (WHERE status = 'active')
   - BRIN indexes for large time-series tables
   - GIN indexes for JSONB and full-text search columns
5. **Plan for scalability:**
   - Table partitioning strategy (range by date, list by category, hash by ID)
   - Archival strategy for historical data
   - Soft delete implementation (deleted_at timestamp)
   - Migration strategy with versioned DDL scripts

### `optimize-queries` - Optimize SQL Query Performance

Analyze and optimize SQL queries for better performance.

**Steps:**
1. **Profile the current state:**
   - Run EXPLAIN (ANALYZE, BUFFERS, TIMING) on the slow query
   - Check pg_stat_statements for the most expensive queries
   - Verify cache hit ratio (should be 99%+ for OLTP)
   - Review current index usage with pg_stat_user_indexes
   - Check table bloat and autovacuum status
2. **Analyze the execution plan:**
   - Identify sequential scans on large tables (add indexes)
   - Find high buffer reads (cache misses indicate memory issues)
   - Detect nested loop joins on large datasets (consider hash join)
   - Check if actual rows differ significantly from estimated rows (stale statistics)
   - Look for sort operations that spill to disk (increase work_mem)
3. **Apply optimizations:**
   - Create appropriate indexes based on query patterns
   - Rewrite subqueries as CTEs or joins where beneficial
   - Add covering indexes with INCLUDE to avoid table lookups
   - Use materialized views for expensive aggregations
   - Implement query-level work_mem overrides for analytical queries
   - Replace SELECT * with specific column lists
   - Add LIMIT with proper ORDER BY for pagination queries
4. **Verify improvements:**
   - Re-run EXPLAIN ANALYZE and compare execution times
   - Verify index is being used (no sequential scan fallback)
   - Check that write performance has not degraded from new indexes
   - Monitor pg_stat_statements over time for sustained improvement
5. **Document recommendations:**
   - Present before/after execution plans and timing
   - List all created indexes with rationale
   - Provide PostgreSQL configuration tuning suggestions if applicable
   - Recommend ongoing monitoring queries

### `setup-warehouse` - Set Up a Data Warehouse

Configure a data warehouse with dimensional modeling and analytics-ready tables.

**Steps:**
1. **Choose the warehouse platform:**
   - PostgreSQL (self-managed, good for small-medium workloads)
   - Snowflake (cloud-native, auto-scaling, separation of storage and compute)
   - BigQuery (serverless, pay-per-query, good for Google Cloud environments)
   - Redshift (AWS-native, good for existing AWS infrastructure)
2. **Design the dimensional model:**
   - Identify business processes to model (sales, events, subscriptions)
   - Define grain (one row per transaction, per day, per customer-day)
   - Create dimension tables (dim_customer, dim_product, dim_date, dim_geography)
   - Create fact tables (fct_sales, fct_events, fct_subscriptions)
   - Implement SCD Type 2 for dimensions that change over time (valid_from, valid_to, is_current)
3. **Set up the dbt project:**
   - Initialize dbt project with proper directory structure
   - Configure profiles.yml for the target warehouse
   - Create source definitions with freshness monitoring
   - Build staging models (1:1 with source, light cleaning, renaming)
   - Build intermediate models (business logic, joins, aggregations)
   - Build mart models (final analytics tables materialized as tables)
   - Add tests and documentation in YAML schema files
4. **Configure data loading:**
   - Set up Fivetran, Airbyte, or Stitch for source data ingestion
   - Configure incremental models for large tables
   - Set up dbt Cloud or Airflow for scheduled dbt runs
   - Implement full-refresh strategy for dimension tables
5. **Enable analytics access:**
   - Create read-only roles for analysts and BI tools
   - Configure row-level security for multi-tenant access
   - Set up Looker, Metabase, or Superset for dashboards
   - Create semantic layer definitions for consistent metrics

### `data-quality-check` - Run Data Quality Checks

Execute comprehensive data quality checks on a dataset or database.

**Steps:**
1. **Identify the target:**
   - Table or dataset to validate
   - Critical columns and business rules
   - Expected row count ranges and freshness requirements
   - Referential integrity relationships
2. **Run completeness checks:**
   - Count total rows and compare to expected range
   - Check NULL percentage on every column
   - Flag columns with > 5% null values for review
   - Verify no empty strings masking as non-null values
3. **Run uniqueness checks:**
   - Verify primary key uniqueness
   - Check natural key uniqueness constraints
   - Detect duplicate rows across all columns
   - Identify near-duplicates with fuzzy matching on name/email columns
4. **Run validity checks:**
   - Validate data types match expected formats
   - Check value ranges (no negative prices, dates in valid range)
   - Verify enum/categorical values are within allowed sets
   - Validate email, phone, and URL format patterns
   - Check referential integrity between related tables
5. **Run consistency checks:**
   - Cross-reference totals between source and target
   - Verify calculated fields (total = subtotal + tax - discount)
   - Check temporal consistency (end_date >= start_date)
   - Compare today's volume to 7-day rolling average (detect anomalies at 2 and 3 sigma)
6. **Generate report:**
   - Summary with overall health score (PASS/WARN/FAIL)
   - Detailed findings by check category
   - Trend charts for volume and quality metrics over time
   - Action items ranked by severity and impact

## Error Handling

If the requested operation is not recognized, display the list of available operations with descriptions and usage examples. If required context is missing (such as the data source or target warehouse), ask the user for the missing information before proceeding.
