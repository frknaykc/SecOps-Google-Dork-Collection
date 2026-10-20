# Error Messages - Google Dork Queries

Dork queries designed to find verbose error messages that leak sensitive server information, SQL syntax, stack traces, and debug details.

## Summary

| Risk Level | Count |
|---|---:|
| Critical | 10 |
| High | 103 |
| Medium | 60 |
| Low | 10 |
| Informational | 1 |

**Total: 184 dorks**

Risk levels prioritize search leads; a matching result is not proof of a vulnerability or unauthorized access.

## Coverage

| Error Type | Description |
|-----------|-------------|
| SQL Errors | Oracle (ORA-*), MySQL, PostgreSQL, SQL Server, DB2 syntax and connection errors |
| PHP Errors | Parse errors, fatal errors, include warnings, division by zero |
| ColdFusion | Error occurred, request processing errors, Lucee errors |
| ASP.NET | Session ID leaks, ELMAH error logs, custom error messages |
| Java/Tomcat | Apache Tomcat error reports, Struts problem reports, EL expression errors |
| Framework | Laravel logs, Whoops error handler, CakePHP routing exceptions |
| Server | 500 Internal Server Errors, 404 pages with server info, Plesk default pages |

## Example Usage

```
# Find SQL injection confirmation via error messages
"You have an error in your SQL syntax near"

# Find exposed Laravel log files
inurl:("/storage/logs/laravel.log") AND intext:("local.ERROR")

# Find Apache Struts in development mode (RCE risk)
intitle:"Struts Problem Report" intext:"development mode is enabled."
```

## Why Error Messages Matter

Verbose error messages are a goldmine for attackers:

- **SQL errors** confirm injectable parameters and reveal database type/version
- **Stack traces** expose file paths, framework versions, and internal architecture
- **Connection errors** reveal database hostnames, usernames, and port numbers
- **Debug pages** (Whoops, Struts dev mode) may enable code execution

## Data Source

CSV file: [`GoogleDork-ErrorMessages.csv`](GoogleDork-ErrorMessages.csv)
