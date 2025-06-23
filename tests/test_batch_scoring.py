import pytest
import pandas as pd
from src.models.batch_score import batch_predict

def test_batch_predict_basic(tmp_path):
    df = pd.DataFrame({
        "structure_id": ["A", "B"],
        "f1": [1.0, 2.0],
        "f2": [3.4, 2.2]
    })
    class DummyModel:
        def predict_proba(self, X):
            return [[0.7, 0.3]] * len(X)
    model = DummyModel()
    results = batch_predict(model, df)
    assert isinstance(results, pd.DataFrame)
    assert "failure_probability" in results.columns
    assert len(results) == 2