# Metadata: label=Terraform Cloud tokens, type=cloud_token, provider=terraform, context=Terraform configuration, generator=secret_generator.py

# Terraform Cloud API Token
variable "tfe_token" {
  default = "xK9mN4oP5qR6sT.atlasv1.7uV8wX9yZ0aB1cD2eF3gH4iJ5kL6mN7oP8qR9sT0uV1wX2yZ3aB4cD5eF6gH7iJ8kL9mN0oP1qR2sT3uV4wX5yZ6aB7cD8eF9gH0iJ1kL2mN3oP4qR5sT6uV7wX8yZ9aB0cD1eF2gH3iJ4kL5mN6oP"
  sensitive = true
}

# Alternative token format
variable "terraform_token" {
  default = "5f6a7b8c9d0e1f.atlasv1.2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a"
  sensitive = true
}

# Terraform Cloud configuration
terraform {
  cloud {
    organization = "example-org"
    token = "1bC2dE3fG4hI5j.atlasv1.K6lM7nO8pQ9rS0tU1vW2xY3zA4bC5dE6fG7hI8jK9lM0nO1pQ2rS3tU4vW5xY6zA7bC8dE9fG0hI1jK2lM3nO4pQ5rS6tU7vW8xY9zA0bC1dE2fG3hI4jK5lM6nO7pQ8rS9tU0vW1xY2zA3bC4dE5fG6hI7jK8lM"

    workspaces {
      name = "production"
    }
  }
}

# Provider configuration with sensitive tokens
provider "aws" {
  access_key = "AKIAEXAMPLE1234567890"
  secret_key = "9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e"
  region     = "us-east-1"
}
