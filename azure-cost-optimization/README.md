# Azure Cost Optimization with Cosmos DB and Blob Storage

This project archives old Cosmos DB billing records to Blob Storage to reduce costs.

## Components
- Cosmos DB for hot data (recent 3 months)
- Blob Storage for cold data
- Azure Functions for archival + fallback reads
- Terraform IaC

## Deployment
1. Set up Terraform backend (optional)
2. Update variables in `variables.tf`
3. `terraform init && terraform apply`

## Functions
- `archive_old_records`: timer-based archival
- `get_billing_record`: fallback reader

Use GitHub Actions in `.github/workflows/deploy.yml` to auto-deploy on push.