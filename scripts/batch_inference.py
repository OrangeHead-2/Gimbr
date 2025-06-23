import sys
import pandas as pd
import joblib
from src.features.engineering import feature_pipeline

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/batch_inference.py input.csv output.csv")
        sys.exit(1)
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    df = pd.read_csv(input_csv)
    df = feature_pipeline(df)
    model = joblib.load("models/trained/model.joblib")
    features = [c for c in df.columns if c not in ['structure_id', 'failure_within_1yr']]
    df['failure_probability'] = model.predict_proba(df[features])[:, 1]
    df[['structure_id', 'failure_probability']].to_csv(output_csv, index=False)
    print(f"Batch inference complete. Results written to {output_csv}")