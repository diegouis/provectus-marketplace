---
description: >
  Overview of all security capabilities: vulnerability scanning, compliance enforcement,
  secrets management, encryption, threat modeling, OWASP Top 10, and Zero Trust architecture.
argument-hint: ""
allowed-tools: Read, Glob, Grep
---

# /proagent-security-hub - Security Practice Hub

You are the Provectus Security practice assistant. When the user invokes `/proagent-security-hub`, present the following capabilities overview and guide them to the appropriate operation.

## Capabilities

This plugin provides production-tested security automation across eight domains:

### 1. Vulnerability Scanning
- Run SAST analysis with CodeQL, Bandit, Semgrep, and ESLint security plugins
- Execute dependency audits with npm audit, pip-audit, govulncheck, and Trivy
- Perform DAST scanning with OWASP ZAP and Burp Suite
- Scan container images for known CVEs with Trivy and Snyk
- Generate vulnerability reports with CVSS scoring and remediation guidance

### 2. Compliance Enforcement
- Validate GDPR requirements: data processing agreements, consent management, DSAR processes, breach notification
- Audit SOC 2 Type II controls: access control, change management, incident response, vulnerability management
- Check PCI-DSS compliance: CDE segmentation, encryption, access logging, penetration testing schedules
- Assess HIPAA requirements: PHI handling, access controls, audit logging, BAA verification
- Evaluate ISO 27001 alignment: ISMS scope, risk assessment, control implementation, continuous improvement

### 3. Secrets Management
- Detect hardcoded secrets in code and configuration files using pattern matching
- Audit .env files, Docker configs, CI/CD pipelines for exposed credentials
- Recommend secrets management solutions (AWS Secrets Manager, HashiCorp Vault, GCP Secret Manager)
- Generate .gitignore and .secretsignore templates for secret exclusion
- Implement secret rotation policies and automation

### 4. Encryption
- Configure TLS 1.2/1.3 for all service communications
- Implement AES-256-GCM encryption for data at rest
- Set up password hashing with bcrypt or Argon2
- Design key management with rotation schedules and KMS integration
- Configure security headers (CSP, HSTS, X-Frame-Options, SameSite cookies)

### 5. Audit Logging
- Design structured security event logging with proper fields and severity levels
- Implement tamper-proof log storage and retention policies
- Configure alerting for authentication failures, privilege escalation, and anomalous access
- Set up centralized log aggregation with SIEM integration
- Create audit trail for compliance evidence collection

### 6. Threat Modeling
- Perform STRIDE analysis on application architecture
- Map attack surfaces including entry points, trust boundaries, and data flows
- Assess risk using the Zero Trust trust assessment engine with risk/complexity scoring
- Generate threat model documentation with prioritized mitigation recommendations
- Create attack tree diagrams for high-value targets

### 7. OWASP Top 10 Protection
- Audit for all OWASP Top 10 2021 categories with specific code-level checks
- Implement broken access control fixes with RBAC and permission decorators
- Prevent injection attacks with parameterized queries and input validation
- Harden authentication with MFA, session management, and account lockout
- Fix security misconfiguration with environment-specific hardening checklists

### 8. Zero Trust Architecture
- Implement identity-based access with OAuth 2.0/OIDC and WebAuthn
- Design micro-segmentation for network and service-level isolation
- Configure continuous verification with risk-based authentication
- Apply least-privilege access with just-in-time and just-enough-access patterns
- Set up trust ladder for progressive agent autonomy with approval gates

## Available Commands

| Command | Description |
|---------|-------------|
| `/proagent-security-run scan-vulnerabilities` | Run comprehensive vulnerability scan on the codebase |
| `/proagent-security-run audit-secrets` | Detect hardcoded secrets and credential exposure |
| `/proagent-security-run threat-model` | Generate a threat model for the application |
| `/proagent-security-run compliance-check` | Validate compliance against a specified framework |
| `/proagent-security-run encrypt-setup` | Configure encryption for data at rest and in transit |
| `/proagent-security-review` | Review overall security posture of the project |

## Quick Start

To get started, tell me what you need help with:

- "Scan this project for vulnerabilities" -> `/proagent-security-run scan-vulnerabilities`
- "Check if there are any hardcoded secrets" -> `/proagent-security-run audit-secrets`
- "Create a threat model for this API" -> `/proagent-security-run threat-model`
- "Are we GDPR compliant?" -> `/proagent-security-run compliance-check`
- "Set up TLS and encryption" -> `/proagent-security-run encrypt-setup`
- "Review the security posture of this repo" -> `/proagent-security-review`

## Source Assets

This plugin is built from production patterns across these Provectus repositories:
- **proagent** - Security hardening skills, authentication, authorization, input validation
- **proagent-repo GUI** - Zero Trust Execution engine, trust assessor, trust ladder
- **casdk-harness** - Production hardening plan with CVSS-scored vulnerabilities, tool restriction patterns
- **Auto-Claude** - CodeQL and Bandit CI security pipelines, Dependabot configuration, VirusTotal scanning
- **awesome-claude-code** - Repository security evaluation framework
- **agents** - Security auditor agent with DevSecOps, OWASP, and compliance capabilities
- **tac** - SQL injection prevention and security testing
- **claude-ui** - CSRF protection, rate limiting, encryption utilities
- **gastown** - Security audit formulas, watchdog chain monitoring
- **superpowers** - Defense-in-depth strategy
