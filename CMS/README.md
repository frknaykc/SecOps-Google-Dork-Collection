# CMS - Google Dork Queries

Dork queries designed to identify Content Management System installations, versions, configurations, and vulnerabilities across WordPress, Joomla, Drupal, TYPO3, Magento, and other CMS platforms.

## Summary

| Risk Level | Count |
|---|---:|
| Critical | 25 |
| High | 16 |
| Medium | 84 |
| Low | 16 |

**Total: 141 dorks**

Risk levels prioritize search leads; a matching result is not proof of a vulnerability or unauthorized access.

## Coverage

| CMS | Dork Count | Description |
|-----|-----------|-------------|
| WordPress | 30+ | Login pages, config files, backup dumps, REST API user enumeration, plugin vulnerabilities, debug logs |
| Joomla | 8 | Admin login, debug console, installer, outdated versions, RSS/Atom feeds |
| Drupal | 4 | User registration, installation detection, changelog version disclosure |
| TYPO3 | 8 | Installation pages, admin login, config file exposure |
| BlogEngine.NET | 2 | Version detection and installation discovery |
| Magento | 1 | Admin login page detection |
| Contao | 2 | File directories and admin pages |
| Nibbleblog | 1 | Installation detection |
| vBulletin | 1 | Version detection |

## Example Usage

```
# Find WordPress REST API user enumeration
inurl:/wp-json/wp/v2/users "id":1

# Find WordPress config backups with DB passwords
inurl:wp-config.php intext:DB_PASSWORD

# Find Joomla installations with debug enabled
"Consola de Joomla! Debug" inurl:index.php

# Find TYPO3 exposed config files
inurl:typo3conf/localconf.php

# Find unfinished WordPress installations
inurl:"/wp-admin/setup-config.php" intitle:"Setup Configuration File"
```

## Why CMS Detection Matters

CMS-specific dorks are valuable because:

- **Version detection** enables targeted exploit matching
- **Config file exposure** reveals database credentials and secret keys
- **Backup files** in upload directories contain full site data
- **Plugin vulnerabilities** (Revolution Slider, WP Mobile Detector) provide direct RCE/LFI
- **REST API enumeration** reveals admin usernames for brute-force attacks

## Data Source

CSV file: [`GoogleDork-CMS.csv`](GoogleDork-CMS.csv)
