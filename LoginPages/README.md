# Login Pages - Google Dork Queries

Dork queries designed to discover exposed login portals, VPN gateways, SSO endpoints, admin panels, Zero Trust proxies, and authentication interfaces.

## Summary

| Risk Level | Count |
|---|---:|
| Critical | 6 |
| High | 28 |
| Medium | 1,661 |
| Low | 10 |

**Total: 1,705 dorks**

Risk levels prioritize search leads; a matching result is not proof of a vulnerability or unauthorized access.

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
