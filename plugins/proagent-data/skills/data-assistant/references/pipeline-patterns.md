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
