---
name: ml-ai-assistant
description: Building ML & AI Systems - model training, inference optimization, MLOps pipelines, experiment tracking, prompt engineering, embeddings, vector stores, LLM application development, and RAG systems. Use when performing any machine learning, deep learning, or AI engineering task.
---

# Building ML & AI Systems

Comprehensive ML and AI skill covering the full lifecycle of machine learning model development, from data preparation through training, evaluation, deployment, and monitoring. Includes modern AI capabilities such as LLM application development, RAG systems, embeddings, and vector stores. Built from production-tested patterns across Provectus engineering teams.

## When to Use This Skill

- Training and evaluating machine learning models (classification, regression, ranking, time series)
- Engineering features from raw data for model input
- Selecting appropriate models for business problems
- Tuning hyperparameters to optimize model performance
- Tracking experiments with MLflow, Weights & Biases, or custom systems
- Deploying models to production via REST APIs, batch pipelines, or managed services
- Building LLM-powered applications with RAG, prompt engineering, and agent architectures
- Creating and managing embeddings and vector stores
- Monitoring model performance and detecting data drift in production
- Debugging LangChain/LangGraph agents via LangSmith traces

## Model Training

### Training Pipeline Design

Every training pipeline should follow this structured progression, derived from `proagent/roles/ml-engineer/skills/model-training.md`:

1. **Data Preparation** - Load, clean, and split data into train/validation/test sets
2. **Feature Engineering** - Create, transform, and select features from raw data
3. **Model Selection** - Choose appropriate model family based on problem type and data characteristics
4. **Training Execution** - Fit model with proper validation, early stopping, and checkpointing
5. **Evaluation** - Comprehensive metric analysis, error investigation, and baseline comparison
6. **Experiment Logging** - Track parameters, metrics, artifacts, and metadata
7. **Model Persistence** - Save model weights, preprocessors, feature schema, and versioned metadata

### Data Splitting Strategies

Derived from `proagent/roles/ml-engineer/skills/model-training.md`:

- **Hold-out Validation:** Single train/val split for large datasets (typically 70/15/15 or 80/10/10)
- **Stratified K-Fold Cross-Validation:** 5-10 folds for smaller datasets; maintains class distribution
- **Time Series Split:** Respects temporal order for sequential data; never shuffle time series
- **Group K-Fold:** Prevents data leakage when samples are grouped (same patient, same user)

### Classification Model Training Pattern

Derived from `proagent/roles/ml-engineer/skills/model-training.md` and `proagent/roles/ml-engineer/commands/train-model.md`:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib

# Set random seeds for reproducibility
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# Load and prepare data
X = df.drop('target', axis=1)
y = df['target']

# Stratified train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)

# Create preprocessing + model pipeline to prevent data leakage
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=10,
        class_weight='balanced',
        random_state=RANDOM_STATE,
        n_jobs=-1
    ))
])

