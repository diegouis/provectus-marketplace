# Amazon Bedrock Knowledge Bases

## RAG Architecture with S3 Vectors

```
Documents (S3) -> Data Ingestion Pipeline -> Chunking Strategy
    -> Embedding Model (Titan Embeddings) -> S3 Vectors (storage)
    -> Retrieval API -> Agent/Application -> Response with citations
```

## Setting Up a Knowledge Base with CDK

```typescript
import * as bedrock from '@cdklabs/generative-ai-cdk-constructs/lib/cdk-lib/bedrock';

const kb = new bedrock.KnowledgeBase(this, 'KnowledgeBase', {
  embeddingsModel: bedrock.BedrockFoundationModel.TITAN_EMBED_TEXT_V2_1024,
  instruction: 'Use this knowledge base to answer questions about our products and documentation.',
});

const dataSource = new bedrock.S3DataSource(this, 'DataSource', {
  bucket: documentsBucket,
  knowledgeBase: kb,
  chunkingStrategy: bedrock.ChunkingStrategy.SEMANTIC,
});
```

## Chunking Strategy Selection Guide

| Strategy | Best For | Chunk Size | Overlap |
|----------|----------|------------|---------|
| **Semantic** | Mixed content types, varied document lengths | Auto-determined | Semantic boundaries |
| **Hierarchical** | Structured documents (manuals, wikis) | Parent: 1500, Child: 300 | Section boundaries |
| **Fixed-Size** | Uniform documents, simple setup | 1000 tokens | 200 tokens |
| **Custom Lambda** | Domain-specific splitting requirements | Custom | Custom |

## Vector Storage Selection Guide

| Storage | Cost | Scale | Best For |
|---------|------|-------|----------|
| **S3 Vectors** | Lowest (90% savings) | Trillions of vectors | Cost-optimized production |
| **OpenSearch Serverless** | Medium | Millions | Hybrid text + vector search |
| **Aurora pgvector** | Medium | Millions | Existing PostgreSQL users |
| **Pinecone** | Higher | Billions | Managed, metadata filtering |
| **Redis Enterprise** | Higher | Millions | Ultra-low latency |
