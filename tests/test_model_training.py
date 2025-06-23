import pytest
import pandas as pd
from src.models.train import train_model

def test_train_model_runs(tmp_path):
    df = pd.DataFrame({
        "f1": [0.1, 0.2, 0.3, 0.4],
        "f2": [1, 2, 3, 4],
        "failure_within_1yr": [0, 1, 0, 1]
    })
    model, metrics = train_model(df, target_col="failure_within_1yr")
    assert hasattr(model, "predict")
    assert "roc_auc" in metrics
    assert metrics["roc_auc"] >= 0 and metrics["roc_auc"] <= 1