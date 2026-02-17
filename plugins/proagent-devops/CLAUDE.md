# Provectus DevOps Practice Plugin

This plugin provides the DevOps practice context for the Provectus agentic coding platform. It equips Claude with production-tested infrastructure and deployment patterns drawn from actual Provectus engineering repositories.

## Practice Scope

The DevOps practice covers six operational domains:

1. **CI/CD Pipelines** - Automated build, test, security scan, and deployment workflows for GitHub Actions, GitLab CI, and Jenkins
2. **Container Orchestration** - Docker containerization, Docker Compose service orchestration, and Kubernetes workload management
3. **Infrastructure as Code** - Terraform modules, Kustomize overlays, and Helm charts for reproducible infrastructure
4. **Monitoring and Observability** - Prometheus metrics, Grafana dashboards, alerting rules, and distributed tracing
5. **Incident Response** - Blameless postmortems, incident runbooks, severity classification, and on-call procedures
6. **Cloud Operations** - AWS (ECS, EKS, Lambda, S3, RDS) and GCP (GKE, Cloud Run, Cloud SQL) resource management

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

### Infrastructure as Code
- Use remote state backends with locking
- Tag all resources with project, environment, team, and cost-center
- Separate configuration per environment using workspaces or overlays

## MCP Integrations

- **GitHub**: Repository management, Actions workflows, and PR operations
- **GitLab**: CI/CD pipelines, merge requests, and container registry
- **Rube (Composio)**: SaaS automation gateway providing access to GitHub, GitLab, CircleCI, Vercel, Render, Datadog, Sentry, and PagerDuty via `RUBE_SEARCH_TOOLS`, `RUBE_MANAGE_CONNECTIONS`, and `RUBE_MULTI_EXECUTE_TOOL`

## Source Repositories

This plugin draws patterns from: proagent, casdk-harness, agents, Auto-Claude, ralph-orchestrator, tac, proagent-repo GUI, and gastown.

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
