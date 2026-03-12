---
name: aws-ai-assistant
description: >
  Building AI Solutions on AWS - Bedrock AgentCore agents, MCP server development
  and deployment, Knowledge Bases RAG with S3 Vectors, generative AI architecture
  patterns, CDK/CloudFormation infrastructure, and AWS AI service integration. Use
  when designing, building, deploying, or reviewing any AI system on Amazon Web
  Services including chatbots, copilots, multi-agent orchestration, content
  generation pipelines, and enterprise knowledge systems. Do NOT use for general
  backend development (use backend-assistant), frontend work (use frontend-assistant),
  or non-AI AWS infrastructure.
---

# Building AI Solutions on AWS

Comprehensive AWS AI skill covering the full lifecycle of AI solution development on Amazon Web Services — from architecture design through agent building, MCP server creation, knowledge base setup, and production deployment.

## When to Use This Skill

- Designing AI architectures on AWS (chatbots, agents, copilots, content generators)
- Building AI agents with Amazon Bedrock AgentCore
- Creating and deploying Model Context Protocol (MCP) servers on AWS
- Setting up RAG systems with Amazon Bedrock Knowledge Bases
- Deploying AI infrastructure with CDK, CloudFormation, or Terraform
- Integrating AWS AI services (Bedrock, SageMaker, Comprehend, Rekognition, etc.)
- Reviewing AWS AI architectures for Well-Architected compliance
- Implementing responsible AI with Bedrock Guardrails
- Optimizing AI workload costs on AWS
- Selecting foundation models (Claude, Nova, Llama, Mistral) for specific use cases
- Configuring Cedar policies for agent access control
- Setting up agent evaluation and observability

## CRITICAL: Ask First, Load Later

**DO NOT** read reference files, run environment detection commands, or load
mode files until the user has told you what they want to do.

**When invoked without clear intent, use `AskUserQuestion`:**

```
AskUserQuestion(
  header: "AWS AI",
  question: "What AWS AI topic would you like help with?",
  options: [
    { label: "Bedrock AgentCore", description: "Build agents with AgentCore, Cedar policies, and evaluations" },
    { label: "MCP Servers on AWS", description: "Create and deploy Model Context Protocol servers on AWS" },
    { label: "RAG / Knowledge Bases", description: "RAG systems, Knowledge Bases, chunking, vector storage" },
    { label: "AI Architecture", description: "AI architecture design, service and model selection, Well-Architected" }
  ]
)
```

If the user selects "Other", offer CDK/IaC infrastructure for AI workloads.

## Reference Routing

> **CONTEXT GUARD**: Load reference files only when the user's request
> matches a specific topic below. Do NOT load all references upfront.

| User Intent | Reference File |
|---|---|
| Building agents with Bedrock AgentCore, Cedar policies, evaluations | `references/agentcore-patterns.md` |
| Creating or deploying MCP servers on AWS | `references/mcp-server-patterns.md` |
| RAG systems, Knowledge Bases, chunking, vector storage | `references/knowledge-bases-rag.md` |
| AI architecture design, service selection, model selection | `references/architecture-patterns.md` |
| CDK infrastructure, CloudFormation, IaC for AI workloads | `references/cdk-iac-patterns.md` |

## Core Principles

- Follow the AWS Well-Architected Generative AI Lens (six pillars)
- Use AgentCore for production agent deployments with session isolation
- Prefer S3 Vectors for cost-optimized vector storage (90% savings)
- Always apply Bedrock Guardrails and Cedar policies for safety
- Deploy infrastructure as code — never ClickOps

## Visual Diagramming

Use Excalidraw MCP for AWS AI architecture diagrams, agent flow diagrams, RAG pipeline topology, and multi-agent orchestration visualizations.

## Reference Assets

See [AWS Bedrock AgentCore Docs](docs.aws.amazon.com/bedrock-agentcore), [AWS MCP Servers](github.com/awslabs/mcp), [Gen AI CDK Constructs](awslabs.github.io/generative-ai-cdk-constructs), and the Well-Architected Generative AI Lens.
