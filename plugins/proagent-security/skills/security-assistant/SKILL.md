---
name: security-assistant
description: Securing Software & Infrastructure - vulnerability scanning (SAST, DAST, XSS, VirusTotal), compliance enforcement (PCI, GDPR, SOC2, HIPAA), secrets management, encryption, audit logging, threat modeling, OWASP Top 10 protection, Zero Trust architecture, agent sandboxing, risk classification, frontend security, and smart contract security. Use when performing any security assessment, hardening, compliance, or threat analysis task.
---

# Securing Software & Infrastructure

Comprehensive security skill covering vulnerability scanning, compliance enforcement, secrets management, threat modeling, OWASP Top 10 protection, Zero Trust architecture, and encryption.

## When to Use This Skill

- Scanning code for vulnerabilities (SAST, DAST, dependency scanning)
- Auditing secrets and credentials in repositories
- Building threat models (STRIDE, PASTA)
- Enforcing compliance frameworks (GDPR, HIPAA, SOC 2, PCI-DSS)
- Implementing Zero Trust architecture and agent sandboxing
- Reviewing code for OWASP Top 10 vulnerabilities
- Setting up encryption, security headers, and rate limiting
- Classifying risk levels for code changes
- Running security audit workflows

## When Invoked Without Clear Intent

**Use `AskUserQuestion`** to present options as a selector widget:

```
AskUserQuestion(
  header: "Security",
  question: "What security topic do you need help with?",
  options: [
    { label: "Vulnerability Scanning", description: "SAST, DAST, CodeQL, Bandit, dependency audit, Trivy" },
    { label: "Secrets & Threat Modeling", description: "Secrets detection, rotation, STRIDE threat modeling" },
    { label: "OWASP Top 10", description: "Broken access control, injection, XSS, SSRF, auth failures" },
    { label: "Compliance", description: "GDPR, SOC 2, PCI-DSS, HIPAA compliance checklists" }
  ]
)
```

If the user selects "Other", present: Zero Trust / Agent Sandboxing, Encryption / Hardening / Audit Logging.

## Reference Routing

> **CONTEXT GUARD**: Load reference files only when the user's request matches a specific topic below. Do NOT load all references upfront.

| User Intent | Reference File |
|---|---|
| SAST, DAST, CodeQL, Bandit, VirusTotal, XSS scanning, dependency audit, Trivy | `references/vulnerability-scanning.md` |
| Secrets detection, secret rotation, STRIDE threat modeling, trust assessment, attack surface | `references/secrets-threats.md` |
| OWASP Top 10, broken access control, injection, XSS, SSRF, auth failures | `references/owasp-patterns.md` |
| Zero Trust, trust ladder, agent sandboxing, identity-based access, micro-segmentation | `references/zero-trust.md` |
| GDPR, SOC 2, PCI-DSS, HIPAA, compliance checklists, DPA, DSAR | `references/compliance-frameworks.md` |
| TLS config, security headers, password hashing, rate limiting, audit logging, risk classification | `references/encryption-hardening.md` |

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate threat model diagrams, Zero Trust architecture maps, compliance workflow flows, and incident response runbook visualizations. Describe what you need in natural language.