# Cross-validation for robust evaluation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='f1')
print(f"CV F1: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

# Train final model and evaluate on test set
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
y_proba = pipeline.predict_proba(X_test)[:, 1]

print(f"Test Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Test F1:        {f1_score(y_test, y_pred):.4f}")
print(f"Test ROC-AUC:   {roc_auc_score(y_test, y_proba):.4f}")

# Save model and artifacts
joblib.dump(pipeline, 'models/model.pkl')
```

### Neural Network Training with Early Stopping

Derived from `proagent/roles/ml-engineer/skills/model-training.md`:

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Set random seeds
np.random.seed(42)
tf.random.set_seed(42)

# Build model
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dropout(0.3),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy', keras.metrics.AUC(name='auc')]
)

# Callbacks for early stopping and checkpointing
callbacks = [
    keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True),
    keras.callbacks.ModelCheckpoint('models/best_model.h5', monitor='val_auc', save_best_only=True, mode='max'),
    keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, min_lr=1e-7),
    keras.callbacks.TensorBoard(log_dir='logs/')
]

history = model.fit(
    X_train_norm, y_train,
    validation_data=(X_val_norm, y_val),
    epochs=100, batch_size=32,
    callbacks=callbacks
)
```

### XGBoost with Early Stopping

Derived from `proagent/roles/ml-engineer/skills/model-training.md`:

```python
import xgboost as xgb

params = {
    'objective': 'binary:logistic',
    'eval_metric': ['logloss', 'auc'],
    'max_depth': 6,
    'learning_rate': 0.1,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'min_child_weight': 3,
    'reg_alpha': 0.1,
    'reg_lambda': 1.0,
    'seed': 42
}

dtrain = xgb.DMatrix(X_train, label=y_train)
dval = xgb.DMatrix(X_val, label=y_val)

model = xgb.train(
    params, dtrain,
    num_boost_round=1000,
    evals=[(dtrain, 'train'), (dval, 'val')],
    early_stopping_rounds=50,
    verbose_eval=20
)

model.save_model('models/xgboost_model.json')
```

## Feature Engineering

Derived from `proagent/roles/ml-engineer/skills/feature-engineering.md`:

### Core Techniques

- **Missing Value Handling:** Imputation (mean/median/KNN), indicator variables, or deletion for <5% missing
- **Categorical Encoding:** One-hot for low cardinality (<10), target encoding for high cardinality, ordinal for natural order
- **Numerical Transformations:** StandardScaler for normally distributed, MinMaxScaler for bounded, log transform for skewed, PowerTransformer for heavy tails
- **Feature Interactions:** Polynomial features, ratio features, domain-specific combinations
- **Temporal Features:** Day of week, month, hour, lag features, rolling aggregates, time since events
- **Text Features:** TF-IDF, count vectorization, word embeddings, sentence transformers

### Data Leakage Prevention

```python
# BAD: Fit scaler on all data before splitting
scaler.fit(X)
X_train, X_test = train_test_split(X)

# GOOD: Fit only on training data using Pipeline
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier())
])
pipeline.fit(X_train, y_train)  # Scaler fits only on X_train
```

## Model Evaluation

Derived from `proagent/roles/ml-engineer/skills/model-evaluation.md`:

### Binary Classification Evaluation

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score,
    roc_curve, precision_recall_curve, average_precision_score
)

def evaluate_binary_classifier(y_true, y_pred, y_pred_proba):
    print(f"Accuracy:  {accuracy_score(y_true, y_pred):.4f}")
    print(f"Precision: {precision_score(y_true, y_pred):.4f}")
    print(f"Recall:    {recall_score(y_true, y_pred):.4f}")
    print(f"F1 Score:  {f1_score(y_true, y_pred):.4f}")
    print(f"ROC-AUC:   {roc_auc_score(y_true, y_pred_proba):.4f}")
    print(f"PR-AUC:    {average_precision_score(y_true, y_pred_proba):.4f}")
    print(classification_report(y_true, y_pred))
```

### Metric Selection Guide

| Problem Type | Primary Metrics | Avoid |
|---|---|---|
| Balanced Classification | Accuracy, F1 | - |
| Imbalanced Classification | F1, ROC-AUC, PR-AUC | Accuracy |
| Cost-Sensitive | Custom cost-weighted metrics | Single threshold |
| Regression | RMSE, MAE, R-squared | - |
| Ranking | NDCG, MAP, MRR | - |

## Experiment Tracking

Derived from `proagent/roles/ml-engineer/skills/experiment-tracking.md`:

### MLflow Tracking Pattern

```python
import mlflow
import mlflow.sklearn

mlflow.set_experiment("customer-churn-prediction")

with mlflow.start_run(run_name="random-forest-baseline"):
    # Log parameters
    mlflow.log_params({
        'n_estimators': 100, 'max_depth': 10,
        'min_samples_split': 10, 'random_state': 42
    })
    mlflow.set_tags({
        'model_type': 'random_forest',
        'dataset_version': 'v1.0',
        'engineer': 'alice'
    })

    # Train and evaluate
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Log metrics
    mlflow.log_metrics({
        'accuracy': accuracy_score(y_test, y_pred),
        'f1_score': f1_score(y_test, y_pred),
        'roc_auc': roc_auc_score(y_test, y_pred_proba)
    })

    # Log model and artifacts
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_artifact('confusion_matrix.png')
```

### Weights & Biases Pattern

```python
import wandb

