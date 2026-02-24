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
