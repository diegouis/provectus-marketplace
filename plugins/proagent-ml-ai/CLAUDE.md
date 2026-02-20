# Provectus ML & AI Practice Plugin

This plugin provides the ML & AI practice context for the Provectus agentic coding platform. It equips Claude with production-tested machine learning and AI application patterns drawn from actual Provectus engineering repositories.

## Practice Scope

The ML & AI practice covers ten operational domains:

1. **Model Training** - Scikit-learn pipelines, TensorFlow/Keras neural networks, XGBoost/LightGBM gradient boosting, PyTorch training loops with cross-validation, early stopping, and checkpointing
2. **Feature Engineering** - Missing value handling, categorical encoding, numerical transformations, temporal features, text features, and feature selection
3. **Model Evaluation** - Classification metrics (F1, ROC-AUC, PR-AUC), regression metrics (RMSE, MAE, R-squared), confusion matrices, ROC/PR curves, error analysis, model comparison with statistical significance testing, and LLM judge evaluation (`ralph-orchestrator/tools/e2e/helpers/llm_judge.py`)
4. **Experiment Tracking** - MLflow parameter/metric/artifact logging, Weights & Biases training visualization, experiment comparison, model registry management
5. **Model Deployment** - FastAPI REST APIs, Docker containerization, AWS SageMaker endpoints, AWS Bedrock integration, Google Vertex AI serving, batch prediction pipelines
6. **LLM Applications** - RAG systems with document loading/chunking/embedding/retrieval, prompt engineering patterns, LangChain/LangGraph/LangGraphJS agent architectures, vector stores (Chroma, Pinecone, Weaviate), embedding models, LangSmith observability (`awesome-claude-skills/langsmith-fetch/SKILL.md`)
7. **Production Monitoring** - Data drift detection with KS tests, prediction distribution tracking, model performance monitoring, retraining triggers
8. **Knowledge Graph Integration** - Graphiti knowledge graph patterns for structured knowledge retrieval and context management (`Auto-Claude/apps/backend/context/graphiti_integration.py`)
9. **Meta-Prompting Frameworks** - Base meta-prompt construction with role knowledge (`proagent-repo/core/meta_prompts/base.py`), meta-prompt creation commands and generation skills (`taches-cc-resources/commands/create-meta-prompt.md`, `taches-cc-resources/skills/create-meta-prompts/SKILL.md`)
10. **ML Pipeline Workflows** - End-to-end ML pipeline patterns including validation workflows (`proagent-repo/core/templates/validation_workflows/ml-engineer.yaml`, `agents/plugins/machine-learning-ops/skills/ml-pipeline-workflow/SKILL.md`)

## Key Conventions

When performing ML & AI tasks, follow these standards:

### Reproducibility
- Always set random seeds at the start of every script: numpy, random, and framework-specific seeds
- Pin all dependency versions in requirements.txt
- Version data alongside code and models
- Log all hyperparameters and training configuration to experiment tracker

### Data Integrity
- Use scikit-learn Pipelines to prevent data leakage (fit preprocessors only on training data)
- Use stratified splitting for classification, time-based splitting for time series
- Never shuffle time series data
- Use GroupKFold when samples share logical groups
- Evaluate on the test set only once as the final step

### Experiment Tracking
- Every training run must log parameters, metrics, and model artifacts
- Use descriptive naming conventions for experiments and runs
- Tag experiments with model type, dataset version, and engineer name
- Save feature importance rankings and evaluation plots as artifacts

### Model Deployment
- Include all preprocessing artifacts (scaler, encoder, tokenizer) with the deployed model
- Add health check endpoints to every serving application
- Validate inputs with Pydantic schemas
- Monitor prediction latency, throughput, and data drift in production
- Document rollback procedures for every deployment

### Code Quality
- Follow the standard ML project structure: data/, notebooks/, src/, models/, configs/, tests/
- Separate training, evaluation, and serving code into distinct modules
- Write unit tests for data loading, preprocessing, and model inference
- Use type hints and docstrings throughout ML code

## MCP Integrations

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)

## Plugin Structure

```
proagent-ml-ai/
  .claude-plugin/plugin.json
  skills/
    ml-ai-assistant/SKILL.md
  commands/proagent-ml-ai-hub.md
  commands/proagent-ml-ai-run.md
  commands/proagent-ml-ai-review.md
  agents/ml-ai-specialist.md
  hooks/hooks.json
  .mcp.json
  CLAUDE.md
  README.md
```
