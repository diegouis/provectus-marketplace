# Provectus AWS AI Practice Plugin

This plugin provides the AWS AI practice context for the Provectus agentic coding platform. It equips Claude with production-tested patterns for designing, building, and deploying AI solutions on Amazon Web Services — from Bedrock agents and MCP servers to full generative AI architectures following AWS Well-Architected best practices.

## Practice Scope

The AWS AI practice covers seven operational domains:

1. **Amazon Bedrock AgentCore** - Building, deploying, and operating AI agents at scale using AgentCore Runtime, Gateway, Identity, Memory, Code Interpreter, Browser, Observability, Policy, and Evaluations — with any framework (CrewAI, LangGraph, LlamaIndex, Google ADK, OpenAI Agents SDK) and any model
2. **MCP Server Development on AWS** - Creating and deploying Model Context Protocol servers using AWS official MCP servers (CDK, Documentation, API, Knowledge, Pricing, Cost Analysis, Bedrock KB Retrieval, Nova Canvas, Lambda Tool, Terraform), deploying custom MCP servers on ECS/EKS with OAuth 2.0 and WAF protection
3. **Amazon Bedrock Knowledge Bases** - RAG system design with multimodal retrieval, S3 Vectors for cost-optimized vector storage, semantic/hierarchical/fixed-size chunking, structured data retrieval, and enterprise governance
4. **Generative AI Architecture** - AWS Well-Architected Generative AI Lens across six lifecycle phases (scoping, model selection, customization, development, deployment, continuous improvement), agentic AI patterns, responsible AI practices
5. **AI Infrastructure as Code** - AWS CDK Generative AI Constructs, CloudFormation templates for AgentCore, Terraform modules, Fullstack AgentCore Solution Template (FAST), and the IaC MCP Server for AI-powered CDK/CloudFormation assistance
6. **AWS AI/ML Service Integration** - SageMaker (training, endpoints, pipelines), Bedrock (model access, guardrails, fine-tuning), Comprehend, Rekognition, Textract, Polly, Transcribe, Lex, Kendra, Amazon Q, and Nova models
7. **Production AI Operations** - AgentCore Observability with CloudWatch and OpenTelemetry, agent quality evaluations (13 pre-built evaluators), Cedar-based policy controls, VPC/PrivateLink security, episodic memory for agent learning, and A2A protocol for multi-agent collaboration

## Key Conventions

When performing AWS AI tasks, follow these standards:

### Architecture Design
- Always start with the AWS Well-Architected Generative AI Lens six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, sustainability
- Follow the generative AI lifecycle: scoping, model selection, customization, development, deployment, continuous improvement
- Design for multi-region availability where AgentCore is supported (us-east-1, us-east-2, us-west-2, ap-south-1, ap-southeast-1, ap-southeast-2, ap-northeast-1, eu-central-1, eu-west-1)
- Use Amazon S3 Vectors for cost-optimized vector storage (up to 90% savings vs traditional vector databases)

### Security
- Enable VPC and PrivateLink for all AgentCore services in production
- Use AgentCore Identity with OAuth-enabled identity-aware authorization
- Implement AgentCore Policy with Cedar language for deterministic access controls
- Separate IAM roles: inference roles vs content ingestion roles to limit blast radius
- Store refresh tokens in AgentCore Identity secure vault
- Apply Bedrock Guardrails for content filtering and responsible AI

### Agent Development
- Use AgentCore Gateway to transform existing APIs and Lambda functions into agent-compatible tools
- Leverage AgentCore Code Interpreter for secure, isolated code execution
- Implement AgentCore Memory (episodic) for agents that learn from user interactions
- Connect to MCP servers through AgentCore Gateway for third-party integrations
- Use AgentCore Evaluations (13 pre-built evaluators) to monitor correctness, safety, and tool selection accuracy
- Deploy with AgentCore Runtime for 8-hour execution windows and session isolation

### Infrastructure as Code
- Use AWS CDK Generative AI Constructs for high-level, Well-Architected patterns
- Define AgentCore resources with CloudFormation or CDK (Runtime, Gateway, Memory, Code Interpreter)
- Tag all AI resources for cost tracking and governance
- Use the IaC MCP Server for AI-powered CDK and CloudFormation template assistance
- Deploy with FAST (Fullstack AgentCore Solution Template) for rapid prototyping

### MCP Server Best Practices
- Use official AWS MCP servers from awslabs for AWS service integrations
- Deploy custom MCP servers on ECS/EKS with OAuth 2.0 authentication
- Protect MCP server endpoints with CloudFront and WAF
- Use stdio transport for local MCP servers, Streamable HTTP for remote
- Follow the MCP specification for tool definitions, resource exposure, and prompt templates

## MCP Integrations

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **AWS CDK**: AI-powered CDK and CloudFormation assistance via `awslabs.cdk-mcp-server`
- **AWS Documentation**: Search and retrieve AWS documentation via `awslabs.aws-documentation-mcp-server`
- **AWS Bedrock KB**: Retrieve from Bedrock Knowledge Bases via `awslabs.bedrock-kb-retrieval-mcp-server`
- **AWS Cost Analysis**: Analyze AWS costs and usage via `awslabs.cost-analysis-mcp-server`

## Source Repositories

This plugin draws patterns from: AWS documentation (Bedrock AgentCore, Well-Architected Generative AI Lens, CDK Constructs), awslabs/mcp (official AWS MCP servers), AWS architecture blogs (generative AI patterns, agentic AI), and AWS prescriptive guidance (serverless agentic AI, IaC patterns).

## Plugin Structure

```
proagent-aws-ai/
  .claude-plugin/plugin.json
  skills/
    aws-ai-assistant/SKILL.md
  commands/proagent-aws-ai-hub.md
  commands/proagent-aws-ai-run.md
  commands/proagent-aws-ai-review.md
  agents/aws-ai-specialist.md
  hooks/hooks.json
  .mcp.json
  CLAUDE.md
  README.md
```
