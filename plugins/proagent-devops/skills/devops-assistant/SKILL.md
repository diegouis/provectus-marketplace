---
name: devops-assistant
description: Managing Infrastructure & Deployments - CI/CD pipelines, Docker/Kubernetes containerization, Terraform/IaC, monitoring and observability, incident response, and multi-cloud operations across AWS and GCP. Use when performing any infrastructure, deployment, or operational task.
---

# Managing Infrastructure & Deployments

Comprehensive DevOps skill covering the full lifecycle of infrastructure management, application deployment, monitoring, and incident response. Built from production-tested patterns across Provectus engineering teams.

## When to Use This Skill

- Designing or implementing CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins)
- Containerizing applications with Docker and Docker Compose
- Orchestrating workloads on Kubernetes (EKS, GKE, AKS)
- Provisioning infrastructure with Terraform or other IaC tools
- Setting up monitoring, alerting, and observability stacks
- Responding to incidents and writing postmortems
- Managing cloud resources on AWS or GCP
- Reviewing infrastructure configurations for security and best practices
- Implementing GitOps workflows with ArgoCD or Flux

## CI/CD Pipeline Design

### Pipeline Stages

Every pipeline should follow this ordered progression:

1. **Checkout** - Retrieve source code from the repository
2. **Build** - Compile or bundle the application
3. **Test** - Run unit tests, integration tests, and linting
4. **Security Scan** - Dependency audit, SAST/DAST, container image scanning with Trivy
5. **Deploy to Staging** - Automatic deployment to staging environment
6. **Deploy to Production** - Gated deployment with approval workflows
7. **Verify** - Post-deployment smoke tests and health checks

### GitHub Actions Pipeline Pattern

