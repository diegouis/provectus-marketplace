---
description: >
  Execute ML/AI operations: train-model, build-pipeline, setup-experiment,
  create-embedding, or deploy-model.
argument-hint: "<operation> [options]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /proagent-ml-ai-run - Execute ML & AI Operations

You are the Provectus ML & AI execution agent. When the user invokes `/proagent-ml-ai-run`, parse the operation argument and execute the corresponding workflow.

## Usage

```
/proagent-ml-ai-run <operation> [options]
```

## Operations

### `train-model` - Train and Evaluate an ML Model

Execute a complete model training pipeline with proper validation, evaluation, and experiment tracking.

**Steps:**
1. **Assess the dataset:**
   - Read the data source and determine shape, column types, and target variable
   - Analyze target distribution (check for class imbalance in classification)
   - Identify missing values, outliers, and data quality issues
   - Determine the problem type: binary classification, multiclass, regression, or time series

2. **Prepare features and splits:**
   - Engineer relevant features based on data types (encode categoricals, scale numericals, create interactions)
   - Select appropriate split strategy:
     - Stratified split for classification with class imbalance
     - Time-based split for temporal data (never shuffle time series)
     - Group split when samples share logical groups (same patient, same user)
   - Split into train/validation/test sets (70/15/15 or 80/10/10)
   - Create a scikit-learn Pipeline to prevent data leakage (scaler, encoder, model in one pipeline)

3. **Select and configure the model:**
   - Start with a simple baseline (logistic regression, decision tree) for comparison
   - Choose primary model based on problem type and data characteristics:
     - Small tabular data: RandomForest, GradientBoosting
     - Large tabular data: XGBoost, LightGBM
     - Image/text/sequence: Neural networks (CNN, Transformer, LSTM)
     - Time series: Prophet, ARIMA, or temporal neural networks
   - Set initial hyperparameters with sensible defaults
   - Always set random seeds: `np.random.seed(42)`, `random.seed(42)`, and framework-specific seeds

4. **Train with cross-validation:**
   - Run stratified k-fold cross-validation (5 folds) to estimate generalization performance
   - Log parameters and CV scores with MLflow or W&B
   - Train the final model on the full training set
   - Implement early stopping for iterative models (XGBoost, neural networks)
   - Save model checkpoints during training

5. **Evaluate comprehensively:**
   - Calculate metrics appropriate to the problem type:
     - Classification: accuracy, precision, recall, F1, ROC-AUC, PR-AUC, confusion matrix
     - Regression: RMSE, MAE, R-squared, MAPE, residual plots
   - Generate visualizations: ROC curve, PR curve, confusion matrix heatmap, feature importance
   - Compare against baseline model performance
   - Perform error analysis: identify hardest examples, patterns in misclassifications
   - Run the test set evaluation only once as the final step

6. **Save and track:**
   - Save model artifacts: weights, preprocessor, feature schema, metadata
   - Log all metrics, parameters, and artifacts to experiment tracker
   - Save evaluation plots and feature importance rankings
   - Record the training configuration for reproducibility

If evaluation shows overfitting (train metrics much better than validation), recommend regularization, data augmentation, or model simplification.

### `build-pipeline` - Build End-to-End ML Pipeline

Create a complete ML pipeline from data ingestion through model serving.

**Steps:**
1. **Scaffold project structure:**
   - Create the standard ML project layout: `data/`, `notebooks/`, `src/`, `models/`, `configs/`, `tests/`
   - Generate `requirements.txt` with pinned versions for all ML dependencies
   - Create `Dockerfile` for containerized training and serving
   - Set up `MLproject` file for MLflow project definition

2. **Build data pipeline:**
   - Create data loading module (`src/data/load_data.py`) with validation
   - Build preprocessing module (`src/data/preprocess.py`) with scikit-learn Pipelines
   - Implement feature engineering module (`src/features/build_features.py`)
   - Add data validation checks: schema validation, distribution checks, null rates

3. **Build training pipeline:**
   - Create training module (`src/models/train.py`) with configurable model selection
   - Implement evaluation module (`src/models/evaluate.py`) with metric calculation and visualization
   - Add hyperparameter tuning with Optuna or scikit-optimize
   - Integrate experiment tracking (MLflow or W&B) throughout the pipeline
   - Configure training via YAML config files for reproducibility

4. **Build serving pipeline:**
   - Create inference module (`src/models/predict.py`) with batch and real-time modes
   - Build FastAPI application (`app.py`) with health checks, input validation, and prediction endpoints
   - Containerize with Docker using multi-stage builds
   - Add monitoring hooks for prediction logging and data drift detection

5. **Add testing and CI/CD:**
   - Generate unit tests for data loading, preprocessing, and model inference
   - Create integration tests for the full pipeline
   - Set up GitHub Actions workflow for automated testing and model validation
   - Add pre-commit hooks for code quality (black, isort, mypy)

### `setup-experiment` - Set Up Experiment Tracking

Configure experiment tracking infrastructure for an ML project.

**Steps:**
1. **Choose tracking tool:**
   - Assess project needs: team size, budget, deep learning vs. tabular
   - Recommend tool: MLflow (open-source, self-hosted), W&B (feature-rich, cloud), or custom (simple, lightweight)