wandb.init(
    project="image-classification",
    name="resnet-transfer-learning",
    config={
        "architecture": "ResNet50",
        "epochs": 50,
        "batch_size": 32,
        "learning_rate": 0.001
    }
)

wandb_callback = wandb.keras.WandbCallback(
    save_model=True, monitor='val_accuracy', mode='max'
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=50, batch_size=32,
    callbacks=[wandb_callback]
)

wandb.finish()
```

## Model Deployment

Derived from `proagent/roles/ml-engineer/skills/model-deployment.md`:

### FastAPI Model Serving

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np
from typing import List

app = FastAPI(title="ML Model API", version="1.0.0")

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

class PredictionRequest(BaseModel):
    features: List[float] = Field(..., min_items=10, max_items=10)

class PredictionResponse(BaseModel):
    prediction: float
    probability: float = None
    model_version: str = "1.0.0"

@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": model is not None}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        features = np.array(request.features).reshape(1, -1)
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        probability = None
        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(features_scaled)[0][1])
        return PredictionResponse(prediction=float(prediction), probability=probability)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### Model Serving Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY models/ models/
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### AWS SageMaker Deployment

Derived from `proagent/roles/ml-engineer/skills/model-deployment.md`:

```python
import sagemaker
from sagemaker.sklearn import SKLearnModel

role = sagemaker.get_execution_role()
sklearn_model = SKLearnModel(
    model_data='s3://my-bucket/models/model.tar.gz',
    role=role,
    entry_point='inference.py',
    framework_version='1.0-1',
    py_version='py3'
)

predictor = sklearn_model.deploy(
    instance_type='ml.m5.large',
    initial_instance_count=1,
    endpoint_name='sklearn-model-endpoint'
)
```

### Batch Prediction Pipeline

```python
import pandas as pd
import joblib
from datetime import datetime

def batch_predict(input_path, output_path, model_path, batch_size=1000):
    model = joblib.load(model_path)
    chunks = pd.read_csv(input_path, chunksize=batch_size)
    predictions = []
    for chunk in chunks:
        X = chunk.drop('id', axis=1)
        preds = model.predict(X)
        chunk_results = pd.DataFrame({
            'id': chunk['id'], 'prediction': preds,
            'predicted_at': datetime.now()
        })
        predictions.append(chunk_results)
    results = pd.concat(predictions, ignore_index=True)
    results.to_csv(output_path, index=False)
```

## Model Monitoring

Derived from `proagent/roles/ml-engineer/skills/model-deployment.md`:

### Data Drift Detection

```python
from scipy import stats
import pandas as pd
import numpy as np

class ModelMonitor:
    def __init__(self, reference_data):
        self.reference_data = reference_data

    def detect_data_drift(self, production_data, threshold=0.05):
        drift_results = {}
        for column in self.reference_data.columns:
            if column in production_data.columns:
                ks_stat, p_value = stats.ks_2samp(
                    self.reference_data[column],
                    production_data[column]
                )
                drift_results[column] = {
                    'ks_statistic': ks_stat,
                    'p_value': p_value,
                    'drift_detected': p_value < threshold
                }
        return drift_results

    def check_prediction_distribution(self, predictions, expected_mean, expected_std, threshold=2.0):
        actual_mean = np.mean(predictions)
        mean_diff_in_stds = abs(actual_mean - expected_mean) / expected_std
        return {
            'alert': mean_diff_in_stds > threshold,
            'actual_mean': actual_mean,
            'expected_mean': expected_mean,
            'deviation': mean_diff_in_stds
        }
