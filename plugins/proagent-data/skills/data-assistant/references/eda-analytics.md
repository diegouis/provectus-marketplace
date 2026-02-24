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
