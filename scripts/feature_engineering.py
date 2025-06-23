import pandas as pd
from src.features.engineering import feature_pipeline

if __name__ == "__main__":
    df = pd.read_csv("data/processed/infra_training.csv")
    df = feature_pipeline(df)
    df.to_csv("data/processed/features.csv", index=False)
    print("Feature engineering complete: data/processed/features.csv")