terraform {
  cloud {
    organization = "Ecom_Bluelion"

    workspaces {
      name = "Ecom_Bluelion"
    }
  }
}

data "google_secret_manager_secret" "host" {
  secret_id = "mysql-address"
}

data "google_secret_manager_secret" "user" {
  secret_id = "mysql-user-bluelion"
}

data "google_secret_manager_secret" "password" {
  secret_id = "mysql-password-bluelion"
}

data "google_secret_manager_secret" "dbname" {
  secret_id = "mysql-database-bluelion"
}

variable "gcp_cred" {
  default=""
  type = string
  sensitive = true
  description = "Google Cloud service account credentials"

}

provider "google" {
  project = "ceri-m1-ecommerce-2022"
  region  = "europe-west1"
  credentials = var.gcp_cred
}

resource "google_cloud_run_service" "bluelion-backend" {
  provider = google
  name         = "bluelion-backend"
  location     = "europe-west1"
  template {
    spec {
      service_account_name = "terraform-bluelion@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
      containers {
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/bluelion/backend:0.0.1"
      }
    }
    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "1"
      }
    }
  }
}

resource "google_cloud_run_service_iam_member" "noauth" {
  location    = google_cloud_run_service.bluelion-backend.location
  project     = google_cloud_run_service.bluelion-backend.project
  service     = google_cloud_run_service.bluelion-backend.name
  role        = "roles/run.invoker"
  member      = "allUsers"
}

output "url" {
  value = "${google_cloud_run_service.bluelion-backend.status[0].url}"
}

