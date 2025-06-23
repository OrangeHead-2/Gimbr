import pytest
import pandas as pd
from src.reporting.looker import export_to_looker

def test_export_to_looker(tmp_path, monkeypatch):
    # Simulate Looker export by writing to a temp CSV
    test_df = pd.DataFrame({"structure_id": [1, 2], "failure_probability": [0.3, 0.7]})
    out_csv = tmp_path / "looker_export.csv"
    monkeypatch.setattr("src.reporting.looker.upload_to_looker_studio", lambda x, y: True)
    result = export_to_looker(test_df, str(out_csv))
    assert result is True