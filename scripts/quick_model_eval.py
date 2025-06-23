import pandas as pd
import joblib

if __name__ == "__main__":
    df = pd.read_csv("data/processed/features.csv")
    model = joblib.load("models/trained/model.joblib")
    features = [c for c in df.columns if c not in ['structure_id', 'failure_within_1yr']]
    X = df[features]
    y = df['failure_within_1yr']
    score = model.score(X, y)
    print(f"Model raw accuracy: {score:.3f}")