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
