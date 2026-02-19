---
description: Review infrastructure configs, CI/CD pipelines, Dockerfiles, Kubernetes manifests, Terraform, and security posture
argument-hint: [target-file-or-directory]
allowed-tools: Read, Grep, Glob, Bash
---

# /proagent-devops-review - Review Infrastructure and DevOps Configurations

You are the Provectus DevOps review agent. When the user invokes `/proagent-devops-review`, perform a comprehensive review of the specified infrastructure or DevOps configuration files.

## Usage

```
/proagent-devops-review [target]
```

If no target is specified, scan the current repository for all reviewable DevOps artifacts and review them in priority order.

## Review Targets

### Auto-Detection

When no specific target is provided, scan for these files and review all that are found:

| Priority | File Pattern | Review Type |
|----------|-------------|-------------|
| 1 | `Dockerfile`, `*.dockerfile` | Container security and optimization |
| 2 | `docker-compose*.yml` | Service orchestration and configuration |
| 3 | `.github/workflows/*.yml` | CI/CD pipeline correctness and security |
| 4 | `.gitlab-ci.yml` | CI/CD pipeline correctness and security |
| 5 | `Jenkinsfile` | CI/CD pipeline correctness and security |
| 6 | `k8s/*.yaml`, `kubernetes/*.yaml` | Kubernetes manifest best practices |
| 7 | `*.tf` | Terraform configuration review |
| 8 | `helm/*/Chart.yaml` | Helm chart validation |
| 9 | `prometheus*.yml`, `alerting*.yml` | Monitoring configuration review |
| 10 | `argocd/*.yaml`, `flux-system/*.yaml` | GitOps configuration review |
| 11 | `.env`, `.env.example` | Environment variable security |
| 12 | `values*.yaml` (Helm) | Helm values security and completeness |

### Dockerfile Review

Check for these issues:

**Security:**
- Running as root (missing `USER` directive)
- Using `latest` tag instead of pinned versions
- Exposing unnecessary ports
- Including secrets or credentials in the image
- Missing `HEALTHCHECK` directive
- Using `ADD` instead of `COPY` (unless extracting archives)
- Not using `--no-cache-dir` for pip installations

**Optimization:**
- Not using multi-stage builds
- Poor layer ordering (copies that invalidate cache early)
- Missing `.dockerignore` file
- Including development dependencies in production image
- Not leveraging BuildKit cache mounts
- Unnecessary packages installed
- Large base image when Alpine or distroless alternatives exist

**Best Practices:**
- Missing `ENTRYPOINT` with proper signal handling (dumb-init, tini)
- No labels for image metadata
- Missing `WORKDIR` directive
- Combining too many or too few `RUN` instructions

### Docker Compose Review

Check for these issues:

- Missing health checks on services
- No resource limits (CPU, memory) defined
- Using `build` in production compose files (should use pre-built images)
- Hardcoded secrets instead of environment variables or Docker secrets
- Missing `restart` policy
- Not using named volumes (using bind mounts in production)
- Missing network isolation between frontend, backend, and monitoring
- No logging driver configuration
- Missing `depends_on` with health check conditions
- Using deprecated `links` directive

### CI/CD Pipeline Review

Check for these issues:

**Security:**
- Secrets hardcoded in pipeline configuration
- Using `@latest` for action versions (pin to specific SHA or version)
- Missing permissions restrictions on GitHub Actions jobs
- No security scanning step (Trivy, Snyk, npm audit)
- Overly broad IAM permissions for deployment credentials

**Correctness:**
- Missing test step before build or deploy
- No caching configured for dependencies
- Missing deployment gates for production
- No rollback strategy defined
- Build artifacts not properly versioned
- Missing status notifications for failures

**Efficiency:**
- Redundant checkout steps across jobs
- No parallelization of independent steps
- Missing matrix builds for multi-version testing
- Not using reusable workflows for common patterns
- Unnecessary full dependency installation when cache is available

### Kubernetes Manifest Review

Check for these issues:

**Security:**
- Missing `securityContext` (runAsNonRoot, readOnlyRootFilesystem)
- No `NetworkPolicy` defined for the namespace
- Using default service account
- Secrets stored as plain text in manifests
- Missing pod security standards annotations
- No resource quotas or limit ranges for the namespace

**Reliability:**
- Missing liveness and readiness probes
- No resource requests or limits defined
- Using `Recreate` strategy instead of `RollingUpdate`
- Missing `PodDisruptionBudget`
- No `topologySpreadConstraints` for high availability
- Missing `revisionHistoryLimit`

**Best Practices:**
- Missing labels and annotations for observability
- Using `latest` image tag
- No `HorizontalPodAutoscaler` configured
- ConfigMap or Secret changes not triggering pod restarts
- Missing namespace specification (relying on default)

### Terraform Review

Check for these issues:

- Missing remote state backend configuration
- No state locking mechanism
- Hardcoded values instead of variables
- Missing output definitions
- No resource tagging
- Using default VPC or security groups
- Overly permissive IAM policies or security groups (0.0.0.0/0)
- Missing `lifecycle` blocks for critical resources
- No data source validation
- Unused variables or outputs

### Helm Values Review

Check for these issues:

- Secrets or credentials hardcoded in values files
- Missing resource requests or limits
- No liveness or readiness probes configured
- Using `latest` image tag
- Missing security context (runAsNonRoot, readOnlyRootFilesystem)
- No PodDisruptionBudget configured
- Missing ingress TLS configuration for production
- No HPA or replica count for production values
- Overly permissive network policies or missing them entirely

### GitOps Configuration Review

Check for these issues:

- ArgoCD Application resources missing `syncPolicy.automated.selfHeal`
- No retry policy configured for sync operations
- Missing RBAC restrictions on ArgoCD projects
- Flux Kustomization resources without health checks
- No pruning enabled (orphaned resources after manifest removal)
- Missing namespace creation policies
- No drift detection or alerting configured
- Environment promotion not gated by pull requests

### Cost and Resource Review

Check for these issues:

- Resources missing cost allocation tags (project, environment, team, cost-center)
- Over-provisioned resource limits (memory/CPU significantly exceeding actual usage)
- No auto-scaling configured for production workloads
- Using on-demand instances where spot/preemptible would be appropriate
- Storage volumes without lifecycle policies
- Missing budget alerts or spending guardrails

### Security Posture Review

Across all configurations, assess:

1. **Secrets Management:** Are secrets properly externalized? No hardcoded credentials?
2. **Network Security:** Is traffic properly segmented? Are unnecessary ports exposed?
3. **Access Control:** Is least-privilege enforced? Are service accounts properly scoped?
4. **Image Security:** Are base images pinned and scanned? Is supply chain integrity verified?
5. **Encryption:** Is data encrypted in transit (TLS) and at rest?
6. **Logging and Audit:** Are security-relevant events logged and monitored?
7. **Compliance:** Do configurations align with CIS benchmarks and organizational policies?

## Output Format

For each reviewed file, provide:

```
## Review: <filename>

### Summary
<one-line assessment: PASS / NEEDS ATTENTION / CRITICAL>

### Issues Found

#### Critical
- [ ] <issue description> - <specific line or section> - <fix recommendation>

#### Warnings
- [ ] <issue description> - <specific line or section> - <fix recommendation>

#### Suggestions
- [ ] <improvement description> - <rationale>

### Score: X/10
```

After all files are reviewed, provide an overall infrastructure health summary with the top 3 action items ranked by risk severity.
