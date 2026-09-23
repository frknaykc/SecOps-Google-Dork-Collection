# OSINT & Cloud SaaS Leakage Google Dorks

A curated collection of Google Dork queries designed for **Open Source Intelligence (OSINT)** and passive corporate footprinting. These template queries locate publicly indexed corporate collaboration spaces, unauthenticated meeting recordings, shared spreadsheets with PII, and exposed API documentation. Replace `<target>` with your target domain, organization, or brand name.

## Summary

| Risk Level | Count | Description |
|------------|-------|-------------|
| Critical | 5 | Direct access to shared customer databases, unprotected meeting recordings, salary rosters, and credential dumps |
| High | 11 | Exposed corporate workspaces, sprint roadmaps, architecture diagrams, API schemas, and form submissions |
| Medium | 3 | Public product UI mockups, organizational charts, and anonymous paste leaks |
| **Total** | **19** | |

## Coverage

| Platform / Focus Area | Description |
|-----------------------|-------------|
| **Collaboration & Workspaces** | Notion, Airtable, Trello, Miro, Figma, Coda public pages and boards |
| **Meeting Recordings** | Zoom cloud recordings (`/rec/play/`, `/rec/share/`), Microsoft Teams video files, Loom screencasts |
| **Corporate PII & HR** | Employee rosters, staff directories, salary spreadsheets, organizational hierarchy charts |
| **API Workspaces & Specs** | Public Postman team workspaces, SwaggerHub public API schemas |
| **Form Analytics & Pastes** | Google Forms live analytics (`viewanalytics`), Rentry, and ControlC paste leaks |

## Query Reference

### Collaboration & Cloud Workspaces (SaaS Leaks)

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `site:notion.site "<target>"` | Publicly published Notion workspaces and internal company wikis | High |
| `site:notion.so "<target>"` | Shared internal processes, onboarding guides, and customer notes | High |
| `site:airtable.com/shr "<target>"` | Publicly shared Airtable bases containing customer data or lead rosters | Critical |
| `site:trello.com/b/ "<target>"` | Public Trello boards revealing sprint tasks, roadmaps, and credentials | High |
| `site:miro.com/app/board/ "<target>"` | Open Miro whiteboards detailing internal system architectures and topologies | High |
| `site:figma.com/file/ "<target>"` | Publicly accessible Figma design files and product prototypes | Medium |
| `site:coda.io/d/ "<target>"` | Public Coda documents containing company project plans and specs | High |

### Meeting Recordings & Media Transcripts

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `site:zoom.us/rec/play "<target>"` | Publicly indexed Zoom cloud meeting recordings without password protection | Critical |
| `site:zoom.us/rec/share "<target>"` | Shared links to sensitive business Zoom conference recordings | Critical |
| `site:sharepoint.com inurl:":v:" "<target>"` | Publicly accessible Microsoft Teams meeting video recordings on SharePoint | High |
| `site:loom.com/share "<target>"` | Open Loom screen recordings containing internal product demos and debug videos | High |

### Corporate PII, HR & Form Analytics

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `site:docs.google.com/spreadsheets/ ("confidential" \| "salary" \| "passwords") "<target>"` | Google Sheets labeled with confidentiality markers, salaries, or passwords | Critical |
| `site:docs.google.com/forms inurl:viewanalytics "<target>"` | Live response analytics and survey submissions for target Google Forms | High |
| `filetype:xlsx \| filetype:csv ("employee list" \| "staff directory" \| "salary") "<target>"` | Downloadable spreadsheets with employee rosters, titles, and salaries | Critical |
| `filetype:pdf ("organization chart" \| "organigramme") "<target>"` | Corporate organizational charts revealing reporting hierarchies | Medium |

### Public API Workspaces & Paste Leaks

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `site:postman.co/workspace/ "<target>"` | Public Postman workspaces revealing internal API collections and endpoints | High |
| `site:app.swaggerhub.com/apis/ "<target>"` | Public SwaggerHub API definitions exposing enterprise API schemas | High |
| `site:rentry.co "<target>"` | Anonymous paste text leaks and configuration notes referencing target | Medium |
| `site:controlc.com "<target>"` | Target configuration dumps and leaked text snippets on ControlC | High |

## Data Source

CSV file: [`GoogleDork-OSINT.csv`](GoogleDork-OSINT.csv)
