# Epic Categories Reference

Standard epic taxonomy for organizing ROM features. Use as defaults but create custom epics when the project domain demands it.

## Standard Epics

### 1. Team Onboarding & Planning
**When to use:** Project kickoff activities, team setup, story refinement.

Sub-categories:
- Team member onboarding and role assignment
- Tool access provisioning (GitHub, AWS, Jira, etc.)
- User story refinement and effort agreement
- Sprint backlog creation and timeline planning
- Kickoff workshops and alignment sessions

### 2. Infrastructure & Foundation
**When to use:** Cloud setup, networking, CI/CD, IaC, secrets, monitoring.

Sub-categories:
- Cloud account setup (AWS, GCP, Azure)
- Networking (VPC, subnets, security groups, load balancers)
- IAM roles and policies
- CI/CD pipelines (build, test, deploy stages)
- Feature flags and config management
- Cost monitoring, budgets, alerts
- Secret management
- IaC templates (Terraform, CloudFormation, CDK)
- Cross-account/cross-region setup

### 3. Data Infrastructure
**When to use:** Databases, data pipelines, data quality, compliance, storage.

Sub-categories:
- Database design and schema (relational, NoSQL, vector)
- Data source connectors (ERP, bank, SaaS APIs)
- ETL/ELT pipelines
- Data quality dimensions and validation
- Data lineage tracking
- Data versioning and retention
- Compliance alignment (GLBA, CCPA, GDPR)
- Feedback storage and centralization
- Data classification

### 4. Application Backend
**When to use:** API endpoints, business logic, server-side features.

Sub-categories:
- RESTful/GraphQL API endpoints
- Business logic and domain services
- RBAC and authorization
- Lifecycle tracking (opportunity, order, etc.)
- Dashboard and analytics endpoints
- Notification rules and logic
- Session management
- Webhook receivers

### 5. Application Frontend
**When to use:** UI components, responsive design, client-side features.

Sub-categories:
- Responsive page layouts
- Form components and wizards
- Data tables and list views
- Dashboard visualizations (charts, graphs)
- Role-based navigation and guards
- Search and filter interfaces
- Feedback mechanisms (in-app)
- Onboarding flows
- Accessibility compliance

### 6. AI/ML Platform
**When to use:** Machine learning models, NLP, agents, scoring, RAG.

Sub-categories:
- Model integration and inference
- Agent orchestration (LangGraph, state machines)
- Decision engines and matching algorithms
- RAG pipelines (embeddings, vector store, retrieval)
- Metadata extraction (LLM-based)
- Semantic search
- Text-to-SQL
- Scoring logic and use-case structures
- Prompt management (registry, versioning, guardrails)
- AI assistant / copilot features
- ML experiment tracking and back-testing
- Evaluation datasets and baselines

### 7. Integration
**When to use:** External APIs, third-party services, webhooks, auth flows.

Sub-categories:
- External API connectors
- Webhook handlers (send and receive)
- OAuth/SSO integration
- Vendor onboarding workflows
- Data sync between systems
- Message queue integration

### 8. Security & Compliance
**When to use:** Auth hardening, audit, compliance frameworks, encryption.

Sub-categories:
- Multi-factor authentication
- Audit logging
- Vulnerability management
- Incident-response procedures
- Privacy notices (GLBA, GDPR)
- SOC 2 / ISO 27001 controls
- Data classification
- Encryption at rest and in transit
- Prompt injection prevention

### 9. Testing & QA
**When to use:** Test suites, evaluation datasets, UAT, security testing.

Sub-categories:
- Unit testing
- Integration testing
- End-to-end testing
- Security testing (OWASP, injection)
- Prompt injection testing
- Performance/load testing
- Evaluation dataset creation
- User acceptance testing (UAT)
- Post-migration smoke tests

### 10. Deployment & Operations
**When to use:** Migration, go-live, operational handover.

Sub-categories:
- Cloud account migration
- Blue-green / canary deployments
- Performance validation
- Contingency planning
- Runbook creation
- Go-live checklist execution
- Knowledge transfer

### 11. Observability
**When to use:** Monitoring, logging, metrics, alerting, dashboards.

Sub-categories:
- Application monitoring
- Infrastructure monitoring
- Custom metrics and KPIs
- Alerting rules and escalation
- Log aggregation and search
- Operational dashboards
- Cost tracking dashboards

---

## Custom Epic Guidelines

Create custom epics when:
- A domain concept has 5+ features that don't fit standard categories
- The project has a unique technical pillar (e.g., "Prompt Management", "Vendor Matching")
- Stakeholders use domain-specific groupings

**Naming convention:** Use title case, 2-4 words, describe the capability (not the technology).

Good: "Vendor Matching Engine", "Prompt Management", "CFO Assistant"
Bad: "LangChain Stuff", "Misc Backend", "Other"
