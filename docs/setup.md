# Setup & Installation Guide

This guide covers how to set up, configure, and execute the pipeline locally using a Linux terminal (such as ChromeOS Crostini / Debian) and VS Code.

## Prerequisites
* Python 3.8 or higher installed in your environment.
* Git for version control.

## Step 1: Clone the Repository
Open your Linux terminal and clone your repository:
```bash
git clone [https://github.com/tgktop/ecommerce-lakehouse-pipeline.git](https://github.com/tgktop/ecommerce-lakehouse-pipeline.git)
cd ecommerce-lakehouse-pipeline
```

## Step 2: Initialize Virtual Environment
Create and activate an isolated Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies
Install the required packages specified in `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Step 4: Execute the Pipeline
Run the modular pipeline scripts in sequential order:
```bash
# 1. Ingest raw e-commerce data and save snapshot
python src/extract.py

# 2. Transform raw data into Star Schema parquet files
python src/transform.py

# 3. Run automated data quality assertions
python src/quality_checks.py

# 4. Load and partition data into lakehouse storage
python src/load.py
```