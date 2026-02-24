## LLM Application Development

### RAG System Architecture

Build Retrieval-Augmented Generation systems with document loading, chunking, embedding, vector storage, and retrieval-augmented prompting:

```python
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Load and chunk documents
loader = DirectoryLoader('./docs', glob="**/*.md")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ". ", " "]
)
chunks = splitter.split_documents(documents)

# Create embeddings and vector store
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")

# Build retrieval chain
retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 5})
llm = ChatOpenAI(model="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

result = qa_chain.invoke({"query": "What are the best practices for model deployment?"})
```

### Prompt Engineering Patterns

- **System Prompt Design:** Define clear role, constraints, output format, and examples
- **Few-Shot Prompting:** Provide 2-5 representative examples for consistent output
- **Chain-of-Thought:** Ask the model to reason step-by-step for complex tasks
- **Output Structuring:** Use JSON mode or Pydantic models for structured outputs
- **Guardrails:** Implement input validation, output filtering, and fallback responses

### Embedding Generation

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

texts = ["Machine learning model training", "Deep neural network architecture"]
embeddings = model.encode(texts, normalize_embeddings=True)

# Compute similarity
similarity = np.dot(embeddings[0], embeddings[1])
```

## Knowledge Graph Integration (Graphiti)

Build structured knowledge graphs for enhanced context retrieval in AI applications. Based on patterns from `Auto-Claude/apps/backend/context/graphiti_integration.py`:

```python
from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType

# Initialize Graphiti knowledge graph
graphiti = Graphiti(
    neo4j_uri="bolt://localhost:7687",
    neo4j_user="neo4j",
    neo4j_password="password"
)

# Add episodes (knowledge units) to the graph
await graphiti.add_episode(
    name="model-deployment-guide",
    episode_body="SageMaker endpoints require inference.py with model_fn, input_fn, predict_fn, output_fn handlers.",
    source=EpisodeType.text,
    source_description="ML deployment documentation"
)

# Search the knowledge graph for relevant context
results = await graphiti.search("How to deploy models to SageMaker?")
for result in results:
    print(f"Fact: {result.fact}")
    print(f"Source: {result.episodes}")
```

### When to Use Knowledge Graphs

- Accumulating structured domain knowledge across multiple ML projects
- Building context-aware AI assistants that learn from project history
- Connecting related concepts across experiments, models, and deployments
- Providing grounded, traceable context to LLM applications (alternative or complement to RAG)

## Meta-Prompting Frameworks

Design and generate meta-prompts that define AI agent roles, capabilities, and behavioral constraints. Based on patterns from `proagent-repo/core/meta_prompts/base.py` and `taches-cc-resources/skills/create-meta-prompts/SKILL.md`:

### Meta-Prompt Structure

```python
# Base meta-prompt template with role knowledge injection
meta_prompt = {
    "role_definition": "You are a senior ML engineer specializing in...",
    "domain_knowledge": [
        "Training pipeline design patterns",
        "Feature engineering best practices",
        "Model evaluation methodologies"
    ],
    "behavioral_constraints": [
        "Always set random seeds for reproducibility",
        "Never fit preprocessors on test data",
        "Log all experiments to tracking server"
    ],
    "output_format": "structured JSON with rationale",
    "examples": [
        {"input": "...", "output": "...", "reasoning": "..."}
    ]
}
```

### Meta-Prompt Creation Workflow

1. Define the target role and domain scope
2. Collect domain knowledge from reference materials and codebase patterns
3. Specify behavioral constraints and guardrails
4. Provide few-shot examples that demonstrate expected behavior
5. Validate the meta-prompt against test scenarios
6. Iterate based on output quality and adherence to constraints

## LLM Judge Evaluation

Evaluate AI-generated outputs programmatically using LLM-as-judge patterns. Based on `ralph-orchestrator/tools/e2e/helpers/llm_judge.py`:

```python
from anthropic import Anthropic

client = Anthropic()

def llm_judge_evaluate(output: str, criteria: list[str], reference: str = None) -> dict:
    """Evaluate AI output using an LLM judge with specified criteria."""
    judge_prompt = f"""Evaluate the following AI-generated output against these criteria:

Criteria:
{chr(10).join(f'- {c}' for c in criteria)}

Output to evaluate:
{output}

{"Reference answer: " + reference if reference else ""}

For each criterion, provide:
1. Score (1-5)
2. Brief justification

Then provide an overall score and summary."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": judge_prompt}]
    )
    return {"evaluation": response.content[0].text}

# Usage for ML model explanations
result = llm_judge_evaluate(
    output=model_explanation,
    criteria=[
        "Technical accuracy of ML concepts",
        "Clarity of explanation for non-technical audience",
        "Completeness of feature importance discussion",
        "Actionable recommendations provided"
    ]
)
```

### LLM Judge Use Cases in ML/AI

- Evaluating model documentation quality and completeness
- Assessing generated code for ML best practice adherence
- Comparing RAG system response quality across configurations
- Validating prompt engineering outputs against acceptance criteria
- A/B testing LLM application responses with automated scoring

## AWS Bedrock Integration

Access foundation models through AWS Bedrock alongside SageMaker for managed inference. Based on patterns from `Auto-Claude/apps/backend/integrations/graphiti/providers_pkg/llm_providers/anthropic_llm.py` and `provectus-marketplace/plugins/proagent-aws-ai/skills/aws-ai-assistant/SKILL.md`:

```python
import boto3
import json

bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

def invoke_bedrock_model(prompt: str, model_id: str = "anthropic.claude-3-sonnet-20240229-v1:0"):
    """Invoke a foundation model via AWS Bedrock."""
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": prompt}]
    })
    response = bedrock_runtime.invoke_model(
        modelId=model_id,
        body=body,
        contentType="application/json",
        accept="application/json"
    )
    result = json.loads(response["body"].read())
    return result["content"][0]["text"]

# Use Bedrock for ML tasks: data analysis, feature suggestions, code generation
analysis = invoke_bedrock_model(
    "Analyze this feature correlation matrix and suggest feature engineering steps: ..."
)
```

### Bedrock vs SageMaker Decision Guide

| Use Case | Bedrock | SageMaker |
|---|---|---|
| Foundation model inference (text, vision) | Preferred | Not applicable |
| Custom model training | Not applicable | Preferred |
| Custom model hosting | Not applicable | Preferred |
| RAG with knowledge bases | Bedrock Knowledge Bases | Custom RAG pipeline |
| Fine-tuning foundation models | Bedrock custom models | SageMaker JumpStart |
| Real-time custom ML inference | Not applicable | SageMaker Endpoints |

## LangSmith Agent Debugging

Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. Requires `langsmith-fetch` (`pip install langsmith-fetch`) with `LANGSMITH_API_KEY` and `LANGSMITH_PROJECT` environment variables configured. Key commands: `langsmith-fetch --last 5`, `langsmith-fetch --errors-only`, `langsmith-fetch --trace-id <id> --verbose`.
