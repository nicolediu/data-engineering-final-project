from google.cloud import bigquery
import pandas as pd
import os

# Ensure your credentials are found
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Nicol/Desktop/Learning/data_engineering_2026/final_project/google_credentials.json"

def run_query(sql):
    client = bigquery.Client()
    try:
        # We run the query and convert to a dataframe immediately
        query_job = client.query(sql)
        results = query_job.result()
        df = results.to_dataframe()
        return df
    except Exception as e:
        return f"❌ BigQuery Error: {e}"

if __name__ == "__main__":
    # Test with a simple query first
    test_sql = "SELECT customer_city, SUM(payment_value) as rev FROM `infra-vertex-494802-i0.raw_ecommerce.reporting_master` GROUP BY 1 LIMIT 5"
    print("Testing BigQuery Connection...")
    print(run_query(test_sql))