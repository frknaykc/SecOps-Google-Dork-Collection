# Recon Google Dorks

Google Dork queries for active reconnaissance -- subdomain enumeration, hidden endpoint discovery, code leak hunting, sensitive document/parameter discovery, and disclosed vulnerability lookups. These are **template-based dorks** where you replace `<target>` with your actual target domain.

## Summary

| Risk Level | Count |
|---|---:|
| Critical | 6 |
| High | 32 |
| Medium | 6,631 |
| Low | 33 |

**Total: 6,702 dorks**

Risk levels prioritize search leads; a matching result is not proof of a vulnerability or unauthorized access.

## Query Reference

### Subdomain & Asset Enumeration

| Query | What It Finds |
|-------|---------------|
| `site:<target> -www -shop -share -ir -mfa` | Hidden subdomains and assets by excluding common/boring subdomains. Keep adding `-term` exclusions until interesting results surface. |

**How to use**: Start broad, then progressively exclude noise:

```
site:tesla.com                          # Everything
site:tesla.com -www                     # Remove main site
site:tesla.com -www -shop               # Remove shop
site:tesla.com -www -shop -share -ir    # Keep narrowing
```

### API & Endpoint Discovery

| Query | What It Finds |
|-------|---------------|
| `site:<target> inurl:api \| site:*/rest \| site:*/v1 \| site:*/v2 \| site:*/v3` | API endpoints including REST and versioned API paths |
| `inurl:apidocs \| inurl:api-docs \| inurl:swagger \| inurl:api-explorer \| inurl:redoc \| inurl:openapi \| intitle:"Swagger UI" site:<target>` | API documentation pages (Swagger, Redoc, OpenAPI) exposing endpoint details |
| `site:<target> ext:php inurl:?` | PHP files with URL parameters -- potential injection points |
| `(site:<target> \| site:<target2>) & "choose file"` | File upload endpoints across multiple domains |
| `site:<target> intext:"choose file" \| intext:"select file" \| intext:"upload PDF"` | File upload forms via button/input text patterns |

### Sensitive File & Extension Discovery

| Query | What It Finds |
|-------|---------------|
| `site:<target> ext:log \| ext:txt \| ext:conf \| ext:cnf \| ext:ini \| ext:env \| ext:sh \| ext:bak \| ext:backup \| ext:swp \| ext:old \| ext:~ \| ext:git \| ext:svn \| ext:htpasswd \| ext:htaccess \| ext:json` | Files with sensitive extensions: logs, configs, backups, VCS, credentials |
| `inurl:conf \| inurl:env \| inurl:cgi \| inurl:bin \| inurl:etc \| inurl:root \| inurl:sql \| inurl:backup \| inurl:admin \| inurl:php site:<target>` | High-value URL paths (config, env, admin, SQL, backup directories) |
| `site:<target> ext:txt \| ext:pdf \| ext:xml \| ext:xls \| ext:xlsx \| ext:ppt \| ext:pptx \| ext:doc \| ext:docx` | Exposed documents (PDF, Office, XML) on target |
| `intext:"confidential" \| intext:"Not for Public Release" \| intext:"internal use only" \| intext:"do not distribute"` | Pages with confidentiality markers indicating sensitive internal documents |

### Environment & Infrastructure Discovery

| Query | What It Finds |
|-------|---------------|
| `inurl:test \| inurl:env \| inurl:dev \| inurl:staging \| inurl:sandbox \| inurl:debug \| inurl:temp \| inurl:internal \| inurl:demo site:<target>` | Test, dev, staging, and internal environments that may lack security controls |
| `inurl:/content/usergenerated \| inurl:/content/dam \| inurl:/jcr:content \| inurl:/libs/granite \| inurl:/etc/clientlibs \| inurl:/content/geometrixx \| inurl:/bin/wcm \| inurl:/crx/de site:<target>` | Adobe Experience Manager (AEM) paths, DAM assets, and CRX/DE console |

