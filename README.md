# Gimbr - Bridge Failure Prediction Platform

A full-stack, production-grade ML system for predicting bridge failure risk, featuring robust data pipelines, model training and monitoring, CI/CD, cloud deployment, and modern dashboard UIs.

---

## Features

- **Data ingestion & feature engineering** (CSV, DVC, drift detection)
- **Model training** (Random Forest, quantization, ONNX export)
- **Experiment tracking & model registry** (MLflow, DVC)
- **Deployment** (SageMaker, AzureML, Vertex AI, Kubernetes, Ray Serve)
- **Batch & real-time serving**
- **Monitoring** (Prometheus, metrics, alerting, drift detection)
- **Automation & CI/CD** (GitHub Actions, Airflow, Databricks Jobs)
- **User dashboards** (Streamlit, Gradio, Looker Studio)
- **Alerting** (Slack notifications)
- **Cloud-native configuration** (YAML/JSON config, Docker Compose, environment variables)

---

## Directory Structure

```
.
├── configs/                # YAML/JSON for models, data, env, dashboards
├── src/
│   ├── data/               # Data ingestion, DVC, drift
│   ├── models/             # Training, quantization, ONNX export
│   ├── registry/           # MLflow, DVC registry sync
│   ├── deployment/         # Cloud/K8s deployment utilities
│   ├── metrics/            # Metrics logging
│   ├── drift/              # Statistical drift detection
│   ├── alerting/           # Slack, Prometheus alerting
│   ├── reporting/          # Looker Studio, CSV export
│   ├── ci_cd/              # GitHub Actions, pipeline triggers
│   ├── monitoring/         # Prometheus export
│   ├── serve/              # Ray Serve, Gradio endpoints
│   ├── dashboard/          # Streamlit dashboard
│   └── jobs/               # Airflow, Databricks
├── tests/                  # Pytest modules
├── assets/                 # UI assets (logo, CSS, JS)
├── dags/                   # Airflow DAGs
├── notebooks/              # Exploratory and DAG code
├── requirements.txt
├── docker-compose.yaml
├── .env.template
└── README.md
```

---

## Getting Started

1. **Clone the repo**
2. **Set up your environment:**
   - Copy `.env.template` to `.env` and fill your secrets.
   - Install dependencies:  
     `pip install -r requirements.txt`
3. **Run services locally:**
   - `docker-compose up`
   - Access FastAPI at `localhost:8000`, MLflow at `localhost:5000`, Prometheus at `localhost:9090`, Airflow at `localhost:8080`
4. **Train & register model:**
   - See `src/models/train.py` and `src/models/register.py`
5. **Serve predictions:**
   - REST API (`src/serve/ray_app.py`), Gradio (`src/serve/gradio_interface.py`), Streamlit (`src/dashboard/streamlit_dashboard.py`)
6. **Monitor, visualize, and get alerts via dashboards and Slack.**

---

## Module Documentation

### `src/data/`

- **ingestion.py**  
  - `load_bridge_data(path)`: Loads CSV bridge data.
  - `validate_bridge_data(df)`: Validates schema and required columns.
- **dvc_integration.py**  
  - `dvc_add(path)`, `dvc_pull()`: DVC CLI wrappers.
- **feature_engineering.py**  
  - `add_traffic_features(df)`, etc.: Feature pipeline steps.

### `src/models/`

- **train.py**  
  - Model training, validation, serialization.
- **quantization.py**  
  - `quantize_rf(rf_model)`: Quantizes RandomForest weights (float16).
- **export_onnx.py**  
  - `export_to_onnx(model, X_sample, path)`: Exports model to ONNX.
- **register.py**  
  - Registers model in MLflow.

### `src/registry/`

- **sync.py**  
  - Registry sync for MLflow & DVC.

### `src/deployment/`

- **sagemaker.py**, **azureml.py**, **vertexai.py**  
  - `deploy_model_*`: Deploys trained model to respective cloud.
- **kubernetes.py**  
  - `deploy_model_kubernetes(yaml_path)`: K8s deployment via YAML.

### `src/metrics/`

- **pipeline_metrics.py**  
  - `PipelineMetricsLogger`: Logs training/serving metrics as JSON lines.

### `src/drift/`

- **detection.py**  
  - `compute_ks_drift(ref, prod)`: Kolmogorov-Smirnov test for drift.

### `src/alerting/`

- **slack.py**  
  - `send_slack_alert(msg, webhook)`: Slack notifications.
- **prometheus_alerts.py**  
  - Prometheus alert rules.

### `src/reporting/`

- **looker.py**  
  - `export_to_looker(df, path)`: Preps and uploads results to Looker Studio.

### `src/ci_cd/`

- **github_actions.py**  
  - `run_pipeline_step(cmd)`: Pipeline command runner.
- **airflow_dag.py**  
  - Airflow DAG definitions.

### `src/monitoring/`

- **prometheus_metrics.py**  
  - Prometheus metrics client for FastAPI endpoints.

### `src/serve/`

- **ray_app.py**  
  - Ray Serve ASGI app for REST inference.
- **gradio_interface.py**  
  - Gradio UI for predictions.

### `src/dashboard/`

- **streamlit_dashboard.py**  
  - Streamlit UI for predictions, drift, metrics.

### `src/jobs/`

- **databricks_job.py**  
  - Databricks batch prediction job runners.

---

## Configuration

- All configs are in `configs/` (YAML/JSON):  
  - `model_config.yaml`
  - `data_config.yaml`
  - `environment.yaml`
  - `dashboard_assets.yaml`
  - Prometheus, Airflow, DVC, MLflow, etc.

---

## Testing

- Run all tests with:  
  `pytest tests/`
- Each core module has full test coverage in `tests/`.

---

## CI/CD

- See `.github/workflows/` or `configs/github_actions_ci.yaml` for build, test, and lint pipelines.
- Airflow and Databricks jobs are defined in `dags/` and `src/jobs/`.

---

## Deployment

- **Docker Compose**: launches all services for local dev.
- **Cloud**: Sagemaker, AzureML, Vertex AI, K8s (see `src/deployment`).
- **Monitoring**: Prometheus scrapes metrics, alerting via Slack and Prometheus rules.

---

## Dashboards

- **Streamlit**: `src/dashboard/streamlit_dashboard.py`
- **Gradio**: `src/serve/gradio_interface.py`
- **Looker Studio**: See `src/reporting/looker.py` and config.
- **Assets**: All UI assets (CSS, JS, logos) in `assets/`

---

## License

MIT

---

## Maintainers

- [yourorg](https://github.com/yourorg)
- [OrangeHead-2](https://github.com/OrangeHead-2)

---
