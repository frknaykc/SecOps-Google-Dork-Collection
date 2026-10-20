<p align="center">
  <img src="Public/logodork.png" alt="Google Dork Collection" width="480" style="max-width: 100%; max-height: 220px; width: auto; height: auto; object-fit: contain; display: block; margin: 0 auto;" />
</p>

<p align="center">
  <a href="https://github.com/frknaykc/SecOps-Google-Dork-Collection/stargazers"><img src="https://img.shields.io/github/stars/frknaykc/SecOps-Google-Dork-Collection?style=flat-square" alt="GitHub stars" /></a>
  <a href="https://github.com/frknaykc/SecOps-Google-Dork-Collection/network/members"><img src="https://img.shields.io/github/forks/frknaykc/SecOps-Google-Dork-Collection?style=flat-square" alt="GitHub forks" /></a>
  <a href="https://github.com/frknaykc/SecOps-Google-Dork-Collection/commits"><img src="https://img.shields.io/github/last-commit/frknaykc/SecOps-Google-Dork-Collection?style=flat-square" alt="Last commit" /></a>
</p>

# Google Dork Collection for Threat Hunters, Bug Bounty Researchers, Pentesters & Red Teamers

<p align="center">
  <strong>16,233 distinct Google Dork queries across 19 categories — research leads for exposed infrastructure, identity and API surfaces, cloud services, and threat hunting.</strong>
</p>

<p align="center">
  <a href="#what-is-a-google-dork">What Is a Google Dork?</a> •
  <a href="#repository-structure">Repository Structure</a> •
  <a href="#csv-format">CSV Format</a> •
  <a href="#usage">Usage</a> •
  <a href="#contributing">Contributing</a>
</p>

---

## Introduction

This repository provides a **CSV collection of Google search-query leads** for authorized research. Search indexing is incomplete, and the queries have not been individually tested against live Google results. The collection helps security researchers, threat hunters, and SOC teams:

- **Detect exposed infrastructure** — Web servers, databases, admin panels, IoT devices, and network equipment
- **Hunt for threats** — C2 servers, RAT panels, web shells, phishing kits, and malware infrastructure
- **Find sensitive data** — Credentials, API keys, config files, backups, and private keys leaked online
- **Identify potential vulnerability leads** — Parameters, error messages, and public configuration that warrant authorized validation
- **Perform reconnaissance** — Subdomain enumeration, code leak hunting, cloud storage discovery, and API endpoint identification

Each query has a **description** and a **risk level** (`Critical` / `High` / `Medium` / `Low` / `Informational`) for prioritizing manual review. A Google result is a lead, not confirmation of exposure, valid credentials, unauthorized access, or a vulnerability. Legacy queries may use outdated syntax or refer to products no longer in use. The latest category expansion and its source references are documented in [Research Sources](RESEARCH_SOURCES.md).

---

## What Is a Google Dork?

A **"Google dork"** refers to the use of advanced Google search operators to uncover information that is not easily accessible through standard search queries. **"Google dorking"** (also commonly known as **"Google hacking"**) is the strategic use of these advanced search techniques to locate sensitive or misconfigured data exposed on the internet.

By combining operators such as `site:`, `filetype:`, `intitle:`, and `inurl:`, users can identify resources that typical search users would not normally discover.

Google Dorking is a powerful **OSINT (Open Source Intelligence)** technique. When used correctly, it can help uncover:

- Exposed credentials
- Misconfigured directories
- Admin login panels
- Sensitive documents
- Unsecured IP cameras
- Files with improper access permissions

These techniques are widely used by:

- **Threat hunters**
- **Bug bounty researchers**
- **Penetration testers (pentesters)**
- **Cybersecurity analysts**

However, the same techniques can also be leveraged by malicious actors for reconnaissance and target identification. For this reason, Google Dorking represents a critical area of knowledge from both **defensive and offensive security** perspectives.

> In the right hands, Google Dorking is a powerful and free reconnaissance tool that helps identify vulnerabilities before they can be exploited — making it an essential skill in modern cybersecurity.

---

## Repository Structure

