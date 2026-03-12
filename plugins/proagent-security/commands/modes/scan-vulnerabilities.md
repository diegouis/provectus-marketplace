# Scan Vulnerabilities — Comprehensive Vulnerability Scan

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
   - Search for hardcoded credentials and API keys (for deep secrets scanning, use `/proagent-security-run audit-secrets` which leverages `security-scan` when available)
   - Search for missing CSRF protection on state-changing endpoints
   - Search for missing authentication decorators on sensitive routes
   - Search for `innerHTML` or `dangerouslySetInnerHTML` (XSS risk)
5. **Generate vulnerability report:**
   - Categorize findings by severity (CRITICAL, HIGH, MEDIUM, LOW)
   - Assign CVSS scores where applicable
   - Provide specific remediation steps for each finding
   - Estimate remediation effort in hours
   - Prioritize findings by risk and effort
