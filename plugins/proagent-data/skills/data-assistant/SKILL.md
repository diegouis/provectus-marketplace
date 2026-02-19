---
name: data-assistant
description: Engineering Data Pipelines & Analytics - ETL/ELT design, dbt transformation patterns, data warehousing, SQL optimization, Airflow orchestration, Spark processing, data quality frameworks, data modeling, and exploratory data analysis. Use when performing any data engineering, analytics, or database task.
---

# Engineering Data Pipelines & Analytics

Comprehensive data engineering skill covering the full lifecycle of data pipeline development, warehouse design, transformation logic, query optimization, data quality assurance, and analytics. Built from production-tested patterns across Provectus engineering teams.

## When to Use This Skill

- Building ETL/ELT data pipelines with Airflow, dbt, or Spark
- Designing data warehouse schemas (star schema, snowflake schema, Data Vault)
- Writing and optimizing SQL queries for PostgreSQL, Snowflake, or BigQuery
- Implementing dbt transformation layers (staging, intermediate, marts)
- Setting up data quality checks and validation frameworks
- Performing exploratory data analysis on datasets
- Designing database schemas for relational and NoSQL databases
- Creating data models for analytics and reporting

## Data Pipeline Architecture

### Pipeline Design Patterns

Every data pipeline should follow this ordered progression:

1. **Extract** - Ingest data from source systems (APIs, databases, files, streams)
2. **Validate** - Check data completeness, freshness, and schema conformance
3. **Transform** - Clean, normalize, join, aggregate, and enrich data
4. **Load** - Write to target data warehouse or data lake
5. **Test** - Run data quality assertions on output tables
6. **Document** - Update data catalog and lineage metadata

### Airflow DAG Pattern

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from airflow.sensors.sql import SqlSensor

default_args = {
    'owner': 'data-engineering',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=30),
    'execution_timeout': timedelta(hours=2),
}

with DAG(
    dag_id='etl_customer_analytics',
    default_args=default_args,
    description='Daily customer analytics ETL pipeline',
    schedule_interval='0 6 * * *',  # 6 AM UTC daily
    start_date=datetime(2024, 1, 1),
    catchup=False,
    max_active_runs=1,
    tags=['analytics', 'daily', 'customer'],
) as dag:

    # Sensor: wait for source data to be available
    wait_for_source = SqlSensor(
        task_id='wait_for_source_data',
        conn_id='source_postgres',
        sql="""
            SELECT COUNT(*) FROM source_events
            WHERE event_date = '{{ ds }}'
            HAVING COUNT(*) > 0
        """,
        mode='poke',
        poke_interval=300,
        timeout=3600,
    )

    # Extract: pull data from source system
    extract_events = SQLExecuteQueryOperator(
        task_id='extract_events',
        conn_id='source_postgres',
        sql="""
            COPY (
                SELECT
                    event_id,
                    user_id,
                    event_type,
                    event_properties,
                    created_at
                FROM source_events
                WHERE event_date = '{{ ds }}'
            ) TO STDOUT WITH CSV HEADER
        """,
    )

    # Transform: clean and aggregate
    transform_metrics = SQLExecuteQueryOperator(
        task_id='transform_customer_metrics',
        conn_id='warehouse',
        sql="""
            INSERT INTO analytics.customer_daily_metrics (
                metric_date,
                customer_id,
                total_events,
                unique_sessions,
                total_revenue,
                avg_session_duration_seconds,
                is_active
            )
            SELECT
                '{{ ds }}'::DATE AS metric_date,
                e.user_id AS customer_id,
                COUNT(*) AS total_events,
                COUNT(DISTINCT e.session_id) AS unique_sessions,
                COALESCE(SUM(
                    CASE WHEN e.event_type = 'purchase'
                    THEN (e.event_properties->>'amount')::DECIMAL(10,2)
                    ELSE 0 END
                ), 0) AS total_revenue,
                AVG(EXTRACT(EPOCH FROM (e.session_end - e.session_start))) AS avg_session_duration_seconds,
                TRUE AS is_active
            FROM staging.events e
            WHERE e.event_date = '{{ ds }}'
            GROUP BY e.user_id
            ON CONFLICT (metric_date, customer_id) DO UPDATE SET
                total_events = EXCLUDED.total_events,
                unique_sessions = EXCLUDED.unique_sessions,
                total_revenue = EXCLUDED.total_revenue,
                avg_session_duration_seconds = EXCLUDED.avg_session_duration_seconds,
                is_active = EXCLUDED.is_active
        """,
    )

    # Quality check: validate output
    quality_check = SQLExecuteQueryOperator(
        task_id='data_quality_check',
        conn_id='warehouse',
        sql="""
            DO $$
            DECLARE
                row_count INTEGER;
                null_count INTEGER;
                negative_revenue INTEGER;
            BEGIN
                SELECT COUNT(*) INTO row_count
                FROM analytics.customer_daily_metrics
                WHERE metric_date = '{{ ds }}';

                IF row_count = 0 THEN
                    RAISE EXCEPTION 'No rows loaded for date {{ ds }}';
                END IF;

                SELECT COUNT(*) INTO null_count
                FROM analytics.customer_daily_metrics
                WHERE metric_date = '{{ ds }}'
                  AND customer_id IS NULL;

                IF null_count > 0 THEN
                    RAISE EXCEPTION 'Found % rows with NULL customer_id', null_count;
                END IF;

                SELECT COUNT(*) INTO negative_revenue
                FROM analytics.customer_daily_metrics
                WHERE metric_date = '{{ ds }}'
                  AND total_revenue < 0;

                IF negative_revenue > 0 THEN
                    RAISE EXCEPTION 'Found % rows with negative revenue', negative_revenue;
                END IF;

                RAISE NOTICE 'Quality checks passed: % rows loaded', row_count;
            END $$;
        """,
    )

    wait_for_source >> extract_events >> transform_metrics >> quality_check
