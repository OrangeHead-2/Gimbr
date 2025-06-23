# Module Documentation

## Data Ingestion & Management (`src/data/`)

### ingestion.py
- `load_bridge_data(path: str) -> pd.DataFrame`  
  Loads bridge data from a CSV or remote URL.
- `validate_bridge_data(df: pd.DataFrame) -> bool`  
  Checks for schema validity.
- `save_processed_data(df, path)`  
  Writes processed features to disk.

### dvc_integration.py
- `dvc_add(path: str) -> int`  
  Wrapper for `dvc add`.
- `dvc_pull() -> int`  
  Wrapper for `dvc pull`.

### feature_engineering.py
- `add_traffic_features(df)`, `add_env_features(df)`, `normalize(df)`  
  Feature engineering steps.

---

## Model Training & Export (`src/models/`)

### train.py
- Loads features, splits data, trains model, saves artifact.

### quantization.py
- `quantize_rf(rf_model)`  
  Converts RandomForest weights to float16.

### export_onnx.py
- `export_to_onnx(model, X_sample, path)`  
  Exports model to ONNX for cross-platform serving.

### register.py
- Registers and stages model in MLflow or DVC.

---

## Model Registry Sync (`src/registry/`)

### sync.py
- `RegistrySync(registry)`  
  Pushes/pulls models to/from a model registry.

---

## Deployment (`src/deployment/`)

### sagemaker.py
- `deploy_model_sagemaker(model, name, instance_type)`  
  Deploys model to AWS SageMaker.

### azureml.py
- `deploy_model_azureml(model, name, compute_type)`  
  Deploys model to Azure ML.

### vertexai.py
- `deploy_model_vertexai(model, name, machine_type)`  
  Deploys to Google Vertex AI.

### kubernetes.py
- `deploy_model_kubernetes(yaml_path)`  
  Deploys via K8s manifest.

---

## Metrics & Monitoring (`src/metrics/`, `src/monitoring/`)

### pipeline_metrics.py
- `PipelineMetricsLogger(log_path)`  
  Logs metrics as JSON lines.

### prometheus_metrics.py
- `PrometheusMetrics`  
  Exposes counters/histograms for API metrics.

---

## Data Drift Detection (`src/drift/`)

### detection.py
- `compute_ks_drift(ref: pd.Series, prod: pd.Series) -> (float, float)`  
  KS test for detecting drift.

---

## Alerting (`src/alerting/`)

### slack.py
- `send_slack_alert(msg, webhook_url)`  
  POSTs alert to Slack.

### prometheus_alerts.py
- Defines Prometheus alerting rules.

---

## Reporting (`src/reporting/`)

### looker.py
- `export_to_looker(df, out_path)`  
  Exports predictions to Google Sheets or Looker.

---

## CI/CD Integration (`src/ci_cd/`)

### github_actions.py
- `run_pipeline_step(cmd, raise_on_error=True)`  
  Runs a shell command, raises or logs error.

### airflow_dag.py
- Defines Airflow DAGs for batch pipelines.

---

## Model Serving (`src/serve/`)

### ray_app.py
- Ray Serve ASGI app, `/predict` and `/health` endpoints.

### gradio_interface.py
- Gradio web interface for real-time predictions.

---

## Dashboards (`src/dashboard/`)

### streamlit_dashboard.py
- Streamlit dashboard for metrics, drift, predictions.

---

## Batch Jobs (`src/jobs/`)

### databricks_job.py
- Loads model, runs batch predictions, writes output CSV.

---

## UI Assets (`assets/`)

- **custom.css**: Theme and layout.
- **dashboard.js**: JS for interactivity.
- **logo.png**, **favicon.ico**: Branding.

---

## Configurations (`configs/`)

- **model_config.yaml**: Model architecture and registry settings.
- **data_config.yaml**: Data sources, splits, DVC paths.
- **environment.yaml**: Dependencies, environment variables.
- **dashboard_assets.yaml**: Theme, layout, components for dashboards.
- **prometheus_config.yaml**, **airflow_config.yaml**, **dvc_config.yaml**, **mlflow_config.yaml**: Service configs.
- **github_actions_ci.yaml**, **docker-compose.yaml**, **requirements.yaml**: CI/CD and deployment.

---

## Testing (`tests/`)

- **test_***.py: Unit tests for every module.
    - Data ingestion, registry, metrics, drift, alerting, quantization, ONNX export, deployment, serving, dashboards, DVC, Airflow, Databricks, Looker, etc.

---

## Notebooks (`notebooks/`)

- Exploratory data analysis, feature engineering, DAG prototyping.

---

## Airflow DAGs (`dags/`)

- Production pipeline orchestration.

---