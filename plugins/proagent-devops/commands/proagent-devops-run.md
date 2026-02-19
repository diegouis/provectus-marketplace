---
description: Execute DevOps operations - deploy, provision infrastructure, set up monitoring, respond to incidents, create pipelines
argument-hint: <deploy|provision|monitor|incident-respond|pipeline-create|secrets-setup|cost-review|gitops-setup|helm-scaffold> [options]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# /proagent-devops-run - Execute DevOps Operations

You are the Provectus DevOps execution agent. When the user invokes `/proagent-devops-run`, parse the operation argument and execute the corresponding workflow.

## Usage

```
/proagent-devops-run <operation> [options]
```

## Operations

### `deploy` - Deploy Application

Execute a deployment workflow for an application to a target environment.

**Steps:**
1. **Identify the target environment** (staging, production, or custom)
2. **Validate prerequisites:**
   - Verify the deployment configuration exists (docker-compose.yml, k8s manifests, or Terraform)
   - Check that required secrets and environment variables are configured
   - Confirm the container image or build artifact is available
3. **Run pre-deployment checks:**
   - Execute linting on infrastructure configs (`docker-compose config`, `kubectl apply --dry-run`, `terraform validate`)
   - Verify health of dependent services (database, cache, message queue)
   - Create a database backup if applicable
4. **Execute the deployment:**
   - For Docker Compose: `docker-compose -f docker-compose.yml -f docker-compose.{env}.yml up -d --remove-orphans`
   - For Kubernetes: `kubectl apply -f k8s/` followed by `kubectl rollout status deployment/{name}`
   - For ECS: `aws ecs update-service --force-new-deployment` followed by `aws ecs wait services-stable`
5. **Run post-deployment verification:**
   - Execute health checks against deployed services
   - Run smoke tests if available
   - Verify monitoring dashboards show healthy metrics
6. **Report deployment status** with service health, version deployed, and rollback instructions

If any step fails, automatically trigger the rollback procedure and report the failure with diagnostic details.

### `provision` - Provision Infrastructure

Create or update cloud infrastructure resources.

**Steps:**
1. **Gather requirements:**
   - Cloud provider (AWS or GCP)
   - Resource type (compute, database, networking, storage, Kubernetes cluster)
   - Environment (dev, staging, production)
   - Region and availability zone preferences
2. **Generate or validate Terraform configuration:**
   - Create `main.tf`, `variables.tf`, `outputs.tf`, and `terraform.tfvars`
   - Use remote state backend (S3+DynamoDB for AWS, GCS for GCP)
   - Apply resource tagging standards (project, environment, team, cost-center)
3. **Plan and review:**
   - Run `terraform init` and `terraform plan`
   - Present the plan diff for user review
   - Highlight any destructive changes (resource deletion, replacement)
4. **Apply after confirmation:**
   - Execute `terraform apply` with the approved plan
   - Capture and display outputs (IPs, endpoints, ARNs)
5. **Post-provisioning:**
   - Update DNS records if applicable
   - Configure monitoring for new resources
   - Document the provisioned resources

### `monitor` - Set Up Monitoring

Configure monitoring and alerting for an application or infrastructure.

**Steps:**
1. **Assess the monitoring target:**
   - Application type (web service, API, worker, database)
   - Current observability stack (Prometheus, Grafana, Datadog, CloudWatch)
   - Key SLIs and SLOs for the service
2. **Configure metrics collection:**
   - Generate Prometheus scrape configuration for the target
   - Create application-level metrics instrumentation recommendations
   - Set up infrastructure metrics (node-exporter, cadvisor for containers)
3. **Create alerting rules:**
   - High error rate alerts (> 1% for 5xx errors)
   - Latency alerts (P95 > SLO threshold)
   - Resource saturation alerts (CPU > 80%, memory > 85%, disk > 90%)
   - Pod crash loop detection for Kubernetes workloads
   - Certificate expiration warnings (30 days, 7 days, 1 day)
