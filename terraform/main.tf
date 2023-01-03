terraform {
  cloud {
    organization = "Ecom_Bluelion"

    workspaces {
      name = "Ecom_Bluelion"
    }
  }
}

provider "google" {
  project = "ceri-m1-ecommerce-2022"
  region  = "europe-west1"
}

