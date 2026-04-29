# data-engineering-final-project
DataTalks.Club 2026 data engineering zoomcamp final project

第一階段：現代化基礎設施 (IaC & CI/CD)
任務： 使用 Terraform 建立 GCP 資源。

改進點：

使用 Terraform Modules 模組化資源，並將狀態檔 (State file) 存放在 GCS 中。

建立 GitHub Actions 流水線，當你提交代碼時，自動執行 terraform plan 進行校驗。

實踐： 定義兩個 Dataset：raw_ecommerce (存放 dlt 進入的資料) 和 analytics_ecommerce (存放 dbt 建模後的資料)。

第二階段：健壯的資料攝取 (Orchestration & dlt)
任務： 使用 Kestra 搭配 dlt 進行攝取。

改進點：

dlt 原生整合： 使用 dlt 的 google_cloud_storage 來源與 bigquery 目的地。利用 dlt 的 write_disposition='replace' 處理維度表，用 append 處理事實表。

密鑰管理： 在 Kestra 中管理 GCP Service Account Key，不要硬編碼在 Python 中。

實際案例： 自動識別 CSV 的數據類型並生成 BigQuery Schema，解決手動定義 Schema 的痛苦。

第三階段：效能優化與成本控管 (Data Warehouse Design)
任務： BigQuery 物理設計。

改進點：

時間往返查詢： 啟用 Time Travel 功能，防止誤刪數據。

分區鍵優化： 訂單表除了 purchase_timestamp 分區，還可以針對 order_status 進行 Clustering，方便分析師過濾「已完成」的訂單。

第四階段：精密建模與商業邏輯 (dbt Engineering)
任務： 實踐 Medallion Architecture (獎章架構)。

改進點：

Bronze (Staging)： stg_orders、stg_customers，僅做重新命名與格式轉換。

Silver (Intermediate)： 處理「一個訂單多個商品」的邏輯，計算每個訂單的總稅額與運費。

Gold (Mart)：

dim_customers：包含客戶的最後購買日期與活躍度標籤。

fct_order_items：顆粒度到「品項」的銷售事實。

技術亮點： 使用 dbt 的 Macros（例如自定義清理函數）和 Packages（如 dbt_utils）來展現專業度。

第五階段：全方位的資料觀測 (Observability)
任務： 使用 Bruin 或 dbt tests。

改進點：

測試分級：

Generic Tests： unique, not_null, accepted_values (例如訂單狀態只能是那幾種)。

Singular Tests： 撰寫 SQL 檢查「付款金額是否等於訂單總額」。

數據鮮度 (Freshness)： 檢查資料是否在過去 24 小時內更新過。

第六階段：商業決策儀表板 (BI)
任務： 視覺化呈現。

改進點：

RFM 分析： 在儀表板呈現客戶的 Recency (近度), Frequency (頻度), Monetary (額度)，這對電商非常有價值。

物流效率分析： 計算「預計送達時間」vs「實際送達時間」的偏差，找出物流瓶頸地區。