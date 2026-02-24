## ML Pipeline Validation Workflows

Define structured validation gates for ML pipelines to ensure quality before promotion. Based on `proagent-repo/core/templates/validation_workflows/ml-engineer.yaml` and `agents/plugins/machine-learning-ops/skills/ml-pipeline-workflow/SKILL.md`:

```yaml
# ml-pipeline-validation.yaml
pipeline:
  name: model-promotion-workflow
  stages:
    - name: data-validation
      checks:
        - schema_match: true
        - null_rate_threshold: 0.05
        - distribution_drift_test: ks_test
        - min_sample_size: 1000

    - name: training-validation
      checks:
        - random_seeds_set: [numpy, random, torch]
        - cross_validation_folds: 5
        - experiment_tracked: true
        - baseline_comparison: required

    - name: evaluation-gate
      checks:
        - min_f1_score: 0.80
        - min_roc_auc: 0.85
        - max_overfitting_gap: 0.05
        - error_analysis_complete: true

    - name: deployment-readiness
      checks:
        - health_endpoint: /health
        - input_validation: pydantic
        - monitoring_configured: true
        - rollback_documented: true
```

## ML Project Structure

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