```

## dbt Transformation Patterns

### Model Layers (Medallion Architecture)

```
sources/          Raw data definitions
    |
staging/          1:1 with source, light cleaning
    |
intermediate/     Business logic, joins, aggregations
    |
marts/            Final analytics tables
```

### Naming Conventions

| Layer        | Prefix         | Example                       |
| ------------ | -------------- | ----------------------------- |
| Staging      | `stg_`         | `stg_stripe__payments`        |
| Intermediate | `int_`         | `int_payments_pivoted`        |
| Marts        | `dim_`, `fct_` | `dim_customers`, `fct_orders` |

### dbt Project Configuration

```yaml
# dbt_project.yml
name: "analytics"
version: "1.0.0"
profile: "analytics"

model-paths: ["models"]
analysis-paths: ["analyses"]
test-paths: ["tests"]
seed-paths: ["seeds"]
macro-paths: ["macros"]

vars:
  start_date: "2020-01-01"

models:
  analytics:
    staging:
      +materialized: view
      +schema: staging
    intermediate:
      +materialized: ephemeral
    marts:
      +materialized: table
      +schema: analytics
```

### Staging Model Pattern

```sql
-- models/staging/stripe/stg_stripe__customers.sql
with source as (
    select * from {{ source('stripe', 'customers') }}
),

renamed as (
    select
        -- ids
        id as customer_id,

        -- strings
        lower(email) as email,
        name as customer_name,

        -- timestamps
        created as created_at,

        -- metadata
        _fivetran_synced as _loaded_at

    from source
)

select * from renamed
```

### Incremental Model Pattern

```sql
-- models/staging/stripe/stg_stripe__payments.sql
{{
    config(
        materialized='incremental',
        unique_key='payment_id',
        on_schema_change='append_new_columns'
    )
}}

with source as (
    select * from {{ source('stripe', 'payments') }}

    {% if is_incremental() %}
    where _fivetran_synced > (select max(_loaded_at) from {{ this }})
    {% endif %}
),

