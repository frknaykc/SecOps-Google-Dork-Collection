# Sensitive Files - Google Dork Queries

Dork queries designed to find exposed configuration files, API keys, credentials, private keys, log files, Infrastructure-as-Code state files, and other sensitive data left accessible on the internet.

## Summary

| Risk Level | Count | Description |
|------------|-------|-------------|
| Critical | 534 | Plaintext private keys, cloud credentials, database passwords, OAuth secrets, and IaC states |
| High | 2,227 | Configuration files, exposed API tokens, server logs, RDP profiles, and repository configs |
| Medium | 103 | Known host lists, public SSH keys, and general environment descriptors |
| **Total** | **2,864** | |

## Coverage

| Category | Description |
|----------|-------------|
| **Infrastructure as Code (IaC)** | Terraform state files (`.tfstate`), variables (`.tfvars`), Kubernetes secrets |
| **Environment Files** | `.env` files with API keys, database passwords, secrets, tokens |
| **Modern SaaS & Auth** | Clerk, Resend, Supabase service role, OpenAI, Anthropic, Stripe, Twilio |
| **Remote Access Profiles** | Remote Desktop (`.rdp`), OpenVPN (`.ovpn`), KeePass (`.kdbx`), SSH known_hosts |
| **Git & Version Control** | `.git-credentials`, `.gitconfig`, exposed `.git` directories, GitHub Actions secrets |
| **Configuration Files** | PHP config, YAML, XML, Docker Compose, Makefiles with credentials |
| **Private Keys & OAuth** | RSA, OpenSSH, PEM private keys, Google OAuth client secrets JSON |
| **Database Credentials** | MongoDB, Redis, PostgreSQL, MySQL connection strings and dumps |
| **Log Files** | Access logs, error logs, debug logs with passwords, tokens, and session data |
| **Password Files** | `.htpasswd`, passwd, shadow, FileZilla configs, registry exports |
| **Cloud Credentials** | AWS access keys, GCP service accounts, Azure client secrets |

## Example Usage

```
# Find exposed Terraform state files containing infrastructure passwords
filetype:tfstate "terraform_version" "serial" "resources"

# Find exposed Supabase Service Role secret keys bypassing RLS
filetype:env "SUPABASE_SERVICE_ROLE_KEY"

# Find exposed .env files with database passwords
filetype:env "DB_PASSWORD"

# Find Google OAuth 2.0 client secret JSON files
filetype:json "client_secret" "client_id" "auth_uri"

# Find exposed OpenVPN configuration profiles
filetype:ovpn "auth-user-pass"
```

## Why Sensitive Files Matter

Exposed sensitive files represent some of the highest-risk findings in reconnaissance:

- **IaC State Files** contain complete cloud topology and plaintext database/IAM passwords
- **API keys** provide direct access to paid services and can be used for lateral movement
- **Private keys** enable authentication bypass and man-in-the-middle attacks
- **Database credentials** provide direct database access
- **Log files** may contain session tokens, passwords, and internal IP addresses
- **Git repositories** expose full source code history including past secrets

## Data Source

CSV file: [`GoogleDork-SensitiveFiles.csv`](GoogleDork-SensitiveFiles.csv)
