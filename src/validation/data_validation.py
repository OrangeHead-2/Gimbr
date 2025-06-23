import pandas as pd

class DataValidationError(Exception):
    pass

class DataValidator:
    def __init__(self, schema, required=None):
        self.schema = schema
        self.required = required or list(schema.keys())

    def validate_columns(self, df):
        missing = [col for col in self.required if col not in df.columns]
        if missing:
            raise DataValidationError(f"Missing columns: {missing}")

    def validate_types(self, df):
        for col, dtype in self.schema.items():
            if col in df.columns:
                try:
                    df[col] = df[col].astype(dtype)
                except Exception as e:
                    raise DataValidationError(f"Column {col} cannot be cast to {dtype}: {e}")
        return df

    def check_duplicates(self, df, subset):
        dupes = df.duplicated(subset=subset)
        if dupes.any():
            raise DataValidationError(f"Duplicate rows found: {df[dupes]}")

    def check_nulls(self, df, allowed=None):
        allowed = allowed or []
        nulls = df.columns[df.isnull().any()].difference(allowed)
        if len(nulls):
            raise DataValidationError(f"Nulls found in columns: {list(nulls)}")

    def validate(self, df, subset=None, allowed_null=None):
        self.validate_columns(df)
        df = self.validate_types(df)
        if subset:
            self.check_duplicates(df, subset)
        self.check_nulls(df, allowed=allowed_null)
        return df