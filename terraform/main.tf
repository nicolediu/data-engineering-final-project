terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file("../google_credentials.json")
  project     = var.project
  region      = var.region
}

# 建立 Data Lake (GCS Bucket)
resource "google_storage_bucket" "data-lake-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true # 如果刪除 terraform 資源，會連同裡面數據一起刪除

  lifecycle_rule {
    condition {
      age = 30 # 超過 30 天的數據自動移動或處理 (可選)
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

# 建立 Data Warehouse (BigQuery Dataset)
resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}