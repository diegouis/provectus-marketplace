# proagent-devops

Provectus DevOps practice plugin for Claude Code. Provides production-tested CI/CD pipelines, container orchestration, infrastructure as code, monitoring, incident response, and cloud operations patterns drawn from actual Provectus engineering repositories.

## Installation

### Option 1: Copy to your project

Copy the `proagent-devops/` directory into your project's `.claude/plugins/` directory:

```bash
cp -r proagent-devops/ /path/to/your-project/.claude/plugins/proagent-devops/
```

### Option 2: Reference from the marketplace

If your project uses the Provectus marketplace plugin loader, add the plugin to your configuration:

```json
{
  "plugins": ["proagent-devops"]
}
```

### Option 3: Symlink for development

```bash
ln -s /path/to/provectus-marketplace/plugins/proagent-devops /path/to/your-project/.claude/plugins/proagent-devops
```

## Prerequisites

Depending on which operations you use, install the following CLI tools:

| Tool | Required For | Install |
|------|-------------|---------|
| `docker` | Container operations | [docs.docker.com](https://docs.docker.com/get-docker/) |
| `kubectl` | Kubernetes operations | [kubernetes.io](https://kubernetes.io/docs/tasks/tools/) |
| `helm` | Helm chart operations | [helm.sh](https://helm.sh/docs/intro/install/) |
| `terraform` | Infrastructure provisioning | [terraform.io](https://developer.hashicorp.com/terraform/install) |
| `aws` | AWS cloud operations | [aws.amazon.com](https://aws.amazon.com/cli/) |
| `gcloud` | GCP cloud operations | [cloud.google.com](https://cloud.google.com/sdk/docs/install) |
| `gh` | GitHub integration | [cli.github.com](https://cli.github.com/) |
| `glab` | GitLab integration | [gitlab.com](https://gitlab.com/gitlab-org/cli) |

## Usage

### Hub Command

View all available DevOps capabilities:

```
/proagent-devops
```

### Run Commands

Execute DevOps operations:

```
/proagent-devops-run deploy          # Deploy application to staging or production
/proagent-devops-run provision       # Provision cloud infrastructure
/proagent-devops-run monitor         # Set up monitoring and alerting
/proagent-devops-run incident-respond # Guide through incident response
/proagent-devops-run pipeline-create  # Generate CI/CD pipeline configuration
```

### Review Command

Review infrastructure configurations for best practices, security, and optimization:

```
/proagent-devops-review              # Auto-detect and review all DevOps configs
/proagent-devops-review Dockerfile   # Review a specific file
```

The review command checks:
- Dockerfiles for security and optimization issues
- Docker Compose files for best practices
- CI/CD pipelines for correctness and security
- Kubernetes manifests for reliability and security
- Terraform configurations for compliance
- Overall security posture across all configurations

### Using the DevOps Specialist Agent

The plugin includes a DevOps specialist agent that can be invoked for complex infrastructure tasks:

```
Ask the devops-specialist to design a multi-region Kubernetes platform with GitOps
```

### Using the Skill Directly

The DevOps assistant skill is available for any infrastructure task:

```
Use the devops-assistant skill to create a GitHub Actions pipeline for this Python project
```

## What This Plugin Provides

### Patterns and Templates
- GitHub Actions CI/CD pipeline with test, security scan, build, and deploy stages
- GitLab CI pipeline with multi-stage builds and manual production gates
- Multi-stage Dockerfile optimized for size, security, and build performance
- Docker Compose production configuration with health checks and resource limits
- Kubernetes Deployment, Service, HPA, and Ingress manifests
- Prometheus alerting rules for error rate, latency, and resource saturation
- Blameless postmortem document template with 5 Whys analysis

### Automated Checks
- Pre-deployment validation hooks that catch configuration errors before they reach production
- Post-deployment health checks that verify service stability after changes
- Security scanning for hardcoded secrets, overly permissive permissions, and missing hardening

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |
| GitLab | `@modelcontextprotocol/server-gitlab` | CI/CD pipelines, merge requests, container registry |
| Rube | `rube.app/mcp` | SaaS automation via Composio SDK |

## Environment Variables

```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your-token"
export GITLAB_PERSONAL_ACCESS_TOKEN="your-token"
export GITLAB_API_URL="https://gitlab.com/api/v4"  # optional, defaults to gitlab.com
```

Note: AWS and GCP operations use their respective CLIs (`aws`, `gcloud`) which should be configured separately via `aws configure` and `gcloud auth login`.

## Source Repositories

This plugin is built from production patterns across 8 Provectus repositories with 126 total assets (89 high-reuse). Key sources include:

- **proagent** - DevOps engineer role with CI/CD, Kubernetes, and Docker skill definitions
- **casdk-harness** - Docker Compose orchestration, Prometheus monitoring, multi-stage Dockerfiles, and infrastructure agent configurations
- **agents** - CI/CD automation, incident response, and Kubernetes operations plugin collections
- **Auto-Claude** - Cross-platform CI/CD workflows and pre-commit hook configurations
- **ralph-orchestrator** - Release management pipelines and version automation
- **tac** - Git operations automation, GitHub API integration, and trigger systems
- **proagent-repo GUI** - SDLC deployment orchestration and validation workflows
- **gastown** - GoReleaser cross-platform build configuration

## Version

- Plugin version: 0.2.0
- Category: devops
- Author: Provectus