renamed as (
    select
        -- ids
        id as payment_id,
        customer_id,
        invoice_id,

        -- amounts (convert cents to dollars)
        amount / 100.0 as amount,
        amount_refunded / 100.0 as amount_refunded,

        -- status
        status as payment_status,

        -- timestamps
        created as created_at,

        -- metadata
        _fivetran_synced as _loaded_at

    from source
)

select * from renamed
```

### Mart Model Pattern (Dimension Table)

```sql
-- models/marts/core/dim_customers.sql
{{
    config(
        materialized='table',
        unique_key='customer_id'
    )
}}

with customers as (
    select * from {{ ref('int_payments_pivoted_to_customer') }}
),

orders as (
    select * from {{ ref('stg_shopify__orders') }}
),

order_summary as (
    select
        customer_id,
        count(*) as total_orders,
        sum(total_price) as total_order_value,
        min(created_at) as first_order_at,
        max(created_at) as last_order_at
    from orders
    group by customer_id
),

final as (
    select
        {{ dbt_utils.generate_surrogate_key(['customers.customer_id']) }} as customer_key,
        customers.customer_id,
        customers.email,
        customers.customer_created_at,
        customers.total_payments,
        customers.successful_payments,
        customers.lifetime_value,
        customers.first_payment_at,
        customers.last_payment_at,
        coalesce(order_summary.total_orders, 0) as total_orders,
        coalesce(order_summary.total_order_value, 0) as total_order_value,
        order_summary.first_order_at,
        order_summary.last_order_at,
        case
            when customers.lifetime_value >= 1000 then 'high'
            when customers.lifetime_value >= 100 then 'medium'
            else 'low'
        end as customer_tier,
        current_timestamp as _loaded_at
    from customers
    left join order_summary using (customer_id)
)

select * from final
```

### Fact Table with Incremental Strategy

```sql
-- models/marts/core/fct_orders.sql
{{
    config(
        materialized='incremental',
        unique_key='order_id',
        incremental_strategy='merge'
    )
}}

with orders as (
    select * from {{ ref('stg_shopify__orders') }}

    {% if is_incremental() %}
    where updated_at > (select max(updated_at) from {{ this }})
    {% endif %}
),

customers as (
    select * from {{ ref('dim_customers') }}
),

final as (
    select
        orders.order_id,
        customers.customer_key,
        orders.customer_id,
        orders.order_status,
        orders.fulfillment_status,
        orders.payment_status,
        orders.subtotal,
        orders.tax,
        orders.shipping,
        orders.total_price,
        orders.total_discount,
        orders.item_count,
        orders.created_at,
        orders.updated_at,
        orders.fulfilled_at,
        current_timestamp as _loaded_at
    from orders
    left join customers on orders.customer_id = customers.customer_id
)

select * from final
```

### dbt Testing and Documentation

```yaml
# models/marts/core/_core__models.yml
version: 2

models:
  - name: dim_customers
    description: Customer dimension with payment and order metrics
    columns:
      - name: customer_key
        description: Surrogate key for the customer dimension
        tests:
          - unique
          - not_null
      - name: customer_id
        description: Natural key from source system
        tests:
          - unique
          - not_null
      - name: customer_tier
        description: Customer value tier based on lifetime value
        tests:
          - accepted_values:
              values: ["high", "medium", "low"]
      - name: lifetime_value
        description: Total amount paid by customer
        tests:
          - dbt_utils.expression_is_true:
              expression: ">= 0"

  - name: fct_orders
    description: Order fact table with all order transactions
    tests:
      - dbt_utils.recency:
          datepart: day
          field: created_at
          interval: 1
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: customer_key
        tests:
          - not_null
          - relationships:
              to: ref('dim_customers')
              field: customer_key
```

### Source Definitions with Freshness

```yaml
# models/staging/stripe/_stripe__sources.yml
version: 2

