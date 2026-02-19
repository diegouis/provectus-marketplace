---
name: security-assistant
description: Securing Software & Infrastructure - vulnerability scanning (SAST, DAST, XSS, VirusTotal), compliance enforcement (PCI, GDPR, SOC2, HIPAA), secrets management, encryption, audit logging, threat modeling, OWASP Top 10 protection, Zero Trust architecture, agent sandboxing, risk classification, frontend security, and smart contract security. Use when performing any security assessment, hardening, compliance, or threat analysis task.
---

# Securing Software & Infrastructure

Comprehensive security skill covering the full lifecycle of application security, infrastructure hardening, compliance enforcement, and threat management. Built from production-tested patterns across Provectus engineering teams.

## When to Use This Skill

- Scanning code for vulnerabilities (SAST, DAST, dependency scanning)
- Auditing secrets and credentials in repositories and configurations
- Building threat models for applications and infrastructure
- Enforcing compliance frameworks (GDPR, HIPAA, SOC 2, PCI-DSS, ISO 27001)
- Setting up encryption for data at rest and in transit
- Implementing Zero Trust architecture and access controls
- Reviewing code for OWASP Top 10 vulnerabilities
- Configuring security headers, CORS, CSRF protections
- Setting up security monitoring, logging, and incident response
- Hardening containers, Kubernetes clusters, and cloud resources
- Scanning for XSS vulnerabilities in frontend applications
- Auditing Solidity smart contracts for Web3 security
- Classifying risk levels for code changes and pull requests
- Sandboxing and hardening autonomous agent deployments
- Running VirusTotal malware scans in CI/CD pipelines
- Executing security audit workflow formulas

## Vulnerability Scanning

### Static Application Security Testing (SAST)

Scan source code for security vulnerabilities before deployment:

```yaml
# CodeQL Analysis (GitHub Actions)
- name: Initialize CodeQL
  uses: github/codeql-action/init@v3
  with:
    languages: ${{ matrix.language }}
    queries: +security-extended,security-and-quality

- name: Perform CodeQL Analysis
  uses: github/codeql-action/analyze@v3
  with:
    category: "/language:${{ matrix.language }}"
```

```yaml
# Bandit for Python Security
- name: Run Bandit security scan
  run: |
    bandit -r src/ -ll -ii -f json -o bandit-report.json || BANDIT_EXIT=$?
    if [ "${BANDIT_EXIT:-0}" -gt 1 ]; then
      echo "Bandit scan failed with exit code $BANDIT_EXIT"
      exit 1
    fi
```

Additional SAST tools by language:
- **Python**: Bandit, Semgrep (OSS tier), CodeQL
- **JavaScript/TypeScript**: ESLint security plugin, Semgrep, CodeQL
- **Go**: gosec, staticcheck
- **Java**: SpotBugs with FindSecBugs, PMD
- **Solidity**: Smart contract security auditing for reentrancy, overflow, and access control vulnerabilities (reference: `agents/plugins/blockchain-web3/skills/solidity-security/SKILL.md`)

For centralized SAST scanning and security hardening commands, see:
- `agents/plugins/security-scanning/commands/security-sast.md` - Dedicated SAST command
- `agents/plugins/security-scanning/commands/security-hardening.md` - Security hardening command

### VirusTotal Malware Scanning

Integrate VirusTotal scanning into CI/CD pipelines to detect malicious artifacts before deployment:

```yaml
# VirusTotal scan workflow (from Auto-Claude)
# Reference: Auto-Claude/.github/workflows/virustotal-scan.yml
- name: VirusTotal Scan
  uses: crazy-max/ghaction-virustotal@v4
  with:
    vt_api_key: ${{ secrets.VT_API_KEY }}
    files: |
      dist/*.tar.gz
      dist/*.whl
```

### XSS Vulnerability Scanning

Dedicated XSS scanning for frontend applications (reference: `agents/plugins/frontend-mobile-security/commands/xss-scan.md`):

