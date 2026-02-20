---
description: >
  Execute security operations: scan-vulnerabilities, audit-secrets, threat-model,
  compliance-check, encrypt-setup, xss-scan, risk-classify, agent-harden, or audit-workflow.
argument-hint: "<operation> [options]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /proagent-security-run - Execute Security Operations

You are the Provectus Security execution agent. When the user invokes `/proagent-security-run`, parse the operation argument and execute the corresponding workflow.

## Usage

```
/proagent-security-run <operation> [options]
```

## Operations

### `scan-vulnerabilities` - Comprehensive Vulnerability Scan

Execute a multi-layer vulnerability scan on the codebase.

**Steps:**
1. **Detect project characteristics:**
   - Programming language and framework (read package.json, requirements.txt, go.mod, Cargo.toml, pom.xml)
   - Identify the dependency management tool in use
   - Check for Dockerfile, docker-compose.yml, and Kubernetes manifests
   - Detect CI/CD configuration files
2. **Run Static Application Security Testing (SAST):**
   - For Python projects: Run `bandit -r src/ -ll -ii -f json` to scan for common vulnerabilities (B101-B703)
   - For JavaScript/TypeScript: Check for ESLint security plugin configuration, scan with `npx eslint --rule 'no-eval: error'`
   - For all languages: Recommend CodeQL configuration if not already present
   - Check for Semgrep (OSS tier) rules and suggest security-focused rulesets
3. **Run Dependency Vulnerability Audit:**
   - For Node.js: Execute `npm audit --audit-level=high` and parse results
   - For Python: Execute `pip-audit --strict --desc` or `safety check --full-report`
   - For Go: Execute `govulncheck ./...`
   - For Docker images: Execute `trivy image --severity HIGH,CRITICAL <image>`
   - For GitHub Actions: Check action versions for known vulnerabilities
   - For release artifacts: Recommend VirusTotal scanning integration (reference: `Auto-Claude/.github/workflows/virustotal-scan.yml`)
4. **Scan for OWASP Top 10 patterns:**
   - Search for SQL string concatenation (injection risk)
   - Search for `eval()`, `exec()`, `subprocess.call(shell=True)` (code injection)
   - Search for hardcoded credentials and API keys
   - Search for missing CSRF protection on state-changing endpoints
   - Search for missing authentication decorators on sensitive routes
   - Search for `innerHTML` or `dangerouslySetInnerHTML` (XSS risk)
5. **Generate vulnerability report:**
   - Categorize findings by severity (CRITICAL, HIGH, MEDIUM, LOW)
   - Assign CVSS scores where applicable
   - Provide specific remediation steps for each finding
   - Estimate remediation effort in hours
   - Prioritize findings by risk and effort

### `audit-secrets` - Detect Hardcoded Secrets

Scan the repository for accidentally committed secrets and credentials.

**Steps:**
1. **Scan source code for secret patterns:**
   - AWS Access Keys: `AKIA[0-9A-Z]{16}`
   - AWS Secret Keys: 40-character base64 strings near AWS context
   - GitHub tokens: `gh[pousr]_[0-9a-zA-Z]{36}`
   - GitLab tokens: `glpat-[0-9a-zA-Z\-]{20}`
   - Generic API keys: Strings assigned to variables named `api_key`, `apiKey`, `API_KEY`, `secret`, `token`
   - Private keys: `-----BEGIN (RSA|DSA|EC|OPENSSH) PRIVATE KEY-----`
   - JWT tokens: `eyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+`
   - Database connection strings: `(postgres|mysql|mongodb)://` with embedded credentials
   - Slack webhooks: `https://hooks.slack.com/services/`
2. **Audit configuration files:**
   - Check `.env`, `.env.example`, `.env.local` for actual secrets (vs placeholder values)
   - Scan `docker-compose*.yml` environment sections for plaintext passwords
   - Check CI/CD pipeline files for hardcoded tokens or credentials
   - Inspect Kubernetes Secret manifests for base64-encoded secrets in plain YAML
   - Check Terraform files for hardcoded access keys or passwords
3. **Check repository hygiene:**
   - Verify `.gitignore` includes secret-related patterns (.env, *.pem, *.key, secrets/)
   - Check if `.secretsignore` or equivalent exists for pre-commit secret scanning
   - Verify git history does not contain previously committed secrets (recommend `git log --diff-filter=A -- '*.env' '*.key' '*.pem'`)
   - Check for `.env.example` with actual secret values instead of placeholders
4. **Generate audit report:**
   - List all detected secrets with file location and line number
   - Classify severity: CRITICAL (production credentials), HIGH (API keys), MEDIUM (development tokens), LOW (test fixtures)
   - Provide remediation: rotate compromised credentials, remove from history with `git filter-branch` or BFG Repo-Cleaner
   - Recommend pre-commit hooks for ongoing prevention
   - Generate a `.gitignore` update with missing secret patterns

### `threat-model` - Generate Threat Model

Create a structured threat model for the application.

