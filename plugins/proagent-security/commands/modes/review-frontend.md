# Review: Frontend Security

Check for XSS and CSRF vulnerabilities (reference: `agents/plugins/frontend-mobile-security/commands/xss-scan.md`, `agents/plugins/frontend-mobile-security/agents/frontend-security-coder.md`):

- `innerHTML`, `dangerouslySetInnerHTML`, `v-html` usage without DOMPurify or equivalent sanitization
- `eval()`, `Function()`, `document.write()` with user-controlled input
- Missing or misconfigured Content Security Policy (allows `unsafe-inline`, `unsafe-eval`)
- CSRF tokens missing on forms with state-changing actions
- Missing SameSite cookie attributes on session cookies
- CORS configuration allowing wildcard or untrusted origins
- Reflected user input in error messages, search results, or URL parameters
