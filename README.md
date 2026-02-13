<p align="center">
  <img src="Public/logodork.png" alt="Google Dork Collection" width="480" style="max-width: 100%; max-height: 220px; width: auto; height: auto; object-fit: contain; display: block; margin: 0 auto;" />
</p>

<p align="center">
  <a href="https://github.com/frknaykc/SecOps-Google-Dork-Collection/stargazers"><img src="https://img.shields.io/github/stars/frknaykc/SecOps-Google-Dork-Collection?style=flat-square" alt="GitHub stars" /></a>
  <a href="https://github.com/frknaykc/SecOps-Google-Dork-Collection/network/members"><img src="https://img.shields.io/github/forks/frknaykc/SecOps-Google-Dork-Collection?style=flat-square" alt="GitHub forks" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License" /></a>
  <a href="https://github.com/frknaykc/SecOps-Google-Dork-Collection/commits"><img src="https://img.shields.io/github/last-commit/frknaykc/SecOps-Google-Dork-Collection?style=flat-square" alt="Last commit" /></a>
</p>

# Google Dork Collection for Threat Hunters, Bug Bounty Researchers, Pentesters & Red Teamers

<p align="center">
  <strong>A curated collection of 18,868+ Google Dork queries organized by category — detect exposed infrastructure, sensitive files, C2 panels, and misconfigurations.</strong>
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

This repository provides **ready-to-use Google Dork queries** — advanced search operators that leverage Google's indexing to uncover information not easily accessible through standard searches. These queries help security researchers, threat hunters, and SOC teams:

- **Detect exposed infrastructure** — Web servers, databases, admin panels, IoT devices, and network equipment
- **Hunt for threats** — C2 servers, RAT panels, web shells, phishing kits, and malware infrastructure
- **Find sensitive data** — Credentials, API keys, config files, backups, and private keys leaked online
- **Identify vulnerabilities** — SQLi, XSS, SSRF, LFI, RCE-prone parameters and error messages
- **Perform reconnaissance** — Subdomain enumeration, code leak hunting, cloud storage discovery, and API endpoint identification

Each query is documented with a **description** and **risk level** (`Critical` / `High` / `Medium` / `Low` / `Informational`) to help prioritize findings during reconnaissance. The queries target exposed infrastructure, misconfigured services, and known technology fingerprints that can be discovered through Google's search index.

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
| Web Servers | [WebServer/](WebServer/) | Identify web server types, versions, default pages, and misconfigurations | 277 |
| Databases | [Database/](Database/) | Find exposed database interfaces, phpMyAdmin, and SQL/NoSQL management tools | 115 |
| Login Pages | [LoginPages/](LoginPages/) | Discover exposed login portals, VPN, SSO, and authentication endpoints | 1,851 |
| Sensitive Files | [SensitiveFiles/](SensitiveFiles/) | Locate exposed config files, API keys, credentials, logs, and private keys | 2,853 |
| IoT Devices | [IoTDevices/](IoTDevices/) | Find internet-connected cameras, printers, NAS, and smart device interfaces | 778 |
| Network Devices | [NetworkDevices/](NetworkDevices/) | Discover monitoring tools, scan reports, network graphs, and device interfaces | 121 |
| CMS | [CMS/](CMS/) | Identify WordPress, Joomla, Drupal, TYPO3, Magento, and other CMS installations | 878 |
| Cloud Services | [CloudServices/](CloudServices/) | Find leaked files on AWS S3, Azure Blob, GCP, and exposed Kubernetes endpoints | 33 |
| Vulnerable Servers | [VulnerableServers/](VulnerableServers/) | Detect vulnerable parameters (XSS, SQLi, SSRF, LFI, RCE), web shells, and exposed admin tools | 2,632 |
| Error Messages | [ErrorMessages/](ErrorMessages/) | Find verbose error messages leaking SQL, stack traces, and server details | 247 |
| Backups | [Backups/](Backups/) | Find exposed backup files, database dumps, and archived web roots | 56 |
| Wiki | [Wiki/](Wiki/) | Discover MediaWiki/WikkaWiki installations, login pages, and misconfigurations | 51 |
| Recon | [Recon/](Recon/) | Template-based dorks for subdomain enum, code leaks, bug bounty, and API discovery | 8,731 |
| Threat Hunting | [ThreatHunting/](ThreatHunting/) | Detect C2 infrastructure, malware panels, web shells, phishing kits, and threat intel resources | 245 |

> **Total: 18,868 unique dorks** across 14 categories.

---

## CSV Format

Each category folder contains a `.csv` file with the following columns:

| Column | Description |
|--------|-------------|
| `Query` | The Google Dork search query |
| `Description` | What the query finds and why it matters |
| `RiskLevel` | Severity rating: `Critical`, `High`, `Medium`, `Low`, `Informational` |

### Risk Levels Explained

| Level | Meaning |
|-------|---------|
| **Critical** | Direct access to admin panels, config files, credentials, or database management interfaces |
| **High** | Server version disclosure, directory listings, sensitive information exposure |
| **Medium** | Server type/version identification, technology stack fingerprinting |
| **Low** | General information gathering, technology identification |
| **Informational** | Default pages, test pages, platform identification with minimal direct risk |

---

## Usage

1. Browse the category folder that matches your objective
2. Open the `.csv` file and pick a query
3. Paste it directly into [Google Search](https://www.google.com/)
4. Combine with `site:target.com` to scope results to a specific target

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

1. Choose the appropriate category folder (or suggest a new one).
2. Add entries to the CSV file following the existing format.
3. Update the folder's `README.md` with descriptions for new entries.
4. Submit a pull request with your additions.

---

## License

This project is provided as-is for educational purposes. See individual category folders for specific attribution where applicable.