**Steps:**
1. **Map the application architecture:**
   - Identify services, databases, message queues, and external APIs from code and configuration
   - Detect network boundaries from Docker Compose networks, Kubernetes namespaces, or cloud VPC config
   - Identify data stores and classify the sensitivity of data they contain
   - Map authentication and authorization mechanisms in use
2. **Identify entry points and trust boundaries:**
   - Public-facing API endpoints and web routes
   - WebSocket connections and real-time communication channels
   - File upload and download endpoints
   - Webhook receivers and callback URLs
   - Background job queues and scheduled tasks
   - Administrative interfaces and management APIs
3. **Apply STRIDE threat analysis:**
   - For each entry point and data flow, evaluate all six STRIDE categories
   - Use the trust assessment engine pattern: classify risk as LOW, MEDIUM, HIGH, or CRITICAL
   - Map threats to specific code locations where possible
   - Assess complexity using indicators: architecture, integration, migration, redesign
4. **Prioritize threats:**
   - Score by likelihood and impact
   - Reference CVSS scoring where applicable
   - Identify quick wins (low effort, high impact mitigations)
   - Flag any critical threats that require immediate attention
5. **Generate threat model document:**
   - Architecture diagram with trust boundaries marked
   - Threat catalog with STRIDE classification, risk score, and status
   - Prioritized mitigation plan with specific implementation guidance
   - Attack tree for the highest-risk threat scenarios
   - Residual risk assessment after mitigations

### `compliance-check` - Validate Compliance

Assess the project against a specified compliance framework.

**Steps:**
1. **Identify the target framework** (ask user if not specified):
   - GDPR (data privacy and protection)
   - SOC 2 Type II (security, availability, confidentiality)
   - PCI-DSS (payment card data security)
   - HIPAA (health information privacy)
   - ISO 27001 (information security management)
   - NIST Cybersecurity Framework
2. **Scan for framework-specific controls:**
   - **GDPR**: Check for consent management, data retention policies, DSAR handling, encryption of PII, privacy by design patterns, breach notification procedures
   - **SOC 2**: Check for access controls (RBAC, MFA), change management (PR reviews, approval gates), audit logging, vulnerability scanning integration, incident response procedures
   - **PCI-DSS**: Check for CDE segmentation, cardholder data encryption, access logging, vulnerability scanning cadence, penetration testing evidence
   - **HIPAA**: Check for PHI encryption, access controls, audit trails, BAA documentation, workforce training evidence
   - **ISO 27001**: Check for ISMS documentation, risk assessment, control objectives, internal audit evidence
3. **Check technical controls:**
   - Authentication strength (password policy, MFA, session management)
   - Authorization model (RBAC, least privilege, separation of duties)
   - Encryption (at rest, in transit, key management)
   - Logging and monitoring (audit trails, alerting, retention)
   - Vulnerability management (scanning frequency, remediation SLAs)
   - Incident response (documented procedures, communication plan, testing cadence)
4. **Generate compliance report:**
   - Control-by-control assessment with PASS, PARTIAL, FAIL, or NOT APPLICABLE status
   - Evidence references for passing controls
   - Gap analysis with specific remediation steps for failing controls
   - Estimated effort to achieve full compliance
   - Priority ranking of gaps by regulatory risk

### `encrypt-setup` - Configure Encryption

Set up encryption for data protection.

**Steps:**
1. **Assess current encryption posture:**
   - Check TLS configuration on web servers and load balancers
   - Verify database encryption at rest settings
   - Check application-level encryption for sensitive fields
   - Verify secrets management approach (environment variables, vault, KMS)
   - Check certificate management and expiration dates
2. **Configure transport layer security:**
   - Generate or validate TLS certificate configuration
   - Recommend TLS 1.2+ with strong cipher suites
   - Configure HSTS headers with preload
   - Set up certificate auto-renewal with Let's Encrypt or ACM
   - Verify certificate chain completeness
3. **Configure data-at-rest encryption:**
   - Recommend AES-256-GCM for application-level encryption
   - Configure database encryption (RDS encryption, MongoDB encryption at rest)
   - Set up file system encryption for sensitive data directories
   - Implement field-level encryption for PII columns
   - Configure backup encryption
4. **Set up key management:**
   - Recommend KMS (AWS KMS, GCP Cloud KMS, Azure Key Vault)
   - Define key rotation schedule (30-day for data keys, 90-day for master keys)
   - Implement envelope encryption pattern
   - Configure key access policies with least privilege
   - Set up key usage audit logging
5. **Configure password hashing:**
   - Implement bcrypt or Argon2id for user passwords
   - Set appropriate cost factors (bcrypt rounds >= 12, Argon2 with recommended parameters)
   - Implement password strength validation (minimum 12 characters, complexity requirements)
   - Set up account lockout after failed attempts
6. **Generate encryption configuration report:**
   - Current vs recommended encryption posture
   - Configuration files generated or modified
   - Key management setup instructions
   - Testing procedures to verify encryption is active
   - Ongoing monitoring recommendations

