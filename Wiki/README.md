# Wiki Google Dorks

Google Dork queries for discovering MediaWiki installations, WikkaWiki instances, wiki login pages, and wiki-related misconfigurations. Wikis are frequent targets because they often allow anonymous editing, expose user data, or run outdated software with known vulnerabilities.

## Summary

| Risk Level | Count | Description |
|------------|-------|-------------|
| High | 5 | Login/registration pages, directory listings, login redirects |
| Medium | 15 | Wiki installations by domain TLD and URL path patterns |
| Low | 17 | General wiki fingerprinting, page footers, content discovery |
| **Total** | **51** | |

## Query Reference

### High Risk

Dorks that find wiki login/registration pages or directory listings -- these can indicate open registration, weak access controls, or exposed wiki data.

| Query | What It Finds |
|-------|---------------|
| `site:.edu "Log in / create account"` | MediaWiki login pages on .edu domains allowing account creation |
| `"Log in / createaccount"` | MediaWiki login/registration pages (may allow open registration) |
| `"wiki/index.php?title=Special:Userlogin&returnto"` | MediaWiki login pages with return-to redirect parameters |
| `inurl:wiki/index.php?title=Special:Userlogin&returnto` | MediaWiki user login pages via URL pattern |
| `"Parent Directory" "Last modified" wikipedia` | Directory listings related to Wikipedia/wiki data or mirrors |

### Medium Risk

Dorks that identify specific wiki installations by domain, path, or subdomain pattern.

| Query | What It Finds |
|-------|---------------|
| `"There is currently no text in this page..."` | Empty/stub wiki pages that may allow anonymous editing |
| `allinurl:".edu/mediawiki/index.php"` | MediaWiki installations on .edu (university) domains |
| `allinurl:".com/mediawiki/index.php"` | MediaWiki installations on .com domains |
| `allinurl:".net/mediawiki/index.php"` | MediaWiki installations on .net domains |
| `allinurl:".org/mediawiki/index.php"` | MediaWiki installations on .org domains |
| `allinurl:".info/mediawiki/index.php"` | MediaWiki installations on .info domains |
| `allinurl:".com/wiki/index.php"` | Wiki installations at /wiki/ path on .com domains |
| `allinurl:".net/wiki/index.php"` | Wiki installations at /wiki/ path on .net domains |
| `allinurl:".org/wiki/index.php"` | Wiki installations at /wiki/ path on .org domains |
| `allinurl:".info/wiki/index.php"` | Wiki installations at /wiki/ path on .info domains |
| `allinurl:".edu/wiki/index.php"` | Wiki installations at /wiki/ path on .edu domains |
| `allinurl:"http://wiki."` | Wiki subdomains (wiki.example.com) across the web |
| `allinurl:"http://mediawiki."` | MediaWiki subdomains (mediawiki.example.com) |
| `allinurl:"http://wikka."` | WikkaWiki installations via wikka subdomain |
| `site:.edu inurl:wiki` | Wiki installations on .edu domains via URL path |
| `inurl:"wiki/index.php?title="` | MediaWiki pages via standard title parameter URL |

### Low Risk

General wiki fingerprinting and content discovery dorks.

| Query | What It Finds |
|-------|---------------|
| `"This page was last modified on" "wiki"` | Wiki pages via MediaWiki footer signature |
| `"This page was last modified on"` | Pages with MediaWiki-style last-modified footer |
| `"This page has been accessed"` | Wiki pages exposing page access/hit counters |
| `Keyword inurl:wiki` | Generic keyword + wiki URL path combination |
| `inurl:MediaWiki_talk` | MediaWiki talk/discussion pages |
| `keyword "wiki" (site:.edu)` | Wiki content on educational institution domains |
| `site:.edu inurl:MediaWiki_talk` | MediaWiki talk pages on .edu domains |
| `site:.edu wiki` | Broad wiki content on educational domains |
| `inurl:wiki` | Any wiki-related URL paths |
| `"isa registered trademark of the Wikimedia Foundation, Inc.,"` | Sites running Wikimedia Foundation software |
| `"wiki inurl:.edu"` | Wiki installations on educational domains |
| `wiki inurl:.edu` | Wiki pages on .edu domains |
| `"Toolbox""This page was last modified` | MediaWiki pages via Toolbox sidebar and modification footer |
| `"Login required to edit"` | Wikis with edit restrictions (protected content) |
| `"Main Page""discussion""edit"` | MediaWiki main pages with discussion and edit tabs |
| `"This page has beenaccessed""Privacy policy"` | Wiki pages with access counters and privacy links |
| `"Wiki:About"` | Wiki About pages revealing software and configuration |

## Why Wikis Matter for Recon

- **Open registration**: Many wikis allow anyone to create accounts and edit content -- useful for C2 operators to plant content
- **Version disclosure**: MediaWiki footer and special pages often reveal exact software version
- **User enumeration**: `Special:ListUsers` and talk pages expose usernames
- **Outdated installs**: Many wikis run years-old versions with known CVEs
- **Internal wikis**: Corporate/academic wikis may leak internal documentation

## Example Usage

Find MediaWiki installations on educational domains:

```
allinurl:".edu/mediawiki/index.php"
```

Find wikis with open registration:

```
"Log in / createaccount"
```

## Data Source

All queries in this collection are sourced from publicly available Google Dorking databases and security research. See the CSV file for the complete machine-readable dataset.