### Sensitive Parameter Discovery

| Query | What It Finds |
|-------|---------------|
| `inurl:email= \| inurl:phone= \| inurl:name= \| inurl:user= inurl:& site:<target>` | URL parameters handling PII (email, phone, name, user) |

### Code & Data Leak Hunting

Search third-party paste/code sites for leaked code, API keys, credentials, or internal references.

| Query | What It Finds |
|-------|---------------|
| `site:pastebin.com "<target>"` | Code or data leaks on Pastebin (credentials, configs, API keys) |
| `site:jsfiddle.net "<target>"` | Code snippets referencing target on JSFiddle |
| `site:codebeautify.org "<target>"` | Code or data referencing target on CodeBeautify |
| `site:codepen.io "<target>"` | Front-end code referencing target on CodePen |
| `site:groups.google.com "<target>"` | Google Groups discussions referencing target (internal comms, leaked info) |

### Disclosed Vulnerabilities & Bug Bounty

| Query | What It Finds |
|-------|---------------|
| `site:openbugbounty.org inurl:reports intext:"<target>"` | Publicly disclosed XSS and open redirect bugs on OpenBugBounty |
| `"submit vulnerability report" \| "powered by bugcrowd" \| "powered by hackerone"` | Bug bounty programs and vulnerability disclosure programs |
| `site:*/security.txt "bounty"` | Security.txt files advertising bug bounty programs |
| `inurl:/.well-known/security ext:txt` | Security.txt files at standard well-known path |
| `site:*.gov.* "responsible disclosure"` | Government responsible disclosure pages |
| `responsible disclosure hall of fame` | Responsible disclosure hall of fame pages |

### Monitoring & Dashboard Discovery

| Query | What It Finds |
|-------|---------------|
| `inurl:grafana inurl:/dashboard/` | Grafana dashboard pages |
| `intitle:"grafana" inurl:"/grafana/login"` | Grafana login pages |
| `inurl:kibana inurl:/dashboard/` | Kibana dashboard pages |
| `inurl:/app/kibana#` | Accessible Kibana interfaces |
| `inurl:nagios/side.php` | Nagios monitoring pages |
| `inurl:cacti` | Cacti network monitoring pages |
| `inurl:munin` | Munin server monitoring pages |

### API Documentation

| Query | What It Finds |
|-------|---------------|
| `inurl:swagger-ui` | Swagger UI API documentation pages |
| `inurl:swagger.json` | Exposed Swagger JSON API definitions |
| `inurl:openapi.json` | Exposed OpenAPI specifications |
| `inurl:/graphql` | Exposed GraphQL endpoints |
| `intitle:"GraphQL Playground"` | GraphQL Playground interactive interfaces |

### Third-Party Asset Enumeration

| Query | What It Finds |
|-------|---------------|
| `site:atlassian.net intext:company` | Company data on Atlassian (Jira/Confluence) |
| `site:github.com intext:company` | Company code on GitHub |
| `site:gitlab.com intext:company` | Company code on GitLab |
| `site:linkedin.com employees target.com` | LinkedIn employee profiles for target |

## Operator Cheat Sheet

| Operator | Meaning | Example |
|----------|---------|---------|
| `site:` | Restrict results to a domain | `site:tesla.com` |
| `-term` | Exclude results containing term | `-www -shop` |
| `ext:` | Filter by file extension | `ext:php` |
| `inurl:` | URL must contain string | `inurl:?` |
| `intext:` | Page body must contain string | `intext:"tesla.com"` |
| `intitle:` | Page title must contain string | `intitle:"Swagger UI"` |
| `\|` | OR -- match either query | `site:a.com \| site:b.com` |
| `&` | AND -- require both queries | `site:a.com & "choose file"` |

## Data Source

All queries in this collection are sourced from publicly available Google Dorking databases and security research. See the CSV file for the complete machine-readable dataset.