- Scan for `innerHTML`, `dangerouslySetInnerHTML`, `v-html` usage without sanitization
- Detect reflected input in templates and error messages
- Validate Content Security Policy headers block `unsafe-inline` and `unsafe-eval`
- Check for DOM-based XSS via `document.write`, `eval`, and `location.href` manipulation
- Review framework-specific XSS vectors (React, Vue, Angular)

### Dependency Vulnerability Scanning

```yaml
# Dependabot configuration
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "security"

  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10

  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"

  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

Runtime dependency audit commands:
```bash
# Node.js
npm audit --audit-level=high
npm audit fix

# Python
pip-audit --strict --desc
safety check --full-report

# Go
govulncheck ./...

# Container images
trivy image --severity HIGH,CRITICAL myregistry.io/myapp:latest
```

### Dynamic Application Security Testing (DAST)

- OWASP ZAP for automated web application scanning
- Burp Suite for interactive security testing
- Nessus for infrastructure vulnerability assessment
- Cloud-native scanning: AWS Inspector, GCP Security Command Center

## Secrets Management

### Secret Detection and Prevention

Patterns to detect in pre-commit scanning:
```
# High-confidence secret patterns
AWS Access Key:       AKIA[0-9A-Z]{16}
AWS Secret Key:       [0-9a-zA-Z/+]{40}
GitHub Token:         gh[pousr]_[0-9a-zA-Z]{36}
GitLab Token:         glpat-[0-9a-zA-Z\-]{20}
Generic API Key:      [aA][pP][iI][-_]?[kK][eE][yY].*['\"][0-9a-zA-Z]{32,}
Private Key:          -----BEGIN (RSA|DSA|EC|OPENSSH) PRIVATE KEY-----
JWT Token:            eyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+
Database URL:         (postgres|mysql|mongodb)://[^\s]+:[^\s]+@
Slack Webhook:        https://hooks.slack.com/services/T[0-9A-Z]+/B[0-9A-Z]+/[a-zA-Z0-9]+
```

Files that should always be excluded from commits:
```gitignore
# Secrets and credentials
.env
.env.local
.env.*.local
*.pem
*.key
*.p12
*.pfx
secrets/
credentials/
**/service-account*.json
```

### Secure Secrets Storage

```python
import os
from dotenv import load_dotenv

# Load from .env file (not committed to git)
load_dotenv()

# Get secrets from environment
API_KEY = os.getenv('EXTERNAL_API_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')

if not API_KEY:
    raise ValueError("EXTERNAL_API_KEY environment variable not set")

# For production, use secrets management service
# AWS Secrets Manager, HashiCorp Vault, GCP Secret Manager
try:
    import boto3
    secrets_client = boto3.client('secretsmanager')
    secret = secrets_client.get_secret_value(SecretId='prod/api/keys')
    API_KEY = json.loads(secret['SecretString'])['external_api_key']
except Exception:
    pass  # Fallback to environment variable
```

Secret rotation policy:
- API keys: Rotate every 90 days
- Database passwords: Rotate every 60 days
- Service account keys: Rotate every 30 days
- SSL/TLS certificates: Monitor expiration, renew 30 days before

## Threat Modeling

### STRIDE Methodology

For each component in the system, evaluate:

| Threat | Description | Example Mitigation |
|--------|-------------|-------------------|
| **Spoofing** | Impersonating a user or system | MFA, OAuth2/OIDC, certificate-based auth |
| **Tampering** | Modifying data or code | HMAC signatures, code signing, integrity checks |
| **Repudiation** | Denying an action occurred | Audit logs, immutable logging, timestamps |
| **Information Disclosure** | Exposing sensitive data | Encryption at rest/in transit, data classification |
| **Denial of Service** | Making a service unavailable | Rate limiting, WAF, auto-scaling, circuit breakers |
| **Elevation of Privilege** | Gaining unauthorized access | RBAC, least privilege, input validation |

### Trust Assessment for Agent Operations

```python
class TaskRisk(Enum):
    LOW = "low"          # Read-only, reversible
    MEDIUM = "medium"    # Modifies files, testable
    HIGH = "high"        # Production impact, external systems
    CRITICAL = "critical"  # Security, data loss potential

# High-risk keywords that trigger elevated assessment
HIGH_RISK_KEYWORDS = [
    "delete", "remove", "drop", "production", "deploy",
    "migrate", "security", "password", "credential",
    "secret", "api_key", "database", "schema",
]
```

Risk-based approval requirements:
- **LOW risk**: Supervised execution, no approval needed
- **MEDIUM risk**: Approval-gated, review before execution
- **HIGH risk**: Monitored execution, requires explicit approval
- **CRITICAL risk**: Zero-touch only with full human oversight

### Attack Surface Analysis

For every application, document:

1. **Entry points**: APIs, web forms, file uploads, webhooks, message queues
2. **Trust boundaries**: Internal vs external networks, user vs admin, service-to-service
3. **Data flows**: Where sensitive data enters, is processed, stored, and transmitted
4. **Dependencies**: Third-party libraries, external services, shared infrastructure

## OWASP Top 10 Protection

### A01: Broken Access Control

```python
from functools import wraps
from flask import g, request, jsonify

def require_permission(permission):
    """Decorator to check user permissions."""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not g.current_user:
                return jsonify({'error': 'Authentication required'}), 401
            if not g.current_user.has_permission(permission):
                logger.warning(
                    f"Unauthorized access attempt: {g.current_user.id} "
                    f"to {request.path}"
                )
                return jsonify({'error': 'Permission denied'}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/api/orders/<order_id>')
@login_required
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    # Verify user owns this order or is admin
    if order.user_id != g.current_user.id and not g.current_user.is_admin:
        logger.warning(
            f"Unauthorized order access: User {g.current_user.id} "
            f"attempted to access order {order_id}"
        )
        return jsonify({'error': 'Access denied'}), 403
    return jsonify(order.to_dict())
```

### A02: Cryptographic Failures

- Use HTTPS/TLS for all communications
- Encrypt sensitive data with AES-256-GCM at rest
- Use strong password hashing (bcrypt, Argon2)
- Implement key rotation with a 30-day cycle
- Store encryption keys in HSM or KMS, never in code

### A03: Injection

```python
from sqlalchemy import text

# ALWAYS use parameterized queries
sql = text("SELECT id, username, email FROM users WHERE username LIKE :query")
users = db.engine.execute(sql, {'query': f'%{query}%'}).fetchall()

# Or use ORM (automatically parameterized)
users = User.query.filter(User.username.like(f'%{query}%')).all()
```

Input validation rules:
- Validate all user input against allowlists
- Sanitize input before use in any context (SQL, HTML, OS commands, LDAP)
- Limit input length and size
- Validate file uploads by type, size, and content (magic bytes)
- Escape output for the rendering context (HTML, JavaScript, URL, CSS)

### A04: Insecure Design

- Apply threat modeling during design phase (STRIDE, PASTA)
- Implement defense in depth with multiple security layers
- Use secure design patterns (fail-safe defaults, complete mediation)
- Define security requirements alongside functional requirements

### A05: Security Misconfiguration

Common misconfigurations to check:
- Default credentials still active
- Unnecessary features or services enabled
- Error messages that leak internal details
- Missing security headers (CSP, HSTS, X-Frame-Options)
- Overly permissive CORS configuration
- Debug mode enabled in production
- Directory listing enabled on web servers

### A06-A10: Additional OWASP Categories

| Category | Key Mitigation |
|----------|---------------|
| A06: Vulnerable Components | Automated dependency scanning with Dependabot/Snyk, regular updates |
| A07: Auth Failures | MFA, strong password policies, account lockout, session timeout |
| A08: Software/Data Integrity | Code signing, SBOM generation, SLSA compliance, verified artifacts |
| A09: Logging Failures | Centralized logging, audit trails, tamper-proof log storage |
| A10: SSRF | URL allowlists, disable redirects, network segmentation |

## Zero Trust Architecture

### Core Principles

1. **Never trust, always verify** - Authenticate and authorize every request
2. **Least privilege access** - Grant minimum permissions needed for each operation
3. **Assume breach** - Design systems to limit blast radius when compromise occurs
4. **Continuous verification** - Validate identity and posture continuously, not just at login

### Implementation Patterns

```python
# Trust ladder for progressive agent autonomy
# Reference: proagent-repo/core/skills/tac/trust-ladder.md
class TrustLevel(Enum):
    SUPERVISED = 1      # Human reviews every action
    APPROVAL_GATED = 2  # Human approves before execution
    MONITORED = 3       # Autonomous with real-time monitoring
    AUTONOMOUS = 4      # Full autonomy with periodic audits
    ZERO_TOUCH = 5      # Complete trust with compliance guardrails
```

### Trust Assessment Engine

Automated trust level assessment based on task risk (reference: `proagent-repo/core/zte/trust_assessor.py`):

- Evaluate task keywords against risk dictionaries (delete, deploy, migrate, credential, etc.)
- Score task complexity using architecture, integration, and scope indicators
- Assign trust level dynamically based on combined risk and complexity score
- Enforce approval gates when trust level exceeds the agent's current authorization

### Agent Sandboxing and Hardening

Production security for autonomous agents (reference: `casdk-harness/src/harness/security.py`, `casdk-harness/docs/HARDENING.md`):

- Sandbox agent execution with restricted filesystem, network, and process access
- Enforce permission boundaries: agents cannot escalate beyond their assigned trust level
- Isolate agent sessions to prevent cross-contamination between tasks
- Implement resource limits (CPU, memory, execution time) for agent processes
- Audit all agent actions with immutable logging for post-incident analysis

Access control enforcement:
- Identity-based access with strong authentication (OAuth 2.0/OIDC, WebAuthn, FIDO2)
- Context-aware policies (device posture, location, time, risk score)
- Micro-segmentation for network access
- Just-in-time and just-enough-access for privileged operations
- Continuous session validation with re-authentication triggers

## Compliance Frameworks

### GDPR Compliance Checklist

- [ ] Data Processing Agreements (DPA) with all processors
- [ ] Privacy by design implemented in all new features
- [ ] Data Subject Access Requests (DSAR) process documented
- [ ] Right to erasure implemented with cascading deletion
- [ ] Data retention policies defined and automated
- [ ] Consent management system operational
- [ ] Data Protection Impact Assessment (DPIA) for high-risk processing
- [ ] Breach notification procedure within 72 hours

### SOC 2 Type II Controls

- [ ] Access controls with RBAC and MFA enforcement
- [ ] Change management with approval workflows
- [ ] Incident response plan tested quarterly
- [ ] Vulnerability management with SLA-based remediation
- [ ] Encryption for data at rest and in transit
- [ ] Audit logging with tamper-proof storage
- [ ] Business continuity and disaster recovery plans tested

### PCI-DSS Requirements

- [ ] Cardholder data environment (CDE) scoped and segmented
- [ ] Encryption of cardholder data in transit and at rest
- [ ] Access to CDE restricted and logged
- [ ] Regular vulnerability scanning and penetration testing
- [ ] Security event monitoring and alerting

## Encryption and Data Protection

### TLS Configuration

```nginx
# Recommended TLS configuration
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
ssl_prefer_server_ciphers off;
ssl_session_timeout 1d;
ssl_session_cache shared:SSL:10m;
ssl_stapling on;
ssl_stapling_verify on;
```

### Security Headers

```
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 0
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

### Password Hashing

```python
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):
    validate_password_strength(password)
    password_hash = generate_password_hash(
        password,
        method='pbkdf2:sha256',
        salt_length=16
    )
    user = User(username=username, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()
```

Password policy:
- Minimum 12 characters
- Must include uppercase, lowercase, number, and special character
- Account lockout after 5 failed attempts for 30 minutes
- No password reuse for last 12 passwords

## Rate Limiting and DoS Protection

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["1000 per day", "100 per hour"],
    storage_uri="redis://localhost:6379"
)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    # Authentication logic

@app.route('/api/search')
@limiter.limit("30 per minute")
def search():
    # Search logic
```

## Security Audit Logging

### What to Log

- Authentication attempts (success and failure)
- Authorization failures and privilege escalation attempts
- Data access to sensitive resources
- Configuration changes to security controls
- API key creation, rotation, and revocation
- User account lifecycle events (creation, modification, deletion)
- File upload and download of sensitive data

### Log Format

```json
{
  "timestamp": "2025-12-09T14:32:01Z",
  "level": "SECURITY",
  "event": "AUTH_FAILURE",
  "actor": "user@example.com",
  "action": "login",
  "resource": "/api/auth/login",
  "outcome": "failure",
  "reason": "invalid_password",
  "ip": "192.168.1.100",
  "user_agent": "Mozilla/5.0...",
  "metadata": {
    "failed_attempts": 3,
    "account_locked": false
  }
}
```

## Risk Classification for Code Changes

Automated risk scoring for pull requests and code changes (reference: `Auto-Claude/apps/backend/analysis/risk_classifier.py`, `Auto-Claude/apps/backend/analysis/security_scanner.py`):

- Classify code changes by risk level (LOW, MEDIUM, HIGH, CRITICAL) based on files modified, keywords present, and scope of change
- Flag changes touching authentication, authorization, encryption, or database schema as elevated risk
- Integrate security scanner module for automated vulnerability detection on changed files
- Generate risk reports that feed into approval workflows and deployment gates

## Security Audit Workflow Formulas

Structured audit workflows using formula-based automation (reference: `gastown/.beads/formulas/security-audit.formula.toml`):

- Define repeatable security audit steps as workflow formulas
- Chain scanning, analysis, and reporting steps into automated audit pipelines
- Track audit findings across iterations with status tracking (open, in-progress, mitigated, accepted)
- Generate compliance evidence artifacts from audit runs

## Security Checklist

- [ ] Use HTTPS for all communications
- [ ] Hash passwords with bcrypt/Argon2
- [ ] Use parameterized queries for all database operations
- [ ] Validate and sanitize all input
- [ ] Implement proper authentication with MFA
- [ ] Implement proper authorization with RBAC
- [ ] Use CSRF tokens for state-changing operations
- [ ] Set secure cookie flags (HttpOnly, Secure, SameSite)
- [ ] Implement rate limiting on sensitive endpoints
- [ ] Keep dependencies updated with automated scanning
- [ ] Use environment variables for secrets
- [ ] Implement security event logging and monitoring
- [ ] Configure security headers (CSP, HSTS, X-Frame-Options)
- [ ] Sanitize error messages to prevent information leakage
- [ ] Implement account lockout after failed attempts
- [ ] Validate file uploads by type, size, and content
- [ ] Use Content Security Policy to prevent XSS
- [ ] Implement proper session management with timeouts

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate interactive diagrams directly in the conversation. Describe what you need in natural language and Excalidraw renders it as an interactive canvas with hand-drawn style.

### When to Use

- Threat model diagrams (STRIDE, attack trees)
- Network security zone and Zero Trust architecture maps
- Compliance workflow and audit trail flows
- Incident response runbook visualizations

### Workflow

1. Describe the diagram you need — be specific about components, relationships, and layout
2. Review the rendered interactive diagram in the chat
3. Request refinements by describing what to change (add/remove/rearrange elements)
4. Use fullscreen mode for detailed editing when needed

### Tips for Effective Diagrams

- Name specific components and their connections (e.g., "API Gateway connects to Auth Service and User Service")
- Specify layout direction when it matters (e.g., "left-to-right flow" or "top-down hierarchy")
- Request specific diagram types (architecture diagram, flowchart, sequence diagram, ER diagram)
- Iterate — start with the overall structure, then refine details