```

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

## LangSmith Agent Debugging

Derived from `awesome-claude-skills/langsmith-fetch/SKILL.md`:

Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio:

```bash
# Install and configure
pip install langsmith-fetch
export LANGSMITH_API_KEY="your_key"
export LANGSMITH_PROJECT="your_project"

# Fetch and analyze traces
langsmith-fetch --last 5
langsmith-fetch --errors-only
langsmith-fetch --trace-id <id> --verbose
```

## ML Project Structure

Derived from `proagent/roles/ml-engineer/templates/ml-project-starter.md`:

```
ml-project/
  data/
    raw/                    # Original, immutable data
    processed/              # Cleaned, transformed data
  notebooks/
    01_exploration.ipynb
    02_preprocessing.ipynb
    03_modeling.ipynb
    04_analysis.ipynb
  src/
    data/load_data.py, preprocess.py
    features/build_features.py
    models/train.py, predict.py, evaluate.py
    visualization/visualize.py
  models/                   # Trained model artifacts
  configs/                  # Training configurations
  experiments/              # Experiment logs and results
  tests/                    # Unit and integration tests
  requirements.txt
  Dockerfile
  MLproject                 # MLflow project definition
```

## Common Pitfalls

1. **Data Leakage:** Fitting preprocessors on all data instead of training set only
2. **No Random Seeds:** Results are not reproducible across runs
3. **Test Set Reuse:** Evaluating on the test set multiple times inflates performance estimates
4. **Wrong Metrics:** Using accuracy for imbalanced classification problems
5. **Missing Preprocessing in Deployment:** Forgetting to include feature engineering in the serving pipeline
6. **No Monitoring:** Deploying without tracking data drift or prediction distribution shifts
7. **Poor Experiment Tracking:** Training many models without logging parameters and results

## Reference Assets

| Asset | Source | Description |
|-------|--------|-------------|
| Model Training Skill | `proagent/roles/ml-engineer/skills/model-training.md` | Complete training pipeline patterns with scikit-learn, TensorFlow, XGBoost |
| Feature Engineering Skill | `proagent/roles/ml-engineer/skills/feature-engineering.md` | Feature creation, transformation, and selection techniques |
| Model Selection Skill | `proagent/roles/ml-engineer/skills/model-selection.md` | Algorithm selection by problem type and data characteristics |
| Hyperparameter Tuning Skill | `proagent/roles/ml-engineer/skills/hyperparameter-tuning.md` | Grid search, random search, Bayesian optimization, Hyperband |
| Model Evaluation Skill | `proagent/roles/ml-engineer/skills/model-evaluation.md` | Metrics, visualizations, statistical significance testing |
| Experiment Tracking Skill | `proagent/roles/ml-engineer/skills/experiment-tracking.md` | MLflow, W&B, Neptune, custom tracking patterns |
| Model Deployment Skill | `proagent/roles/ml-engineer/skills/model-deployment.md` | FastAPI serving, SageMaker, batch prediction, monitoring |
| Train Model Command | `proagent/roles/ml-engineer/commands/train-model.md` | End-to-end training pipeline command template |
| ML Project Starter | `proagent/roles/ml-engineer/templates/ml-project-starter.md` | Standard ML project directory structure |
| LangSmith Fetch Skill | `awesome-claude-skills/langsmith-fetch/SKILL.md` | LangChain/LangGraph agent debugging via LangSmith traces |
| LLM Architect Agent | `agents/plugins/llm-application-dev/agents/llm-architect.md` | RAG systems and agent architecture design |
| OpenAI LLM Utility | `tac/Code/tac-6/.claude/hooks/utils/llm/oai.py` | OpenAI API integration utility |
| Anthropic LLM Utility | `tac/Code/tac-6/.claude/hooks/utils/llm/anth.py` | Anthropic API integration utility |
| NL-to-SQL Processor | `tac/Code/tac-6/app/server/core/llm_processor.py` | LLM-powered natural language to SQL translation |
| ML Engineer Role | `proagent/roles/ml-engineer/README (1).md` | ML engineer role definition and quick start guide |
