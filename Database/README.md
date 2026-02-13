# Database - Google Dork Queries

Dork queries designed to find exposed database interfaces, management tools, SQL dump files, and database configuration leaks.

## Summary

| Risk Level | Count |
|------------|-------|
| Critical | 24 |
| High | 8 |
| Medium | 4 |

**Total: 115 dorks**

## Coverage

| Database Type | Description |
|--------------|-------------|
| MySQL | Dump files, connection errors, configuration leaks |
| PostgreSQL | Connection strings, JDBC credentials, parser errors |
| MongoDB | Connection URIs, SRV strings, passwords |
| phpMyAdmin | Login pages, SQL dumps, setup pages, query interfaces |
| SQLite | Exposed SQLite database files |
| Generic SQL | Setup scripts, backup files, CREATE TABLE statements |

## Example Usage

```
# Find exposed phpMyAdmin running as root
intitle:phpMyAdmin "Welcome to phpMyAdmin *" "running on as root@"

# Find MongoDB connection strings with passwords
"mongodb://" "password"

# Find MySQL dump files with schema info
"-- MySQL dump" "Server version" "Table structure for table"

# Find phpMyAdmin SQL dumps with password data
filetype:sql "phpmyAdmin SQL Dump" (pass|password|passwd|pwd)
```

## Data Source

CSV file: [`GoogleDork-Database.csv`](GoogleDork-Database.csv)
