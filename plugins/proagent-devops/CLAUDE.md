# Provectus DevOps Practice Plugin

This plugin provides the DevOps practice context for the Provectus agentic coding platform. It equips Claude with production-tested infrastructure and deployment patterns drawn from actual Provectus engineering repositories.

## Practice Scope

The DevOps practice covers nine operational domains:

1. **CI/CD Pipelines** - Automated build, test, security scan, and deployment workflows for GitHub Actions, GitLab CI, and Jenkins; reusable workflow templates and release preparation patterns (from `Auto-Claude/.github/workflows/prepare-release.yml`)
2. **Container Orchestration** - Docker containerization, Docker Compose service orchestration, and Kubernetes workload management; production-hardened compose patterns (from `casdk-harness/docker-compose.prod.yml`)
3. **Infrastructure as Code** - Terraform modules and module libraries, Kustomize overlays, Helm chart scaffolding, and Nix flakes for reproducible infrastructure
4. **Monitoring and Observability** - Prometheus metrics collection and configuration, Grafana dashboards, alerting rules (from `casdk-harness/config/monitoring/alerting.yml`), and distributed tracing
5. **Incident Response** - Blameless postmortems, incident runbooks, severity classification, on-call procedures, and dedicated incident responder workflows
6. **Cloud Operations** - AWS (ECS, EKS, Lambda, S3, RDS) and GCP (GKE, Cloud Run, Cloud SQL) resource management with multi-cloud architecture patterns
7. **Secrets Management** - External secret managers (Vault, AWS Secrets Manager, GCP Secret Manager), secrets rotation, and secret injection patterns
8. **GitOps Workflows** - ArgoCD and Flux-based continuous reconciliation, environment promotion via pull requests, and drift detection
9. **Cloud Cost Optimization** - FinOps practices, right-sizing, reserved/spot instance strategies, and cost allocation tagging

## Key Conventions

When performing DevOps tasks, follow these standards:

### Deployment
- Always run validation before applying changes
- Provide rollback instructions with every deployment action
- Use blue-green or canary strategies for production deployments
- Create database backups before any migration or deployment

### Security
- All containers must run as non-root users
- Pin base image versions; never use latest in production
- Scan images with Trivy in every CI pipeline
- Store secrets in external secret managers, never in code or config files
- Enforce network segmentation between frontend, backend, and monitoring tiers

### Monitoring
- Every service must expose a /health endpoint
- Define SLIs and SLOs before setting alert thresholds
- Use the RED method (Rate, Errors, Duration) for service dashboards
- Reference `casdk-harness/config/monitoring/alerting.yml` for production alerting rule patterns
- Use `casdk-harness/src/harness/monitoring.py` as a reference for Prometheus metrics collector implementation

### Infrastructure as Code
- Use remote state backends with locking
- Tag all resources with project, environment, team, and cost-center
- Separate configuration per environment using workspaces or overlays
- Reference the Terraform module library patterns from `agents/plugins/cloud-infrastructure/skills/terraform-module-library/`

### Secrets Management
- Never store secrets in code, config files, or container images
- Use external secret managers (HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager)
- Implement secrets rotation policies and audit secret access
- Reference patterns from `agents/plugins/cicd-automation/skills/secrets-management/`

### Cost Optimization
- Tag all cloud resources for cost allocation and chargeback
- Review right-sizing recommendations monthly
- Use spot/preemptible instances for fault-tolerant workloads
- Reference cost optimization patterns from `agents/plugins/cloud-infrastructure/skills/cost-optimization/`

## MCP Integrations

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **GitLab**: CI/CD pipelines, merge requests, and container registry via `@modelcontextprotocol/server-gitlab`
- **Rube (Composio)**: SaaS automation gateway for CircleCI, Vercel, Render, Datadog, Sentry, PagerDuty, and 200+ integrations via `https://rube.app/mcp`

## Source Repositories

Built from 13 Provectus internal engineering repositories:

- **agents** - Cloud architect, Terraform specialist, Kubernetes architect, and incident responder agent definitions; skills for GitHub Actions templates, secrets management, Terraform module library, cost optimization, Helm chart scaffolding, GitOps workflows, Prometheus configuration, and Grafana dashboards
- **Auto-Claude** - Release preparation workflow (`.github/workflows/prepare-release.yml`)
- **casdk-harness** - Docker Compose with Prometheus and Grafana (`docker-compose.yml`), production Docker Compose with security hardening (`docker-compose.prod.yml`), Prometheus alerting rules (`config/monitoring/alerting.yml`), Prometheus metrics collector (`src/harness/monitoring.py`)
- **proagent-repo** - Multi-service Docker Compose (`docker-compose.yml`), GitHub integration for CI/CD (`core/integrations/github.py`)
- **ralph-orchestrator** - Dockerfile, CI workflow (`.github/workflows/ci.yml`), Kubernetes deployment guide (`docs/deployment/kubernetes.md`), Docker deployment guide (`docs/deployment/docker.md`)
- **provectus-marketplace** - DevOps assistant skill, DevOps specialist agent
- **awos**, **claude-ui**, **gastown**, **superpowers**, **taches-cc-resources**, **awesome-claude-code**, **proagent-repo GUI** - Supporting infrastructure patterns and configurations

## Plugin Structure

```
proagent-devops/
  .claude-plugin/plugin.json
  skills/devops-assistant/SKILL.md
  commands/proagent-devops-hub.md
  commands/proagent-devops-run.md
  commands/proagent-devops-review.md
  agents/devops-specialist.md
  hooks/hooks.json
  .mcp.json
  CLAUDE.md
  README.md
```
