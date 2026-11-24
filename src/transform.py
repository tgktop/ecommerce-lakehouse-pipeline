import os
import json
import glob
import pandas as pd

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

def get_latest_raw_file(raw_dir):
    """Finds the most recent raw JSON snapshot in the data/raw directory."""
    files = glob.glob(os.path.join(raw_dir, "*.json"))
    if not files:
        raise FileNotFoundError(f"No raw JSON snapshots found in {raw_dir}")
    latest_file = max(files, key=os.path.getctime)
    return latest_file

def transform_data():
    """
    Reads the latest raw snapshot, cleans fields, and models 
    the data into a Star Schema (Dimension & Fact tables).
    """
    raw_filepath = get_latest_raw_file(RAW_DIR)
    print(f"Reading raw data from: {raw_filepath}")
    
    with open(raw_filepath, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
        
    df = pd.DataFrame(raw_data)
    print(f"Loaded {len(df)} records into DataFrame for transformation.")
    
    # 1. Clean & standardize columns
    df['title'] = df['title'].str.strip()
    df['category'] = df['category'].str.lower().str.strip()
    
    # Extract rating fields safely if nested as a dictionary
    if 'rating' in df.columns:
        df['rating_rate'] = df['rating'].apply(lambda x: x.get('rate') if isinstance(x, dict) else None)
        df['rating_count'] = df['rating'].apply(lambda x: x.get('count') if isinstance(x, dict) else None)
        df = df.drop(columns=['rating'])
    
    # 2. Build Dimension Table: dim_categories
    categories = df[['category']].drop_duplicates().reset_index(drop=True)
    categories['category_id'] = categories.index + 1
    
    # Merge category_id back to main dataframe
    df = df.merge(categories, on='category', how='left')
    
    # 3. Build Dimension Table: dim_products
    dim_products = df[['id', 'title', 'price', 'category_id', 'description']].copy()
    dim_products.rename(columns={'id': 'product_id'}, inplace=True)
    
    # 4. Build Fact Table: fact_inventory_sales
    fact_sales = df[['id', 'price', 'rating_rate', 'rating_count']].copy()
    fact_sales.rename(columns={'id': 'product_id'}, inplace=True)
    fact_sales['quantity_sold_estimate'] = 10  # Mock metric for analytical demonstration
    fact_sales['total_revenue_estimate'] = fact_sales['price'] * fact_sales['quantity_sold_estimate']
    
    # Save transformed tables locally as CSV/Parquet staging files
    dim_products.to_parquet(os.path.join(PROCESSED_DIR, "dim_products.parquet"), index=False)
    categories.to_parquet(os.path.join(PROCESSED_DIR, "dim_categories.parquet"), index=False)
    fact_sales.to_parquet(os.path.join(PROCESSED_DIR, "fact_inventory_sales.parquet"), index=False)
    
    print("Transformation complete. Star schema tables saved to data/processed/")

if __name__ == "__main__":
    transform_data()