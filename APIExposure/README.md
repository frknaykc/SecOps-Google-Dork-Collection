# API Documentation and Developer Interfaces — Google Dorks

Google queries for publicly indexed API specifications and developer consoles. Visibility alone does not imply unauthenticated API access or exploitable behavior.

## Summary

| Risk Level | Count |
|---|---:|
| Medium | 5 |
| Low | 59 |
| Informational | 1 |

**Total: 65 dorks**

## Coverage

OpenAPI/Swagger, ReDoc, Springdoc, GraphQL consoles (including Dagster), gRPC configuration, AsyncAPI event descriptions, and webhook integration references.

## Usage

Grouped API-path and documentation queries formerly listed in `Recon` are maintained here. Their alternatives share one `site:<target>` scope; public documentation or a Swagger UI title does not establish a vulnerability.

Replace `<target>` with an organization name or domain as appropriate for the query. Search only authorized scopes. Manually verify whether an indexed result is current, publicly accessible, and actually relevant; never collect or publish discovered secret values.

## Reference

- https://spec.openapis.org/oas/latest.html

The complete query list and individual descriptions are in [GoogleDork-APIExposure.csv](GoogleDork-APIExposure.csv).
