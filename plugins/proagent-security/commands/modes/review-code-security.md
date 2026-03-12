# Review: Code Security

Check for these vulnerability patterns:

## Injection Flaws
- SQL string concatenation or interpolation instead of parameterized queries
- Command injection via `os.system()`, `subprocess.call(shell=True)`, `exec()`, `eval()`
- Template injection in Jinja2, Handlebars, or other template engines
- LDAP injection in directory service queries
- XPath injection in XML processing
- Log injection through unsanitized user input in log statements

## Authentication and Session Management
- Plaintext password storage or weak hashing (MD5, SHA1 without salt)
- Missing MFA on sensitive operations
- Session tokens in URLs or predictable session IDs
- Missing session timeout or absolute session lifetime
- Password reset tokens without expiration
- Missing account lockout after failed login attempts
- Credential comparison vulnerable to timing attacks

## Authorization
- Missing permission checks on API endpoints
- Insecure Direct Object Reference (IDOR) vulnerabilities
- Missing ownership validation on resource access
- Client-side only authorization checks
- Role hierarchy bypass opportunities
- Missing authorization on file upload/download endpoints

## Cross-Site Scripting (XSS)
- Use of `innerHTML`, `dangerouslySetInnerHTML`, `v-html` without sanitization
- Unescaped output in templates
- Missing Content Security Policy headers
- Reflected input in error messages or search results

## Cross-Site Request Forgery (CSRF)
- Missing CSRF tokens on state-changing forms
- CSRF tokens in GET requests (should be POST/PUT/DELETE only)
- Missing SameSite cookie attribute
- CORS misconfiguration allowing unauthorized origins
