import pandas as pd

def schema_from_df(df):
    return {col: str(dtype) for col, dtype in df.dtypes.items()}

if __name__ == "__main__":
    ref_file = "data/processed/infra_training.csv"
    new_file = "data/processed/infra_training_new.csv"
    ref_df = pd.read_csv(ref_file, nrows=100)
    new_df = pd.read_csv(new_file, nrows=100)
    ref_schema = schema_from_df(ref_df)
    new_schema = schema_from_df(new_df)
    schema_diff = {k: (ref_schema[k], new_schema[k])
                   for k in ref_schema if k in new_schema and ref_schema[k] != new_schema[k]}
    missing = [k for k in ref_schema if k not in new_schema]
    extra = [k for k in new_schema if k not in ref_schema]
    if schema_diff or missing or extra:
        print("Schema differences detected:")
        if schema_diff:
            print("  Changed columns:", schema_diff)
        if missing:
            print("  Missing columns in new:", missing)
        if extra:
            print("  Extra columns in new:", extra)
    else:
        print("No schema differences detected.")