sources:
  - name: stripe
    description: Raw Stripe data loaded via Fivetran
    database: raw
    schema: stripe
    loader: fivetran
    loaded_at_field: _fivetran_synced
    freshness:
      warn_after: { count: 12, period: hour }
      error_after: { count: 24, period: hour }
    tables:
      - name: customers
        description: Stripe customer records
        columns:
          - name: id
            description: Primary key
            tests:
              - unique
              - not_null
      - name: payments
        description: Stripe payment transactions
        columns:
          - name: id
            tests:
              - unique
              - not_null
          - name: customer_id
            tests:
              - not_null
              - relationships:
                  to: source('stripe', 'customers')
                  field: id
```

### dbt Macros for DRY Code

```sql
-- macros/cents_to_dollars.sql
{% macro cents_to_dollars(column_name, precision=2) %}
    round({{ column_name }} / 100.0, {{ precision }})
{% endmacro %}

-- macros/limit_data_in_dev.sql
{% macro limit_data_in_dev(column_name, days=3) %}
    {% if target.name == 'dev' %}
        where {{ column_name }} >= dateadd(day, -{{ days }}, current_date)
    {% endif %}
{% endmacro %}
```

### dbt Commands Reference

```bash
# Development
dbt run                          # Run all models
dbt run --select staging         # Run staging models only
dbt run --select +fct_orders     # Run fct_orders and its upstream
dbt run --select fct_orders+     # Run fct_orders and its downstream
dbt run --full-refresh           # Rebuild incremental models

# Testing
dbt test                         # Run all tests
dbt test --select stg_stripe     # Test specific models
dbt build                        # Run + test in DAG order

# Documentation
dbt docs generate                # Generate docs
dbt docs serve                   # Serve docs locally

# Debugging
dbt compile                      # Compile SQL without running
dbt debug                        # Test connection
dbt ls --select tag:critical     # List models by tag
```

## Database Schema Design

### Relational Schema Design Workflow

1. **Analyze Data Requirements** - Identify entities, attributes, relationships, data volume, and query patterns
2. **Choose Database Type** - PostgreSQL for structured data with ACID; MongoDB for flexible schema; Redis for caching
3. **Design Tables** - Create tables with proper primary keys, data types, and normalization to 3NF
4. **Define Relationships** - One-to-many via foreign keys, many-to-many via junction tables, one-to-one with unique constraints
5. **Add Constraints** - Primary keys, foreign keys, NOT NULL, CHECK, and DEFAULT values
6. **Create Indexes** - Index foreign keys, WHERE columns, JOIN columns, and create composite indexes for multi-column queries
7. **Plan for Scalability** - Partition large tables, plan sharding, implement soft deletes, and design archival strategies

### PostgreSQL Schema Pattern

```sql
-- Users table
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  username VARCHAR(50) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  email_verified BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_login_at TIMESTAMP
);

-- Orders table
CREATE TABLE orders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  order_number VARCHAR(50) UNIQUE NOT NULL,
  status VARCHAR(20) DEFAULT 'pending' CHECK (
    status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled', 'refunded')
  ),
  subtotal DECIMAL(10, 2) NOT NULL,
  tax DECIMAL(10, 2) NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(3) DEFAULT 'USD',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for common queries
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_created_at ON orders(created_at DESC);

-- Auto-update timestamps
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_orders_updated_at BEFORE UPDATE ON orders
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

### Data Warehouse Schema Pattern (Star Schema)

