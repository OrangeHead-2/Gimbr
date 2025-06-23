import pandas as pd

def add_time_features(df, date_col):
    if date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col])
        df["year"] = df[date_col].dt.year
        df["month"] = df[date_col].dt.month
        df["dayofweek"] = df[date_col].dt.dayofweek
        df["dayofyear"] = df[date_col].dt.dayofyear
    return df