# Metadata: label=Sumo Logic credentials in Terraform, type=api_key, provider=sumologic, context=Terraform configuration, generator=manual

terraform {
  required_providers {
    sumologic = {
      source  = "SumoLogic/sumologic"
      version = "~> 2.0"
    }
  }
}

# Provider configuration
provider "sumologic" {
  access_id   = "suTERRAFORM123456789"
  access_key  = "terraform1234567890abcdef1234567890abcdef1234567890abcdef123456789"
  environment = "us2"
}

# Alternative provider configuration
provider "sumologic" {
  alias       = "eu"
  access_id   = "suEU198765432109B"
  access_key  = "3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a"
  environment = "eu"
}

# HTTP Source with URL
resource "sumologic_http_source" "app_logs" {
  name         = "Application Logs"
  category     = "app/logs"
  collector_id = "123456789"

  # The URL will contain a token like:
  # https://collectors.sumologic.com/receiver/v1/http/YXBwX2xvZ3Nfc291cmNlX3Rva2VuXzEyMzQ1Njc4OTA=
}

# Variables with sensitive values
variable "sumologic_access_id" {
  type      = string
  default   = "suVAR1234567890ABCD"
  sensitive = true
}

variable "sumologic_access_key" {
  type      = string
  default   = "var1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
  sensitive = true
}

# Installation token for collector
variable "installation_token" {
  type      = string
  default   = "suINSTALL5678901234WXYZ1234ABCD5678EFGH9012IJKL"
  sensitive = true
}
