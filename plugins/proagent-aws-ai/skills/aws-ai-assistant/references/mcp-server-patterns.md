# MCP Server Development on AWS

## Official AWS MCP Servers

AWS provides official MCP servers via the `awslabs` organization:

| Server | Package | Purpose |
|--------|---------|---------|
| CDK | `awslabs.cdk-mcp-server` | CDK and CloudFormation assistance |
| Documentation | `awslabs.aws-documentation-mcp-server` | AWS documentation search |
| API | `awslabs.aws-api-mcp-server` | Execute AWS API calls via natural language |
| Knowledge | `awslabs.aws-knowledge-mcp-server` | AWS knowledge and regional availability |
| Pricing | `awslabs.aws-pricing-mcp-server` | AWS pricing information |
| Bedrock KB | `awslabs.bedrock-kb-retrieval-mcp-server` | Knowledge Base retrieval |
| Cost Analysis | `awslabs.cost-analysis-mcp-server` | Cost and usage analysis |
| Nova Canvas | `awslabs.nova-canvas-mcp-server` | Image generation with Nova |
| Lambda Tool | `awslabs.lambda-tool-mcp-server` | Expose Lambda as MCP tools |
| Terraform | `awslabs.terraform-mcp-server` | Terraform assistance |
| Core | `awslabs.core-mcp-server` | Core AWS MCP utilities |

## Installing AWS MCP Servers

```json
{
  "mcpServers": {
    "aws-cdk": {
      "command": "uvx",
      "args": ["awslabs.cdk-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    },
    "aws-docs": {
      "command": "uvx",
      "args": ["awslabs.aws-documentation-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    },
    "bedrock-kb": {
      "command": "uvx",
      "args": ["awslabs.bedrock-kb-retrieval-mcp-server@latest"],
      "env": {
        "KNOWLEDGE_BASE_ID": "your-kb-id",
        "AWS_REGION": "us-east-1",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

## Building a Custom MCP Server

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";
import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3";

const server = new McpServer({
  name: "my-aws-ai-server",
  version: "1.0.0",
});

const bedrockClient = new BedrockRuntimeClient({ region: "us-east-1" });
const s3Client = new S3Client({ region: "us-east-1" });

// Tool: Invoke a Bedrock model
server.tool(
  "invoke-model",
  "Invoke an Amazon Bedrock foundation model with a prompt",
  {
    prompt: { type: "string", description: "The prompt to send to the model" },
    modelId: { type: "string", description: "Bedrock model ID (e.g., anthropic.claude-sonnet-4-5-20250929-v1:0)" },
  },
  async ({ prompt, modelId }) => {
    const command = new InvokeModelCommand({
      modelId,
      contentType: "application/json",
      body: JSON.stringify({
        anthropic_version: "bedrock-2023-05-31",
        messages: [{ role: "user", content: prompt }],
        max_tokens: 1024,
      }),
    });
    const response = await bedrockClient.send(command);
    const result = JSON.parse(new TextDecoder().decode(response.body));
    return {
      content: [{ type: "text", text: result.content[0].text }],
    };
  }
);

// Resource: Expose S3 documents
server.resource(
  "s3-document",
  "s3://{bucket}/{key}",
  async (uri) => {
    const [bucket, ...keyParts] = uri.replace("s3://", "").split("/");
    const key = keyParts.join("/");
    const command = new GetObjectCommand({ Bucket: bucket, Key: key });
    const response = await s3Client.send(command);
    const content = await response.Body.transformToString();
    return {
      contents: [{ uri, mimeType: "text/plain", text: content }],
    };
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Deploying MCP Servers on AWS

Architecture for secure remote MCP server deployment:

```
User/Agent -> CloudFront (CDN + DDoS) -> WAF (Request filtering)
    -> ALB (Load balancing) -> ECS Fargate (MCP Server containers)
    -> OAuth 2.0 Provider (Cognito) for authentication
    -> VPC Private Subnets for network isolation
```

CDK deployment pattern:

```typescript
import * as cdk from 'aws-cdk-lib';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as elbv2 from 'aws-cdk-lib/aws-elasticloadbalancingv2';
import * as wafv2 from 'aws-cdk-lib/aws-wafv2';

export class McpServerStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string) {
    super(scope, id);

    const vpc = new ec2.Vpc(this, 'McpVpc', { maxAzs: 2 });
    const cluster = new ecs.Cluster(this, 'McpCluster', { vpc });

    const taskDef = new ecs.FargateTaskDefinition(this, 'McpTask', {
      memoryLimitMiB: 512,
      cpu: 256,
    });

    taskDef.addContainer('mcp-server', {
      image: ecs.ContainerImage.fromAsset('./mcp-server'),
      portMappings: [{ containerPort: 3000 }],
      logging: ecs.LogDrivers.awsLogs({ streamPrefix: 'mcp-server' }),
      healthCheck: {
        command: ['CMD-SHELL', 'curl -f http://localhost:3000/health || exit 1'],
        interval: cdk.Duration.seconds(30),
      },
    });

    const service = new ecs.FargateService(this, 'McpService', {
      cluster,
      taskDefinition: taskDef,
      desiredCount: 2,
      assignPublicIp: false,
    });

    const alb = new elbv2.ApplicationLoadBalancer(this, 'McpAlb', {
      vpc,
      internetFacing: true,
    });

    const listener = alb.addListener('McpListener', { port: 443 });
    listener.addTargets('McpTarget', {
      port: 3000,
      targets: [service],
      healthCheck: { path: '/health' },
    });
  }
}
```
