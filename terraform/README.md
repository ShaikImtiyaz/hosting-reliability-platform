# Terraform Infrastructure

## Overview

This directory contains the Terraform configuration used to provision the Azure infrastructure for the **Hosting Reliability Platform**.

The infrastructure is designed using Infrastructure as Code (IaC) principles and provisions Azure resources required for deploying the application on Azure Kubernetes Service (AKS).

---

## Architecture

```
GitHub
   │
Terraform
   │
Azure Resource Group
   │
Azure Container Registry (ACR)
   │
Azure Kubernetes Service (AKS)
   │
Hosting Reliability Platform
```

---

## Technologies Used

* Terraform v1.13+
* Azure CLI
* Azure Resource Manager (AzureRM Provider)
* Azure Container Registry (ACR)
* Azure Kubernetes Service (AKS)

---

## Folder Structure

```
terraform/
├── versions.tf
├── provider.tf
├── variables.tf
├── terraform.tfvars.example
├── resource-group.tf
├── acr.tf
├── aks.tf
├── outputs.tf
├── locals.tf
└── README.md
```

---

## Prerequisites

Ensure the following tools are installed:

* Terraform
* Azure CLI
* Git
* Docker Desktop (for later deployment stages)

Verify installation:

```bash
terraform version
az version
docker --version
git --version
```

---

## Azure Login

Authenticate with Azure:

```bash
az login
```

Verify the active subscription:

```bash
az account show --output table
```

---

## Configuration

Create a local Terraform variables file:

```bash
cp terraform.tfvars.example terraform.tfvars
```

Update `terraform.tfvars` with your Azure Subscription ID and resource names.

Example:

```hcl
subscription_id     = "<your-subscription-id>"
location            = "Central India"
resource_group_name = "rg-hosting-reliability-dev"
acr_name            = "your-acr-name"
aks_name            = "aks-hosting-reliability"
```

> **Important:** Do not commit `terraform.tfvars` to Git.

---

## Initialize Terraform

```bash
terraform init
```

---

## Format Configuration

```bash
terraform fmt
```

---

## Validate Configuration

```bash
terraform validate
```

---

## Review the Execution Plan

```bash
terraform plan -out=tfplan
```

Review the planned changes before applying them.

---

## Apply Infrastructure

```bash
terraform apply tfplan
```

Terraform will provision the Azure resources defined in the configuration.

---

## View Outputs

```bash
terraform output
```

---

## Verify Resources

### Resource Groups

```bash
az group list --output table
```

### Azure Container Registry

```bash
az acr list --output table
```

### Azure Kubernetes Service

```bash
az aks list --output table
```

---

## Destroy Infrastructure

To remove all Azure resources created by Terraform:

```bash
terraform destroy
```

This helps avoid unnecessary Azure charges after completing the project.

---

## Best Practices

* Keep infrastructure changes in version control.
* Review every `terraform plan` before applying.
* Do not commit secrets or environment-specific files.
* Keep `terraform.tfvars` local.
* Commit `terraform.tfvars.example` for documentation.
* Use descriptive Git commit messages for infrastructure changes.

---

## Deployment Workflow

```
Developer
     │
Git Commit
     │
Terraform Plan
     │
Terraform Apply
     │
Azure Resource Group
     │
Azure Container Registry
     │
Azure Kubernetes Service
     │
Application Deployment
```

---

## Future Enhancements

* GitHub Actions CI/CD
* Azure Monitor Integration
* Log Analytics Workspace
* ELK Stack Deployment
* Kubernetes Horizontal Pod Autoscaler
* Self-Healing Automation
* Infrastructure Monitoring
* Automated Container Image Deployment

---

## Author

**Shaik Mohammed Imtiyaz**

Hosting Reliability Engineer Project

Built for hands-on learning in:

* Terraform
* Azure
* Docker
* Kubernetes
* Infrastructure as Code
* Site Reliability Engineering (SRE)
* Cloud Automation