```sql
-- Dimension: Date
CREATE TABLE dim_date (
  date_key INTEGER PRIMARY KEY,
  full_date DATE NOT NULL,
  year INTEGER NOT NULL,
  quarter INTEGER NOT NULL,
  month INTEGER NOT NULL,
  month_name VARCHAR(20) NOT NULL,
  week_of_year INTEGER NOT NULL,
  day_of_week INTEGER NOT NULL,
  day_name VARCHAR(20) NOT NULL,
  is_weekend BOOLEAN NOT NULL,
  is_holiday BOOLEAN DEFAULT FALSE,
  fiscal_year INTEGER,
  fiscal_quarter INTEGER
);

-- Dimension: Customer
CREATE TABLE dim_customer (
  customer_key BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  customer_id VARCHAR(50) NOT NULL,
  email VARCHAR(255),
  customer_name VARCHAR(200),
  segment VARCHAR(50),
  tier VARCHAR(20),
  acquisition_channel VARCHAR(100),
  first_order_date DATE,
  is_current BOOLEAN DEFAULT TRUE,
  valid_from TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  valid_to TIMESTAMP DEFAULT '9999-12-31'
);

-- Dimension: Product
CREATE TABLE dim_product (
  product_key BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  product_id VARCHAR(50) NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  category VARCHAR(100),
  subcategory VARCHAR(100),
  brand VARCHAR(100),
  unit_price DECIMAL(10, 2),
  is_active BOOLEAN DEFAULT TRUE,
  valid_from TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  valid_to TIMESTAMP DEFAULT '9999-12-31'
);

-- Fact: Sales
CREATE TABLE fct_sales (
  sale_key BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  date_key INTEGER NOT NULL REFERENCES dim_date(date_key),
  customer_key BIGINT NOT NULL REFERENCES dim_customer(customer_key),
  product_key BIGINT NOT NULL REFERENCES dim_product(product_key),
  order_id VARCHAR(50) NOT NULL,
  quantity INTEGER NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  discount_amount DECIMAL(10, 2) DEFAULT 0,
  tax_amount DECIMAL(10, 2) DEFAULT 0,
  total_amount DECIMAL(10, 2) NOT NULL,
  loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) PARTITION BY RANGE (date_key);

-- Partition by year
CREATE TABLE fct_sales_2024 PARTITION OF fct_sales
  FOR VALUES FROM (20240101) TO (20250101);
CREATE TABLE fct_sales_2025 PARTITION OF fct_sales
  FOR VALUES FROM (20250101) TO (20260101);

-- Indexes on fact table
CREATE INDEX idx_fct_sales_date ON fct_sales(date_key);
CREATE INDEX idx_fct_sales_customer ON fct_sales(customer_key);
CREATE INDEX idx_fct_sales_product ON fct_sales(product_key);
CREATE INDEX idx_fct_sales_order ON fct_sales(order_id);
```

## SQL Query Optimization

### Using EXPLAIN ANALYZE

```sql
-- Always analyze execution plans for slow queries
EXPLAIN (ANALYZE, BUFFERS, TIMING)
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.name
HAVING COUNT(o.id) > 5;

-- Look for:
-- 1. Sequential Scans on large tables (add indexes)
-- 2. High "Buffers: shared read" (cache misses)
-- 3. Nested Loop joins with large datasets (consider Hash Join)
-- 4. Actual time >> planned time (run ANALYZE to update statistics)
```

### Common Optimization Patterns

```sql
-- Use covering indexes to avoid table lookups
CREATE INDEX idx_users_covering
ON users(email) INCLUDE (name, created_at);

-- Partial index for filtered queries
CREATE INDEX idx_active_users ON users(email)
WHERE status = 'active';

-- BRIN index for large time-series tables
CREATE INDEX idx_logs_timestamp ON logs USING BRIN(timestamp);

-- GIN index for JSONB and full-text search
CREATE INDEX idx_products_tags ON products USING GIN(tags);
CREATE INDEX idx_docs_content ON documents USING GIN(to_tsvector('english', content));

-- Batch operations for better performance
INSERT INTO users (email, name) VALUES
    ('user1@example.com', 'User 1'),
    ('user2@example.com', 'User 2'),
    ('user100@example.com', 'User 100');
```

### Window Functions for Analytics

