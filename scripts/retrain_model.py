import yaml
import pandas as pd
from src.data.preprocessing import preprocess_pipeline
from src.features.engineering import feature_pipeline
from src.models.train import train_model
from src.models.evaluate import evaluate_classification, save_evaluation

if __name__ == "__main__":
    with open("config/data_config.yaml") as f:
        data_cfg = yaml.safe_load(f)
    with open("config/model_config.yaml") as f:
        model_cfg = yaml.safe_load(f)
    schema = {
        "structure_id": "object",
        "inspection_date": "datetime64[ns]",
        "last_maintenance_date": "datetime64[ns]",
        "avg_daily_traffic": "float64",
        "bridge_condition": "object",
        "failure_within_1yr": "int64",
        "latitude": "float64",
        "longitude": "float64",
        "precipitation": "float64",
        "avg_temp": "float64",
        "corrosion_level": "float64",
        "previous_failures": "int64",
        "soil_type": "object",
        "region_code": "object"
    }
    impute_strategy = {
        "avg_daily_traffic": "mean",
        "precipitation": "mean",
        "avg_temp": "mean",
        "corrosion_level": 0,
        "previous_failures": 0
    }
    win_cols = ["avg_daily_traffic", "precipitation", "avg_temp", "corrosion_level"]

    # Preprocess
    df = pd.read_csv("data/raw/bridges.csv")
    df = preprocess_pipeline(df, schema, impute_strategy, win_cols)
    df = feature_pipeline(df)
    df.to_csv("data/processed/features.csv", index=False)

    # Train
    model = train_model(df, model_cfg, "models/trained/")

    # Evaluate
    features = [c for c in df.columns if c not in ['structure_id', 'failure_within_1yr']]
    X = df[features]
    y = df['failure_within_1yr']
    y_probs = model.predict_proba(X)[:, 1]
    y_pred = model.predict(X)
    results = evaluate_classification(y, y_pred, y_probs)
    save_evaluation(results)
    print("Retraining complete. Model and metrics updated.")