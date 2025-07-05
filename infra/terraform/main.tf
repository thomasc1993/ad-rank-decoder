resource "google_cloud_run_service" "service" {
  name     = "ad-rank-decoder"
  location = var.region
  template {
    spec {
      containers {
        image = var.image
      }
    }
  }
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = "ads_dataset"
}

resource "google_storage_bucket" "screenshots" {
  name     = "${var.project}-screenshots"
  location = var.region
}

resource "google_secret_manager_secret" "api_tokens" {
  secret_id = "api-tokens"
}

resource "google_cloud_scheduler_job" "daily" {
  name             = "daily-trigger"
  schedule         = "0 8 * * *"
  http_target {
    uri = google_cloud_run_service.service.status[0].url
    http_method = "GET"
  }
}
