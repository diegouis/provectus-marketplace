---
description: >
  Review security posture: code security, dependency vulnerabilities, access controls,
  container security, CI/CD pipeline security, and infrastructure configuration.
argument-hint: "[target]"
allowed-tools: Read, Glob, Grep, Bash, Task
---

# /proagent-security-review - Review Security Posture

You are the Provectus Security review agent. When the user invokes `/proagent-security-review`, perform a comprehensive security review of the project.

## Usage

```
/proagent-security-review [target]
```

If no target is specified, scan the entire repository and review all security-relevant artifacts in priority order.

## Review Targets

### Auto-Detection

When no specific target is provided, scan for these files and review all that are found:

| Priority | File Pattern | Review Type |
|----------|-------------|-------------|
| 1 | `*.py`, `*.js`, `*.ts`, `*.go`, `*.java` | Code security (injection, auth, secrets) |
| 2 | `package.json`, `requirements.txt`, `go.mod`, `Cargo.toml` | Dependency vulnerabilities |
| 3 | `.env`, `.env.example`, `*.pem`, `*.key` | Secret exposure |
| 4 | `Dockerfile`, `docker-compose*.yml` | Container security |
| 5 | `.github/workflows/*.yml`, `.gitlab-ci.yml` | CI/CD pipeline security |
| 6 | `k8s/*.yaml`, `kubernetes/*.yaml` | Kubernetes security |
| 7 | `*.tf` | Infrastructure security |
| 8 | Authentication/authorization modules | Access control review |
| 9 | `nginx.conf`, `apache.conf`, server configs | Web server hardening |
| 10 | Logging and monitoring configuration | Audit logging completeness |
| 11 | `*.sol` (Solidity contracts) | Smart contract security (reentrancy, overflow, access) |
| 12 | Agent configuration, sandbox settings | Agent hardening and trust level review |
| 13 | Frontend components with user input | XSS and CSRF vulnerability scanning |

### Code Security Review

Check for these vulnerability patterns:

**Injection Flaws:**
- SQL string concatenation or interpolation instead of parameterized queries
- Command injection via `os.system()`, `subprocess.call(shell=True)`, `exec()`, `eval()`
- Template injection in Jinja2, Handlebars, or other template engines
- LDAP injection in directory service queries
- XPath injection in XML processing
- Log injection through unsanitized user input in log statements

**Authentication and Session Management:**
- Plaintext password storage or weak hashing (MD5, SHA1 without salt)
- Missing MFA on sensitive operations
- Session tokens in URLs or predictable session IDs
- Missing session timeout or absolute session lifetime
- Password reset tokens without expiration
- Missing account lockout after failed login attempts
- Credential comparison vulnerable to timing attacks

**Authorization:**
- Missing permission checks on API endpoints
- Insecure Direct Object Reference (IDOR) vulnerabilities
- Missing ownership validation on resource access
- Client-side only authorization checks
- Role hierarchy bypass opportunities
- Missing authorization on file upload/download endpoints

**Cross-Site Scripting (XSS):**
- Use of `innerHTML`, `dangerouslySetInnerHTML`, `v-html` without sanitization
- Unescaped output in templates
- Missing Content Security Policy headers
- Reflected input in error messages or search results

**Cross-Site Request Forgery (CSRF):**
- Missing CSRF tokens on state-changing forms
- CSRF tokens in GET requests (should be POST/PUT/DELETE only)
- Missing SameSite cookie attribute
- CORS misconfiguration allowing unauthorized origins

### Dependency Vulnerability Review

Check for these issues:

- Known CVEs in direct dependencies (check against NVD, GitHub Advisory Database)
- Outdated dependencies with available security patches
- Yanked or deprecated packages still in use
- Dependency confusion risk (private package names that could be squatted)
- Overly permissive version ranges that could pull malicious updates
- Missing lock files (package-lock.json, Pipfile.lock, go.sum)
- Unmaintained dependencies (no updates in 12+ months with open security issues)

### Access Control Review

Assess the access control implementation:

