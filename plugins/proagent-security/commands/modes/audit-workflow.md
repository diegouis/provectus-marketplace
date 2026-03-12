# Audit Workflow — Execute Security Audit Workflow

Run a structured security audit using formula-based workflows (reference: `gastown/.beads/formulas/security-audit.formula.toml`).

**Steps:**
1. **Select audit scope:**
   - Full application audit, infrastructure audit, compliance audit, or targeted component audit
   - Identify in-scope systems, repositories, and configurations
2. **Execute audit formula steps:**
   - Run vulnerability scanning (SAST, SCA, container scanning)
   - Run secrets audit (uses `security-scan` if available, falls back to manual patterns)
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
