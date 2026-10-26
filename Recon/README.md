# Recon Google Dorks

Google Dork queries for active reconnaissance -- subdomain enumeration, hidden endpoint discovery, code leak hunting, sensitive document/parameter discovery, and disclosed vulnerability lookups. These are **template-based dorks** where you replace `<target>` with your actual target domain.

## Summary

| Risk Level | Count |
|---|---:|
| Critical | 5 |
| High | 29 |
| Medium | 6,633 |
| Low | 37 |

**Total: 6,704 dorks**

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
| `site:<target> ext:php inurl:?` | PHP files with URL parameters -- potential injection points |
| `(site:<target> \| site:<target2>) & "choose file"` | File upload endpoints across multiple domains |
| `site:<target> intext:"choose file" \| intext:"select file" \| intext:"upload PDF"` | File upload forms via button/input text patterns |

### Sensitive File & Extension Discovery

| Query | What It Finds |
|-------|---------------|
| `site:<target> (inurl:config OR inurl:env OR inurl:setting OR inurl:backup OR inurl:admin OR inurl:php)` | URL keyword inventory; matches alone do not establish exposure |
| `inurl:conf \| inurl:env \| inurl:cgi \| inurl:bin \| inurl:etc \| inurl:root \| inurl:sql \| inurl:backup \| inurl:admin \| inurl:php site:<target>` | High-value URL paths (config, env, admin, SQL, backup directories) |
| `site:<target> ext:txt \| ext:pdf \| ext:xml \| ext:xls \| ext:xlsx \| ext:ppt \| ext:pptx \| ext:doc \| ext:docx` | Exposed documents (PDF, Office, XML) on target |
| `intext:"confidential" \| intext:"Not for Public Release" \| intext:"internal use only" \| intext:"do not distribute"` | Pages with confidentiality markers indicating sensitive internal documents |

### Environment & Infrastructure Discovery

| Query | What It Finds |
|-------|---------------|
| `site:<target> (inurl:test OR inurl:env OR inurl:dev OR inurl:staging OR inurl:sandbox OR inurl:debug OR inurl:temp OR inurl:internal OR inurl:demo)` | Environment-related URL keywords; names do not prove weak access controls |
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

The user-submitted policy queries include a historical `2021` filter. Retain it for historical research or deliberately change it for a different period; verify current policy terms separately.

| Query | What It Finds |
|-------|---------------|
| `site:openbugbounty.org inurl:reports intext:"<target>"` | Publicly disclosed XSS and open redirect bugs on OpenBugBounty |
| `"submit vulnerability report" \| "powered by bugcrowd" \| "powered by hackerone"` | Bug bounty programs and vulnerability disclosure programs |
| `site:*/security.txt "bounty"` | Security.txt files advertising bug bounty programs |
| `inurl:/.well-known/security ext:txt` | Security.txt files at standard well-known path |
| `site:*.gov.* "responsible disclosure"` | Government responsible disclosure pages |
| `responsible disclosure hall of fame` | Responsible disclosure hall of fame pages |
| `site:<target> inurl:support intext:security "2021"` | Historical support/security references, not a current policy guarantee |
| `site:<target> intext:security report reward` | Security reporting pages mentioning rewards |
| `site:<target> inurl:security report monetary` | Security URLs mentioning reports and monetary terms |
| `site:<target> inurl:security inurl:report inurl:bounty` | URLs combining disclosure-program keywords |

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

Grouped API discovery queries are maintained in [APIExposure](../APIExposure/); the grouped log/configuration/backup query is in [SensitiveFiles](../SensitiveFiles/). They are not duplicated here.

All queries in this collection are sourced from publicly available Google Dorking databases and security research. See the CSV file for the complete machine-readable dataset.
