import yaml
import pandas as pd
from src.models.train import train_model

if __name__ == "__main__":
    with open("config/model_config.yaml") as f:
        model_cfg = yaml.safe_load(f)
    df = pd.read_csv("data/processed/features.csv")
    model = train_model(df, model_cfg, "models/trained/")
    print("Model training complete.")