```sql
-- Running total and ranking
SELECT
    order_date,
    customer_id,
    total_amount,
    SUM(total_amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY total_amount DESC
    ) AS order_rank,
    LAG(total_amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS previous_order_amount,
    total_amount - LAG(total_amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS amount_change
FROM orders;

-- Sessionization with window functions
WITH events_with_gaps AS (
    SELECT
        user_id,
        event_timestamp,
        EXTRACT(EPOCH FROM (
            event_timestamp - LAG(event_timestamp) OVER (
                PARTITION BY user_id ORDER BY event_timestamp
            )
        )) AS seconds_since_last_event
    FROM events
),
sessions AS (
    SELECT
        *,
        SUM(CASE WHEN seconds_since_last_event > 1800 OR seconds_since_last_event IS NULL
            THEN 1 ELSE 0 END) OVER (
            PARTITION BY user_id ORDER BY event_timestamp
        ) AS session_id
    FROM events_with_gaps
)
SELECT
    user_id,
    session_id,
    MIN(event_timestamp) AS session_start,
    MAX(event_timestamp) AS session_end,
    COUNT(*) AS event_count,
    EXTRACT(EPOCH FROM (MAX(event_timestamp) - MIN(event_timestamp))) AS session_duration_seconds
FROM sessions
GROUP BY user_id, session_id;
```

## PostgreSQL Performance Tuning

### Memory Configuration

```conf
# postgresql.conf
shared_buffers = 8GB            # 25-40% of RAM
work_mem = 8MB                  # OLTP: many small connections
maintenance_work_mem = 1GB      # For VACUUM, CREATE INDEX
effective_cache_size = 24GB     # 50-75% of total RAM

# WAL Configuration
wal_buffers = 16MB
checkpoint_timeout = 15min
max_wal_size = 4GB

# Query Planner (SSD storage)
random_page_cost = 1.1
effective_io_concurrency = 200
```

### Monitoring Cache Hit Ratio

```sql
-- Should be 99%+
SELECT
    sum(heap_blks_read) as heap_read,
    sum(heap_blks_hit) as heap_hit,
    sum(heap_blks_hit) / NULLIF(sum(heap_blks_hit) + sum(heap_blks_read), 0) * 100
        as cache_hit_ratio
FROM pg_statio_user_tables;

-- Find unused indexes
SELECT
    schemaname, tablename, indexname,
    idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY pg_relation_size(indexrelid) DESC;

-- Most expensive queries
SELECT
    query, calls, mean_exec_time, total_exec_time, rows
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 20;
```

### Partitioning for Large Tables

```sql
-- Range partitioning by date
CREATE TABLE orders (
    id BIGSERIAL,
    customer_id INT,
    order_date DATE NOT NULL,
    total DECIMAL(10,2)
) PARTITION BY RANGE (order_date);

CREATE TABLE orders_2024_q1 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');
CREATE TABLE orders_2024_q2 PARTITION OF orders
    FOR VALUES FROM ('2024-04-01') TO ('2024-07-01');
```

## Data Quality Framework

### Great Expectations Pattern

```python
import great_expectations as gx

context = gx.get_context()

# Define expectations for a dataset
validator = context.sources.pandas_default.read_csv("data/customers.csv")

# Schema expectations
validator.expect_table_columns_to_match_ordered_list([
    "customer_id", "email", "name", "created_at", "tier"
])

# Completeness expectations
validator.expect_column_values_to_not_be_null("customer_id")
validator.expect_column_values_to_not_be_null("email")

# Uniqueness expectations
validator.expect_column_values_to_be_unique("customer_id")
validator.expect_column_values_to_be_unique("email")

# Format expectations
validator.expect_column_values_to_match_regex("email", r"^[^@]+@[^@]+\.[^@]+$")

# Range expectations
validator.expect_column_values_to_be_in_set("tier", ["high", "medium", "low"])

# Statistical expectations
validator.expect_column_mean_to_be_between("lifetime_value", min_value=0, max_value=100000)
validator.expect_table_row_count_to_be_between(min_value=1000, max_value=10000000)

results = validator.validate()
```