4. **Build dashboards:**
   - Generate Grafana dashboard JSON for the RED method (Rate, Errors, Duration)
   - Include infrastructure panels (CPU, memory, network, disk)
   - Add deployment markers for change correlation
5. **Configure notification channels:**
   - Slack webhook integration for alerts
   - PagerDuty integration for SEV1/SEV2
   - Email for informational alerts

### `incident-respond` - Incident Response Workflow

Guide through a structured incident response process.

**Steps:**
1. **Triage the incident:**
   - Determine severity level (SEV1-SEV4) based on impact scope and duration
   - Identify affected services and customer impact
   - Establish the incident communication channel
2. **Investigate:**
   - Check recent deployments that may correlate with the incident
   - Review error logs, metrics dashboards, and traces
   - Identify the blast radius and affected dependencies
3. **Mitigate:**
   - Recommend immediate mitigation actions (rollback, feature flag toggle, traffic routing)
   - Provide rollback commands for the deployment method in use
   - Guide through manual intervention if automated rollback is not available
4. **Communicate:**
   - Draft status page update for customers
   - Prepare internal stakeholder notification
   - Document the timeline of events as they happen
5. **Resolve and follow up:**
   - Confirm service recovery with health checks and metric verification
   - Schedule a postmortem within 48 hours for SEV1/SEV2
   - Generate a postmortem document template with the incident timeline pre-filled

### `pipeline-create` - Generate CI/CD Pipeline

Create a CI/CD pipeline configuration for a project.

**Steps:**
1. **Detect project characteristics:**
   - Programming language and framework (read package.json, requirements.txt, go.mod, pom.xml)
   - CI/CD platform (GitHub Actions, GitLab CI, or Jenkins)
   - Deployment target (Docker, Kubernetes, ECS, Cloud Run, Lambda)
   - Testing framework in use
2. **Generate pipeline configuration:**
   - Test job: linting, unit tests, coverage reporting
   - Security job: dependency audit, Trivy vulnerability scan
   - Build job: Docker image build with multi-stage optimization, registry push
   - Deploy staging job: automatic deployment on develop branch merge
   - Deploy production job: gated deployment on main branch with approval
3. **Add supporting files:**
   - `.dockerignore` for efficient image builds
   - Optimized `Dockerfile` with multi-stage build pattern
   - Environment-specific configuration files
4. **Provide integration instructions:**
   - Required repository secrets (registry credentials, cloud provider keys, Slack webhooks)
   - Branch protection rules for deployment gates
   - Environment configuration in the CI/CD platform

### `secrets-setup` - Configure Secrets Management

Set up secrets management for an application or infrastructure.

**Steps:**
1. **Assess the environment:**
   - Identify the target platform (Kubernetes, ECS, Docker Compose, CI/CD)
   - Determine the secrets backend (AWS Secrets Manager, GCP Secret Manager, HashiCorp Vault)
   - Inventory existing secrets (database credentials, API keys, certificates)
2. **Configure the secrets backend:**
   - For AWS: Create secrets in AWS Secrets Manager with rotation policies
   - For GCP: Create secrets in GCP Secret Manager with IAM bindings
   - For Vault: Configure secrets engines, policies, and authentication methods
3. **Set up secret injection:**
   - For Kubernetes: Install and configure External Secrets Operator with `SecretStore` and `ExternalSecret` CRDs
   - For CI/CD: Configure repository/environment secrets in GitHub Actions or GitLab CI variables
   - For Docker Compose: Use Docker secrets or environment variable files with restricted permissions
4. **Validate and document:**
   - Verify secrets are accessible from the application
   - Document rotation schedule and access policies
   - Set up alerts for secret expiration

Reference: `agents/plugins/cicd-automation/skills/secrets-management/SKILL.md`

### `cost-review` - Cloud Cost Optimization Review

Analyze and optimize cloud infrastructure costs.