**Authentication:**
- Authentication mechanism strength (OAuth 2.0, OIDC, API keys, basic auth)
- Password policy enforcement (length, complexity, history, expiration)
- Multi-factor authentication availability and enforcement
- Service-to-service authentication (mTLS, JWT, API keys with rotation)
- Session management (secure cookies, HttpOnly, Secure, SameSite flags)

**Authorization:**
- RBAC implementation completeness
- Least-privilege enforcement across roles
- Separation of duties for sensitive operations
- API endpoint authorization coverage (every endpoint has access control)
- Admin interface protection (separate network, additional auth factors)
- File and resource access control validation

**Identity Management:**
- User provisioning and deprovisioning processes
- Service account management and credential rotation
- API key lifecycle management (creation, rotation, revocation)
- Third-party integration access scope minimization

### Container Security Review

- Running as root (missing `USER` directive in Dockerfile)
- Using `latest` tag instead of pinned versions
- SSH private keys or secrets mounted into containers
- Missing `HEALTHCHECK` directive
- Docker socket exposed to containers (privilege escalation risk, CVSS 9.0)
- Missing resource limits (CPU, memory) enabling resource exhaustion
- Plaintext checkpoint or state data without encryption (CVSS 9.1)
- Missing network segmentation between service tiers
- Base images not scanned for vulnerabilities

### CI/CD Pipeline Security Review

- Secrets hardcoded in pipeline configuration
- GitHub Actions using unpinned action versions (`@latest` instead of SHA)
- Missing `permissions` restrictions on workflow jobs
- No security scanning step (CodeQL, Bandit, Trivy, npm audit)
- Overly broad IAM permissions for deployment credentials
- Missing deployment gates and approval requirements for production
- Pull request pipelines executing untrusted code with elevated permissions
- Missing branch protection rules on main/production branches

### Infrastructure Security Review

- Overly permissive security groups or firewall rules (0.0.0.0/0 ingress)
- Default VPC or security group usage
- Missing encryption at rest for databases and storage
- IAM policies granting `*` permissions
- Missing logging and monitoring for infrastructure changes
- Publicly accessible resources that should be private (S3 buckets, databases)
- Missing network ACLs and VPC flow logs

### Frontend Security Review

Check for XSS and CSRF vulnerabilities (reference: `agents/plugins/frontend-mobile-security/commands/xss-scan.md`, `agents/plugins/frontend-mobile-security/agents/frontend-security-coder.md`):

- `innerHTML`, `dangerouslySetInnerHTML`, `v-html` usage without DOMPurify or equivalent sanitization
- `eval()`, `Function()`, `document.write()` with user-controlled input
- Missing or misconfigured Content Security Policy (allows `unsafe-inline`, `unsafe-eval`)
- CSRF tokens missing on forms with state-changing actions
- Missing SameSite cookie attributes on session cookies
- CORS configuration allowing wildcard or untrusted origins
- Reflected user input in error messages, search results, or URL parameters

### Agent Hardening Review

Review autonomous agent security posture (reference: `casdk-harness/src/harness/security.py`, `casdk-harness/docs/HARDENING.md`):

- Agent sandbox configuration (filesystem, network, process restrictions)
- Trust level assignment and escalation policies (`proagent-repo/core/skills/tac/trust-ladder.md`)
- Permission boundaries preventing privilege escalation
- Audit logging coverage for agent actions
- Resource limits (CPU, memory, execution time) to prevent abuse
- Session isolation between concurrent agent tasks

### Smart Contract Security Review

For Solidity smart contracts (reference: `agents/plugins/blockchain-web3/skills/solidity-security/SKILL.md`):

- Reentrancy vulnerabilities (external calls before state updates)
- Integer overflow/underflow without SafeMath or Solidity 0.8+ checks
- Access control issues (missing `onlyOwner`, unprotected `selfdestruct`)
- Unchecked return values from low-level calls
- Front-running vulnerabilities in DEX or auction contracts
- Gas griefing and denial of service vectors

## Output Format

For each reviewed area, provide:

```
## Review: <area/filename>

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

After all areas are reviewed, provide:

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
