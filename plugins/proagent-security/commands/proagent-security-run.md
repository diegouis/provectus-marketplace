---
description: >
  Execute security operations: scan-vulnerabilities, audit-secrets, threat-model,
  compliance-check, encrypt-setup, xss-scan, risk-classify, agent-harden, or audit-workflow.
argument-hint: "<operation> [options]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /proagent-security-run — Execute Security Operations

Parse the operation from the user's arguments. Read and execute the corresponding mode file at `commands/modes/{operation}.md`.

## Available Operations

| Operation | Description |
|-----------|-------------|
| `scan-vulnerabilities` | Multi-layer vulnerability scan (SAST, SCA, OWASP Top 10) |
| `audit-secrets` | Detect hardcoded secrets and credential exposure |
| `threat-model` | Generate STRIDE threat model for the application |
| `compliance-check` | Validate compliance against GDPR, SOC 2, PCI-DSS, HIPAA, ISO 27001 |
| `encrypt-setup` | Configure encryption for data at rest and in transit |
| `xss-scan` | Scan frontend code for XSS vulnerabilities |
| `risk-classify` | Classify code change risk level (LOW/MEDIUM/HIGH/CRITICAL) |
| `agent-harden` | Harden autonomous agent deployments with sandboxing |
| `audit-workflow` | Execute structured security audit workflow |

## Dispatch

1. Match the user's operation argument to the table above
2. Read and execute `commands/modes/{operation}.md`
3. If the operation is not recognized, display the table above and ask the user to choose

## Error Handling

If required context is missing (such as the project type or compliance framework), ask the user for the missing information before proceeding.
