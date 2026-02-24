## Agent Workload Operations

When running AI agent workloads in production:

- **OOM prevention**: Cap input sizes, monitor memory usage, set process limits
- **Orphaned agent cleanup**: Monitor agent processes and terminate those exceeding time or resource bounds
- **Recovery mechanisms**: Implement checkpointing so interrupted agent tasks can resume
- **Observability**: Integrate structured error reporting (Sentry or similar) for agent subprocess failures

## Incident Response

### Postmortem Template

Follow blameless postmortem principles:
1. **Timeline** - Document exact times for detection, escalation, mitigation, and resolution
2. **Root Cause Analysis** - Use the 5 Whys method to identify systemic causes
3. **Impact Assessment** - Quantify customer impact, revenue loss, and technical damage
4. **Action Items** - Create prioritized, owned, and time-bound follow-up tickets
5. **Lessons Learned** - Document what went well, what went wrong, and where you got lucky

### Incident Severity Levels

| Level | Criteria | Response Time | Postmortem Required |
|-------|----------|---------------|---------------------|
| SEV1 | Full outage, data loss | Immediate | Yes |
| SEV2 | Degraded service, > 15 min | 15 minutes | Yes |
| SEV3 | Minor impact, workaround available | 1 hour | Optional |
| SEV4 | Cosmetic or non-urgent | Next business day | No |

## Deployment Strategies

### Blue-Green Deployment

1. Deploy new version alongside current version
2. Run health checks and smoke tests against new version
3. Switch traffic from current (blue) to new (green) via load balancer
4. Keep blue environment as instant rollback target
5. Decommission blue after verification period

### Canary Deployment

1. Deploy new version to a small subset of instances (5-10%)
2. Monitor error rates, latency, and business metrics
3. Gradually increase traffic percentage if metrics are healthy
4. Roll back immediately if anomalies are detected
5. Complete rollout when confidence is established

### Rollback Procedure

```bash
#!/bin/bash
set -euo pipefail

# Pre-deployment: create database backup
docker-compose exec -T postgres pg_dump -U $DB_USER $DB_NAME | gzip > "backups/backup-$(date +%Y%m%d-%H%M%S).sql.gz"

# Deploy with health checking
docker-compose up -d --remove-orphans

# Verify each service health
for service in postgres redis api web; do
  attempts=0
  while [ $attempts -lt 30 ]; do
    if docker-compose ps | grep "$service" | grep -q "healthy"; then
      echo "$service is healthy"
      break
    fi
    sleep 5
    attempts=$((attempts + 1))
  done
  if [ $attempts -eq 30 ]; then
    echo "ROLLBACK: $service failed health check"
    docker-compose down
    VERSION="previous" docker-compose up -d
    exit 1
  fi
done
```

## Security Best Practices

- Run containers as non-root users with read-only root filesystems where possible
- Scan container images with Trivy or Snyk in every CI pipeline run
- Implement network policies for pod-to-pod communication isolation
- Use Kubernetes Pod Security Standards (restricted profile for production)
- Store secrets in external secret managers (AWS Secrets Manager, HashiCorp Vault, GCP Secret Manager)
- Enforce RBAC with least-privilege service accounts
- Enable audit logging for all cluster operations
- Sign container images with Sigstore/cosign for supply chain security

## Secrets Management

Reference: `agents/plugins/cicd-automation/skills/secrets-management/SKILL.md`

### Secret Storage Backends

| Backend | Use Case | Integration |
|---------|----------|-------------|
| AWS Secrets Manager | AWS-native workloads | IAM role-based access, automatic rotation |
| GCP Secret Manager | GCP-native workloads | Service account-based access, versioned secrets |
| HashiCorp Vault | Multi-cloud, on-prem | Dynamic secrets, PKI, transit encryption |
| Kubernetes Secrets | In-cluster apps | External Secrets Operator for sync from cloud backends |

### Patterns

- Use External Secrets Operator to sync cloud secrets into Kubernetes Secrets
- Rotate secrets on a defined schedule (90 days for credentials, 365 days for certificates)
- Audit all secret access through cloud provider audit logs
- Never pass secrets as environment variables in CI/CD logs; use masked variables or secret injection
- For GitHub Actions, use repository or environment secrets; never hardcode in workflow files
- For Docker, use BuildKit `--secret` mounts during build; never use `ARG` or `ENV` for secrets