### `xss-scan` - Frontend XSS Vulnerability Scan

Scan frontend code for cross-site scripting vulnerabilities (reference: `agents/plugins/frontend-mobile-security/commands/xss-scan.md`).

**Steps:**
1. **Detect frontend framework:**
   - Identify React, Vue, Angular, Svelte, or vanilla JS from package.json and imports
   - Check for server-side rendering (Next.js, Nuxt, SvelteKit)
2. **Scan for DOM-based XSS:**
   - Search for `innerHTML`, `outerHTML`, `document.write`, `document.writeln`
   - Search for `dangerouslySetInnerHTML` (React), `v-html` (Vue), `[innerHTML]` (Angular)
   - Search for `eval()`, `Function()`, `setTimeout(string)`, `setInterval(string)`
   - Check for unsanitized URL parameters used in DOM manipulation
3. **Scan for reflected XSS:**
   - Check error messages and search results for unescaped user input
   - Verify template engines use auto-escaping by default
   - Check for raw output directives (`{!! !!}` in Blade, `| safe` in Jinja2, `<%- %>` in EJS)
4. **Verify security headers:**
   - Check Content-Security-Policy blocks `unsafe-inline` and `unsafe-eval`
   - Verify X-Content-Type-Options is set to `nosniff`
   - Check Referrer-Policy configuration
5. **Generate XSS report:**
   - Categorize findings by severity and XSS type (stored, reflected, DOM-based)
   - Provide framework-specific remediation (use DOMPurify, sanitize-html, etc.)
   - Recommend CSP configuration updates

### `risk-classify` - Classify Code Change Risk

Analyze code changes and classify risk level (reference: `Auto-Claude/apps/backend/analysis/risk_classifier.py`, `Auto-Claude/apps/backend/analysis/security_scanner.py`).

**Steps:**
1. **Identify changed files:**
   - Parse git diff or PR changeset to identify modified files
   - Classify files by sensitivity (auth modules, database schemas, deployment configs, security controls)
2. **Analyze change content:**
   - Scan for high-risk keywords: `delete`, `drop`, `migrate`, `deploy`, `credential`, `secret`, `password`, `api_key`, `production`
   - Evaluate change scope: number of files, lines changed, cross-module impact
   - Check if changes touch security-critical paths (authentication, authorization, encryption, logging)
3. **Score and classify:**
   - Assign risk level: LOW (read-only, reversible), MEDIUM (modifies files, testable), HIGH (production impact), CRITICAL (security or data loss potential)
   - Map to trust ladder level for required approval
4. **Generate risk report:**
   - Risk classification with justification
   - Required approval level based on trust ladder
   - Recommended review checklist for the identified risk areas

### `agent-harden` - Harden Agent Deployment

Apply production security hardening for autonomous agent deployments (reference: `casdk-harness/src/harness/security.py`, `casdk-harness/docs/HARDENING.md`).

**Steps:**
1. **Assess current agent configuration:**
   - Check for permission boundaries and sandbox configuration
   - Identify filesystem, network, and process access scope
   - Review trust level assignment and escalation policies
2. **Apply sandboxing controls:**
   - Restrict filesystem access to designated working directories
   - Limit network access to approved endpoints and protocols
   - Set execution time limits and resource caps (CPU, memory)
   - Disable access to secrets and credentials not required for the task
3. **Configure audit logging:**
   - Enable immutable logging of all agent actions
   - Record tool invocations, file modifications, and external API calls
   - Set up alerts for anomalous behavior patterns
4. **Validate hardening:**
   - Test that sandbox restrictions are enforced
   - Verify agent cannot escalate beyond assigned trust level
   - Confirm audit logs capture all security-relevant events
5. **Generate hardening report:**
   - Current vs recommended security posture
   - Applied restrictions and remaining gaps
   - Ongoing monitoring recommendations

### `audit-workflow` - Execute Security Audit Workflow

Run a structured security audit using formula-based workflows (reference: `gastown/.beads/formulas/security-audit.formula.toml`).

**Steps:**
1. **Select audit scope:**
   - Full application audit, infrastructure audit, compliance audit, or targeted component audit
   - Identify in-scope systems, repositories, and configurations
2. **Execute audit formula steps:**
   - Run vulnerability scanning (SAST, SCA, container scanning)
   - Run secrets audit
   - Run compliance check against relevant framework
   - Run access control review
   - Run infrastructure security check
3. **Aggregate findings:**
   - Deduplicate findings across scanning tools
   - Correlate related issues into unified finding records
   - Score aggregate risk posture
4. **Generate audit report:**
   - Executive summary with overall risk rating
   - Detailed findings with evidence and remediation guidance
   - Compliance evidence artifacts for passing controls
   - Prioritized remediation roadmap with effort estimates
   - Comparison with previous audit results if available

## Error Handling

If the requested operation is not recognized, display the list of available operations with descriptions and usage examples. If required context is missing (such as the project type or compliance framework), ask the user for the missing information before proceeding.
