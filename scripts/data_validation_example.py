import pandas as pd
from src.validation.data_validation import DataValidator

schema = {
    "structure_id": "object",
    "inspection_date": "datetime64[ns]",
    "failure_within_1yr": "int64"
}
required = ["structure_id", "inspection_date", "failure_within_1yr"]

df = pd.read_csv("data/processed/infra_training.csv")
validator = DataValidator(schema=schema, required=required)
try:
    df = validator.validate(df, subset=["structure_id"], allowed_null=["corrosion_level"])
except Exception as e:
    print(f"Validation failed: {e}")
    exit(1)