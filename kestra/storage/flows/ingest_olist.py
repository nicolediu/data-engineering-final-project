import dlt
import pandas as pd
import os

# 1. Define where the data is
DATA_DIR = "/app/storage/data" # Ensure this points to your CSVs

def load_olist_data():
    # 2. Initialize dlt with BigQuery as the destination
    pipeline = dlt.pipeline(
        pipeline_name="olist_ingestion",
        destination="bigquery",
        dataset_name="raw_ecommerce" # The one you created with Terraform!
    )

    # 3. Iterate through CSV files and load them
    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv"):
            table_name = file.replace(".csv", "").replace("olist_", "").replace("_dataset", "")
            df = pd.read_csv(os.path.join(DATA_DIR, file))
            
            info = pipeline.run(df, table_name=table_name, write_disposition="replace")
            print(f"Loaded {table_name}: {info}")

if __name__ == "__main__":
    load_olist_data()