import os
import pandas as pd

PROCESSED_DIR = "data/processed"

def load_and_partition_data():
    """
    Simulates loading processed star schema tables into a partitioned 
    lakehouse storage layer (mimicking S3 partition structures).
    """
    print("Executing Load & Partitioning Layer...")
    
    products_path = os.path.join(PROCESSED_DIR, "dim_products.parquet")
    df = pd.read_parquet(products_path)
    
    # Create a partitioned storage directory structure
    partitioned_dir = os.path.join(PROCESSED_DIR, "partitioned_sales")
    os.makedirs(partitioned_dir, exist_ok=True)
    
    # Partition the dataset by category_id to optimize analytical query scans
    for category_id, group_df in df.groupby('category_id'):
        cat_folder = os.path.join(partitioned_dir, f"category_id={category_id}")
        os.makedirs(cat_folder, exist_ok=True)
        
        output_file = os.path.join(cat_folder, "data.parquet")
        group_df.to_parquet(output_file, index=False)
        print(f"Loaded {len(group_df)} records into partition: {cat_folder}")
        
    print("Load & Partitioning Layer completed successfully! 🚀")

if __name__ == "__main__":
    load_and_partition_data()