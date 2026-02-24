## Model Deployment

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
