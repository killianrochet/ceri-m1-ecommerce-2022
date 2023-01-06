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

  name     = "bluelion-backend"
  location = "europe-west1"

  template {
    spec {
      service_account_name = "terraform-bluelion@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
      containers {
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/bluelion/backend:0.0.1"
        env {
          name = "DATABASE_ADDRESS"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.address.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "DATABASE_NAME"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.database.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "PASSWORD"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.password.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "DATABASE_USER"
          value = "orangedog"
        }
        ports {
          container_port = 5000
        }
      }
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "1"
      }
    }
  }

  traffic {
    percent = 100
    latest_revision = true
  }
}


resource "google_cloud_run_service" "bluelion-frontend" {

  name     = "bluelion-frontend"
  location = "europe-west1"

  template {
    spec {
      service_account_name = "terraform-bluelion@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
      containers {
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/bluelion-frontend:0.0.1"
        env {
          name = "BACKEND_URL"
          value = google_cloud_run_service.bluelion-backend.status[0].url
        }
        ports {
          container_port = 80
        }
      }
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "1"
      }
    }
  }

  traffic {
    percent = 100
    latest_revision = true
  }
}

resource "google_cloud_run_service_iam_member" "noauth" {
  location    = google_cloud_run_service.bluelion-backend.location
  project     = google_cloud_run_service.bluelion-backend.project
  service     = google_cloud_run_service.bluelion-backend.name
  role        = "roles/run.invoker"
  member      = "allUsers"
}

output "back_url" {
  value = google_cloud_run_service.bluelion-backend.status[0].url
}

output "front_url" {
  value       = google_cloud_run_service.bluelion-frontend.status[0].url
}


