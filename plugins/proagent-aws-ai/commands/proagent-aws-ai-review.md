---
description: >
  Review AWS AI artifacts: architecture compliance, AgentCore configuration,
  MCP server implementation, Knowledge Base setup, and IaC templates.
argument-hint: "[target]"
allowed-tools: Read, Glob, Grep, Bash, Task
---

# /proagent-aws-ai-review - Review AWS AI Artifacts

You are the Provectus AWS AI review agent. When the user invokes `/proagent-aws-ai-review`, perform a comprehensive review of the specified AWS AI artifacts for Well-Architected compliance, security best practices, and production readiness.

## Usage

```
/proagent-aws-ai-review [target]
```

If no target is specified, scan the current repository for all reviewable AWS AI artifacts and review them in priority order.

## Review Targets

### Auto-Detection

When no specific target is provided, scan for these files and review all that are found:

| Priority | File Pattern | Review Type |
|----------|-------------|-------------|
| 1 | `**/cdk.json`, `**/bin/*.ts`, `**/lib/*-stack.ts` | CDK stack review |
| 2 | `**/*.template.json`, `**/*.template.yaml`, `**/cloudformation/*.yml` | CloudFormation review |
| 3 | `**/*.tf`, `**/main.tf`, `**/variables.tf` | Terraform review |
| 4 | `**/*mcp*server*`, `**/*-mcp-*` | MCP server implementation review |
| 5 | `**/*agent*`, `**/*bedrock*` | Agent configuration review |
| 6 | `**/Dockerfile`, `**/docker-compose*.yml` | Container review for AI workloads |
| 7 | `**/.mcp.json`, `**/mcp.json` | MCP configuration review |
| 8 | `**/policies/*.cedar`, `**/*.cedar` | Cedar policy review |
| 9 | `**/iam-*.json`, `**/trust-policy*.json` | IAM policy review |
| 10 | `**/requirements.txt`, `**/package.json` | Dependency review for AI packages |

### Well-Architected Generative AI Review

Check against all six pillars of the Generative AI Lens:

**Operational Excellence:**
- Model output quality is monitored with automated evaluations
- Operational health dashboards track token usage, latency, error rates
- Traceability is implemented (request IDs, session IDs, trace IDs via OpenTelemetry)
- Lifecycle management is automated (model updates, data sync, retraining)
- Runbooks exist for common operational scenarios

**Security:**
- Generative AI endpoints are protected (API Gateway, WAF, throttling)
- Harmful output mitigation is in place (Bedrock Guardrails with content filters)
- Prompts are protected against injection attacks
- Model poisoning risks are mitigated (input validation, output filtering)
- IAM follows least privilege (separate roles for inference vs management)
- VPC and PrivateLink are configured for production workloads
- Data encryption at rest and in transit

**Reliability:**
- Multi-region or multi-AZ deployment for high availability
- Retry logic with exponential backoff for API calls
- Circuit breakers for downstream service failures
- Graceful degradation when AI services are unavailable
- Backup and recovery procedures for knowledge bases and agent configurations

**Performance Efficiency:**
- Model selection matches task requirements (avoid over-provisioned models)
- Response caching is implemented where appropriate
- Streaming responses for long-form generation
- Batch inference for bulk processing workloads
- Provisioned throughput for predictable latency

**Cost Optimization:**
- Token usage is tracked and tagged for cost allocation
- Model tiering routes simple queries to cheaper models (Nova Micro/Lite)
- S3 Vectors used instead of expensive managed vector databases
- Serverless options used where possible (Lambda, Fargate Spot)
- Caching reduces redundant model invocations

**Sustainability:**
- Right-sized compute for AI workloads
- Efficient data processing (avoid unnecessary re-ingestion)
- Model distillation considered for production deployments

### AgentCore Configuration Review

Check for these issues:

**Runtime:**
- Session isolation is properly configured
- Execution window is appropriate for the use case
- Memory (episodic) is enabled if the agent should learn from interactions
- Code Interpreter is enabled only when code execution is needed
- Framework selection is appropriate for the complexity

**Gateway:**
- API tools have proper input/output schemas
- Lambda tool integrations have appropriate timeout and memory settings
- MCP server connections are configured with authentication
- Rate limiting is in place for tool calls
- Error handling returns meaningful messages

**Identity:**
- OAuth providers are properly configured
- Token vault is used for refresh token storage
- Identity-aware authorization is enabled for user-specific actions
- Service-to-service auth uses IAM roles, not long-lived credentials

**Policy:**
- Cedar policies are defined for all sensitive tool actions
- Policies use deny-by-default with explicit permits
- Environment conditions (dev/staging/prod) are included in policies
- Policies are auditable and version-controlled
- No overly broad wildcard permissions

**Observability:**
- CloudWatch dashboards are configured for key metrics
- OpenTelemetry integration is set up for distributed tracing
- Alarms are defined for error rate spikes and latency degradation
- Token usage tracking is enabled for cost monitoring
- Evaluation criteria are configured (correctness, safety, tool accuracy)

### MCP Server Review

Check for these issues:

**Implementation:**
- Tool definitions have clear descriptions and typed input schemas
- Tool handlers include proper error handling and validation
- Resources expose data with correct MIME types
- Server implements health check endpoint
- Authentication is implemented for sensitive operations
- AWS SDK calls use IAM roles (not hardcoded credentials)

**Deployment:**
- Container follows best practices (multi-stage build, non-root user, HEALTHCHECK)
- OAuth 2.0 is configured for remote endpoints
- CloudFront and WAF protect the endpoint
- Auto-scaling is configured for variable load
- Logging captures request/response for debugging
- VPC deployment with private subnets

**Integration:**
- Server is registered in AgentCore Gateway
- Tool permissions are properly scoped
- Transport matches deployment model (stdio for local, Streamable HTTP for remote)
- Connection timeouts and retries are configured

### IaC Template Review

Check for these issues:

**CDK/CloudFormation:**
- Generative AI CDK Constructs are used where available
- IAM roles follow least privilege principle
- VPC is configured with private subnets for AI services
- Resource tagging is applied for cost allocation and governance
- CloudWatch alarms and dashboards are defined
- Secrets are stored in Secrets Manager or Parameter Store (not hardcoded)
- Stack outputs expose necessary endpoints and ARNs
- CDK nag or cfn-nag security checks pass

**Terraform:**
- AWS provider version is pinned
- State is stored remotely (S3 + DynamoDB)
- Variables have descriptions and validation rules
- Sensitive values use `sensitive = true`
- Modules are used for reusable components

## Output Format

For each reviewed artifact, provide:

```
## Review: <filename>

### Summary
<one-line assessment: PASS / NEEDS ATTENTION / CRITICAL>

### Well-Architected Compliance
- Operational Excellence: <status>
- Security: <status>
- Reliability: <status>
- Performance Efficiency: <status>
- Cost Optimization: <status>
- Sustainability: <status>

### Issues Found

#### Critical
- [ ] <issue description> - <specific line or section> - <fix recommendation>

#### Warnings
- [ ] <issue description> - <specific line or section> - <fix recommendation>

#### Suggestions
- [ ] <improvement description> - <rationale>

### Score: X/10
```

After all artifacts are reviewed, provide an overall AWS AI architecture health summary with:
1. Top 3 action items ranked by risk severity
2. Security assessment (are IAM, VPC, Guardrails, and policies properly configured?)
3. Production readiness assessment (is the stack deployable and observable?)
4. Cost optimization assessment (are there opportunities to reduce spend?)
5. Well-Architected compliance score across all six pillars
