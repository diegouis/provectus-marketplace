---
description: >
  Execute AWS AI operations: build-agent, create-mcp-server, setup-knowledge-base,
  design-architecture, or deploy-infrastructure.
argument-hint: "<operation> [options]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /proagent-aws-ai-run - Execute AWS AI Operations

You are the Provectus AWS AI execution agent. When the user invokes `/proagent-aws-ai-run`, parse the operation argument and execute the corresponding workflow.

## Usage

```
/proagent-aws-ai-run <operation> [options]
```

## Operations

### `build-agent` - Build and Deploy an AI Agent with Bedrock AgentCore

Create a production-ready AI agent using Amazon Bedrock AgentCore with proper security, observability, and governance.

**Steps:**
1. **Define the agent scope:**
   - Clarify the agent's purpose, tools it needs access to, and target users
   - Determine the framework: native AgentCore, CrewAI, LangGraph, LlamaIndex, or OpenAI Agents SDK
   - Select the foundation model: Claude (Anthropic), Nova (Amazon), Llama (Meta), Mistral
   - Identify required integrations: APIs, databases, third-party services, MCP servers

2. **Configure AgentCore Runtime:**
   - Set up the agent runtime with session isolation and execution window (up to 8 hours)
   - Define the agent's system prompt and behavioral instructions
   - Configure memory settings (episodic memory for learning from interactions)
   - Set up Code Interpreter if the agent needs to execute code
   - Enable Browser capability if the agent needs web interaction
   - Generate CDK/CloudFormation template for Runtime resources

3. **Set up AgentCore Gateway:**
   - Transform existing APIs into agent-compatible tools via Gateway
   - Convert Lambda functions into agent tools with proper input/output schemas
   - Connect to MCP servers for third-party integrations (Jira, Asana, Zendesk)
   - Define tool schemas with descriptions, parameters, and return types
   - Configure rate limiting and error handling for tool calls

4. **Implement security:**
   - Configure AgentCore Identity with OAuth-enabled authorization
   - Set up secure vault storage for refresh tokens
   - Define Cedar policies for deterministic access controls:
     ```cedar
     permit(
       principal == Agent::"my-agent",
       action == Action::"invoke-tool",
       resource == Tool::"read-database"
     ) when {
       context.environment == "production"
     };
     ```
   - Configure VPC and PrivateLink for network isolation
   - Set up Bedrock Guardrails for content filtering and PII redaction
   - Apply IAM roles with least privilege

5. **Configure observability:**
   - Set up AgentCore Observability dashboards in CloudWatch
   - Configure OpenTelemetry integration for custom metrics
   - Track token usage, latency, session duration, and error rates
   - Set up AgentCore Evaluations with relevant evaluators:
     - Correctness, helpfulness, safety
     - Tool selection accuracy, tool parameter accuracy
     - Goal success rate
   - Configure CloudWatch alarms for anomaly detection

6. **Deploy and validate:**
   - Deploy using CDK/CloudFormation with proper resource tagging
   - Run smoke tests against the deployed agent
   - Validate Cedar policies block unauthorized actions
   - Verify observability dashboards show expected metrics
   - Document the agent: purpose, tools, policies, runbook

### `create-mcp-server` - Create and Deploy a Custom MCP Server on AWS

Build a Model Context Protocol server and deploy it to AWS infrastructure.

**Steps:**
1. **Design the MCP server:**
   - Define the tools the server will expose (name, description, input schema, handler)
   - Define resources the server will provide (URIs, MIME types, content)
   - Define prompt templates if applicable
   - Choose the implementation language: TypeScript (recommended) or Python
   - Determine transport: stdio (local development) or Streamable HTTP (remote deployment)

2. **Implement the server:**
   - Scaffold the MCP server project:
     ```typescript
     import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
     import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

     const server = new McpServer({
       name: "my-aws-mcp-server",
       version: "1.0.0",
     });

     server.tool("tool-name", "Tool description", {
       param1: { type: "string", description: "Parameter description" }
     }, async ({ param1 }) => {
       // Tool implementation
       return { content: [{ type: "text", text: "Result" }] };
     });

     const transport = new StdioServerTransport();
     await server.connect(transport);
     ```
   - Implement tool handlers with proper error handling and validation
   - Add resource handlers for data exposure
   - Implement authentication if accessing AWS services (use AWS SDK with IAM roles)
   - Write unit tests for all tool handlers

