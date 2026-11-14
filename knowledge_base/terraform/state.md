# Terraform State

Source: https://developer.hashicorp.com/terraform/language/state

## Overview

Terraform State is a file that stores information about the infrastructure managed by Terraform.

It maps configuration resources to real-world infrastructure objects.

## Purpose of State

Terraform uses state to:

- Track managed resources.
- Map configuration to infrastructure.
- Determine changes required during execution.
- Store resource metadata and dependencies.

## Local State

By default, Terraform stores state in a local file named terraform.tfstate.

This file should not be committed to version control because it may contain sensitive information.

## Remote State

Remote state stores Terraform state in an external backend.

Common benefits include:

- Collaboration between team members.
- Centralized state management.
- Controlled access.
- Support for state locking, depending on the backend.

## State Locking

State locking prevents multiple operations from modifying the same state simultaneously.

This helps avoid conflicts and state corruption.

## Common Commands

```bash
terraform state list
terraform state show RESOURCE_ADDRESS
terraform state pull
terraform state mv SOURCE DESTINATION
```

## Important Considerations

- Never manually edit state files unless absolutely necessary.
- Protect state files because they may contain sensitive data.
- Use remote backends for team environments.
- Enable state locking when supported.
- Back up state before performing risky operations.