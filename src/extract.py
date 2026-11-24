import os
import json
import requests
from datetime import datetime

# Define raw data storage path
RAW_DATA_DIR = "data/raw"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

def fetch_ecommerce_data():
    """
    Fetches raw e-commerce sample data from a reliable public endpoint 
    and archives it as a timestamped JSON snapshot.
    """
    # Using a reliable public sample API for product/order telemetry
    url = "https://fakestoreapi.com/products"
    
    print(f"Connecting to data source: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        raw_data = response.json()
        
        # Generate a unique timestamped filename for auditability & immutability
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ecommerce_snapshot_{timestamp}.json"
        filepath = os.path.join(RAW_DATA_DIR, filename)
        
        # Save raw snapshot
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(raw_data, f, indent=4)
            
        print(f"Successfully extracted and archived raw snapshot to: {filepath}")
        return filepath

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        raise

if __name__ == "__main__":
    fetch_ecommerce_data()