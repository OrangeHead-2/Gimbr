import pandas as pd
from src.notification.slack import send_slack_alert

if __name__ == "__main__":
    pred_file = "models/evaluation/predictions.csv"
    webhook = "https://hooks.slack.com/services/XXXX/YYY/ZZZ"  # secure this in prod!
    df = pd.read_csv(pred_file)
    high_risk = df[df["failure_probability"] >= 0.75]
    for _, row in high_risk.iterrows():
        msg = f"Critical Alert: Structure {row['structure_id']} has predicted failure risk {row['failure_probability']:.2%}. Immediate review needed."
        send_slack_alert(webhook, msg)
    print(f"Sent {len(high_risk)} batch alerts.")