# proagent-security

Provectus Security practice plugin for Claude Code. Provides production-tested vulnerability scanning (SAST, DAST, XSS, VirusTotal), compliance enforcement (GDPR, SOC 2, PCI-DSS, HIPAA, ISO 27001, NIST CSF), secrets management, encryption, audit logging, threat modeling (STRIDE, PASTA), OWASP Top 10 protection, Zero Trust architecture with trust ladder, agent sandboxing and access control, frontend security, risk classification, smart contract auditing, and security audit workflows drawn from actual Provectus engineering repositories.

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
| `semgrep` | Multi-language SAST (OSS tier) | [semgrep.dev](https://semgrep.dev/docs/getting-started/) |
| `govulncheck` | Go vulnerability scanning | `go install golang.org/x/vuln/cmd/govulncheck@latest` |
| `gh` | GitHub security alerts and APIs | [cli.github.com](https://cli.github.com/) |
| `glab` | GitLab security reports and APIs | [gitlab.com](https://gitlab.com/gitlab-org/cli) |
| `security-scan` | Automated secrets detection (audit-secrets) | `pip install security-scan` (also requires `gitleaks` on PATH) |

### Recommended: security-scan

The `security-scan` CLI provides automated secrets detection with 3-tier severity classification (BLOCKED/WARNING/APPROVED), baseline filtering for known findings, and VCS commenting support. When installed, the `audit-secrets` operation and pre-commit hooks will automatically use it for more accurate and comprehensive scanning.

```bash
# Install security-scan
pip install security-scan

# Also install gitleaks (required by security-scan)
# macOS: brew install gitleaks
# Linux: see https://github.com/gitleaks/gitleaks#installing
```

## Usage

### Hub Command

View all available security capabilities:

```
/proagent-security-hub
```

### Run Commands

Execute security operations:

```
/proagent-security-run scan-vulnerabilities   # Run comprehensive vulnerability scan (SAST, SCA, OWASP)
/proagent-security-run audit-secrets          # Detect hardcoded secrets and credentials
/proagent-security-run threat-model           # Generate a threat model (STRIDE, trust assessment)
/proagent-security-run compliance-check       # Validate compliance against a framework (GDPR, SOC 2, PCI-DSS, HIPAA, ISO 27001, NIST)
/proagent-security-run encrypt-setup          # Configure encryption for data protection
/proagent-security-run xss-scan              # Frontend XSS vulnerability scanning
/proagent-security-run risk-classify         # Classify code change risk level
/proagent-security-run agent-harden          # Harden autonomous agent deployments
/proagent-security-run audit-workflow        # Execute structured security audit workflow
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
- Frontend components for XSS and CSRF vulnerabilities
- Agent configurations for sandbox and trust level hardening
- Solidity smart contracts for reentrancy, overflow, and access control issues

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
- OWASP Top 10 remediation patterns with code examples for all 10 categories (A01-A10)
- Parameterized query patterns for SQL injection prevention
- RBAC implementation with permission decorators and ownership validation
- Password hashing with bcrypt/Argon2 including strength validation
- Rate limiting configuration for authentication and API endpoints
- Security header configuration (CSP, HSTS, X-Frame-Options, SameSite)
- TLS configuration with recommended cipher suites
- Zero Trust trust ladder with five progressive autonomy levels
- Micro-segmentation with Kubernetes NetworkPolicy examples
- Just-in-time access patterns with automatic expiry
- Agent sandboxing and hardening patterns for production autonomous agents
- Risk classification for code changes with keyword and scope analysis
- XSS vulnerability scanning with framework-specific detection (React, Vue, Angular)
- Solidity smart contract security patterns (reentrancy, overflow, access control)
- Security audit workflow formulas for repeatable audit processes

### Automated Checks
- Pre-commit hooks that scan for AWS keys, GitHub tokens, private keys, database URLs, and generic secrets
- Dependency vulnerability audit hooks that run before npm install, pip install, Docker build, and Go module operations
- Sensitive file write detection (.env, .pem, .key, .p12, .pfx) with .gitignore verification
- Pattern-based secret detection covering 10+ credential types
- VirusTotal malware scanning integration for CI/CD pipelines
- Automated risk scoring for pull requests and code changes

### Compliance Checklists
- GDPR compliance checklist with data processing, consent, erasure, and breach notification controls
- SOC 2 Type II control assessment with access control, change management, and monitoring checks
- PCI-DSS requirement validation for cardholder data protection
- HIPAA security rule checklist with PHI encryption, access controls, BAA verification, and breach notification
- ISO 27001 controls with ISMS scope, risk assessment, asset inventory, and internal audit
- NIST Cybersecurity Framework covering Identify, Protect, Detect, Respond, and Recover functions
- Framework-agnostic technical control verification (authentication, authorization, encryption, logging)

### MCP Servers

All marketplace plugins include a standard set of core MCP servers for cross-practice consistency. The security plugin adds GitLab for vulnerability report access.

| Server | Package | Purpose | Why |
|--------|---------|---------|-----|
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions, code scanning alerts, secret scanning | Security-specific |
| GitLab | `@modelcontextprotocol/server-gitlab` | Projects, MRs, SAST/DAST results, vulnerability reports | Security-specific |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Threat model diagrams, Zero Trust architecture maps | Security-specific |
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads | Core convention |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides | Core convention |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar | Core convention |

> **Note:** Slack, Google Drive, and Google Workspace are included as part of the marketplace core MCP convention across all 20 plugins. They enable cross-practice capabilities like sharing audit reports via Drive, notifying teams via Slack, and scheduling security reviews via Calendar. GitHub, GitLab, and Excalidraw are directly relevant to security workflows.

## Plugin Structure

```
proagent-security/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── security-assistant/
│       ├── SKILL.md
│       └── references/
│           ├── compliance-frameworks.md
│           ├── encryption-hardening.md
│           ├── owasp-patterns.md
│           ├── secrets-threats.md
│           ├── vulnerability-scanning.md
│           └── zero-trust.md
├── commands/
│   ├── proagent-security-hub.md
│   ├── proagent-security-run.md
│   ├── proagent-security-review.md
│   └── modes/
│       ├── scan-vulnerabilities.md
│       ├── audit-secrets.md
│       ├── threat-model.md
│       ├── compliance-check.md
│       ├── encrypt-setup.md
│       ├── xss-scan.md
│       ├── risk-classify.md
│       ├── agent-harden.md
│       ├── audit-workflow.md
│       ├── review-code-security.md
│       ├── review-dependencies.md
│       ├── review-access-control.md
│       ├── review-container.md
│       ├── review-cicd.md
│       ├── review-infrastructure.md
│       ├── review-frontend.md
│       ├── review-agent-hardening.md
│       └── review-smart-contract.md
├── agents/
│   └── security-specialist.md
├── hooks/
│   └── hooks.json
├── .mcp.json
├── CLAUDE.md
└── README.md
```

## Source Repositories

Built from 10 Provectus internal repositories: `agents`, `Auto-Claude`, `awos`, `casdk-harness`, `claude-ui`, `gastown`, `proagent-repo`, `proagent-repo GUI`, `provectus-marketplace`, `ralph-orchestrator`. Key external assets include security scanning commands and hardening agents from `agents`, risk classification and VirusTotal workflows from `Auto-Claude`, agent sandboxing from `casdk-harness`, trust ladder and ZTE assessor from `proagent-repo`, audit formulas from `gastown`, and security considerations from `ralph-orchestrator`.

## Version

- Plugin version: 0.4.3
- Category: security
- Author: Provectus
