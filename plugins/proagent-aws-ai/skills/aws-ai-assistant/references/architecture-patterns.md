# Architecture Patterns, Service Selection, and Common Pitfalls

## Generative AI Architecture Patterns

### Pattern 1: Conversational AI Agent

```
User -> API Gateway -> Lambda (auth) -> Bedrock Agent
    -> AgentCore Runtime (session, memory)
    -> AgentCore Gateway (tools: Lambda, APIs, MCP servers)
    -> Bedrock Knowledge Base (RAG for context)
    -> Bedrock Guardrails (safety, PII)
    -> Response with citations
```

### Pattern 2: Multi-Agent Orchestration

```
User Request -> Supervisor Agent (routing, planning)
    -> Specialist Agent 1 (e.g., research) via A2A protocol
    -> Specialist Agent 2 (e.g., analysis) via A2A protocol
    -> Specialist Agent 3 (e.g., writing) via A2A protocol
    -> Supervisor Agent (aggregation, quality check)
    -> Response
```

### Pattern 3: Enterprise Knowledge Copilot

```
Enterprise Data Sources -> S3 (documents, wikis, tickets)
    -> Bedrock Knowledge Base (multimodal, S3 Vectors)
    -> Bedrock Agent with Guardrails
    -> Cognito Authentication
    -> React Frontend (FAST template)
    -> CloudWatch Observability
```

### Pattern 4: Content Generation Pipeline

```
Request -> API Gateway -> Step Functions (orchestration)
    -> Bedrock (text generation, Claude/Nova)
    -> Bedrock (image generation, Nova Canvas)
    -> S3 (output storage)
    -> SNS (notification)
    -> CloudWatch (monitoring)
```

## AWS AI Service Selection Guide

| Use Case | Primary Service | Supporting Services |
|----------|----------------|-------------------|
| Conversational agents | Bedrock AgentCore | Knowledge Bases, Guardrails |
| Document Q&A (RAG) | Bedrock Knowledge Bases | S3 Vectors, Bedrock Models |
| Text generation | Bedrock (Claude/Nova) | Guardrails, CloudWatch |
| Image generation | Bedrock (Nova Canvas) | S3, CloudFront |
| Speech-to-text | Amazon Transcribe | S3, Comprehend |
| Text-to-speech | Amazon Polly | S3, CloudFront |
| Document processing | Amazon Textract | Comprehend, S3 |
| Sentiment analysis | Amazon Comprehend | S3, QuickSight |
| Image/video analysis | Amazon Rekognition | S3, Lambda |
| Enterprise search | Amazon Kendra | S3, RDS, SharePoint |
| Code assistance | Amazon Q Developer | CodeWhisperer |
| Custom ML models | Amazon SageMaker | S3, ECR, CloudWatch |
| ML model serving | SageMaker Endpoints | Auto Scaling, CloudWatch |

## Model Selection Guide

| Model | Strengths | Latency | Cost | Best For |
|-------|-----------|---------|------|----------|
| **Claude Sonnet** | Complex reasoning, coding, analysis | Medium | Medium | General-purpose, coding |
| **Claude Haiku** | Fast, efficient, accurate | Low | Low | High-volume, simple tasks |
| **Nova Pro** | Balanced, multimodal | Medium | Medium | General-purpose |
| **Nova Lite** | Fast, cost-effective | Low | Low | Simple tasks, high volume |
| **Nova Micro** | Text-only, fastest | Lowest | Lowest | Classification, routing |
| **Llama 3** | Open source, customizable | Medium | Medium | Fine-tuning, self-hosting |
| **Mistral** | Multilingual, efficient | Low | Low | Code, multilingual tasks |

## Common Pitfalls

1. **No Guardrails** — Deploying agents without Bedrock Guardrails for content safety and PII protection
2. **Overly permissive IAM** — Using broad `bedrock:*` permissions instead of specific actions and resources
3. **No observability** — Running agents without AgentCore Observability or CloudWatch monitoring
4. **Expensive vector storage** — Using managed vector databases when S3 Vectors offers 90% savings
5. **Missing Cedar policies** — Deploying agents without deterministic access controls via AgentCore Policy
6. **ClickOps infrastructure** — Creating resources manually instead of using CDK/CloudFormation/Terraform
7. **Single-region deployment** — Not planning for multi-region availability in production
8. **No evaluation** — Deploying agents without continuous quality evaluation via AgentCore Evaluations
9. **Wrong model for the task** — Using expensive models (Claude Opus) for simple tasks that Nova Micro can handle
10. **Unprotected MCP servers** — Deploying remote MCP servers without OAuth 2.0, WAF, or VPC isolation
