import pandas as pd
import json
import time
from google.cloud import pubsub_v1
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Nicol/Desktop/Learning/data_engineering_2026/final_project/google_credentials.json"
# --- CONFIGURATION ---
PROJECT_ID = "infra-vertex-494802-i0" # Replace with your GCP Project ID
TOPIC_ID = "olist-orders-stream"
CSV_PATH = "data/olist_orders_dataset.csv" 

# Initialize Publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

def publish_orders():
    # Load your existing Olist data
    df = pd.read_csv(CSV_PATH)
    
    print(f"🚀 Starting stream... Publishing {len(df)} orders.")

    for index, row in df.iterrows():
        # Convert the row to a dictionary
        order_data = row.to_dict()
        
        # Add a real-time event timestamp (Critical for FBM latency tracking)
        order_data['event_timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S')
        
        # Convert to JSON string and then to bytes
        message_json = json.dumps(order_data)
        message_bytes = message_json.encode("utf-8")

        # Publish to GCP Pub/Sub
        future = publisher.publish(topic_path, message_bytes)
        
        if index % 10 == 0:
            print(f"✅ Published Order ID: {order_data['order_id']} (Index: {index})")
        
        # Simulate a real-time interval (e.g., 1 order every 2 seconds)
        time.sleep(2) 

if __name__ == "__main__":
    publish_orders()