### SQL-Based Data Quality Checks

```sql
-- Row count check
SELECT
    'row_count' AS check_name,
    CASE WHEN COUNT(*) > 0 THEN 'PASS' ELSE 'FAIL' END AS result,
    COUNT(*) AS actual_value
FROM analytics.customer_daily_metrics
WHERE metric_date = CURRENT_DATE - INTERVAL '1 day';

-- Null check on critical columns
SELECT
    'null_check' AS check_name,
    CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END AS result,
    COUNT(*) AS null_count
FROM analytics.customer_daily_metrics
WHERE metric_date = CURRENT_DATE - INTERVAL '1 day'
  AND (customer_id IS NULL OR metric_date IS NULL);

-- Referential integrity check
SELECT
    'referential_integrity' AS check_name,
    CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END AS result,
    COUNT(*) AS orphan_count
FROM fct_orders f
LEFT JOIN dim_customer d ON f.customer_key = d.customer_key
WHERE d.customer_key IS NULL;

-- Freshness check
SELECT
    'data_freshness' AS check_name,
    CASE WHEN MAX(loaded_at) > CURRENT_TIMESTAMP - INTERVAL '24 hours'
         THEN 'PASS' ELSE 'FAIL' END AS result,
    MAX(loaded_at) AS last_load_time
FROM analytics.customer_daily_metrics;

-- Volume anomaly detection (compare to 7-day average)
WITH daily_counts AS (
    SELECT
        metric_date,
        COUNT(*) AS row_count
    FROM analytics.customer_daily_metrics
    WHERE metric_date >= CURRENT_DATE - INTERVAL '8 days'
    GROUP BY metric_date
),
stats AS (
    SELECT
        AVG(row_count) AS avg_count,
        STDDEV(row_count) AS stddev_count
    FROM daily_counts
    WHERE metric_date < CURRENT_DATE - INTERVAL '1 day'
)
SELECT
    'volume_anomaly' AS check_name,
    CASE
        WHEN ABS(d.row_count - s.avg_count) > 3 * s.stddev_count THEN 'FAIL'
        WHEN ABS(d.row_count - s.avg_count) > 2 * s.stddev_count THEN 'WARN'
        ELSE 'PASS'
    END AS result,
    d.row_count AS actual_count,
    s.avg_count AS expected_count
FROM daily_counts d
CROSS JOIN stats s
WHERE d.metric_date = CURRENT_DATE - INTERVAL '1 day';
```

## Exploratory Data Analysis

### Systematic EDA Workflow

1. **Load and Inspect** - Check dimensions, column types, memory usage, first/last rows
2. **Data Quality** - Missing values, duplicates, outliers, data entry errors
3. **Distributions** - Summary statistics, histograms, bar charts, skewness
4. **Relationships** - Correlations, scatter plots, box plots by category
5. **Patterns** - Segment by categories, compare subgroups, identify trends
6. **Document** - Note quality issues, patterns, assumptions, next steps

### Quick EDA Function

```python
import pandas as pd
import numpy as np

def quick_eda(df, target=None):
    """Perform quick exploratory data analysis"""
    print(f"Shape: {df.shape}")
    print(f"Memory: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

    # Missing values
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("\nMissing Values:")
        print(missing[missing > 0].sort_values(ascending=False))

    # Numerical summary
    print("\nNumerical Features Summary:")
    print(df.describe())

    # Categorical summary
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        n_unique = df[col].nunique()
        print(f"\n{col}: {n_unique} unique values")
        if n_unique <= 10:
            print(f"  {df[col].value_counts().to_dict()}")

    # Top correlations
    num_cols = df.select_dtypes(include=[np.number]).columns
    if len(num_cols) > 1:
        corr_matrix = df[num_cols].corr()
        corr_pairs = []
        for i in range(len(corr_matrix)):
            for j in range(i+1, len(corr_matrix)):
                corr_pairs.append({
                    'Feature 1': corr_matrix.index[i],
                    'Feature 2': corr_matrix.columns[j],
                    'Correlation': abs(corr_matrix.iloc[i, j])
                })
        corr_df = pd.DataFrame(corr_pairs).sort_values('Correlation', ascending=False)
        print("\nTop 5 Correlations:")
        print(corr_df.head())
```

