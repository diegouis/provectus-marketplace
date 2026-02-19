# Provectus Security Practice Plugin

This plugin provides the Security practice context for the Provectus agentic coding platform. It equips Claude with production-tested security patterns drawn from actual Provectus engineering repositories.

## Practice Scope

The Security practice covers eleven operational domains:

1. **Vulnerability Scanning** - SAST with CodeQL and Bandit, DAST with OWASP ZAP, dependency scanning with npm audit/pip-audit/Trivy, container image scanning, VirusTotal malware scanning (`Auto-Claude/.github/workflows/virustotal-scan.yml`)
2. **Compliance Enforcement** - GDPR, SOC 2 Type II, PCI-DSS, HIPAA, ISO 27001, and NIST CSF framework assessment and validation; specialized PCI compliance skill (`agents/plugins/payment-processing/skills/pci-compliance/SKILL.md`) and GDPR data handling skill (`agents/plugins/hr-legal-compliance/skills/gdpr-data-handling/SKILL.md`)
3. **Secrets Management** - Detection of hardcoded credentials, secret rotation policies, integration with AWS Secrets Manager, HashiCorp Vault, and GCP Secret Manager
4. **Encryption** - TLS 1.2/1.3 configuration, AES-256-GCM for data at rest, bcrypt/Argon2 password hashing, KMS key management and rotation
5. **Audit Logging** - Structured security event logging, tamper-proof storage, SIEM integration, compliance evidence collection
6. **Threat Modeling** - STRIDE and PASTA methodologies, attack surface analysis, trust assessment with risk/complexity scoring, attack tree generation
7. **OWASP Top 10 Protection** - Code-level checks for all 10 categories with specific remediation patterns for injection, broken access control, cryptographic failures
8. **Zero Trust Architecture** - Trust ladder with five progressive autonomy levels (`proagent-repo/core/skills/tac/trust-ladder.md`), trust assessment engine (`proagent-repo/core/zte/trust_assessor.py`), identity-based access, continuous verification, micro-segmentation
9. **Frontend Security** - XSS vulnerability scanning (`agents/plugins/frontend-mobile-security/commands/xss-scan.md`), CSRF protection, CSP configuration, frontend-specific secure coding patterns (`agents/plugins/frontend-mobile-security/agents/frontend-security-coder.md`)
10. **Agent Sandboxing and Access Control** - Production agent hardening (`casdk-harness/src/harness/security.py`, `casdk-harness/docs/HARDENING.md`), permission boundaries, sandbox isolation for autonomous agents
11. **Risk Classification** - Automated risk scoring for code changes (`Auto-Claude/apps/backend/analysis/risk_classifier.py`), security scanner module (`Auto-Claude/apps/backend/analysis/security_scanner.py`), security audit workflow formulas (`gastown/.beads/formulas/security-audit.formula.toml`)

## Key Conventions

When performing security tasks, follow these standards:

### Assessment
- Always read existing code and configurations before recommending changes
- Use CVSS scoring for objective vulnerability ranking
- Prioritize findings by exploitability and business impact, not just severity
- Distinguish between confirmed vulnerabilities and potential risks

### Remediation
- Provide specific code changes and configuration updates, not just descriptions
- Include parameterized query examples when fixing injection vulnerabilities
- Reference OWASP cheat sheets for implementation guidance
- Recommend tests alongside security fixes to prevent regressions

### Secrets
- Never log, display, or store secrets in plaintext
- Use environment variables or secrets managers for all credentials
- Enforce .gitignore patterns for .env, *.pem, *.key, and secrets/ directories
- Recommend secret rotation schedules based on credential type

### Compliance
- Map findings to specific framework controls (e.g., SOC 2 CC6.1, GDPR Article 32)
- Provide evidence references for passing controls
- Estimate remediation effort for failing controls
- Prioritize gaps by regulatory risk

### Zero Trust
- Apply least-privilege access as the default for all operations
- Require authentication and authorization on every endpoint
- Use the trust ladder model for agent operations: Supervised -> Approval-Gated -> Monitored -> Autonomous -> Zero-Touch (see `proagent-repo/core/skills/tac/trust-ladder.md`)
- Classify tasks by risk (LOW, MEDIUM, HIGH, CRITICAL) using the trust assessor (`proagent-repo/core/zte/trust_assessor.py`)
- Apply agent sandboxing patterns from `casdk-harness/src/harness/security.py` for production agent isolation

### Frontend Security
- Scan for XSS vulnerabilities using dedicated scanning commands (see `agents/plugins/frontend-mobile-security/commands/xss-scan.md`)
- Validate CSP headers block inline scripts and unsafe-eval
- Enforce SameSite cookie attributes and CSRF token usage on all state-changing forms
- Review `innerHTML`, `dangerouslySetInnerHTML`, and `v-html` usage for sanitization

### Risk Classification and Audit Workflows
- Use automated risk classification for code changes based on keyword analysis and change scope (`Auto-Claude/apps/backend/analysis/risk_classifier.py`)
- Run security scanner modules for automated vulnerability detection (`Auto-Claude/apps/backend/analysis/security_scanner.py`)
- Reference security audit workflow formulas for structured audit processes (`gastown/.beads/formulas/security-audit.formula.toml`)

## MCP Integrations

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **GitLab**: Project management, vulnerability reports, SAST/DAST pipeline results, dependency scanning, and merge request approvals via `@modelcontextprotocol/server-gitlab`

## Source Repositories

> Built from Provectus internal engineering practices across 10 repositories: `agents`, `Auto-Claude`, `awos`, `casdk-harness`, `claude-ui`, `gastown`, `proagent-repo`, `proagent-repo GUI`, `provectus-marketplace`, `ralph-orchestrator`. Key external assets include security scanning commands and hardening agents from `agents`, risk classification and VirusTotal workflows from `Auto-Claude`, agent sandboxing from `casdk-harness`, trust ladder and ZTE assessor from `proagent-repo`, audit formulas from `gastown`, and security considerations from `ralph-orchestrator`.

## Plugin Structure

```
proagent-security/
  .claude-plugin/plugin.json
  skills/security-assistant/SKILL.md
  commands/proagent-security-hub.md
  commands/proagent-security-run.md
  commands/proagent-security-review.md
  agents/security-specialist.md
  hooks/hooks.json
  .mcp.json
  CLAUDE.md
  README.md
```
