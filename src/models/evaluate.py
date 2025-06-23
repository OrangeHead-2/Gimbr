from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, classification_report
import json
import os

def evaluate_classification(y_true, y_pred, y_probs):
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "f1": float(f1_score(y_true, y_pred)),
        "roc_auc": float(roc_auc_score(y_true, y_probs)),
        "report": classification_report(y_true, y_pred, output_dict=True)
    }

def save_evaluation(results, path="models/evaluation/metrics.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(results, f, indent=2)