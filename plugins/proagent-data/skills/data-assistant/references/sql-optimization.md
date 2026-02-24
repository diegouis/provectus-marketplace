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