| Category | Folder | Description | Dork Count |
|----------|--------|-------------|------------|
| Web Servers | [WebServer/](WebServer/) | Identify web server types, versions, default pages, and misconfigurations | 260 |
| Databases | [Database/](Database/) | Find exposed database interfaces, phpMyAdmin, and SQL/NoSQL management tools | 86 |
| Login Pages | [LoginPages/](LoginPages/) | Discover exposed login portals, VPN, SSO, and authentication endpoints | 1,705 |
| Identity & Access | [IdentityAccess/](IdentityAccess/) | Inventory OIDC/OAuth, SAML, SCIM, and public identity integration references | 56 |
| Sensitive Files | [SensitiveFiles/](SensitiveFiles/) | Locate indexed configs, API keys, credentials, logs, workflow exports, and private-key leads | 2,789 |
| IoT Devices | [IoTDevices/](IoTDevices/) | Find internet-connected cameras, printers, NAS, and smart device interfaces | 773 |
| Network Devices | [NetworkDevices/](NetworkDevices/) | Discover monitoring tools, scan reports, network graphs, and device interfaces | 119 |
| CMS | [CMS/](CMS/) | Identify WordPress, Joomla, Drupal, TYPO3, Magento, and other CMS installations | 141 |
| Cloud Services | [CloudServices/](CloudServices/) | Inventory AWS, Azure, GCP, R2, Wasabi, B2, and Firebase/Supabase storage leads | 95 |
| Vulnerable Servers | [VulnerableServers/](VulnerableServers/) | Find parameters and interfaces that may warrant authorized security testing | 2,593 |
| Error Messages | [ErrorMessages/](ErrorMessages/) | Find verbose error messages leaking SQL, stack traces, and server details | 184 |
| Backups | [Backups/](Backups/) | Find exposed backup files, database dumps, and archived web roots | 72 |
| Wiki | [Wiki/](Wiki/) | Discover MediaWiki/WikkaWiki installations, login pages, and misconfigurations | 44 |
| Recon | [Recon/](Recon/) | Template-based dorks for subdomain enum, code leaks, bug bounty, and API discovery | 6,702 |
| Threat Hunting | [ThreatHunting/](ThreatHunting/) | Find public C2, malware, incident-response, and defensive telemetry research leads | 304 |
| DevOps & CI/CD | [DevOpsCI/](DevOpsCI/) | Inventory pipelines, orchestration, SBOMs, attestations, and observability references | 105 |
| AI, LLM & MLOps | [AI-MLOps/](AI-MLOps/) | Find AI platform interfaces, A2A/MCP discovery references, and model-service leads | 104 |
| API Exposure | [APIExposure/](APIExposure/) | Discover OpenAPI/AsyncAPI descriptions, GraphQL references, and developer interfaces | 63 |
| OSINT & Leaks | [OSINT/](OSINT/) | Discover exposed SaaS collaboration spaces (Notion, Airtable, Trello), Zoom recordings, and PII | 38 |

> **Total: 16,233 unique dorks** across 19 categories. Exact and typographic/case/whitespace variants have been deduplicated; queries have not been validated against live Google results.

---

## CSV Format

Each category folder contains a `.csv` file with the following columns:

| Column | Description |
|--------|-------------|
| `Query` | The Google Dork search query |
| `Description` | What the query finds and why it matters |
| `RiskLevel` | Manual-review priority, not a verified severity or vulnerability |

### Risk Levels Explained

| Level | Meaning |
|-------|---------|
| **Critical** | Potentially high-impact exposure lead; verify the result and access controls manually |
| **High** | Potentially sensitive data or privileged interface lead requiring review |
| **Medium** | Configuration, technology, or endpoint lead that may warrant investigation |
| **Low** | General asset or technology inventory lead |
| **Informational** | Public metadata or documentation with no implied security defect |

---

## Usage

1. Browse the category matching your research objective.
2. Open its CSV and choose a query. Replace `<target>` after `site:` with an authorized domain. For queries such as `site:github.com "<target>"`, use a relevant organization or project name instead.
3. Paste the query into [Google Search](https://www.google.com/) for manual review. Some legacy queries need syntax adjustments; Google may ignore quoted punctuation or not index the referenced resource.
4. Where a query does not already define scope, add `site:example.com` for an authorized domain. Do not treat a search match as a confirmed vulnerability.

---

## Legal Disclaimer

> **WARNING**: This repository is provided for **educational and authorized security testing purposes only**.

- **Always** obtain proper written authorization before performing any reconnaissance or testing against systems you do not own.
- Unauthorized access to computer systems is **illegal** in most jurisdictions.
- The authors are **not responsible** for any misuse of the information contained in this repository.
- Use these dorks responsibly and ethically, in compliance with all applicable laws and regulations.
- Google may rate-limit or block automated queries. Respect Google's Terms of Service.

---

## Contributing

To add new dork queries:

1. Choose the most specific existing category, or propose a new category if the topic does not fit.
2. Add entries to its CSV with a query-specific English description. Never include retrieved credential values or claim a result proves a vulnerability.
3. Avoid duplicate queries across categories, including typographic quote, case, and whitespace variants. Update the category and root README counts.
4. Run `python3 scripts/validate_collection.py` and `python3 -m unittest discover -s tests -v` before submitting a pull request.

---

## License

No repository-wide license file is currently included. Do not assume that the MIT badge previously shown here granted redistribution rights for third-party query collections; verify attribution and licensing before reusing external material.
