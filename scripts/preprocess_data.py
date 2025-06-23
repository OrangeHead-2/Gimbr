import yaml
import pandas as pd
from src.data.preprocessing import preprocess_pipeline

if __name__ == "__main__":
    with open("config/data_config.yaml") as f:
        data_cfg = yaml.safe_load(f)
    schema = {
        "structure_id": "object",
        "inspection_date": "datetime64[ns]",
        "last_maintenance_date": "datetime64[ns]",
        "avg_daily_traffic": "float64",
        "bridge_condition": "object",
        "failure_within_1yr": "int64",
        "latitude": "float64",
        "longitude": "float64",
        "precipitation": "float64",
        "avg_temp": "float64",
        "corrosion_level": "float64",
        "previous_failures": "int64",
        "soil_type": "object",
        "region_code": "object"
    }
    impute_strategy = {
        "avg_daily_traffic": "mean",
        "precipitation": "mean",
        "avg_temp": "mean",
        "corrosion_level": 0,
        "previous_failures": 0
    }
    win_cols = ["avg_daily_traffic", "precipitation", "avg_temp", "corrosion_level"]

    # Assume one main raw file for simplicity
    inf_path = "data/raw/bridges.csv"
    df = pd.read_csv(inf_path)
    df = preprocess_pipeline(df, schema, impute_strategy, win_cols)
    df.to_csv("data/processed/infra_training.csv", index=False)
    print("Preprocessing complete: data/processed/infra_training.csv")