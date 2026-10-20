# DevOps, CI/CD & Cloud Infrastructure Google Dorks

A curated collection of Google Dork queries for discovering exposed continuous integration/continuous deployment (CI/CD) pipelines, container registries, Kubernetes cluster endpoints, observability dashboards, and secrets management tools.

## Summary

| Risk Level | Count |
|---|---:|
| Critical | 15 |
| High | 15 |
| Medium | 5 |
| Low | 70 |

**Total: 105 dorks**

Risk levels prioritize search leads; a matching result is not proof of a vulnerability or unauthorized access.

## Coverage

| Platform / Component | Description |
|----------------------|-------------|
| **CI/CD Engines** | Jenkins, GitLab, Gitea, Argo CD, Argo Workflows, TeamCity, Bamboo |
| **Containers & Registries** | Docker Registry v2 API, Harbor, Portainer, Rancher |
| **Kubernetes & Clusters** | Kubernetes Dashboard, Kubelet ports (`10250`/`10255`), etcd API (`2379`) |
| **Secrets & Config** | HashiCorp Vault, HashiCorp Consul |
| **Observability & Metrics** | Prometheus, Grafana, Jaeger Tracing, Zipkin, Checkmk, Zabbix, Uptime Kuma, OpenTelemetry Collector |
| **Workflow Orchestration** | n8n, Prefect, Dagster, Temporal |
| **Supply-Chain Evidence** | GitHub artifact attestations, SLSA provenance, SPDX and CycloneDX SBOMs |
| **Message Brokers** | RabbitMQ Management, Kafdrop, AKHQ (Kafka GUI) |

## Query Reference

### CI/CD Engines & GitOps

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `intitle:"Argo CD" inurl:"/applications"` | Exposed Argo CD GitOps continuous delivery control planes | Critical |
| `intitle:"Argo Workflows" inurl:":2746"` | Exposed Argo Workflows Kubernetes pipeline interfaces | Critical |
| `intitle:"Dashboard [Jenkins]" inurl:":8080"` | Exposed Jenkins automation servers without authentication | Critical |
| `inurl:":8080/job/" intitle:"Jenkins"` | Exposed Jenkins job definitions and build console outputs | Critical |
| `intitle:"Explore projects · GitLab" site:<target>` | Exposed GitLab projects and source repositories | High |
| `intitle:"Explore - Gitea: Git with a cup of tea"` | Exposed Gitea self-hosted Git instances | High |
| `intitle:"Log in to TeamCity"` | Exposed JetBrains TeamCity CI/CD build login pages | High |
| `intitle:"Log In - Atlassian Bamboo"` | Exposed Atlassian Bamboo CI server login portals | High |

### Container Registries & Management

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `intitle:"Harbor" inurl:"/harbor/projects"` | Exposed Harbor container registries and internal projects | Critical |
| `inurl:"/v2/_catalog" intitle:"index of"` | Exposed private Docker Registry HTTP API v2 catalog endpoints | Critical |
| `intitle:"Portainer" (inurl:":9000" \| inurl:":9443/#/auth")` | Exposed Portainer container management UI login pages | Critical |
| `intitle:"Rancher" inurl:"/login"` | Exposed Rancher multi-cluster Kubernetes management dashboards | Critical |

### Kubernetes & Secrets Infrastructure

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `intitle:"Kubernetes Dashboard"` | Exposed Kubernetes Dashboard cluster management web interfaces | Critical |
| `inurl:":10255/pods" \| inurl:":10250/pods"` | Exposed Kubernetes Kubelet API endpoints listing pods | Critical |
| `inurl:":2379/version" \| inurl:":2379/v2/keys"` | Exposed Kubernetes etcd distributed key-value store endpoints | Critical |
| `intitle:"Vault" inurl:":8200/ui/"` | Exposed HashiCorp Vault secrets management UI consoles | Critical |
| `intitle:"Consul by HashiCorp" inurl:":8500/ui"` | Exposed HashiCorp Consul service mesh and KV store UIs | Critical |

### Observability, Tracing & Monitoring

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `intitle:"Prometheus Time Series Collection" inurl:":9090/graph"` | Exposed Prometheus monitoring and alerting web consoles | High |
| `inurl:":9090/targets" intitle:"Prometheus"` | Exposed Prometheus scrape targets exposing internal topology | High |
| `intitle:"Grafana" (inurl:"/login" \| inurl:"/d/" \| inurl:"/dashboards")` | Exposed Grafana metric visualization dashboards | High |
| `intitle:"SonarQube" inurl:"/projects"` | Exposed SonarQube code quality and security dashboards | High |
| `intitle:"Jaeger UI" inurl:":16686"` | Exposed Jaeger distributed tracing dashboards | High |
| `intitle:"Zipkin" inurl:":9411"` | Exposed Zipkin distributed tracing web consoles | High |
| `intitle:"Uptime Kuma" inurl:":3001"` | Exposed Uptime Kuma monitoring dashboards | Medium |
| `intitle:"Checkmk" inurl:"/check_mk/login.py"` | Checkmk IT infrastructure monitoring login portals | High |
| `intitle:"Zabbix" inurl:"index.php"` | Exposed Zabbix enterprise monitoring web login pages | High |
| `intitle:"Sign In to Sentry"` | Self-hosted Sentry crash reporting login pages | High |

### Message Brokers & Event Streams

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `intitle:"RabbitMQ Management"` | Exposed RabbitMQ message broker management consoles | High |
| `intitle:"Kafdrop" (inurl:":9000" \| inurl:":9001")` | Exposed Kafdrop Kafka cluster web UI browsers | Critical |
| `intitle:"AKHQ" inurl:":8080"` | Exposed AKHQ (Kafka GUI) management interfaces | Critical |

## Data Source

CSV file: [`GoogleDork-DevOpsCI.csv`](GoogleDork-DevOpsCI.csv)
