import joblib
import pandas as pd

if __name__ == "__main__":
    model = joblib.load("models/trained/model.joblib")
    df = pd.read_csv("data/processed/features.csv")
    features = [c for c in df.columns if c not in ['structure_id', 'failure_within_1yr']]
    importance = model.feature_importances_
    fi_df = pd.DataFrame({"feature": features, "importance": importance})
    fi_df = fi_df.sort_values("importance", ascending=False)
    fi_df.to_csv("models/evaluation/feature_importance.csv", index=False)
    print("Feature importance report generated: models/evaluation/feature_importance.csv")