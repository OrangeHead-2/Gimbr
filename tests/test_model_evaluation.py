import pytest
import pandas as pd
from src.models.evaluate import evaluate_model
from sklearn.ensemble import RandomForestClassifier

def test_evaluate_model_binary():
    X = pd.DataFrame({"a": [1,2,3,4], "b": [9,8,7,6]})
    y = [0, 1, 0, 1]
    model = RandomForestClassifier().fit(X, y)
    metrics = evaluate_model(model, X, y)
    assert "roc_auc" in metrics
    assert 0 <= metrics["roc_auc"] <= 1