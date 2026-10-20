# Identity and SaaS Access — Google Dorks

Publicly indexed identity-provider metadata, federation configuration, and OAuth integration references for authorized asset inventory. A discovery document or callback URL is not a security vulnerability.

## Summary

| Risk Level | Count |
|---|---:|
| High | 3 |
| Medium | 2 |
| Low | 40 |
| Informational | 11 |

**Total: 56 dorks**

## Coverage

OIDC discovery, OAuth authorization metadata, SAML metadata, SCIM provisioning metadata and schemas, workload identity federation, and public integration configuration.

## Usage

Replace `<target>` with an organization name or domain as appropriate for the query. Search only authorized scopes. Manually verify whether an indexed result is current, publicly accessible, and actually relevant; never collect or publish discovered secret values.

## Reference

- https://www.cisa.gov/news-events/news/cisa-and-nist-release-guidelines-protect-federal-cloud-identity-systems-token-theft-forgery-and

The complete query list and individual descriptions are in [GoogleDork-IdentityAccess.csv](GoogleDork-IdentityAccess.csv).
