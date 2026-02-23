# proagent-aws-ai

Designing AI architectures on AWS — Bedrock AgentCore agents, MCP server development, Knowledge Bases RAG, generative AI architecture with Well-Architected best practices, CDK infrastructure, and AWS AI service integration.

## Installation

### Option 1: Copy to your project

```bash
cp -r proagent-aws-ai/ /path/to/your-project/.claude/plugins/proagent-aws-ai/
```

### Option 2: Reference from the marketplace

```json
{
  "plugins": ["proagent-aws-ai"]
}
```

### Option 3: Symlink for development

```bash
ln -s /path/to/provectus-marketplace/plugins/proagent-aws-ai /path/to/your-project/.claude/plugins/proagent-aws-ai
```

## Prerequisites

| Requirement | Purpose |
|-------------|---------|
| AWS CLI configured | Deploying infrastructure, managing services |
| Node.js + `npx` | Running MCP servers |
| AWS CDK (`npm install -g aws-cdk`) | Infrastructure as Code deployments |

## Usage

### Overview

```
/proagent-aws-ai-hub
```

Shows all capabilities, available commands, and quick-start routing across 7 operational domains.

### Execute workflows

```
/proagent-aws-ai-run <mode>
```

Available modes:
- `build-agent` — Create production AI agent with AgentCore (Runtime, Gateway, Identity, security, observability)
- `create-mcp-server` — Build and deploy custom MCP server on AWS (ECS/Fargate, OAuth 2.0)
- `setup-knowledge-base` — Create Bedrock Knowledge Base with RAG (S3 Vectors, chunking, ingestion)
- `design-architecture` — Create comprehensive AWS AI architecture with Well-Architected Lens
- `deploy-infrastructure` — Deploy AI stack with IaC (CDK, CloudFormation, Terraform, FAST template)

### Review AWS AI artifacts

```
/proagent-aws-ai-review [target]
```

Comprehensive review covering Well-Architected compliance (6 pillars), AgentCore configuration, MCP server implementation, IaC templates, security posture, and cost optimization.

## Component Inventory

| Component | Path | Purpose |
|-----------|------|---------|
| Plugin manifest | `.claude-plugin/plugin.json` | Name, version, description |
| MCP config | `.mcp.json` | Core MCP server configurations |
| Core skill | `skills/aws-ai-assistant/SKILL.md` | AWS AI patterns, AgentCore, MCP, Knowledge Bases |
| Hub command | `commands/proagent-aws-ai-hub.md` | Capabilities overview and routing |
| Run command | `commands/proagent-aws-ai-run.md` | Workflow execution (5 modes) |
| Review command | `commands/proagent-aws-ai-review.md` | Well-Architected review |
| Specialist agent | `agents/aws-ai-specialist.md` | Senior AWS AI architect subagent |
| Hooks | `hooks/hooks.json` | Destructive op detection, IaC validation |

## Version

- Plugin version: 0.2.0
- Category: aws-ai
- Author: Provectus
