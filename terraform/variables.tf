variable "project" {
  description = "GCP Project ID"
  default     = "infra-vertex-494802-i0" 
}

variable "region" {
  description = "Project Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "raw_ecommerce"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "infra-vertex-494802-i0-data-lake" 
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}