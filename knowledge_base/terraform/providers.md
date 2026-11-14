# Terraform Providers

Source: https://developer.hashicorp.com/terraform/docs/providers

## Overview

Providers are plugins that allow Terraform to interact with cloud platforms, infrastructure services, and other APIs.

They define the resources and data sources that Terraform can manage.

## Provider Configuration

A provider must be configured before Terraform can manage resources from a specific platform.

Example:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}
```

## Provider Responsibilities

- Authenticate with external platforms.
- Manage infrastructure resources.
- Retrieve information about existing resources.
- Communicate with service APIs.

## Provider Versions

Terraform allows providers to use version constraints.

Version constraints help maintain compatibility and avoid unexpected changes.

## Common Commands

```bash
terraform init
terraform providers
terraform version
```

## Important Considerations

- Providers are downloaded during terraform init.
- Provider versions should be controlled.
- Credentials should not be hardcoded in configuration files.
- Provider documentation should be consulted before using resources or data sources.