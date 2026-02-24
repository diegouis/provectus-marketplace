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
