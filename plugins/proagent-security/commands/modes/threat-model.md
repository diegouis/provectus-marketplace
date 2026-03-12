# Threat Model — Generate Threat Model

Create a structured threat model for the application.

**Steps:**
1. **Map the application architecture:**
   - Identify services, databases, message queues, and external APIs from code and configuration
   - Detect network boundaries from Docker Compose networks, Kubernetes namespaces, or cloud VPC config
   - Identify data stores and classify the sensitivity of data they contain
   - Map authentication and authorization mechanisms in use
2. **Identify entry points and trust boundaries:**
   - Public-facing API endpoints and web routes
   - WebSocket connections and real-time communication channels
   - File upload and download endpoints
   - Webhook receivers and callback URLs
   - Background job queues and scheduled tasks
   - Administrative interfaces and management APIs
3. **Apply STRIDE threat analysis:**
   - For each entry point and data flow, evaluate all six STRIDE categories
   - Use the trust assessment engine pattern: classify risk as LOW, MEDIUM, HIGH, or CRITICAL
   - Map threats to specific code locations where possible
   - Assess complexity using indicators: architecture, integration, migration, redesign
4. **Prioritize threats:**
   - Score by likelihood and impact
   - Reference CVSS scoring where applicable
   - Identify quick wins (low effort, high impact mitigations)
   - Flag any critical threats that require immediate attention
5. **Generate threat model document:**
   - Architecture diagram with trust boundaries marked
   - Threat catalog with STRIDE classification, risk score, and status
   - Prioritized mitigation plan with specific implementation guidance
   - Attack tree for the highest-risk threat scenarios
   - Residual risk assessment after mitigations
