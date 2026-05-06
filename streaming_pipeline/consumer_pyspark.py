import os
import json
from datetime import datetime
from google.cloud import pubsub_v1
from google.cloud import bigquery  # New library for Phase 3

# --- CONFIGURATION ---
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Nicol/Desktop/Learning/data_engineering_2026/final_project/google_credentials.json"
PROJECT_ID = "infra-vertex-494802-i0"
SUBSCRIPTION_ID = "olist-orders-stream-sub"
TABLE_ID = f"{PROJECT_ID}.olist_streaming.realtime_orders"

# Initialize Clients
subscriber = pubsub_v1.SubscriberClient()
bq_client = bigquery.Client()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

def callback(message):
    try:
        # 1. Parse the data
        data = json.loads(message.data.decode("utf-8"))
        
        # 2. Calculate Lag (Same as Phase 2)
        event_time = datetime.strptime(data['event_timestamp'], '%Y-%m-%d %H:%M:%S')
        lag = (datetime.now() - event_time).total_seconds()
        
        # 3. Write to BigQuery (The Phase 3 "Magic")
        # We send the data as a list of dictionaries
        errors = bq_client.insert_rows_json(TABLE_ID, [data])
        
        if not errors:
            print(f"✅ Order {data['order_id'][:8]}... saved to BigQuery | Lag: {lag:.2f}s")
        else:
            print(f"❌ BigQuery Error: {errors}")
            
        # 4. Acknowledge the message
        message.ack()

    except Exception as e:
        print(f"⚠️ Error processing message: {e}")

print(f"Streaming Olist data to BigQuery...")

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()