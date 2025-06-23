import pandas as pd

def postprocess_predictions(df, threshold=0.5):
    """Add a column for high-risk flag."""
    df["high_risk_flag"] = (df["failure_probability"] >= threshold).astype(int)
    return df