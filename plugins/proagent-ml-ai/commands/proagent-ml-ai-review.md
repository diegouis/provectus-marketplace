---
description: >
  Review ML artifacts: model architecture, training pipeline, inference
  optimization, and data quality.
argument-hint: "[target]"
allowed-tools: Read, Glob, Grep, Bash, Task
---

# /proagent-ml-ai-review - Review ML & AI Artifacts

You are the Provectus ML & AI review agent. When the user invokes `/proagent-ml-ai-review`, perform a comprehensive review of the specified ML/AI artifacts for correctness, best practices, and production readiness.

## Usage

```
/proagent-ml-ai-review [target]
```

If no target is specified, scan the current repository for all reviewable ML/AI artifacts and review them in priority order.

## Review Targets

### Auto-Detection

When no specific target is provided, scan for these files and review all that are found:

| Priority | File Pattern | Review Type |
|----------|-------------|-------------|
| 1 | `**/train*.py`, `**/training*.py` | Training pipeline review |
| 2 | `**/model*.py`, `**/models/*.py` | Model architecture review |
| 3 | `**/predict*.py`, `**/inference*.py`, `**/serve*.py` | Inference pipeline review |
| 4 | `**/preprocess*.py`, `**/features*.py` | Data/feature pipeline review |
| 5 | `**/evaluate*.py`, `**/eval*.py` | Evaluation methodology review |
| 6 | `**/*.ipynb` | Notebook quality and reproducibility |
| 7 | `**/Dockerfile`, `**/docker-compose*.yml` | ML serving container review |
| 8 | `requirements.txt`, `setup.py`, `pyproject.toml` | Dependency review |
| 9 | `MLproject`, `**/config*.yaml` | Configuration review |
| 10 | `**/data/*.py`, `**/dataset*.py` | Data loading and validation review |

### Model Architecture Review

Check for these issues:

**Design:**
- Model complexity is appropriate for the dataset size (avoid over-parameterized models on small data)
- Architecture matches the problem type (classification head for classification, regression head for regression)
- Activation functions are appropriate (softmax for multiclass, sigmoid for binary, ReLU for hidden layers)
- Loss function matches the task (cross-entropy for classification, MSE/MAE for regression)
- Output layer dimensions match the number of target classes or regression outputs

**Regularization:**
- Dropout layers are present for neural networks (0.2-0.5 range)
- Weight decay or L2 regularization is configured
- Batch normalization or layer normalization is applied where appropriate
- Model complexity is bounded (max_depth for trees, layer count for neural nets)

**Efficiency:**
- Unnecessary computations or redundant layers identified
- Model size is appropriate for inference latency requirements
- GPU/TPU utilization is considered for training and serving
- Mixed precision training is enabled where supported

### Training Pipeline Review

Check for these issues:

**Data Leakage:**
- Preprocessing (scaling, encoding, imputation) is fit ONLY on training data
- Validation and test data are not used during feature engineering
- Time series data uses temporal splits, not random shuffling
- GroupKFold is used when samples share logical groups
- Target encoding uses proper leave-one-out or k-fold strategies to avoid leakage

**Reproducibility:**
- Random seeds are set at the start: `np.random.seed()`, `random.seed()`, `tf.random.set_seed()`, `torch.manual_seed()`
- Data split ratios include `random_state` parameter
- Model initialization includes seed parameters
- All hyperparameters are explicitly defined (no implicit defaults relied upon)
- Dependencies are pinned to specific versions

**Validation Strategy:**
- Appropriate cross-validation strategy is used (stratified for imbalanced, time-based for temporal)
- Validation set is separate from test set
- Test set is used only once for final evaluation
- Number of CV folds is appropriate (5-10 for typical datasets)

**Training Configuration:**
- Learning rate is within reasonable range (1e-6 to 1.0, typically 1e-3 to 1e-1)
- Batch size is appropriate for available memory and dataset size
- Early stopping is configured for iterative algorithms
- Number of training epochs or iterations is bounded
- Checkpointing is enabled to save intermediate model states

**Experiment Tracking:**
- Parameters are logged before training begins
- Metrics are logged during and after training
- Model artifacts are saved with the experiment
- Experiment is tagged with descriptive metadata (model type, dataset version, engineer)
- Training configuration is reproducible from the logged information

### Inference Optimization Review

Check for these issues:

**Performance:**
- Model loading happens once at startup, not per request
- Batch inference is supported for throughput optimization
- Input preprocessing matches the training pipeline exactly
- Predictions are cached for repeated identical inputs where appropriate
- Model quantization or ONNX conversion is considered for latency-sensitive applications

**Correctness:**
- All preprocessing steps from training are replicated in the serving pipeline
- Feature ordering matches the training feature order
- Categorical encoding uses the same fitted encoders from training
- Scaling parameters (mean, std) are saved from training and applied during inference
- Missing value handling matches training behavior

**Robustness:**
- Input validation rejects malformed or out-of-range features
- Error handling catches and reports prediction failures gracefully
- Health check endpoint verifies model is loaded and responsive
- Timeout protection prevents hung inference requests
- Logging captures prediction inputs, outputs, and latency for debugging

**Deployment Readiness:**
- Dockerfile follows best practices (multi-stage, non-root user, HEALTHCHECK, pinned versions)
- Dependencies are minimal and production-only (no dev tools or test frameworks)
- Environment variables are used for configuration (model path, port, log level)
- Model versioning is embedded in the serving response
- API documentation (OpenAPI/Swagger) is auto-generated

### Data Quality Review

Check for these issues:

**Completeness:**
- Missing value rates are documented per feature
- Missing value strategy is appropriate (imputation, deletion, indicator variables)
- Features with >50% missing values are flagged for investigation
- Data schema is validated before training (expected columns, types, ranges)

**Consistency:**
- Target variable distribution is analyzed (check for extreme imbalance)
- Feature distributions are checked for anomalies (unexpected spikes, constant values)
- Duplicate records are identified and handled
- Categorical values are validated against expected vocabularies
- Numerical features are checked for unreasonable ranges or units

**Representativeness:**
- Training data distribution is compared to expected production distribution
- Temporal coverage is sufficient for the prediction task
- Class distribution is documented and accounted for (oversampling, class weights, or metric selection)
- Train/test distribution similarity is verified (no significant population shift)

**Integrity:**
- Data pipeline is idempotent (rerunning produces the same result)
- Data versioning is in place (DVC, LakeFS, or manual versioning)
- Data lineage is documented (source, transformations, filtering criteria)
- Personally identifiable information (PII) is handled appropriately

## Output Format

For each reviewed file, provide:

```
## Review: <filename>

### Summary
<one-line assessment: PASS / NEEDS ATTENTION / CRITICAL>

### Issues Found

#### Critical
- [ ] <issue description> - <specific line or section> - <fix recommendation>

#### Warnings
- [ ] <issue description> - <specific line or section> - <fix recommendation>

#### Suggestions
- [ ] <improvement description> - <rationale>

### Score: X/10
```

After all files are reviewed, provide an overall ML pipeline health summary with:
1. Top 3 action items ranked by risk severity
2. Reproducibility assessment (can the training be exactly reproduced?)
3. Production readiness assessment (is the model deployable as-is?)
4. Data quality assessment (are there data issues that could affect model reliability?)
