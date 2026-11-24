import os
import pandas as pd

PROCESSED_DIR = "data/processed"

def run_quality_checks():
    """
    Runs automated data quality assertions on processed star schema tables.
    Fails the pipeline if nulls, duplicates, or invalid metrics are detected.
    """
    print("Starting Data Quality Validation...")
    
    # Load processed tables
    dim_products_path = os.path.join(PROCESSED_DIR, "dim_products.parquet")
    fact_sales_path = os.path.join(PROCESSED_DIR, "fact_inventory_sales.parquet")
    
    if not os.path.exists(dim_products_path) or not os.path.exists(fact_sales_path):
        raise FileNotFoundError("Processed Parquet files not found. Run transform.py first.")
        
    df_products = pd.read_parquet(dim_products_path)
    df_sales = pd.read_parquet(fact_sales_path)
    
    # 1. Check for null primary keys in dim_products
    assert df_products['product_id'].isnull().sum() == 0, "DATA QUALITY FAIL: Null values found in product_id!"
    
    # 2. Check for duplicate primary keys in dim_products
    assert df_products['product_id'].duplicated().sum() == 0, "DATA QUALITY FAIL: Duplicate product_id entries found!"
    
    # 3. Check for negative prices in dim_products
    assert (df_products['price'] >= 0).all(), "DATA QUALITY FAIL: Negative product prices detected!"
    
    # 4. Check for negative revenue estimates in fact_sales
    assert (df_sales['total_revenue_estimate'] >= 0).all(), "DATA QUALITY FAIL: Negative revenue estimates detected!"
    
    print("All Data Quality Checks Passed Successfully! 🎉")

if __name__ == "__main__":
    run_quality_checks()