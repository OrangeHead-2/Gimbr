import pandas as pd
from src.models.train import train_model

def test_train_model_runs(tmp_path):
    df = pd.DataFrame({
        'structure_id': [1,2,3,4],
        'avg_daily_traffic': [10000, 25000, 5000, 40000],
        'bridge_condition': ['Good', 'Poor', 'Fair', 'Excellent'],
        'last_maintenance_date': ['2023-01-01']*4,
        'inspection_date': ['2024-01-01']*4,
        'failure_within_1yr': [0, 1, 0, 0]
    })
    model = train_model(df, "config/model_config.yaml", tmp_path)
    assert hasattr(model, "predict_proba")