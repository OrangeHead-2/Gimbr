import pandas as pd
from src.notification.slack import send_slack_alert
import os

if __name__ == "__main__":
    pred_file = "models/evaluation/predictions.csv"
    webhook = os.environ.get("GIMBR_SLACK_WEBHOOK")
    threshold = float(os.environ.get("GIMBR_ALERT_THRESHOLD", 0.9))
    df = pd.read_csv(pred_file)
    exceed = df[df["failure_probability"] >= threshold]
    for _, row in exceed.iterrows():
        msg = f"🚨 URGENT: Structure {row['structure_id']} exceeds {threshold:.0%} failure risk ({row['failure_probability']:.2%})"
        send_slack_alert(webhook, msg)
    print(f"Triggered {len(exceed)} urgent alerts.")