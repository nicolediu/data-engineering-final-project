# 🛒 Olist E-commerce End-to-End Analytics Pipeline
### *An Automated ELT Solution with Kestra, dbt, and BigQuery*

---

## 📖 Project Overview
This project demonstrates a full-stack **ELT (Extract, Load, Transform)** pipeline designed to turn raw e-commerce data into actionable business insights. By leveraging modern data engineering tools, the pipeline automates the journey from raw CSV ingestion to a high-fidelity executive dashboard.

## 🛠️ Tech Stack
| Layer | Tool | Purpose |
| :--- | :--- | :--- |
| **Orchestration** | `Kestra` | Workflow management and automation |
| **Ingestion** | `Python` & `dlt` | Extracting Olist CSVs and loading to BigQuery |
| **Warehouse** | `Google BigQuery` | Highly scalable cloud data storage |
| **Transformation** | `dbt Core` | SQL modeling, casting, and data joins |
| **Visualization** | `Looker Studio` | Business Intelligence and reporting |

---

## 🏗️ Architecture & Workflow

### 1. Ingestion (**Bronze Layer**)
The pipeline begins with a **Kestra** flow that triggers a Python script. This script utilizes **dlt** (Data Load Tool) to ingest raw Olist datasets.
*   **Source:** Raw Olist CSV files (Orders, Customers, Products).
*   **Destination:** BigQuery raw dataset.

### 2. Transformation (**Silver & Gold Layers**)
We use **dbt** to structure the data into a maintainable hierarchy:
*   **Staging (Silver):** Cleans raw data and applies critical `CAST` operations to convert string timestamps into proper date objects.
*   **Marts (Gold):** Aggregates data into a final Fact table (`fct_customer_orders`) for optimized querying.

### 3. Data Quality & Governance
*   **Testing:** Automated dbt tests ensure `unique` and `not_null` constraints on primary keys.
*   **Lineage:** The project structure allows for automated documentation and a visual lineage graph of the entire data flow.

---

## 📊 Business Insights
The final **Looker Studio** dashboard provides real-time visibility into:
*   **Geographic Sales:** A heatmap of orders across Brazilian states.
*   **Operational Health:** Distribution of order statuses (Delivered vs. Canceled).
*   **Growth Metrics:** Time-series analysis of purchasing volume over time.

## 💻 Setup & Installation

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    ```
2.  **Install Dependencies:**
    
```bash
    pip install -r requirements.txt
    ```
3.  **Configure Profiles:**
    Ensure your `profiles.yml` is correctly mapped to your **Google Cloud Project ID** and dataset.
4.  **Run the Pipeline:**
    Execute the flow via the **Kestra UI** or run `dbt build` in the terminal.

---

> **Note:** This project was developed in **April 2026** as a final data engineering project focusing on the Olist e-commerce dataset.

### 🛡️ Security
Standard professional security protocols are followed. All sensitive credentials (GCP JSON keys), environment variables, and local virtual environments (`venv/`) are excluded via `.gitignore`.