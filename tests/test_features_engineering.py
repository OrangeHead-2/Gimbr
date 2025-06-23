import pytest
import pandas as pd
from src.features.engineering import add_traffic_features, add_env_features

def test_add_traffic_features():
    df = pd.DataFrame({
        "structure_id": [1, 2],
        "avg_daily_traffic": [1000, 2000]
    })
    out = add_traffic_features(df)
    assert 'traffic_bin' in out.columns
    assert out.shape[0] == 2

def test_add_env_features():
    df = pd.DataFrame({
        "structure_id": [1, 2],
        "soil_type": ["loam", "clay"]
    })
    out = add_env_features(df)
    assert 'soil_score' in out.columns
    assert out.shape[0] == 2