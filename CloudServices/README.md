# Cloud Services Google Dorks

Google Dork queries for finding sensitive files, leaked data, and misconfigurations across cloud storage platforms and developer services. These are **template-based dorks** -- replace `<target>` with your actual target domain.

## Summary

| Risk Level | Count | Description |
|------------|-------|-------------|
| Critical | 30 | Direct access to leaked docs, source code, credentials, multi-cloud storage, and IaC secrets |
| High | 9 | Exposed artifacts, Supabase storage, Kubernetes endpoints, Docker configs |
| Medium | 8 | URL pattern discovery, health check endpoints |
| **Total** | **47** | |

## Query Reference

### Document & File Storage Platforms

| Query | Platform | What It Finds |
|-------|----------|---------------|
| `site:docs.google.com inurl:"/d/" "<target>"` | Google Docs | Internal documents, spreadsheets, and presentations |
| `site:drive.google.com "<target>"` | Google Drive | Publicly shared files on Google Drive |
| `site:onedrive.live.com "<target>"` | OneDrive | Internal presentations, photos, documents accidentally public |
| `site:dropbox.com/s "<target>"` | Dropbox | Shared links with source code, proprietary info, customer data |
| `site:box.com/s "<target>"` | Box | Internal reports, client contracts, sensitive business files |

### Developer & DevOps Platforms

| Query | Platform | What It Finds |
|-------|----------|---------------|
| `site:dev.azure.com "<target>"` | Azure DevOps | Repos, pipelines, API keys, auth tokens |
| `site:sharepoint.com "<target>"` | SharePoint | Internal communications, project plans, employee records |
| `site:firebaseio.com "<target>"` | Firebase | App secrets, user data, private API endpoints |
| `site:firebaseio.com inurl:".json"` | Firebase | Open Firebase Realtime Databases returning JSON without auth |
| `site:*.supabase.co/storage/v1/object/public/` | Supabase | Publicly accessible files and media hosted on Supabase buckets |
| `site:jfrog.io "<target>"` | JFrog | Exposed artifacts, builds, and release packages |

### Cloud Object Storage (Multi-Cloud)

| Query | Platform | What It Finds |
|-------|----------|---------------|
| `site:s3.amazonaws.com "<target>"` | AWS S3 (primary) | Files on the main S3 subdomain |
| `site:s3-external-1.amazonaws.com "<target>"` | AWS S3 (external-1) | Files on lesser-known S3 subdomain |
| `site:s3.dualstack.us-east-1.amazonaws.com "<target>"` | AWS S3 (dualstack) | Files on S3 dualstack (IPv4+IPv6) subdomain |
| `site:s3.amazonaws.com intitle:index.of.bucket` | AWS S3 | S3 buckets with directory listing enabled |
| `site:blob.core.windows.net "<target>"` | Azure Blob Storage | Files stored in Azure Blob containers |
| `site:blob.core.windows.net intitle:"Index of"` | Azure Blob Storage | Azure Blob containers with directory listing |
| `site:storage.googleapis.com intitle:"Index of"` | Google Cloud Storage | GCS buckets with directory listing |
| `site:googleapis.com "<target>"` | Google Cloud Storage | Google Cloud Storage and API data |
| `site:digitaloceanspaces.com "<target>"` | DigitalOcean Spaces | Database backups, config files, logs |
| `site:r2.cloudflarestorage.com "<target>"` | Cloudflare R2 | Files and buckets on Cloudflare R2 object storage |
| `site:s3.wasabisys.com "<target>"` | Wasabi Cloud | Files stored on Wasabi Hot Cloud Storage |
| `site:*.backblazeb2.com "<target>"` | Backblaze B2 | Files and data stored on Backblaze B2 cloud storage |
| `site:f000.backblazeb2.com "<target>"` | Backblaze B2 | Files on Backblaze B2 primary download node |
| `site:oss-*.aliyuncs.com "<target>"` | Alibaba Cloud OSS | Files on Alibaba Cloud OSS object storage buckets |
| `site:cos.*.myqcloud.com "<target>"` | Tencent Cloud COS | Files stored on Tencent Cloud COS object storage |
| `site:objectstorage.*.oraclecloud.com "<target>"` | Oracle OCI | Files on Oracle Cloud Infrastructure (OCI) object storage |
| `site:s3.*.scw.cloud "<target>"` | Scaleway Cloud | Files stored on Scaleway Object Storage |
| `intitle:index.of.bucket` | Any Cloud Storage | Cloud storage buckets with open directory listings |

### Infrastructure as Code & Cluster Credentials

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `filetype:tfstate "terraform_version" "<target>"` | Exposed Terraform state files referencing target infrastructure | Critical |
| `filetype:tfvars "access_key" \| "secret_key"` | Exposed Terraform variable files containing cloud access keys | Critical |
| `filetype:yaml "apiVersion: v1" "kind: Secret" "data:"` | Exposed Kubernetes Secret definitions with credentials | Critical |
| `"clusters:" "client-certificate-data:" filetype:yaml` | Exposed Kubernetes kubeconfig files granting cluster API access | Critical |

### Kubernetes & Container Endpoints

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `inurl:/metrics` | Exposed Kubernetes/Prometheus metrics endpoints | High |
| `inurl:/healthz` | Exposed Kubernetes health check endpoints | Medium |
| `inurl:/actuator` | Exposed Spring Boot actuator endpoints | High |
| `inurl:/actuator/env` | Spring Boot actuator environment endpoint (leaks config) | Critical |
| `intitle:"index of" "docker-compose"` | Exposed Docker Compose files in directory listings | High |

## Data Source

CSV file: [`GoogleDork-CloudServices.csv`](GoogleDork-CloudServices.csv)
