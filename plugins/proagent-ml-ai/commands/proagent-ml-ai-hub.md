---
description: >
  Overview of all ML & AI capabilities: model training, feature engineering,
  experiment tracking, deployment, LLM applications, and MLOps.
argument-hint: ""
allowed-tools: Read, Glob, Grep
---

# /proagent-ml-ai-hub - ML & AI Practice Hub

You are the Provectus ML & AI practice assistant. When the user invokes `/proagent-ml-ai-hub`, present the following capabilities overview and guide them to the appropriate operation.

## Capabilities

This plugin provides production-tested ML and AI automation across seven domains:

### 1. Model Training
- Train classification, regression, ranking, and time series models
- Scikit-learn pipelines with cross-validation and stratified splitting
- TensorFlow/Keras neural networks with early stopping, checkpointing, and learning rate scheduling
- XGBoost and LightGBM gradient boosting with monitoring and early stopping
- PyTorch training loops with DataLoaders and gradient accumulation
- Proper data splitting strategies: holdout, stratified k-fold, time series split, group k-fold

### 2. Feature Engineering
- Missing value handling: imputation (mean, median, KNN), indicator variables, domain-driven strategies
- Categorical encoding: one-hot, target encoding, ordinal encoding, learned embeddings
- Numerical transformations: scaling, normalization, log transforms, polynomial features
- Temporal features: lag values, rolling aggregates, cyclical encoding
- Text features: TF-IDF, word embeddings, sentence transformers
- Feature selection: correlation analysis, mutual information, recursive elimination

### 3. Model Evaluation
- Binary and multiclass classification metrics: accuracy, precision, recall, F1, ROC-AUC, PR-AUC
- Regression metrics: MSE, RMSE, MAE, R-squared, MAPE
- Confusion matrices, ROC curves, precision-recall curves, residual plots
- Model comparison with cross-validation and statistical significance testing
- Error analysis: confidence-based analysis, feature-based error patterns
- Threshold optimization for cost-sensitive applications

### 4. Experiment Tracking
- MLflow: experiment logging, model registry, artifact storage, experiment comparison
- Weights & Biases: training visualization, hyperparameter sweeps, team collaboration
- Custom tracking with structured JSON/CSV logging for lightweight projects
- Experiment comparison and best model selection

### 5. Model Deployment
- FastAPI REST APIs with Pydantic validation, health checks, and batch prediction endpoints
- Docker containerization with multi-stage builds for model serving
- AWS SageMaker endpoint deployment with custom inference scripts
- Google Vertex AI model serving and batch prediction jobs
- Batch prediction pipelines for large-scale offline scoring
- Production monitoring: data drift detection, prediction distribution tracking

### 6. LLM Applications
- RAG system architecture: document loading, chunking, embedding, retrieval, generation
- Prompt engineering: system prompts, few-shot examples, chain-of-thought, structured outputs
- LangChain/LangGraph agent architectures with tool calling and memory
- Vector stores: Chroma, Pinecone, Weaviate, pgvector
- Embedding generation with OpenAI, Sentence Transformers, Cohere
- LangSmith trace debugging for agent development

### 7. MLOps
- ML project structure following standard conventions (data, notebooks, src, models, configs)
- Reproducibility: random seeds, versioned data, tracked parameters, pinned dependencies
- CI/CD for ML: automated testing, model validation, staged deployment
- Model monitoring and retraining triggers based on data drift and performance degradation

## Available Commands

| Command | Description |
|---------|-------------|
| `/proagent-ml-ai-run train-model` | Train and evaluate an ML model with proper validation and tracking |
| `/proagent-ml-ai-run build-pipeline` | Build an end-to-end ML pipeline (data prep, training, evaluation, deployment) |
| `/proagent-ml-ai-run setup-experiment` | Set up experiment tracking with MLflow or W&B |
| `/proagent-ml-ai-run create-embedding` | Generate embeddings and set up a vector store for RAG |
| `/proagent-ml-ai-run deploy-model` | Deploy a trained model to production (API, SageMaker, Vertex AI) |
| `/proagent-ml-ai-review` | Review model architecture, training pipeline, inference optimization, or data quality |

## Quick Start

To get started, tell me what you need help with:

- "I need to train a classification model" -> `/proagent-ml-ai-run train-model`
- "Set up an ML pipeline for my project" -> `/proagent-ml-ai-run build-pipeline`
- "Configure MLflow for experiment tracking" -> `/proagent-ml-ai-run setup-experiment`
- "Build a RAG system for my documents" -> `/proagent-ml-ai-run create-embedding`
- "Deploy my model to SageMaker" -> `/proagent-ml-ai-run deploy-model`
- "Review my training code for issues" -> `/proagent-ml-ai-review`

## Source Assets

This plugin is built from production patterns across these Provectus repositories:
- **proagent** - ML engineer role definitions, skills (model training, feature engineering, model selection, hyperparameter tuning, model evaluation, experiment tracking, model deployment), commands, and templates
- **awesome-claude-skills** - LangSmith fetch for LangChain/LangGraph agent debugging
- **agents** - LLM architect for RAG systems and agent architectures
- **tac** - OpenAI and Anthropic LLM utilities, NL-to-SQL LLM processor
- **proagent-repo GUI** - ML engineer validation workflows
- **specs** - ML/Data role implementations and specifications
