# Login Pages - Google Dork Queries

Dork queries designed to discover exposed login portals, VPN gateways, SSO endpoints, admin panels, and authentication interfaces.

## Summary

| Risk Level | Count |
|------------|-------|
| High | 20 |
| Medium | 11 |
| Low | 5 |

**Total: 1,851 dorks**

## Coverage

| Category | Description |
|----------|-------------|
| CMS Login | WordPress, Joomla admin login pages |
| Monitoring | Grafana, Kibana, Jenkins, GitLab login pages |
| SSO/OAuth | Keycloak, OAuth, OpenID login endpoints |
| VPN | SSL VPN, Cisco ASA, Citrix NetScaler login pages |
| Admin Panels | Generic admin panels, phpMyAdmin, dashboard logins |
| Remote Access | Remote desktop web connections, portal logins |

## Example Usage

```
# Find Jenkins CI login pages
intitle:"Jenkins" inurl:"/login"

# Find Cisco ASA VPN login pages
inurl:/+CSCOE+/logon.html

# Find any admin login pages with parameter URLs
inurl:& intext:admin intext:login

# Find Grafana dashboard login pages
inurl:login "Welcome to Grafana"
```

## Data Source

CSV file: [`GoogleDork-LoginPages.csv`](GoogleDork-LoginPages.csv)
