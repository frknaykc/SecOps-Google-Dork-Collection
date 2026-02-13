# Cloud Services Google Dorks

Google Dork queries for finding sensitive files, leaked data, and misconfigurations across cloud storage platforms and developer services. These are **template-based dorks** -- replace `<target>` with your actual target domain.

## Summary

| Risk Level | Count | Description |
|------------|-------|-------------|
| Critical | 18 | Direct access to leaked docs, source code, credentials, cloud storage |
| High | 8 | Exposed artifacts, Kubernetes endpoints, Docker configs |
| Medium | 7 | URL pattern discovery, health check endpoints |
| **Total** | **33** | |

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
| `site:jfrog.io "<target>"` | JFrog | Exposed artifacts, builds, and release packages |

### Cloud Object Storage

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
| `intitle:index.of.bucket` | Any Cloud Storage | Cloud storage buckets with open directory listings |

### Kubernetes & Container Endpoints

| Query | What It Finds |
|-------|---------------|
| `inurl:/metrics` | Exposed Kubernetes/Prometheus metrics endpoints |
| `inurl:/healthz` | Exposed Kubernetes health check endpoints |
| `inurl:/actuator` | Exposed Spring Boot actuator endpoints |
| `inurl:/actuator/env` | Spring Boot actuator environment endpoint (leaks config) |
| `intitle:"index of" "docker-compose"` | Exposed Docker Compose files in directory listings |

## Related HackerOne Reports

- **Firebase misconfiguration**: [HackerOne #1065134](https://hackerone.com/reports/1065134) -- Exposed Firebase database with user data
- **JFrog artifact exposure**: [HackerOne #911606](https://hackerone.com/reports/911606) -- Leaked build artifacts and packages

## Example Usage

Search multiple cloud platforms at once:

```
(site:dropbox.com/s | site:box.com/s | site:onedrive.live.com) "tesla.com"
```

Combine with specific file types:

```
site:digitaloceanspaces.com "tesla.com" filetype:sql
site:s3.amazonaws.com "tesla.com" filetype:env
```

## Data Source

All queries in this collection are sourced from publicly available Google Dorking databases and security research. See the CSV file for the complete machine-readable dataset.
