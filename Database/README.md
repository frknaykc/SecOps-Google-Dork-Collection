# Database - Google Dork Queries

Dork queries designed to find exposed database interfaces, management tools, SQL dump files, NoSQL datastores, and database configuration leaks.

## Summary

| Risk Level | Count | Description |
|------------|-------|-------------|
| Critical | 35 | Direct access to database management tools, credentials, and open SQL/NoSQL databases |
| High | 24 | Exposed database interfaces, login panels, and sensitive schema definitions |
| Medium | 71 | Database connection error messages, version disclosures, and query fingerprints |
| **Total** | **130** | |

## Coverage

| Database Type / Tool | Description |
|-----------------------|-------------|
| **MySQL / MariaDB** | Dump files, connection errors, configuration leaks |
| **PostgreSQL** | Connection strings, JDBC credentials, parser errors |
| **MongoDB & Mongo Express** | Connection URIs, SRV strings, unauthenticated Mongo Express web UIs |
| **Redis & phpRedisAdmin** | Exposed Redis Commander and phpRedisAdmin web management interfaces |
| **ClickHouse & InfluxDB** | Dressed web client query consoles and time-series endpoints |
| **Elasticsearch** | Exposed clusters, cluster health, and index catalogs (`_cat/indices`) |
| **Neo4j & CouchDB** | Neo4j Browser and CouchDB Fauxton web consoles |
| **phpMyAdmin & Adminer** | Login pages, SQL dumps, root interfaces, Adminer single-file managers |
| **MinIO & CloudBeaver** | S3-compatible console and universal cloud database managers |
| **SQLite** | Exposed SQLite/SQLite3 database files |
| **Metabase** | Uncompleted setup endpoints allowing takeover |

## Example Usage

```
# Find unauthenticated Mongo Express database managers
intitle:"Mongo Express" "Databases" "Collections"

# Find exposed Redis Commander web management interfaces
intitle:"Redis Commander" inurl:":8081"

# Find open Elasticsearch clusters listing indexed data
inurl:":9200/_cat/indices?v"

# Find exposed phpMyAdmin running as root
intitle:phpMyAdmin "Welcome to phpMyAdmin *" "running on as root@"

# Find ClickHouse database web client query interfaces
inurl:":8123/play" intitle:"ClickHouse Client"
```

## Data Source

CSV file: [`GoogleDork-Database.csv`](GoogleDork-Database.csv)
