Olist E-commerce End-to-End Analytics Pipeline
🚀 Project Overview
This project demonstrates a full-stack ELT (Extract, Load, Transform) pipeline. It automates the transition of raw e-commerce data into actionable business insights using a modern data stack. The pipeline ingests raw Olist datasets, transforms them into a "Gold" layer for analysis, and visualizes key performance indicators.

🛠️ Tech Stack
Orchestration: Kestra

Ingestion: Python & dlt (Data Load Tool)

Data Warehouse: Google BigQuery

Transformation: dbt Core (v1.x)

Visualization: Google Looker Studio

Infrastructure: Terraform (GCP Provider)

🏗️ Architecture & Workflow
1. Ingestion (Bronze Layer)
Using Kestra as the orchestrator, we execute a Python script powered by dlt to ingest raw CSV files from the Olist e-commerce dataset. These are loaded directly into BigQuery as raw, immutable tables.

2. Transformation (Silver & Gold Layers)
We utilize dbt to manage the transformation layer:

Staging (Silver): Cleaned raw data, renamed columns for consistency, and cast string dates into proper TIMESTAMP formats for time-series analysis.

Marts (Gold): Created a final Fact table (fct_customer_orders) by joining orders and customer location data to enable geographic sales analysis.

3. Data Quality & Documentation
Testing: Implemented dbt data tests (unique, not_null) to ensure integrity across primary keys.

Lineage: Automated documentation and lineage graphs provided by dbt to track data flow from source to destination.

📊 Business Insights
The final output is an automated executive dashboard in Looker Studio featuring:

Sales Heatmap: Visualizing order concentration across Brazilian states.

Order Status Distribution: Tracking delivery success vs. cancellation rates.

Growth Trends: Time-series analysis of purchasing behavior.

💻 How to Run
Environment: Set up a Python virtual environment and install dependencies: pip install dbt-bigquery dlt.

Credentials: Place your GCP Service Account JSON key in the root directory (ensure it is ignored by Git).

dbt Setup: Ensure your profiles.yml is configured to point to your BigQuery project.

Orchestration: Import the .yaml flow into your Kestra instance and trigger the execution.

🛡️ Security Note
This repository follows professional security practices. All sensitive credentials, including profiles.yml and GCP JSON keys, are excluded via .gitignore.