module "gcs_bucket" {
  source     = "./modules/gcs"
  bucket_name = "pm-mlops-data"
}

module "vm_instance" {
  source     = "./modules/compute"
  project_id = var.project_id
  region     = "us-central1"
}