import pandas as pd
from src.validation.data_validation import DataValidator

if __name__ == "__main__":
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
    required = list(schema.keys())
    files = [
        "data/raw/bridges.csv",
        "data/processed/infra_training.csv",
        "data/processed/features.csv"
    ]
    validator = DataValidator(schema=schema, required=required)
    for f in files:
        try:
            df = pd.read_csv(f)
            df = validator.validate(df)
            print(f"Validation OK: {f}")
        except Exception as e:
            print(f"Validation FAILED for {f}: {e}")