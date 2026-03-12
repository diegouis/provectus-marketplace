# Compliance Check — Validate Compliance

Assess the project against a specified compliance framework.

**Steps:**
1. **Identify the target framework** (ask user if not specified):
   - GDPR (data privacy and protection)
   - SOC 2 Type II (security, availability, confidentiality)
   - PCI-DSS (payment card data security)
   - HIPAA (health information privacy)
   - ISO 27001 (information security management)
   - NIST Cybersecurity Framework
2. **Scan for framework-specific controls:**
   - **GDPR**: Check for consent management, data retention policies, DSAR handling, encryption of PII, privacy by design patterns, breach notification procedures
   - **SOC 2**: Check for access controls (RBAC, MFA), change management (PR reviews, approval gates), audit logging, vulnerability scanning integration, incident response procedures
   - **PCI-DSS**: Check for CDE segmentation, cardholder data encryption, access logging, vulnerability scanning cadence, penetration testing evidence
   - **HIPAA**: Check for PHI encryption, access controls, audit trails, BAA documentation, workforce training evidence
   - **ISO 27001**: Check for ISMS documentation, risk assessment, control objectives, internal audit evidence
3. **Check technical controls:**
   - Authentication strength (password policy, MFA, session management)
   - Authorization model (RBAC, least privilege, separation of duties)
   - Encryption (at rest, in transit, key management)
   - Logging and monitoring (audit trails, alerting, retention)
   - Vulnerability management (scanning frequency, remediation SLAs)
   - Incident response (documented procedures, communication plan, testing cadence)
4. **Generate compliance report:**
   - Control-by-control assessment with PASS, PARTIAL, FAIL, or NOT APPLICABLE status
   - Evidence references for passing controls
   - Gap analysis with specific remediation steps for failing controls
   - Estimated effort to achieve full compliance
   - Priority ranking of gaps by regulatory risk
