# AI Infrastructure as Code

## CDK Generative AI Constructs

```typescript
import { bedrock, opensearchserverless } from '@cdklabs/generative-ai-cdk-constructs';

// RAG with OpenSearch Serverless
const vectorStore = new opensearchserverless.VectorCollection(this, 'VectorStore');

const kb = new bedrock.KnowledgeBase(this, 'KB', {
  embeddingsModel: bedrock.BedrockFoundationModel.TITAN_EMBED_TEXT_V2_1024,
  vectorStore: vectorStore,
});

// Agent with knowledge base
const agent = new bedrock.Agent(this, 'Agent', {
  foundationModel: bedrock.BedrockFoundationModel.ANTHROPIC_CLAUDE_SONNET_V1,
  instruction: 'You are a helpful assistant that answers questions using the knowledge base.',
  knowledgeBases: [kb],
});

// Guardrails
const guardrail = new bedrock.Guardrail(this, 'Guardrail', {
  name: 'content-safety',
  blockedInputMessaging: 'I cannot process this request.',
  blockedOutputsMessaging: 'I cannot provide this response.',
  contentFilters: [
    {
      type: bedrock.ContentFilterType.SEXUAL,
      inputStrength: bedrock.FilterStrength.HIGH,
      outputStrength: bedrock.FilterStrength.HIGH,
    },
    {
      type: bedrock.ContentFilterType.HATE,
      inputStrength: bedrock.FilterStrength.HIGH,
      outputStrength: bedrock.FilterStrength.HIGH,
    },
  ],
});
```

## CloudFormation for AgentCore

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Bedrock AgentCore AI Stack

Resources:
  AgentRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Principal:
              Service: bedrock.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: BedrockInvoke
          PolicyDocument:
            Statement:
              - Effect: Allow
                Action:
                  - bedrock:InvokeModel
                Resource: !Sub arn:aws:bedrock:${AWS::Region}::foundation-model/*

  Agent:
    Type: AWS::Bedrock::Agent
    Properties:
      AgentName: my-ai-agent
      FoundationModel: anthropic.claude-sonnet-4-5-20250929-v1:0
      Instruction: |
        You are a helpful AI assistant. Use the available tools
        and knowledge base to answer user questions accurately.
      AgentResourceRoleArn: !GetAtt AgentRole.Arn
      IdleSessionTTLInSeconds: 1800

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

Outputs:
  AgentId:
    Value: !GetAtt Agent.AgentId
  KnowledgeBaseId:
    Value: !GetAtt KnowledgeBase.KnowledgeBaseId
```
