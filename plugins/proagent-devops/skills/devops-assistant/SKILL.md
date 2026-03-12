---
name: devops-assistant
description: Managing Infrastructure & Deployments - CI/CD pipelines (GitHub Actions templates, GitLab CI, release workflows), Docker/Kubernetes containerization (Helm chart scaffolding, production-hardened compose), Terraform/IaC (module libraries, Nix flakes), monitoring and observability (Prometheus configuration, Grafana dashboards, alerting rules), secrets management, GitOps workflows (ArgoCD, Flux), incident response, cloud cost optimization, and multi-cloud operations across AWS and GCP. Use when performing any infrastructure, deployment, or operational task.
---

# Managing Infrastructure & Deployments

Comprehensive DevOps skill covering CI/CD pipelines, containerization, Kubernetes orchestration, Terraform IaC, monitoring, incident response, and cloud operations.

## When to Use This Skill

- Designing or implementing CI/CD pipelines (GitHub Actions, GitLab CI)
- Containerizing applications with Docker and Docker Compose
- Orchestrating workloads on Kubernetes (EKS, GKE, AKS)
- Scaffolding Helm charts for Kubernetes deployments
- Provisioning infrastructure with Terraform
- Setting up monitoring, alerting, and observability (Prometheus, Grafana)
- Implementing GitOps workflows with ArgoCD or Flux
- Managing secrets across environments
- Optimizing cloud costs and implementing FinOps practices
- Responding to incidents and writing postmortems

## When Invoked Without Clear Intent

**MANDATORY**: You MUST call the `AskUserQuestion` tool — do NOT render these options as text:

AskUserQuestion(
  header: "DevOps",
  question: "What infrastructure or deployment topic do you need help with?",
  options: [
    { label: "CI/CD Pipelines", description: "GitHub Actions, GitLab CI, release workflows" },
    { label: "Containers & Kubernetes", description: "Docker, Compose, K8s, Helm charts, ArgoCD" },
    { label: "Terraform / IaC", description: "Terraform modules, cloud cost optimization, FinOps" },
    { label: "Monitoring & Observability", description: "Prometheus, Grafana, alerting rules, dashboards" }
  ]
)

If the user selects "Other", present: GitOps (ArgoCD/Flux), Operations (incident response, secrets, deployment strategies).

## Reference Routing

> **CONTEXT GUARD**: Load reference files only when the user's request matches a specific topic below. Do NOT load all references upfront.

| User Intent | Reference File |
|---|---|
| CI/CD pipelines, GitHub Actions, GitLab CI, pipeline stages, release workflows | `references/cicd-patterns.md` |
| Docker, Dockerfile, Docker Compose, multi-stage builds, container hardening | `references/container-patterns.md` |
| Kubernetes, deployments, services, HPA, Helm charts, ArgoCD sync | `references/k8s-patterns.md` |
| GitOps, ArgoCD Application, environment promotion, drift detection, Flux | `references/gitops-patterns.md` |
| Terraform modules, IaC, cloud cost optimization, tagging, FinOps | `references/iac-patterns.md` |
| Prometheus, Grafana, alerting rules, metrics, dashboards, observability | `references/monitoring-patterns.md` |
| Agent workloads, incident response, deployment strategies, blue-green, canary, rollback, secrets, security | `references/operations-patterns.md` |

## Composio App Automations

Integrates with GitHub, GitLab, CircleCI, Vercel, Render, Datadog, Sentry, and PagerDuty via the Rube MCP server (`RUBE_SEARCH_TOOLS` → `RUBE_MANAGE_CONNECTIONS` → `RUBE_MULTI_EXECUTE_TOOL`).

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate infrastructure architecture diagrams, CI/CD pipeline flows, deployment strategy visualizations, and monitoring topology maps. Describe what you need in natural language.
