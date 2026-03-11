# Amazon Bedrock AgentCore

## AgentCore Architecture Overview

Amazon Bedrock AgentCore is the agentic platform for building, deploying, and operating AI agents at scale. It provides nine integrated services:

| Service | Purpose |
|---------|---------|
| **Runtime** | Execute agents with 8-hour windows, session isolation, A2A protocol |
| **Gateway** | Transform APIs/Lambda into agent tools, connect MCP servers |
| **Identity** | OAuth authorization, identity-aware access, secure token vault |
| **Memory** | Episodic memory for agent learning across interactions |
| **Code Interpreter** | Secure, isolated code execution environments |
| **Browser** | Web interaction capabilities at scale |
| **Observability** | CloudWatch dashboards, OpenTelemetry, metrics tracking |
| **Policy** | Cedar-based deterministic access controls |
| **Evaluations** | 13 pre-built evaluators for quality monitoring |

## Building an Agent with AgentCore

```python
import boto3
import json

bedrock_agent = boto3.client('bedrock-agent')

# Create an agent
response = bedrock_agent.create_agent(
    agentName='customer-support-agent',
    description='AI agent for customer support with tool access',
    foundationModel='anthropic.claude-sonnet-4-5-20250929-v1:0',
    instruction="""You are a customer support agent. Help users with their inquiries
    by searching the knowledge base and taking actions through available tools.
    Always verify user identity before making account changes.
    Be concise, helpful, and professional.""",
    idleSessionTTLInSeconds=1800,
)

agent_id = response['agent']['agentId']

# Create an action group (tools)
bedrock_agent.create_agent_action_group(
    agentId=agent_id,
    agentVersion='DRAFT',
    actionGroupName='customer-tools',
    actionGroupExecutor={'lambda': 'arn:aws:lambda:us-east-1:123456789:function:customer-tools'},
    apiSchema={
        'payload': json.dumps({
            'openapi': '3.0.0',
            'paths': {
                '/lookup-order': {
                    'post': {
                        'summary': 'Look up customer order by order ID',
                        'operationId': 'lookupOrder',
                        'parameters': [
                            {'name': 'orderId', 'in': 'query', 'required': True, 'schema': {'type': 'string'}}
                        ]
                    }
                }
            }
        })
    }
)
```

## AgentCore Policy with Cedar

Define deterministic access controls using the Cedar policy language:

```cedar
// Allow the agent to read customer data
permit(
    principal == Agent::"customer-support-agent",
    action == Action::"invoke-tool",
    resource == Tool::"lookup-order"
) when {
    context.userAuthenticated == true
};

// Block the agent from deleting data
forbid(
    principal == Agent::"customer-support-agent",
    action == Action::"invoke-tool",
    resource == Tool::"delete-account"
);

// Allow refunds only up to $100
permit(
    principal == Agent::"customer-support-agent",
    action == Action::"invoke-tool",
    resource == Tool::"process-refund"
) when {
    context.refundAmount <= 100
};
```

## AgentCore Evaluations

Monitor agent quality with 13 pre-built evaluators:

```python
# Configure evaluations for an agent
evaluation_config = {
    'evaluators': [
        {'type': 'CORRECTNESS', 'weight': 0.3},
        {'type': 'HELPFULNESS', 'weight': 0.2},
        {'type': 'SAFETY', 'weight': 0.2},
        {'type': 'TOOL_SELECTION_ACCURACY', 'weight': 0.15},
        {'type': 'TOOL_PARAMETER_ACCURACY', 'weight': 0.1},
        {'type': 'GOAL_SUCCESS_RATE', 'weight': 0.05},
    ],
    'schedule': 'CONTINUOUS',
    'alertThreshold': 0.7,
}
```