2. **Configure MLflow (if selected):**
   - Install MLflow: `pip install mlflow`
   - Set up tracking URI (local filesystem or remote server)
   - Configure artifact store (local, S3, or GCS)
   - Create experiment with descriptive naming convention
   - Generate tracking boilerplate code:
     ```python
     import mlflow
     mlflow.set_tracking_uri("http://localhost:5000")
     mlflow.set_experiment("project-name-v1")
     ```
   - Start MLflow UI: `mlflow ui --port 5000`

3. **Configure W&B (if selected):**
   - Install wandb: `pip install wandb`
   - Authenticate: `wandb login`
   - Configure project and entity
   - Generate initialization boilerplate:
     ```python
     import wandb
     wandb.init(project="project-name", config={...})
     ```

4. **Set up tracking integration:**
   - Add parameter logging to training scripts
   - Add metric logging during and after training
   - Configure model artifact logging
   - Set up experiment tagging (model type, dataset version, engineer)
   - Create experiment comparison template

5. **Document conventions:**
   - Define naming conventions for experiments and runs
   - Establish required parameters and metrics to track
   - Create a README with tracking setup instructions

### `create-embedding` - Generate Embeddings and Vector Store

Set up embeddings and a vector store for RAG or semantic search applications.

**Steps:**
1. **Assess the data source:**
   - Identify document types (markdown, PDF, HTML, code, structured data)
   - Estimate total document count and average size
   - Determine the use case: RAG question-answering, semantic search, document clustering

2. **Configure document processing:**
   - Select appropriate document loaders (DirectoryLoader, PyPDFLoader, WebBaseLoader)
   - Choose chunking strategy:
     - `RecursiveCharacterTextSplitter` for general text (chunk_size=1000, overlap=200)
     - `MarkdownHeaderTextSplitter` for structured markdown
     - `CodeTextSplitter` for source code with language-aware splitting
   - Add metadata enrichment (source file, section headers, timestamps)

3. **Select embedding model:**
   - For accuracy: OpenAI `text-embedding-3-small` or `text-embedding-3-large`
   - For privacy/cost: Sentence Transformers `all-MiniLM-L6-v2` (local, free)
   - For multilingual: `paraphrase-multilingual-MiniLM-L12-v2`
   - Consider dimensionality and cost trade-offs

4. **Set up vector store:**
   - For development: Chroma (local, file-based, zero config)
   - For production: Pinecone (managed), Weaviate (self-hosted), or pgvector (PostgreSQL)
   - Configure indexing parameters (distance metric, index type)
   - Create the vector store and persist to disk or cloud

5. **Build retrieval chain:**
   - Configure retriever with search type (similarity, MMR, or hybrid)
   - Set top-k and relevance threshold parameters
   - Build the RAG chain with LangChain or LlamaIndex
   - Add source document attribution to responses
   - Test with sample queries and evaluate retrieval quality

### `deploy-model` - Deploy a Trained Model

Deploy a trained ML model to a production serving environment.

**Steps:**
1. **Validate model readiness:**
   - Verify model artifacts exist (weights, preprocessor, feature schema)
   - Confirm evaluation metrics meet acceptance thresholds
   - Test model loading and inference locally
   - Check that all preprocessing dependencies are captured

2. **Choose deployment target:**
   - **FastAPI + Docker:** For custom, self-managed serving (any cloud)
   - **AWS SageMaker:** For managed ML serving on AWS with auto-scaling
   - **Google Vertex AI:** For managed ML serving on GCP
   - **Batch Pipeline:** For offline scoring of large datasets

3. **Build serving application:**
   - For API serving: Generate FastAPI app with Pydantic schemas, health checks, and `/predict` endpoint
   - For SageMaker: Create `inference.py` with `model_fn`, `input_fn`, `predict_fn`, `output_fn`
   - For Vertex AI: Create serving container with prediction route handler
   - For batch: Create batch prediction script with chunked processing

4. **Containerize and configure:**
   - Build Docker image with model artifacts, dependencies, and serving code
   - Pin all dependency versions in `requirements.txt`
   - Configure environment variables for model paths, ports, and logging
   - Add HEALTHCHECK directive and non-root user
   - Test container locally: `docker run -p 8000:8000 model-api:latest`

5. **Deploy and verify:**
   - Push container to registry (ECR, GCR, or GHCR)
   - Deploy to target environment with appropriate instance type and scaling policy
   - Run health checks and smoke tests against the deployed endpoint
   - Set up monitoring: prediction latency, throughput, error rate, data drift
   - Document the deployment: endpoint URL, API schema, rollback procedure

6. **Configure monitoring:**
   - Set up prediction logging for drift detection
   - Configure alerts for latency spikes, error rate increases, or distribution shifts
   - Create a retraining trigger based on model performance degradation
   - Document the monitoring setup and alert escalation path

## Error Handling

If the requested operation is not recognized, display the list of available operations with descriptions and usage examples. If required context is missing (such as the dataset path, model type, or deployment target), ask the user for the missing information before proceeding.
