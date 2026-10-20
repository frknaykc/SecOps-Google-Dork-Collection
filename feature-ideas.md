# Collection Coverage and Follow-ups

This repository is a static, English-language CSV collection of **16,233 distinct Google search queries across 19 categories**. Search results provide leads, not proof of a vulnerability. Replace `<target>` with an authorized domain or organization name as appropriate, and verify results manually. Do not store discovered secret values.

## Implemented coverage

`IdentityAccess/` and `APIExposure/` were added as dedicated categories. The expanded `AI-MLOps/` includes MCP and A2A discovery; `DevOpsCI/` includes workflow orchestration, attestations, and SBOMs; `IdentityAccess/` includes SCIM; `APIExposure/` includes AsyncAPI. Each category README has its own CSV count. See [Research Sources](RESEARCH_SOURCES.md) for the documented basis and search limitations.

## Further priorities

1. **Search-quality review:** Test a representative sample of each category manually within an authorized scope; record which operators and file types Google actually indexes. Avoid promising a result for every query.
2. **Scope clarity:** Distinguish `site:<target>` domain templates from organization-name searches on public code hosts. Treat OIDC, SCIM, and A2A discovery documents as inventory data rather than defects.
3. **Secret hygiene:** Review examples for sample variables versus server-side credentials. Do not collect discovered credential values, and check third-party license and attribution before importing external queries.
4. **Threat-hunting playbooks:** Keep passive Google dorks in `ThreatHunting/`; if added later, log-based hypotheses, ATT&CK techniques, data sources, and false-positive notes belong in separate playbooks. [MITRE container API detection strategy](https://attack.mitre.org/detectionstrategies/DET0198/).

Query syntax and indexing change over time. None of the collection's queries is guaranteed to work against a particular target. Run `python3 scripts/validate_collection.py` and `python3 -m unittest discover -s tests -v` after editing CSVs or counts. No paid search API or hosting plan is required.
