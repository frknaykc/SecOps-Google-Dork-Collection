# Backups Google Dorks

Google Dork queries for finding exposed backup files, database dumps, archived web roots, and other forgotten or misconfigured backup artifacts. These are among the highest-value reconnaissance targets because backups often contain credentials, source code, and full database contents.

## Summary

| Risk Level | Count |
|---|---:|
| Critical | 23 |
| High | 24 |
| Medium | 20 |
| Low | 5 |

**Total: 72 dorks**

Risk levels prioritize search leads; a matching result is not proof of a vulnerability or unauthorized access.

## Query Reference

### Critical Risk

These dorks find backup files that very likely contain credentials, database contents, or full application source code.

| Query | What It Finds |
|-------|---------------|
| `inurl:backup.zip` | Downloadable ZIP backup archives -- may contain entire site or DB |
| `inurl:backup.rar` | Downloadable RAR backup archives |
| `inurl:backup.tar` | Downloadable TAR backup archives |
| `inurl:backup.tar.gz` | Downloadable compressed TAR backup archives |
| `inurl:backup.sql` | Exposed SQL database backup files with table structures and data |
| `inurl:database.sql` | Exposed database SQL dump files |
| `inurl:dump.sql` | SQL dump files with potential credentials and full data |
| `inurl:backup filetype:sql` | SQL backup files in backup-related URL paths |
| `inurl:save filetype:sql` | Saved SQL files that may contain database exports |
| `filetype:sql password` | SQL files containing password fields or data |
| `filetype:sql username` | SQL files containing username fields or data |
| `inurl:db-backup` | Database backup directories or files |
| `inurl:backup-db` | Database backup paths (alternative naming convention) |
| `inurl:jenkins-backup` | Jenkins CI/CD server backup files (may contain secrets, job configs) |
| `inurl:gitlab-backup` | GitLab instance backup files (repos, configs, user data) |

### High Risk

These dorks find backup archives, directory listings, and file types commonly associated with backup artifacts.

| Query | What It Finds |
|-------|---------------|
| `inurl:backup` | URLs containing backup paths or directories |
| `inurl:backups` | URLs containing backups directories |
| `inurl:web.zip` | ZIP archives of web application files |
| `inurl:website.zip` | ZIP archives containing entire website backups |
| `inurl:site.zip` | ZIP archives of site content |
| `inurl:www.zip` | ZIP archives of www root directory |
| `inurl:public_html.zip` | ZIP archives of public_html (common hosting root) |
| `inurl:html.zip` | ZIP archives of HTML directory content |
| `filetype:bak` | .bak backup files (source code, configs) |
| `filetype:old` | .old renamed files (previous config versions) |
| `filetype:backup` | Files with .backup extension |
| `filetype:swp` | Vim swap files leaking file contents being edited |
| `filetype:sql` | Any exposed SQL files on the web |
| `filetype:db` | Exposed database files (.db format) |
| `filetype:sqlite` | Exposed SQLite database files |
| `filetype:sqlite3` | Exposed SQLite3 database files |
| `inurl:docker-backup` | Docker container/volume backup files |
| `inurl:ci-backup` | CI/CD pipeline backup files |
| `intitle:"Index of" backup` | Directory listings of backup folders |
| `intitle:"Index of" backups` | Directory listings of backups folders |
| `intitle:"Index of" dump` | Directory listings of dump folders |
| `intitle:"Index of" database` | Directory listings of database folders |
| `inurl:backup "Parent Directory"` | Apache-style directory listings in backup paths |

### Medium Risk

| Query | What It Finds |
|-------|---------------|
| `filetype:orig` | .orig files created during patching or editing |
| `filetype:tmp` | Temporary files with sensitive intermediate data |
| `filetype:abk` | .abk (AutoBackup) files from various applications |

## Example Usage

To find exposed SQL database backups:

```
inurl:backup.sql
```

This may reveal files like:
- `https://example.com/backup/db_backup.sql` -- full database dump
- `https://example.com/old/backup.sql` -- forgotten migration file

These files often contain `CREATE TABLE`, `INSERT INTO` statements with usernames, password hashes, emails, and other sensitive data.

## Combination Tips

Combine backup dorks with site-specific operators for targeted recon:

```
inurl:backup.sql site:target.com
filetype:sql password site:target.com
intitle:"Index of" backup site:target.com
```

## Data Source

All queries in this collection are sourced from publicly available Google Dorking databases and security research. See the CSV file for the complete machine-readable dataset.