## Spark Processing Patterns

### PySpark ETL Pattern

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("customer_analytics") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Read from source
events_df = spark.read \
    .format("parquet") \
    .option("mergeSchema", "true") \
    .load("s3://data-lake/events/")

# Transform: aggregate customer metrics
customer_metrics = events_df \
    .filter(F.col("event_date") == F.lit("2024-01-15")) \
    .groupBy("customer_id") \
    .agg(
        F.count("*").alias("total_events"),
        F.countDistinct("session_id").alias("unique_sessions"),
        F.sum(
            F.when(F.col("event_type") == "purchase", F.col("amount"))
            .otherwise(0)
        ).alias("total_revenue"),
        F.min("event_timestamp").alias("first_event"),
        F.max("event_timestamp").alias("last_event")
    )

# Write to warehouse
customer_metrics.write \
    .format("parquet") \
    .mode("overwrite") \
    .partitionBy("metric_date") \
    .save("s3://data-warehouse/customer_metrics/")
```

## Composio App Automations

This plugin integrates with Composio-powered SaaS automation skills via the Rube MCP server. These skills connect to real external services for end-to-end workflow automation.

### Available Automations

| Skill | Service | Key Capabilities |
|-------|---------|-----------------|
| googlesheets-automation | Google Sheets | Create/read/update spreadsheets, manage worksheets, batch operations, formula support |
| airtable-automation | Airtable | Create/update records, manage bases and tables, query with filters, field management |
| supabase-automation | Supabase | Database operations, table management, row CRUD, SQL queries via Supabase API |
| amplitude-automation | Amplitude | Event tracking, user analytics, cohort management, chart and dashboard queries |
| mixpanel-automation | Mixpanel | Event ingestion, funnel analysis, user profile management, data export |
| posthog-automation | PostHog | Feature flags, event capture, session recordings, A/B test management |
| segment-automation | Segment | Track events, identify users, manage sources/destinations, data routing |

### Usage Pattern

All Composio automations follow a three-step workflow:

1. **Discover tools**: Use `RUBE_SEARCH_TOOLS` with a use case description to find available tools and their schemas
2. **Connect service**: Use `RUBE_MANAGE_CONNECTIONS` to activate the toolkit connection (handles OAuth automatically)
3. **Execute actions**: Use `RUBE_MULTI_EXECUTE_TOOL` with the discovered tool slug and schema-compliant arguments

### Configuration

Add the Rube MCP server to your `.mcp.json`:
```json
"rube": {
  "url": "https://rube.app/mcp"
}
```

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate interactive diagrams directly in the conversation. Describe what you need in natural language and Excalidraw renders it as an interactive canvas with hand-drawn style.

### When to Use

- Data pipeline and ETL/ELT flow diagrams
- Data warehouse schema and lineage maps
- Airflow DAG and orchestration visualizations
- Data quality checkpoint flow diagrams

### Workflow

1. Describe the diagram you need — be specific about components, relationships, and layout
2. Review the rendered interactive diagram in the chat
3. Request refinements by describing what to change (add/remove/rearrange elements)
4. Use fullscreen mode for detailed editing when needed

### Tips for Effective Diagrams

- Name specific components and their connections (e.g., "API Gateway connects to Auth Service and User Service")
- Specify layout direction when it matters (e.g., "left-to-right flow" or "top-down hierarchy")
- Request specific diagram types (architecture diagram, flowchart, sequence diagram, ER diagram)
- Iterate — start with the overall structure, then refine details
