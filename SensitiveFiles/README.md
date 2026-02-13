# Sensitive Files - Google Dork Queries

Dork queries designed to find exposed configuration files, API keys, credentials, private keys, log files, and other sensitive data left accessible on the internet.

## Summary

| Risk Level | Count |
|------------|-------|
| Critical | 110 |
| High | 40 |
| Medium | 10 |

**Total: 2,853 dorks**

## Coverage

| Category | Description |
|----------|-------------|
| Environment Files | .env files with API keys, database passwords, secrets, tokens |
| API Keys & Tokens | OpenAI, Anthropic, Stripe, Twilio, Slack, Discord, SendGrid, Mailgun, HuggingFace, Cohere |
| Git & Version Control | .git-credentials, .gitconfig, exposed .git directories, GitHub Actions secrets |
| Configuration Files | PHP config, YAML, XML, Docker Compose, Makefiles with credentials |
| Private Keys | RSA, OpenSSH, PEM private keys |
| Database Credentials | MongoDB, Redis, PostgreSQL, MySQL connection strings and dumps |
| Log Files | Access logs, error logs, debug logs with passwords, tokens, and session data |
| Password Files | .htpasswd, passwd, shadow, FileZilla configs, registry exports |
| Cloud Credentials | AWS access keys, GCP service accounts, Azure client secrets |
| Framework Secrets | React, Next.js, Angular environment variables, Firebase configs |
| CI/CD Tokens | CircleCI, Travis CI, DigitalOcean, Heroku tokens |

## Example Usage

```
# Find exposed .env files with database passwords
filetype:env "DB_PASSWORD"

# Find exposed RSA private keys
"BEGIN RSA PRIVATE KEY"

# Find Slack tokens in code
"xoxb-"

# Find AWS credentials in log files
filetype:log "AWS_ACCESS_KEY_ID"

# Find exposed .git repositories
intext:"index of /.git" "parent directory"
```

## Why Sensitive Files Matter

Exposed sensitive files represent some of the highest-risk findings in reconnaissance:

- **API keys** provide direct access to paid services and can be used for lateral movement
- **Private keys** enable authentication bypass and man-in-the-middle attacks
- **Database credentials** provide direct database access
- **Log files** may contain session tokens, passwords, and internal IP addresses
- **Git repositories** expose full source code history including past secrets

## Data Source

CSV file: [`GoogleDork-SensitiveFiles.csv`](GoogleDork-SensitiveFiles.csv)
