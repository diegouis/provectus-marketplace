# Review: Access Control

Assess the access control implementation:

## Authentication
- Authentication mechanism strength (OAuth 2.0, OIDC, API keys, basic auth)
- Password policy enforcement (length, complexity, history, expiration)
- Multi-factor authentication availability and enforcement
- Service-to-service authentication (mTLS, JWT, API keys with rotation)
- Session management (secure cookies, HttpOnly, Secure, SameSite flags)

## Authorization
- RBAC implementation completeness
- Least-privilege enforcement across roles
- Separation of duties for sensitive operations
- API endpoint authorization coverage (every endpoint has access control)
- Admin interface protection (separate network, additional auth factors)
- File and resource access control validation

## Identity Management
- User provisioning and deprovisioning processes
- Service account management and credential rotation
- API key lifecycle management (creation, rotation, revocation)
- Third-party integration access scope minimization
