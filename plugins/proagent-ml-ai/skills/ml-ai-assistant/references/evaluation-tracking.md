## Model Evaluation

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
