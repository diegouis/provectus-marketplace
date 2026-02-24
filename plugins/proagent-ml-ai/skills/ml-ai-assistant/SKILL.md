---
name: ml-ai-assistant
description: Building ML & AI Systems - model training, inference optimization, MLOps pipelines, experiment tracking, prompt engineering, embeddings, vector stores, LLM application development, RAG systems, knowledge graph integration (Graphiti), meta-prompting frameworks, LLM judge evaluation, and AWS AI services (SageMaker, Bedrock). Use when performing any machine learning, deep learning, or AI engineering task.
---

# Building ML & AI Systems

Comprehensive ML and AI skill covering model training, evaluation, deployment, monitoring, LLM application development, RAG systems, and knowledge graph integration.

## When to Use This Skill

- Training and evaluating machine learning models (classification, regression, ranking)
- Engineering features and tuning hyperparameters
- Tracking experiments with MLflow or Weights & Biases
- Deploying models via REST APIs, SageMaker, or Bedrock
- Building LLM-powered applications with RAG and prompt engineering
- Creating embeddings and managing vector stores
- Monitoring model performance and detecting data drift
- Building knowledge graphs with Graphiti
- Evaluating AI outputs using LLM judge patterns
- Designing ML pipeline validation workflows

## Reference Routing

> **CONTEXT GUARD**: Load reference files only when the user's request matches a specific topic below. Do NOT load all references upfront.

| User Intent | Reference File |
|---|---|
| Model training, data splitting, scikit-learn, TensorFlow, XGBoost, feature engineering | `references/training-patterns.md` |
| Model evaluation, metrics, classification report, MLflow, W&B, experiment tracking | `references/evaluation-tracking.md` |
| Model deployment, FastAPI serving, SageMaker, batch prediction, data drift monitoring | `references/deployment-patterns.md` |
| RAG systems, prompt engineering, embeddings, vector stores, Graphiti, LLM judge, Bedrock, LangSmith | `references/llm-patterns.md` |
| ML pipeline validation, project structure, common pitfalls, validation gates | `references/pipeline-workflows.md` |

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate ML pipeline diagrams, RAG topology maps, experiment DAGs, and model deployment architecture visualizations. Describe what you need in natural language.
