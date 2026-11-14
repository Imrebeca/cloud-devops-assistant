# AWS IAM — Identity and Access Management

Source: https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html

## Overview

AWS Identity and Access Management (IAM) is a service that helps securely control access to AWS resources.

IAM allows administrators to manage authentication and authorization across AWS services.

## IAM Users

An IAM user represents an identity that can access AWS resources.

Users can have:

- Console passwords.
- Access keys for programmatic access.
- Permissions assigned through policies.

## IAM Groups

An IAM group is a collection of IAM users.

Groups simplify permission management by allowing administrators to assign policies to multiple users.

## IAM Roles

An IAM role is an identity with specific permissions that can be assumed by trusted entities.

Common use cases:

- EC2 instances accessing S3.
- Lambda functions accessing AWS services.
- Cross-account access.
- Federated access.

## IAM Policies

IAM policies define permissions by specifying which actions are allowed or denied on AWS resources.

Policies are written in JSON and commonly contain:

- Effect: Allow or Deny.
- Action: the AWS operations.
- Resource: the resources affected.
- Condition: optional rules that control when permissions apply.

## Principle of Least Privilege

The principle of least privilege means granting only the permissions required to perform a specific task.

Benefits:

- Reduces the attack surface.
- Limits unauthorized access.
- Improves security governance.

## Authentication and Authorization

Authentication verifies the identity of a user or service.

Authorization determines which actions that identity is permitted to perform.

## Common Security Practices

- Prefer IAM roles over long-term access keys for workloads.
- Enable multi-factor authentication where appropriate.
- Apply least-privilege permissions.
- Review and remove unused credentials.
- Avoid using the root account for routine operations.