import pytest
import pandas as pd
import os
from src.jobs.databricks_job import run_databricks_job

def test_run_databricks_job(monkeypatch, tmp_path):
    # Simulate Databricks job: input CSV, output CSV, and a dummy model
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"
    df = pd.DataFrame({"structure_id": [1, 2], "f1": [0.1, 0.2], "f2": [0.5, 0.6]})
    df.to_csv(input_csv, index=False)
    monkeypatch.setattr("src.jobs.databricks_job.load_model", lambda *a, **k: type("Dummy", (), {"predict_proba": lambda self, X: [[0.1,0.9]]*len(X)})())
    run_databricks_job(input_path=str(input_csv), output_path=str(output_csv))
    assert os.path.exists(output_csv)
    out_df = pd.read_csv(output_csv)
    assert "failure_probability" in out_df.columns