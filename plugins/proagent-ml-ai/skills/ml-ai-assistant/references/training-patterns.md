## Model Training

### Training Pipeline Design

Every training pipeline should follow this structured progression:

1. **Data Preparation** - Load, clean, and split data into train/validation/test sets
2. **Feature Engineering** - Create, transform, and select features from raw data
3. **Model Selection** - Choose appropriate model family based on problem type and data characteristics
4. **Training Execution** - Fit model with proper validation, early stopping, and checkpointing
5. **Evaluation** - Comprehensive metric analysis, error investigation, and baseline comparison
6. **Experiment Logging** - Track parameters, metrics, artifacts, and metadata
7. **Model Persistence** - Save model weights, preprocessors, feature schema, and versioned metadata

### Data Splitting Strategies

- **Hold-out Validation:** Single train/val split for large datasets (typically 70/15/15 or 80/10/10)
- **Stratified K-Fold Cross-Validation:** 5-10 folds for smaller datasets; maintains class distribution
- **Time Series Split:** Respects temporal order for sequential data; never shuffle time series
- **Group K-Fold:** Prevents data leakage when samples are grouped (same patient, same user)

### Classification Model Training Pattern

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
