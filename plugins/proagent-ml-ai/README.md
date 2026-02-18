# proagent-ml-ai

Provectus ML & AI practice plugin for the agentic coding platform. Provides production-tested patterns for machine learning model development, deployment, and AI application engineering.

## Overview

This plugin equips Claude with comprehensive ML and AI capabilities drawn from actual Provectus engineering repositories. It covers the full lifecycle from data preparation through model training, evaluation, deployment, and production monitoring, along with modern AI application development including LLM-powered RAG systems, prompt engineering, and vector stores.

## Installation

Copy this plugin directory into your project's `.claude/plugins/` directory or reference it from the Provectus marketplace.

## Capabilities

### Model Training
Train classification, regression, ranking, and time series models with scikit-learn, TensorFlow, PyTorch, XGBoost, and LightGBM. Includes proper data splitting, cross-validation, early stopping, and checkpointing patterns.

### Feature Engineering
Handle missing values, encode categoricals, transform numericals, create temporal features, and select the most predictive features using correlation analysis, mutual information, and recursive elimination.

### Model Evaluation
Evaluate models with appropriate metrics by problem type. Generate confusion matrices, ROC/PR curves, residual plots. Compare models with cross-validation and statistical significance tests. Perform error analysis to understand failure modes.

### Experiment Tracking
Track experiments with MLflow or Weights & Biases. Log parameters, metrics, and artifacts. Compare experiments, select best models, and manage model registry with stage transitions.

### Model Deployment
Deploy models via FastAPI REST APIs, AWS SageMaker endpoints, Google Vertex AI serving, or batch prediction pipelines. Containerize with Docker multi-stage builds. Monitor data drift and prediction distributions in production.

### LLM Applications
Build RAG systems with document loading, chunking, embedding generation, and vector store management. Engineer prompts with system instructions, few-shot examples, and chain-of-thought reasoning. Debug LangChain/LangGraph agents with LangSmith traces.

### MLOps
Scaffold ML projects with standard directory structures. Enforce reproducibility through random seeds, versioned data, and pinned dependencies. Set up CI/CD for ML with automated testing and staged deployment.

## Commands

| Command | Description |
|---------|-------------|
| `/proagent-ml-ai-hub` | Practice overview and capability guide |
| `/proagent-ml-ai-run train-model` | Train and evaluate an ML model |
| `/proagent-ml-ai-run build-pipeline` | Build an end-to-end ML pipeline |
| `/proagent-ml-ai-run setup-experiment` | Set up experiment tracking |
| `/proagent-ml-ai-run create-embedding` | Generate embeddings and vector store |
| `/proagent-ml-ai-run deploy-model` | Deploy a model to production |
| `/proagent-ml-ai-review` | Review ML artifacts for best practices |

## Plugin Structure

```
proagent-ml-ai/
  .claude-plugin/plugin.json    # Plugin metadata and registration
  skills/
    ml-ai-assistant/SKILL.md    # Core ML & AI skill with patterns and examples
  commands/
    proagent-ml-ai-hub.md       # Practice hub and capability overview
    proagent-ml-ai-run.md       # Execution commands (train, build, deploy)
    proagent-ml-ai-review.md    # Review commands (architecture, pipeline, data)
  agents/
    ml-ai-specialist.md         # ML/AI specialist agent definition
  hooks/
    hooks.json                  # Model validation and experiment logging hooks
  .mcp.json                     # MCP server integrations (GitHub)
  CLAUDE.md                    # Plugin conventions and standards
  README.md                    # This file
```

## Source Repositories

This plugin synthesizes production patterns from:

| Repository | Assets Used |
|-----------|-------------|
| proagent | ML engineer role definition, 7 skills (model-training, feature-engineering, model-selection, hyperparameter-tuning, model-evaluation, experiment-tracking, model-deployment), train-model command, ML project starter template |
| awesome-claude-skills | LangSmith fetch skill for LangChain/LangGraph agent debugging |
| agents | LLM architect agent for RAG systems and agent architectures |
| tac | OpenAI and Anthropic LLM utilities, NL-to-SQL LLM processor |
| proagent-repo GUI | ML engineer validation workflow configuration |
| specs | ML/Data role implementation specifications |

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |

## Requirements

- Python 3.9+
- Core ML: scikit-learn, pandas, numpy, matplotlib, seaborn
- Deep Learning: tensorflow or pytorch (as needed)
- Gradient Boosting: xgboost, lightgbm (as needed)
- Experiment Tracking: mlflow or wandb
- Model Serving: fastapi, uvicorn, pydantic
- LLM Applications: langchain, chromadb, sentence-transformers (as needed)
- Containerization: Docker

## License

MIT
