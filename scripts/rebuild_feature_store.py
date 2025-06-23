import pandas as pd
from src.features.engineering import feature_pipeline

if __name__ == "__main__":
    df = pd.read_csv("data/raw/bridges.csv")
    df = feature_pipeline(df)
    df.to_parquet("data/feature_store/features.parquet")
    print("Feature store rebuilt: data/feature_store/features.parquet")