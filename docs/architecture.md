# Architecture & Pipeline Design

This document details the technical architecture, data flow, and modeling strategies implemented in the pipeline.

## Pipeline Flow

```
[ Raw API / Source ] 
        │
        ▼
   (extract.py) ──► Saves immutable snapshot to data/raw/
        │
        ▼
   (transform.py) ──► Cleans & structures data into Star Schema
        │
        ▼
 (quality_checks.py) ─► Asserts nulls, duplicates & negative values
        │
        ▼
     (load.py) ──► Partitions & saves output to data/processed/partitioned_sales/
```

## 1. Extraction (`src/extract.py`)
Connects to external REST endpoints, fetches raw JSON records, and writes an immutable timestamped file (`ecommerce_snapshot_YYYYMMDD_HHMMSS.json`) to `data/raw/` to guarantee data reproducibility and full lineage tracking.

## 2. Transformation & Modeling (`src/transform.py`)
Parses the raw JSON payload using Pandas and structures the data into a normalized **Star Schema**:
* **`dim_categories`**: Dimension table containing unique product categories and surrogate category IDs.
* **`dim_products`**: Dimension table containing product details, pricing, descriptions, and category mappings.
* **`fact_inventory_sales`**: Fact table holding quantitative analytical metrics (estimated quantities sold and total revenue calculations).

## 3. Data Quality Gates (`src/quality_checks.py`)
Acts as an automated validation barrier before data enters downstream reporting layers. It asserts that:
* Primary keys (`product_id`) contain zero nulls.
* No duplicate primary keys exist.
* Product prices and revenue calculations are strictly non-negative.

## 4. Storage & Partitioning (`src/load.py`)
Simulates a modern cloud data lake structure by organizing processed Parquet files into partition folders based on category (`data/processed/partitioned_sales/category_id=X/`). This enables partition pruning, ensuring analytical queries scan only relevant data subsets.