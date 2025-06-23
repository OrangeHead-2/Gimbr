import pandas as pd

def preprocess_pipeline(df, schema, impute_strategy, win_cols):
    # Cast columns
    for col, dtype in schema.items():
        if col in df.columns:
            try:
                df[col] = df[col].astype(dtype)
            except Exception:
                pass
    # Fill missing values
    for col, strat in impute_strategy.items():
        if col in df.columns:
            if strat == "mean":
                df[col] = df[col].fillna(df[col].mean())
            else:
                df[col] = df[col].fillna(strat)
    # Rolling mean (window=3 for demo)
    for col in win_cols:
        if col in df.columns:
            df[col + "_rolling_mean"] = df[col].rolling(window=3, min_periods=1).mean()
    return df