terraform {
  cloud {
    organization = "Ecom_Bluelion"

    workspaces {
      name = "Ecom_Bluelion"
    }
  }
}

data "google_secret_manager_secret" "address" {
  secret_id = "mysql-address"
}

data "google_secret_manager_secret" "user" {
  secret_id = "mysql-user-bluelion"
}

data "google_secret_manager_secret" "password" {
  secret_id = "mysql-password-bluelion"
}

data "google_secret_manager_secret" "database" {
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
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/bluelion/backend:0.0.23"
        env {
          name = "INSTANCE_CONNECTION_NAME"
          value = "ceri-m1-ecommerce-2022:europe-west1:mysql-primary"
        }
        env {
          name = "DB_NAME"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.database.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "DB_PASS"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.password.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "DB_USER"
          value = "bluelion"
        }
        ports {
          container_port = 8080
        }
      }
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "1"
        "run.googleapis.com/cloudsql-instances" = "ceri-m1-ecommerce-2022:europe-west1:mysql-primary"
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
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/bluelion/frontend:0.0.23"
        env {
          name = "BACKEND_URL"
          value = google_cloud_run_service.bluelion-backend.status[0].url
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


data "google_iam_policy" "invokers" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_member" "invokers" {
  location = google_cloud_run_service.bluelion-backend.location
  service = google_cloud_run_service.bluelion-backend.name
  project     = google_cloud_run_service.bluelion-backend.project
  role    = "roles/run.invoker"
  member  = "allUsers"
}

output "url" {
  value = "${google_cloud_run_service.bluelion-backend.status[0].url}"
}

output "front_url" {
  value = "${google_cloud_run_service.bluelion-frontend.status[0].url}"
}

