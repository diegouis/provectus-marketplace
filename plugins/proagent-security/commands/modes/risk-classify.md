# Risk Classify — Classify Code Change Risk

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
