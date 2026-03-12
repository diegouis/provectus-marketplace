# XSS Scan — Frontend XSS Vulnerability Scan

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
