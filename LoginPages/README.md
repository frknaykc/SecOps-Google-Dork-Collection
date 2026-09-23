# Login Pages - Google Dork Queries

Dork queries designed to discover exposed login portals, VPN gateways, SSO endpoints, admin panels, Zero Trust proxies, and authentication interfaces.

## Summary

| Risk Level | Count | Description |
|------------|-------|-------------|
| Critical | 6 | High-impact enterprise VPN gateways (Palo Alto GlobalProtect, Ivanti, Fortinet, F5, Citrix, Teleport) |
| High | 36 | Enterprise SSO endpoints, admin consoles, and remote management portals |
| Medium | 1,811 | Generic admin logins, CMS authentication pages, and portal forms |
| Low | 6 | Informational authentication landing pages and password reset screens |
| **Total** | **1,859** | |

## Coverage

| Category | Description |
|----------|-------------|
| **Enterprise VPN & Zero Trust** | Palo Alto GlobalProtect, Ivanti / Pulse Secure, Fortinet SSL-VPN, SonicWall, Teleport |
| **Application Delivery Controllers** | F5 BIG-IP TMUI / APM, Citrix NetScaler Gateway |
| **SSO / IAM** | Keycloak realms, Okta, OAuth, OpenID Connect authentication endpoints |
| **CMS Login** | WordPress (`wp-login.php`), Joomla, Drupal, Magento admin portals |
| **Monitoring & CI/CD** | Jenkins, GitLab, Grafana, Kibana login screens |
| **Remote Access** | RDP Web Access, Apache Guacamole, VMware Horizon web portals |

## Example Usage

```
# Find Palo Alto Networks GlobalProtect VPN login portals
intitle:"GlobalProtect Portal" inurl:"/global-protect/login.esp"

# Find Ivanti Connect Secure / Pulse Secure SSL-VPN portals
inurl:"/dana-na/auth/url_default/welcome.cgi"

# Find Fortinet FortiGate SSL-VPN authentication pages
inurl:"/remote/login" "FortiToken" | "Please login"

# Find F5 BIG-IP TMUI / APM login interfaces
inurl:"/tmui/login.jsp" | inurl:"/my.policy"

# Find Teleport Zero Trust access proxy login pages
intitle:"Teleport" inurl:":3080/web/login"
```

## Data Source

CSV file: [`GoogleDork-LoginPages.csv`](GoogleDork-LoginPages.csv)
