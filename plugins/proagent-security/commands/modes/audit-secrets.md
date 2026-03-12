# Audit Secrets — Detect Hardcoded Secrets

Scan the repository for accidentally committed secrets and credentials.

**Steps:**
1. **Check for `security-scan` CLI availability:**
   - Run `which security-scan` to determine if the tool is installed
   - If available, proceed to step 2 (automated scan)
   - If not available, proceed to step 3 (manual pattern scan)

2. **Automated scan with `security-scan` (preferred):**
   - Execute `security-scan scan . --format json` to get structured results
   - If a `security-scan.yaml` config exists in the repo root, use it: `security-scan -c security-scan.yaml scan . --format json`
   - Parse the JSON output — findings are classified as BLOCKED, WARNING, or APPROVED
   - Map severity tiers: BLOCKED → CRITICAL/HIGH, WARNING → MEDIUM, APPROVED → LOW
   - For pre-commit context, add the `--staged-only` flag: `security-scan scan --staged-only --format json`
   - To generate a baseline for known findings: `security-scan baseline .`
   - Also generate a markdown report: `security-scan scan . --format markdown`
   - **Note:** An exit code of 1 means BLOCKED findings were detected (not a tool crash). Parse JSON output for details.
   - **Note:** `security-scan` wraps gitleaks and adds custom regex rules, 3-tier severity classification, and baseline filtering. Requires `gitleaks` on PATH.
   - After the automated scan, continue to step 4 (configuration audit) — `security-scan` focuses on code patterns but does not audit configuration hygiene

3. **Fallback: Manual pattern scan (when `security-scan` is not installed):**
   - AWS Access Keys: `AKIA[0-9A-Z]{16}`
   - AWS Secret Keys: 40-character base64 strings near AWS context
   - GitHub tokens: `gh[pousr]_[0-9a-zA-Z]{36}`
   - GitLab tokens: `glpat-[0-9a-zA-Z\-]{20}`
   - Generic API keys: Strings assigned to variables named `api_key`, `apiKey`, `API_KEY`, `secret`, `token`
   - Private keys: `-----BEGIN (RSA|DSA|EC|OPENSSH) PRIVATE KEY-----`
   - JWT tokens: `eyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+`
   - Database connection strings: `(postgres|mysql|mongodb)://` with embedded credentials
   - Slack webhooks: `https://hooks.slack.com/services/`

4. **Audit configuration files:**
   - Check `.env`, `.env.example`, `.env.local` for actual secrets (vs placeholder values)
   - Scan `docker-compose*.yml` environment sections for plaintext passwords
   - Check CI/CD pipeline files for hardcoded tokens or credentials
   - Inspect Kubernetes Secret manifests for base64-encoded secrets in plain YAML
   - Check Terraform files for hardcoded access keys or passwords
5. **Check repository hygiene:**
   - Verify `.gitignore` includes secret-related patterns (.env, *.pem, *.key, secrets/)
   - Check if `.secretsignore` or equivalent exists for pre-commit secret scanning
   - Verify git history does not contain previously committed secrets (recommend `git log --diff-filter=A -- '*.env' '*.key' '*.pem'`)
   - Check for `.env.example` with actual secret values instead of placeholders
6. **Generate audit report:**
   - If `security-scan` was used, incorporate its BLOCKED/WARNING/APPROVED classification
   - List all detected secrets with file location and line number
   - Classify severity: CRITICAL (production credentials, BLOCKED findings), HIGH (API keys), MEDIUM (development tokens, WARNING findings), LOW (test fixtures, APPROVED findings)
   - Provide remediation: rotate compromised credentials, remove from history with `git filter-branch` or BFG Repo-Cleaner
   - Recommend pre-commit hooks for ongoing prevention (suggest `security-scan scan --staged-only` as a pre-commit hook)
   - Generate a `.gitignore` update with missing secret patterns
