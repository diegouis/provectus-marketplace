# proagent-security

Provectus Security practice plugin for Claude Code. Provides production-tested vulnerability scanning, compliance enforcement, secrets management, encryption, audit logging, threat modeling, OWASP Top 10 protection, and Zero Trust architecture patterns drawn from actual Provectus engineering repositories.

## Installation

### Option 1: Copy to your project

Copy the `proagent-security/` directory into your project's `.claude/plugins/` directory:

```bash
cp -r proagent-security/ /path/to/your-project/.claude/plugins/proagent-security/
```

### Option 2: Reference from the marketplace

If your project uses the Provectus marketplace plugin loader, add the plugin to your configuration:

```json
{
  "plugins": ["proagent-security"]
}
```

### Option 3: Symlink for development

```bash
ln -s /path/to/provectus-marketplace/plugins/proagent-security /path/to/your-project/.claude/plugins/proagent-security
```

## Prerequisites

Depending on which operations you use, install the following CLI tools:

| Tool | Required For | Install |
|------|-------------|---------|
| `bandit` | Python SAST scanning | `pip install bandit` |
| `pip-audit` | Python dependency audit | `pip install pip-audit` |
| `trivy` | Container and filesystem scanning | [aquasecurity.github.io](https://aquasecurity.github.io/trivy/) |
| `semgrep` | Multi-language SAST | [semgrep.dev](https://semgrep.dev/docs/getting-started/) |
| `govulncheck` | Go vulnerability scanning | `go install golang.org/x/vuln/cmd/govulncheck@latest` |
| `gh` | GitHub security alerts and APIs | [cli.github.com](https://cli.github.com/) |
| `glab` | GitLab security reports and APIs | [gitlab.com](https://gitlab.com/gitlab-org/cli) |

## Usage

### Hub Command

View all available security capabilities:

```
/proagent-security-hub
```

### Run Commands

Execute security operations:

```
/proagent-security-run scan-vulnerabilities   # Run comprehensive vulnerability scan
/proagent-security-run audit-secrets          # Detect hardcoded secrets and credentials
/proagent-security-run threat-model           # Generate a threat model for the application
/proagent-security-run compliance-check       # Validate compliance against a framework
/proagent-security-run encrypt-setup          # Configure encryption for data protection
```

### Review Command

Review the security posture of the project:

```
/proagent-security-review                     # Auto-detect and review all security aspects
/proagent-security-review auth                # Review authentication and authorization
/proagent-security-review dependencies        # Review dependency vulnerabilities
```

The review command checks:
- Source code for injection, authentication, and authorization vulnerabilities
- Dependencies for known CVEs and outdated packages
- Configuration files for secret exposure and misconfiguration
- Container images for vulnerabilities and hardening issues
- CI/CD pipelines for security scanning coverage
- Infrastructure code for overly permissive policies
- Access controls for least-privilege enforcement

### Using the Security Specialist Agent

The plugin includes a security specialist agent for complex security tasks:

```
Ask the security-specialist to perform a threat model for this microservices architecture
```

### Using the Skill Directly

The security assistant skill is available for any security task:

```
Use the security-assistant skill to review this API for OWASP Top 10 vulnerabilities
```

## What This Plugin Provides

### Patterns and Templates
- CodeQL and Bandit CI/CD security scanning pipeline configuration
- Dependabot configuration for automated dependency patching across npm, pip, Docker, and GitHub Actions
- OWASP Top 10 remediation patterns with before/after code examples
- Parameterized query patterns for SQL injection prevention
- RBAC implementation with permission decorators and ownership validation
- Password hashing with bcrypt/Argon2 including strength validation
- Rate limiting configuration for authentication and API endpoints
- Security header configuration (CSP, HSTS, X-Frame-Options, SameSite)
- TLS configuration with recommended cipher suites
- Zero Trust trust ladder with five progressive autonomy levels

### Automated Checks
- Pre-commit hooks that scan for AWS keys, GitHub tokens, private keys, database URLs, and generic secrets
- Dependency vulnerability audit hooks that run before npm install, pip install, Docker build, and Go module operations
- Pattern-based secret detection covering 10+ credential types

### Compliance Checklists
- GDPR compliance checklist with data processing, consent, erasure, and breach notification controls
- SOC 2 Type II control assessment with access control, change management, and monitoring checks
- PCI-DSS requirement validation for cardholder data protection
- Framework-agnostic technical control verification (authentication, authorization, encryption, logging)

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| GitLab | `@modelcontextprotocol/server-gitlab` | GitLab projects, MRs, vulnerability reports |

## Source Repositories

This plugin is built from production patterns across 10 Provectus repositories with 51 total assets (37 high-reuse). Key sources include:

- **proagent** - Security hardening skill with authentication, authorization, input validation, encryption, and OWASP patterns
- **proagent-repo GUI** - Zero Trust Execution engine with trust assessor, trust ladder, and policy compliance monitoring
- **casdk-harness** - Production hardening plan with CVSS-scored vulnerabilities, tool restriction patterns, permission allow/deny lists
- **Auto-Claude** - CodeQL/Bandit security scanning pipeline, Dependabot configuration, VirusTotal artifact scanning, secrets ignore templates
- **awesome-claude-code** - Repository security evaluation framework with Claude Code ecosystem risk analysis
- **agents** - Security auditor agent with DevSecOps, OWASP, compliance, threat modeling, and incident response capabilities
- **tac** - SQL injection prevention implementation and E2E security testing commands
- **claude-ui** - CSRF protection middleware, rate limiting middleware, encryption utilities, password hashing
- **gastown** - Security policy and vulnerability reporting, security audit workflow formulas, watchdog chain monitoring
- **superpowers** - Defense-in-depth security strategy

## Version

- Plugin version: 0.2.0
- Category: security
- Author: Provectus
