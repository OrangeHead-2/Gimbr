import pandas as pd
import os

class FeatureStore:
    def __init__(self, path='data/processed/features.parquet'):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
    
    def save(self, df: pd.DataFrame):
        df.to_parquet(self.path, index=False)
    
    def load(self) -> pd.DataFrame:
        return pd.read_parquet(self.path)