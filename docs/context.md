# Project Context & Goals

## Overview
The E-Commerce & Supply Chain Lakehouse Pipeline is a modular, automated data engineering solution designed to bridge the gap between raw, unstructured e-commerce data sources and decision-ready analytical storage. 

## Business Problem Addressed
In modern retail and supply chain operations, data is often fragmented across multiple API endpoints, JSON logs, and transactional databases. Analysts and data scientists struggle with:
* Inconsistent data hygiene (missing primary keys, duplicate records, unvalidated values).
* Monolithic ingestion scripts that lack modularity, auditability, or version control.
* Inefficient query performance caused by scanning raw, unpartitioned file formats.

## Engineering Objectives
* **Modular ELT Design:** Decouple extraction, transformation, quality assurance, and loading into distinct, maintainable Python scripts.
* **Auditability & Reproducibility:** Archive immutable, timestamped raw JSON snapshots (`data/raw/`) to ensure full data lineage.
* **Dimensional Modeling:** Structure flat records into a normalized **Star Schema** (`dim_products`, `dim_categories`, and `fact_inventory_sales`).
* **Lakehouse Storage Optimization:** Transition data into columnar Apache Parquet format with partition pruning (`category_id=X`) to minimize query scan costs.