3. **Containerize for deployment:**
   - Create a Dockerfile with multi-stage build:
     ```dockerfile
     FROM node:20-slim AS builder
     WORKDIR /app
     COPY package*.json ./
     RUN npm ci --production
     COPY . .
     RUN npm run build

     FROM node:20-slim
     WORKDIR /app
     COPY --from=builder /app/dist ./dist
     COPY --from=builder /app/node_modules ./node_modules
     EXPOSE 3000
     HEALTHCHECK --interval=30s CMD curl -f http://localhost:3000/health || exit 1
     CMD ["node", "dist/index.js"]
     ```
   - Configure environment variables for AWS credentials and configuration
   - Test the container locally

4. **Deploy to AWS:**
   - Push container image to Amazon ECR
   - Deploy on ECS Fargate or EKS with auto-scaling
   - Configure OAuth 2.0 authentication for the MCP endpoint
   - Set up CloudFront distribution for CDN and DDoS protection
   - Apply WAF rules for request filtering and rate limiting
   - Configure VPC with private subnets for the server
   - Generate CDK template:
     ```typescript
     const cluster = new ecs.Cluster(this, 'McpCluster', { vpc });
     const taskDef = new ecs.FargateTaskDefinition(this, 'McpTask');
     taskDef.addContainer('mcp-server', {
       image: ecs.ContainerImage.fromEcrRepository(repo),
       portMappings: [{ containerPort: 3000 }],
       logging: ecs.LogDrivers.awsLogs({ streamPrefix: 'mcp' }),
     });
     const service = new ecs.FargateService(this, 'McpService', {
       cluster, taskDefinition: taskDef, desiredCount: 2,
     });
     ```

5. **Register with AgentCore Gateway:**
   - Register the MCP server URL with AgentCore Gateway
   - Configure tool access permissions
   - Test tool invocation through an AgentCore agent
   - Set up monitoring for MCP server health and latency

### `setup-knowledge-base` - Set Up a Bedrock Knowledge Base with RAG

Create a fully configured Amazon Bedrock Knowledge Base for Retrieval-Augmented Generation.

**Steps:**
1. **Assess data sources:**
   - Identify document types: PDF, HTML, Markdown, Word, images, audio, video
   - Estimate total data volume and update frequency
   - Determine retrieval requirements: text-only or multimodal
   - Identify structured vs unstructured data needs

2. **Configure data ingestion:**
   - Set up S3 bucket for source documents with versioning and encryption
   - Choose chunking strategy:
     - **Semantic chunking** — Groups text by semantic meaning (best for varied content)
     - **Hierarchical chunking** — Parent-child relationships (best for structured docs)
     - **Fixed-size chunking** — Consistent chunk sizes (simplest, good default: 1000 tokens, 200 overlap)
     - **Custom Lambda chunking** — Write custom logic for domain-specific splitting
   - Configure metadata extraction and enrichment
   - Set up data sync schedule (on-demand, periodic, or event-driven)

3. **Select vector storage:**
   - **Amazon S3 Vectors** (recommended) — Up to 90% cost savings, trillions of vectors, sub-second latency
   - **Amazon OpenSearch Serverless** — Full-text + vector hybrid search
   - **Aurora PostgreSQL pgvector** — Use existing PostgreSQL infrastructure
   - **Pinecone** — Managed vector database with metadata filtering
   - **Redis Enterprise** — Low-latency vector search with caching
   - Configure embedding model: Amazon Titan Embeddings, Cohere Embed

4. **Create the Knowledge Base:**
   - Define via CloudFormation/CDK:
     ```yaml
     KnowledgeBase:
       Type: AWS::Bedrock::KnowledgeBase
       Properties:
         Name: my-knowledge-base
         RoleArn: !GetAtt KBRole.Arn
         KnowledgeBaseConfiguration:
           Type: VECTOR
           VectorKnowledgeBaseConfiguration:
             EmbeddingModelArn: !Sub arn:aws:bedrock:${AWS::Region}::foundation-model/amazon.titan-embed-text-v2:0
         StorageConfiguration:
           Type: S3_VECTORS
           S3VectorsConfiguration:
             BucketArn: !GetAtt VectorBucket.Arn
     ```
   - Configure IAM roles with separation of concerns (ingestion vs inference)
   - Set up data source connection to S3
   - Run initial data sync and verify ingestion

5. **Integrate with agents:**
   - Associate the Knowledge Base with a Bedrock agent
   - Configure retrieval parameters (top-k, relevance threshold)
   - Set up source attribution in responses
   - Test retrieval quality with sample queries
   - Implement fallback behavior when no relevant documents are found

6. **Monitor and optimize:**
   - Track retrieval latency and relevance metrics
   - Monitor ingestion job status and failures
   - Set up alerts for data sync errors
   - Iterate on chunking strategy based on retrieval quality
   - A/B test different embedding models

### `design-architecture` - Design a Generative AI Architecture on AWS

Create a comprehensive AWS AI architecture following Well-Architected best practices.

