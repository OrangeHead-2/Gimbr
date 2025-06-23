import pandas as pd
from src.models.train import drift_detection

if __name__ == "__main__":
    # Compare recent data with reference data to detect drift
    ref_df = pd.read_csv("data/processed/features.csv")
    new_df = pd.read_csv("data/processed/features_new.csv")
    feature_cols = [c for c in ref_df.columns if c not in ['structure_id', 'failure_within_1yr']]
    drift_report = drift_detection(new_df, ref_df, feature_cols)
    drifted = {k: v for k, v in drift_report.items() if v['p_value'] < 0.05}
    if drifted:
        print("Drift detected in columns:", drifted)
        import json
        with open("models/evaluation/drift_report.json", "w") as f:
            json.dump(drift_report, f, indent=2)
    else:
        print("No significant feature drift detected.")