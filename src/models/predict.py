import pandas as pd
import joblib

def predict_failure(df, model_path):
    model = joblib.load(model_path)
    features = [c for c in df.columns if c not in ['structure_id', 'failure_within_1yr']]
    preds = model.predict_proba(df[features])[:, 1]
    df['failure_probability'] = preds
    return df[['structure_id', 'failure_probability']]