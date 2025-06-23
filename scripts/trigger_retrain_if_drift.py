import json
import subprocess

if __name__ == "__main__":
    drift_report_path = "models/evaluation/drift_report.json"
    with open(drift_report_path) as f:
        drift_report = json.load(f)
    # If any feature drifted, retrain
    drifted_cols = [k for k, v in drift_report.items() if v.get("p_value", 1) < 0.05]
    if drifted_cols:
        print(f"Drift detected in: {drifted_cols}. Triggering retraining.")
        subprocess.run(["python", "scripts/retrain_model.py"], check=True)
    else:
        print("No drift detected. No retrain needed.")