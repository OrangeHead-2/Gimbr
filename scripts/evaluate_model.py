import pandas as pd
import joblib
from src.models.evaluate import evaluate_classification, save_evaluation

if __name__ == "__main__":
    df = pd.read_csv("data/processed/features.csv")
    model = joblib.load("models/trained/model.joblib")
    features = [c for c in df.columns if c not in ['structure_id', 'failure_within_1yr']]
    X = df[features]
    y = df['failure_within_1yr']
    y_probs = model.predict_proba(X)[:, 1]
    y_pred = model.predict(X)
    results = evaluate_classification(y, y_pred, y_probs)
    save_evaluation(results)
    print("Model evaluation complete. Results saved to models/evaluation/metrics.json")