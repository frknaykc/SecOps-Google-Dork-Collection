# Vulnerable Servers Google Dorks

Google Dork queries for detecting servers with vulnerable parameters and error pages that leak sensitive information. These dorks target common vulnerability classes (XSS, SQLi, SSRF, LFI, RCE, Open Redirect) by searching for URL parameter patterns known to be exploitation-prone. Replace `<target>` with your actual target domain.

## Summary

| Risk Level | Count |
|---|---:|
| Critical | 116 |
| High | 2,328 |
| Medium | 149 |

**Total: 2,593 dorks**

Risk levels prioritize search leads; a matching result is not proof of a vulnerability or unauthorized access.

## Query Reference

### Server Error Pages

| Query | What It Finds |
|-------|---------------|
| `inurl:"error" \| intitle:"exception" \| intitle:"failure" \| intitle:"server at" \| inurl:exception \| "database error" \| "SQL syntax" \| "undefined index" \| "unhandled exception" \| "stack trace" site:<target>` | Server error pages leaking stack traces, SQL syntax errors, database errors, and debug info |

### XSS-Prone Parameters

| Query | What It Finds |
|-------|---------------|
| `inurl:q= \| inurl:s= \| inurl:search= \| inurl:query= \| inurl:keyword= \| inurl:lang= inurl:& site:<target>` | Parameters that commonly reflect user input (search, query, keyword, lang) -- test for reflected XSS |

### Open Redirect-Prone Parameters

| Query | What It Finds |
|-------|---------------|
| `inurl:url= \| inurl:return= \| inurl:next= \| inurl:redirect= \| inurl:redir= \| inurl:ret= \| inurl:r2= \| inurl:page= inurl:& inurl:http site:<target>` | Redirect parameters (url, return, next, redirect) with HTTP values -- test for open redirect |

### SQLi-Prone Parameters

| Query | What It Finds |
|-------|---------------|
| `inurl:id= \| inurl:pid= \| inurl:category= \| inurl:cat= \| inurl:action= \| inurl:sid= \| inurl:dir= inurl:& site:<target>` | Parameters commonly used in database queries (id, pid, category) -- test for SQL injection |

### SSRF-Prone Parameters

| Query | What It Finds |
|-------|---------------|
| `inurl:http \| inurl:url= \| inurl:path= \| inurl:dest= \| inurl:html= \| inurl:data= \| inurl:domain= \| inurl:page= inurl:& site:<target>` | Parameters that may fetch external resources (url, path, dest, domain) -- test for SSRF |

### LFI-Prone Parameters

| Query | What It Finds |
|-------|---------------|
| `inurl:include \| inurl:dir \| inurl:detail= \| inurl:file= \| inurl:folder= \| inurl:inc= \| inurl:locate= \| inurl:doc= \| inurl:conf= inurl:& site:<target>` | Parameters that may read local files (file, folder, include, doc, conf) -- test for LFI |

### RCE-Prone Parameters

| Query | What It Finds |
|-------|---------------|
| `inurl:cmd \| inurl:exec= \| inurl:query= \| inurl:code= \| inurl:do= \| inurl:run= \| inurl:read= \| inurl:ping= inurl:& site:<target>` | Parameters that may execute system commands (cmd, exec, run, ping) -- test for RCE |

## Testing Workflow

1. **Find endpoints** using the dorks above
2. **Verify parameters** exist and accept user input
3. **Test with benign payloads** first (e.g., `?id=1' OR '1'='1` for SQLi)
4. **Document findings** with evidence before reporting

## Example Usage

Find SQL injection candidates on a target:

```
inurl:id= | inurl:pid= | inurl:category= | inurl:cat= | inurl:action= | inurl:sid= | inurl:dir= inurl:& site:tesla.com
```

Find pages leaking server errors:

```
inurl:"error" | intitle:"exception" | "database error" | "SQL syntax" | "stack trace" site:tesla.com
```

### SQLi-Prone URL Patterns

Common PHP endpoints with ID parameters that are frequently vulnerable to SQL injection:

| Query | What It Finds |
|-------|---------------|
| `product.php?id=` | Product pages with injectable ID parameter |
| `category.php?id=` | Category pages with injectable ID parameter |
| `article.php?id=` | Article pages with injectable ID parameter |
| `news.php?id=` | News pages with injectable ID parameter |

### Web Shell Detection

| Query | What It Finds |
|-------|---------------|
| `(intitle:"phpshell" OR intitle:"c99shell" OR intitle:"r57shell")` | Deployed PHP web shells on compromised servers |
| `ext:php intitle:"b374k"` | b374k web shell installations |
| `intitle:"WSO 2.4" [ Sec. Info ]` | WSO web shell on compromised servers |

### Exposed Admin Tools

| Query | What It Finds |
|-------|---------------|
| `intitle:"Solr Admin" "Solr Query Syntax"` | Exposed Apache Solr admin interfaces |
| `intitle:"InfluxDB - Admin Interface" -github` | Exposed InfluxDB admin interfaces |
| `inurl:"/jmx-console/HtmlAdaptor?action"` | Exposed JBoss JMX Console (potential RCE) |

## Data Source

All queries in this collection are sourced from publicly available Google Dorking databases and security research. See the CSV file for the complete machine-readable dataset.
