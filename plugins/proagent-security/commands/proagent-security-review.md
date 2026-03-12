---
description: >
  Review security posture: code security, dependency vulnerabilities, access controls,
  container security, CI/CD pipeline security, and infrastructure configuration.
argument-hint: "[target]"
allowed-tools: Read, Glob, Grep, Bash, Task
---

# /proagent-security-review — Review Security Posture

Perform a comprehensive security review. Detect which areas apply, then read and execute the relevant mode files.

## Auto-Detection

Scan for these files and review all that are found:

| Priority | File Pattern | Mode File |
|----------|-------------|-----------|
| 1 | `*.py`, `*.js`, `*.ts`, `*.go`, `*.java` | `commands/modes/review-code-security.md` |
| 2 | `package.json`, `requirements.txt`, `go.mod`, `Cargo.toml` | `commands/modes/review-dependencies.md` |
| 3 | `.env`, `.env.example`, `*.pem`, `*.key` | Use `/proagent-security-run audit-secrets` |
| 4 | `Dockerfile`, `docker-compose*.yml` | `commands/modes/review-container.md` |
| 5 | `.github/workflows/*.yml`, `.gitlab-ci.yml` | `commands/modes/review-cicd.md` |
| 6 | `k8s/*.yaml`, `kubernetes/*.yaml`, `*.tf` | `commands/modes/review-infrastructure.md` |
| 7 | Authentication/authorization modules | `commands/modes/review-access-control.md` |
| 8 | Frontend components with user input | `commands/modes/review-frontend.md` |
| 9 | Agent configuration, sandbox settings | `commands/modes/review-agent-hardening.md` |
| 10 | `*.sol` (Solidity contracts) | `commands/modes/review-smart-contract.md` |

## Dispatch

1. If a specific target is provided, review only that area
2. If no target, scan the repository and review all applicable areas in priority order
3. For each area, read and execute the corresponding mode file

## Output Format

For each reviewed area:

```
## Review: <area>

### Summary
<one-line assessment: PASS / NEEDS ATTENTION / CRITICAL>

### Issues Found

#### Critical (CVSS 9.0+)
- [ ] <issue> - <location> - <fix recommendation>

#### High (CVSS 7.0-8.9)
- [ ] <issue> - <location> - <fix recommendation>

#### Medium (CVSS 4.0-6.9)
- [ ] <issue> - <location> - <fix recommendation>

#### Low (CVSS 0.1-3.9)
- [ ] <issue> - <location> - <fix recommendation>

### Score: X/10
```

After all areas, provide:

```
## Overall Security Posture

### Score: X/10

### Top 3 Action Items (by risk severity)
1. <highest risk item with specific remediation>
2. <second highest risk item>
3. <third highest risk item>

### Estimated Remediation Effort
- Critical items: Xh
- High items: Xh
- Medium items: Xh
- Total: Xh
```
