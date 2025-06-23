import joblib
import pandas as pd

class ModelServer:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, df):
        features = [c for c in df.columns if c not in ['structure_id', 'failure_within_1yr']]
        return self.model.predict_proba(df[features])[:, 1]