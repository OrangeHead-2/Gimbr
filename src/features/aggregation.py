import pandas as pd

def aggregate_by_region(df, region_col, agg_cols=None):
    if agg_cols is None:
        agg_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    agg = df.groupby(region_col)[agg_cols].mean().reset_index()
    return agg