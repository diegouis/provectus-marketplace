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