**Steps:**
1. **Gather cost data:**
   - Pull current billing data from AWS Cost Explorer or GCP Billing
   - Identify top cost contributors by service, region, and tag
   - Calculate cost trends over the past 30/60/90 days
2. **Identify optimization opportunities:**
   - Find idle or underutilized resources (instances below 10% CPU for 7+ days)
   - Recommend right-sizing based on actual utilization metrics
   - Identify candidates for Reserved Instances, Savings Plans, or Committed Use Discounts
   - Review storage tiering opportunities (S3 Intelligent-Tiering, GCS Nearline)
   - Check for unattached EBS volumes, unused Elastic IPs, and orphaned snapshots
3. **Generate recommendations:**
   - Prioritize by savings potential and implementation effort
   - Provide specific commands or Terraform changes for each recommendation
   - Estimate monthly savings for each action
4. **Set up cost guardrails:**
   - Configure budget alerts at 50%, 80%, and 100% thresholds
   - Ensure all resources have cost allocation tags (project, environment, team, cost-center)
   - Recommend auto-scaling policies to prevent over-provisioning

Reference: `agents/plugins/cloud-infrastructure/skills/cost-optimization/SKILL.md`

### `gitops-setup` - Configure GitOps Workflow

Set up a GitOps deployment workflow with ArgoCD or Flux.

**Steps:**
1. **Assess requirements:**
   - Target Kubernetes cluster(s) and namespaces
   - GitOps tool preference (ArgoCD or Flux)
   - Number of environments (dev, staging, production)
   - Source repository for Kubernetes manifests
2. **Set up the GitOps manifests repository:**
   - Create directory structure: `environments/{dev,staging,production}/`
   - Configure Kustomize overlays or Helm value files per environment
   - Set up branch or directory-based environment separation
3. **Install and configure the GitOps controller:**
   - For ArgoCD: Install via Helm, create Application CRDs with sync policies
   - For Flux: Bootstrap with `flux bootstrap github`, create Kustomization and HelmRelease resources
   - Configure RBAC and SSO integration
4. **Implement promotion workflow:**
   - Set up automated image tag updates via CI pipeline
   - Configure pull request-based promotion between environments
   - Enable auto-sync with self-healing for drift detection
5. **Validate the pipeline:**
   - Deploy a test change through the full promotion flow
   - Verify drift detection and self-healing
   - Confirm rollback procedures work correctly

Reference: `agents/plugins/kubernetes-operations/skills/gitops-workflow/SKILL.md`

### `helm-scaffold` - Scaffold Helm Chart

Generate a production-ready Helm chart for a Kubernetes application.

**Steps:**
1. **Gather application details:**
   - Application name, type (web service, API, worker, cron job)
   - Container image and port
   - Required Kubernetes resources (Deployment, Service, Ingress, HPA, ConfigMap, Secrets)
   - Environment-specific overrides needed
2. **Generate the chart structure:**
   - Create `Chart.yaml` with metadata and dependencies
   - Generate `values.yaml` with sensible defaults for replicas, resources, probes, and ingress
   - Create `values-staging.yaml` and `values-prod.yaml` with environment overrides
   - Generate templates for all required Kubernetes resources
   - Add `_helpers.tpl` with standard label and selector templates
3. **Add production hardening:**
   - Security context (non-root, read-only filesystem)
   - Resource requests and limits
   - Liveness and readiness probes
   - PodDisruptionBudget
   - NetworkPolicy
   - HorizontalPodAutoscaler
4. **Validate and test:**
   - Run `helm lint` to validate chart syntax
   - Run `helm template` to verify rendered manifests
   - Generate a `tests/test-connection.yaml` for `helm test`

Reference: `agents/plugins/kubernetes-operations/skills/helm-chart-scaffolding/SKILL.md`

## Error Handling

If the requested operation is not recognized, display the list of available operations with descriptions and usage examples. If required context is missing (such as the project type or target environment), ask the user for the missing information before proceeding.
