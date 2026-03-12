# Encrypt Setup — Configure Encryption

Set up encryption for data protection.

**Steps:**
1. **Assess current encryption posture:**
   - Check TLS configuration on web servers and load balancers
   - Verify database encryption at rest settings
   - Check application-level encryption for sensitive fields
   - Verify secrets management approach (environment variables, vault, KMS)
   - Check certificate management and expiration dates
2. **Configure transport layer security:**
   - Generate or validate TLS certificate configuration
   - Recommend TLS 1.2+ with strong cipher suites
   - Configure HSTS headers with preload
   - Set up certificate auto-renewal with Let's Encrypt or ACM
   - Verify certificate chain completeness
3. **Configure data-at-rest encryption:**
   - Recommend AES-256-GCM for application-level encryption
   - Configure database encryption (RDS encryption, MongoDB encryption at rest)
   - Set up file system encryption for sensitive data directories
   - Implement field-level encryption for PII columns
   - Configure backup encryption
4. **Set up key management:**
   - Recommend KMS (AWS KMS, GCP Cloud KMS, Azure Key Vault)
   - Define key rotation schedule (30-day for data keys, 90-day for master keys)
   - Implement envelope encryption pattern
   - Configure key access policies with least privilege
   - Set up key usage audit logging
5. **Configure password hashing:**
   - Implement bcrypt or Argon2id for user passwords
   - Set appropriate cost factors (bcrypt rounds >= 12, Argon2 with recommended parameters)
   - Implement password strength validation (minimum 12 characters, complexity requirements)
   - Set up account lockout after failed attempts
6. **Generate encryption configuration report:**
   - Current vs recommended encryption posture
   - Configuration files generated or modified
   - Key management setup instructions
   - Testing procedures to verify encryption is active
   - Ongoing monitoring recommendations
