import pytest
import pandas as pd
from src.data.ingestion import load_bridge_data, validate_bridge_data

def test_load_bridge_data(tmp_path):
    # Create a dummy CSV
    data = pd.DataFrame({"structure_id": [1, 2], "feature": [10, 20]})
    csv_path = tmp_path / "bridges.csv"
    data.to_csv(csv_path, index=False)
    df = load_bridge_data(str(csv_path))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)

def test_validate_bridge_data():
    valid = pd.DataFrame({"structure_id": [1, 2], "feature": [10, 20]})
    invalid = pd.DataFrame({"feature": [5, 10]})
    assert validate_bridge_data(valid) is True
    assert validate_bridge_data(invalid) is False