Derived from `proagent/roles/devops-engineer/skills/cicd-pipeline.md` and `agents/plugins/cicd-automation/skills/github-actions-templates/SKILL.md`:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  DOCKER_REGISTRY: ghcr.io

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v3

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm audit --audit-level=high
      - uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'

  build:
    needs: [test, security-scan]
    if: github.event_name == 'push'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v2
      - uses: docker/login-action@v3
        with:
          registry: ${{ env.DOCKER_REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/metadata-action@v5
        id: meta
        with:
          images: ${{ env.DOCKER_REGISTRY }}/${{ github.repository }}
          tags: |
            type=ref,event=branch
            type=sha,prefix={{branch}}-
            type=semver,pattern={{version}}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  deploy-staging:
    needs: build
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment:
      name: staging
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - run: |
          aws ecs update-service --cluster staging-cluster --service app-service --force-new-deployment
          aws ecs wait services-stable --cluster staging-cluster --services app-service

  deploy-production:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: production
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - run: |
          aws ecs update-service --cluster production-cluster --service app-service --force-new-deployment
          aws ecs wait services-stable --cluster production-cluster --services app-service
```

### GitLab CI Pipeline Pattern

Derived from `proagent/roles/devops-engineer/skills/cicd-pipeline.md` and `casdk-harness/src/harness/agents/configs/infra-gitlab-ci-expert.md`:

```yaml
stages:
  - test
  - build
  - deploy

variables:
  DOCKER_DRIVER: overlay2

test:unit:
  stage: test
  image: node:20
  cache:
    paths:
      - node_modules/
  script:
    - npm ci
    - npm run lint
    - npm test -- --coverage

test:security:
  stage: test
  image: aquasec/trivy:latest
  script:
    - trivy fs --exit-code 1 --severity HIGH,CRITICAL .

build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  only:
    - main
    - develop

deploy:staging:
  stage: deploy
  environment:
    name: staging
  script:
    - kubectl set image deployment/app app=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA --namespace=staging
    - kubectl rollout status deployment/app --namespace=staging
  only:
    - develop

deploy:production:
  stage: deploy
  environment:
    name: production
  when: manual
  script:
    - kubectl set image deployment/app app=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA --namespace=production
    - kubectl rollout status deployment/app --namespace=production
  only:
    - main
```

## Docker Containerization

### Optimized Multi-Stage Dockerfile

Derived from `casdk-harness/src/harness/agents/configs/infra-docker-engineer.md` and `casdk-harness/agents/main/Dockerfile`:

```dockerfile
# Build stage
FROM node:20-alpine AS builder
RUN apk add --no-cache python3 make g++
WORKDIR /app
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm npm ci --only=production && npm cache clean --force
COPY . .
RUN npm run build
RUN npm prune --production

# Runtime stage
FROM node:20-alpine AS runtime
RUN apk add --no-cache dumb-init curl && rm -rf /var/cache/apk/*
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
WORKDIR /app
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/package.json ./
ENV NODE_ENV=production PORT=3000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1
USER nodejs
EXPOSE 3000
ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "dist/index.js"]
```

### Docker Compose Production Pattern

Derived from `casdk-harness/docker-compose.yml` and `casdk-harness/src/harness/agents/configs/infra-docker-engineer.md`:

```yaml
version: '3.9'

x-healthcheck-defaults: &healthcheck-defaults
  interval: 30s
  timeout: 3s
  retries: 3
  start_period: 30s

services:
  api:
    build:
      context: ./api
      target: runtime
    restart: unless-stopped
    environment:
      NODE_ENV: production
      DATABASE_URL: postgres://${DB_USER}:${DB_PASSWORD}@postgres:5432/${DB_NAME}
      REDIS_URL: redis://redis:6379
    networks:
      - frontend
      - backend
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      <<: *healthcheck-defaults
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '2'
          memory: 1024M

  postgres:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - backend
    healthcheck:
      <<: *healthcheck-defaults
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data
    networks:
      - backend
    healthcheck:
      <<: *healthcheck-defaults
      test: ["CMD", "redis-cli", "ping"]

  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus
    networks:
      - monitoring
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana:latest
    volumes:
      - grafana_data:/var/lib/grafana
    networks:
      - monitoring
      - frontend
    ports:
      - "3000:3000"

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
  monitoring:
    driver: bridge

volumes:
  postgres_data:
  redis_data:
  prometheus_data:
  grafana_data:
```

## Kubernetes Orchestration

### Application Deployment Pattern

Derived from `proagent/roles/devops-engineer/skills/kubernetes-orchestration.md` and `agents/plugins/kubernetes-operations/agents/kubernetes-architect.md`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  namespace: production
spec:
  replicas: 3
  revisionHistoryLimit: 5
  selector:
    matchLabels:
      app: myapp
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: myapp
    spec:
      serviceAccountName: myapp
      securityContext:
        runAsNonRoot: true
        runAsUser: 1001
      containers:
      - name: myapp
        image: myregistry.io/myapp:1.0.0
        ports:
        - containerPort: 3000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: myapp-secrets
              key: database-url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 10
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: myapp
  namespace: production
spec:
  type: ClusterIP
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 3000
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### GitOps with ArgoCD

Derived from `agents/plugins/kubernetes-operations/skills/gitops-workflow/SKILL.md`:

- Store all Kubernetes manifests in a Git repository as the single source of truth
- Use ArgoCD Application CRDs to define sync policies and health checks
- Implement environment promotion via pull requests (dev -> staging -> production)
- Enable auto-sync with self-healing for drift detection and remediation
- Use Kustomize overlays or Helm value files for environment-specific configuration

### Helm Chart Best Practices

Derived from `agents/plugins/kubernetes-operations/skills/helm-chart-scaffolding/SKILL.md`:

- Maintain a standardized chart structure with Chart.yaml, values.yaml, and templates/
- Use `.helmignore` to exclude unnecessary files from chart packages
- Validate charts with `helm lint` and `helm template` before deployment
- Implement chart testing with `helm test` hooks
- Version charts semantically and publish to a chart repository

## Monitoring and Observability

### Prometheus Metrics Collection

Derived from `casdk-harness/src/harness/monitoring.py` and `casdk-harness/config/monitoring/prometheus.yml`:

Key metrics to track:
- `request_duration_seconds` - Request latency histogram
- `requests_total{status}` - Request counter by status code
- `active_connections` - Current active connections gauge
- `deployment_duration_seconds` - Deployment time histogram
- `deployment_status{environment, result}` - Deployment outcome counter

### Alerting Rules

```yaml
groups:
  - name: application
    rules:
      - alert: HighErrorRate
        expr: rate(requests_total{status=~"5.."}[5m]) / rate(requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected (> 5%)"

      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "P95 latency above 2 seconds"

      - alert: PodCrashLooping
        expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
        for: 15m
        labels:
          severity: critical
        annotations:
          summary: "Pod {{ $labels.pod }} is crash looping"
```

## Incident Response

### Postmortem Template

Derived from `agents/plugins/incident-response/skills/postmortem-writing/SKILL.md`:

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

Derived from `casdk-harness/src/harness/agents/configs/infra-docker-engineer.md`:

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

## Reference Assets

| Asset | Source | Description |
|-------|--------|-------------|
| CI/CD Pipeline Skill | `proagent/roles/devops-engineer/skills/cicd-pipeline.md` | Full pipeline design patterns for GitHub Actions, GitLab CI, Jenkins |
| Kubernetes Orchestration | `proagent/roles/devops-engineer/skills/kubernetes-orchestration.md` | Deployment, Service, Ingress, HPA, StatefulSet patterns |
| Docker Containerization | `proagent/roles/devops-engineer/skills/docker-containerization.md` | Multi-stage builds, optimization, security |
| Docker Engineer Agent | `casdk-harness/src/harness/agents/configs/infra-docker-engineer.md` | Production Docker Compose, monitoring, deployment scripts |
| K8s Engineer Agent | `casdk-harness/src/harness/agents/configs/infra-k8s-engineer.md` | Kubernetes cluster management |
| GCP Architect Agent | `casdk-harness/src/harness/agents/configs/infra-gcp-architect.md` | Google Cloud architecture patterns |
| GitLab CI Expert Agent | `casdk-harness/src/harness/agents/configs/infra-gitlab-ci-expert.md` | GitLab CI pipeline patterns |
| GitHub Actions Templates | `agents/plugins/cicd-automation/skills/github-actions-templates/SKILL.md` | Reusable workflow templates |
| Postmortem Writing | `agents/plugins/incident-response/skills/postmortem-writing/SKILL.md` | Blameless postmortem methodology |
| Kubernetes Architect | `agents/plugins/kubernetes-operations/agents/kubernetes-architect.md` | GitOps, service mesh, platform engineering |
| Helm Chart Scaffolding | `agents/plugins/kubernetes-operations/skills/helm-chart-scaffolding/SKILL.md` | Helm chart best practices |
| GitOps Workflow | `agents/plugins/kubernetes-operations/skills/gitops-workflow/SKILL.md` | ArgoCD/Flux GitOps patterns |
| Release Bump | `ralph-orchestrator/.claude/skills/release-bump/SKILL.md` | Version bump automation |
| CI Workflow | `Auto-Claude/.github/workflows/ci.yml` | Cross-platform CI pipeline |
| Release Workflow | `Auto-Claude/.github/workflows/release.yml` | Multi-platform release workflow |
| Prometheus Config | `casdk-harness/config/monitoring/prometheus.yml` | Prometheus monitoring setup |
| Deployment Orchestrator | `proagent-repo GUI/core/orchestration/sdlc/deployer.py` | SDLC deployment automation |