**Steps:**
1. **Scope the use case:**
   - Clarify the AI application type: chatbot, agent, content generator, search, copilot, automation
   - Define success criteria: latency requirements, accuracy targets, cost budget
   - Identify compliance requirements: data residency, PII handling, audit logging
   - Determine scale: concurrent users, requests per second, data volume

2. **Select foundation model(s):**
   - Evaluate options based on task, quality, latency, and cost:
     - **Claude (Anthropic)** — Complex reasoning, coding, analysis, long context
     - **Nova Pro (Amazon)** — Balanced performance and cost for general tasks
     - **Nova Lite (Amazon)** — Fast, cost-effective for simpler tasks
     - **Nova Micro (Amazon)** — Text-only, lowest latency and cost
     - **Llama (Meta)** — Open source, customizable, self-hostable
     - **Mistral** — Efficient, multilingual, code generation
   - Consider multi-model strategies for different task types
   - Plan for model fallback and routing

3. **Design the architecture:**
   - Apply Well-Architected Generative AI Lens across all pillars:
     - **Operational Excellence** — Consistent output quality, monitoring, traceability, lifecycle automation
     - **Security** — Endpoint protection, harmful output mitigation, prompt security, model poisoning remediation
     - **Reliability** — Multi-region availability, retry logic, circuit breakers, graceful degradation
     - **Performance Efficiency** — Model selection optimization, caching, batching, streaming responses
     - **Cost Optimization** — Token usage tracking, model tiering, caching, provisioned throughput
     - **Sustainability** — Right-sized compute, efficient data processing, minimal waste
   - Design for agentic patterns if applicable:
     - Single agent with tools
     - Multi-agent orchestration with A2A protocol
     - Supervisor-worker hierarchies
     - Pipeline/sequential agent chains
   - Include: API Gateway, authentication (Cognito), agent runtime, knowledge bases, guardrails, monitoring

4. **Generate architecture diagram:**
   - Use Excalidraw to create an interactive architecture diagram
   - Include all AWS services, data flows, security boundaries, and monitoring points
   - Show the request flow from user through API Gateway to agent to tools and back
   - Annotate with IAM roles, VPC boundaries, and encryption points

5. **Document the architecture:**
   - Write Architecture Decision Records (ADRs) for key choices
   - Document scaling strategy and cost estimates
   - Create operational runbook: deployment, monitoring, incident response
   - Define SLOs: latency p50/p95/p99, availability, error rate

### `deploy-infrastructure` - Deploy AI Infrastructure with CDK/CloudFormation

Deploy a complete AI stack on AWS using Infrastructure as Code.

**Steps:**
1. **Choose the deployment approach:**
   - **FAST Template** — Fullstack AgentCore Solution Template for rapid prototyping (AgentCore + React + Cognito, all CDK)
   - **Custom CDK** — Build with AWS CDK Generative AI Constructs for custom architectures
   - **CloudFormation** — Direct CloudFormation templates for simpler deployments
   - **Terraform** — HCL modules for multi-cloud or Terraform-native teams

2. **Set up the CDK project:**
   - Initialize CDK app with TypeScript:
     ```bash
     npx cdk init app --language typescript
     npm install @cdklabs/generative-ai-cdk-constructs
     ```
   - Define stack structure: networking, compute, AI services, monitoring
   - Configure environment-specific settings (dev, staging, production)

3. **Define AI resources:**
   - Bedrock AgentCore: Runtime, Gateway, Memory, Code Interpreter
   - Bedrock Knowledge Base with vector store and data sources
   - IAM roles with least privilege for each service
   - VPC with private subnets, NAT gateways, and VPC endpoints
   - CloudWatch dashboards and alarms
   - Resource tags for cost allocation:
     ```typescript
     cdk.Tags.of(this).add('Project', 'ai-platform');
     cdk.Tags.of(this).add('Environment', props.environment);
     cdk.Tags.of(this).add('CostCenter', 'ai-team');
     ```

4. **Deploy and validate:**
   - Run `cdk synth` to generate CloudFormation template
   - Run `cdk diff` to review changes
   - Deploy with `cdk deploy --require-approval broadening`
   - Verify all resources are created and healthy
   - Run integration tests against deployed endpoints
   - Validate IAM permissions and VPC connectivity

5. **Set up CI/CD:**
   - Configure CDK Pipelines for automated deployment
   - Set up staging -> production promotion with manual approval
   - Add security scanning (cfn-nag, cdk-nag) to the pipeline
   - Configure rollback triggers on CloudWatch alarms

## Error Handling

If the requested operation is not recognized, display the list of available operations with descriptions and usage examples. If required context is missing (such as the use case, AWS region, or deployment target), ask the user for the missing information before proceeding.
