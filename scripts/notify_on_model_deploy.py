import os
from src.notification.slack import send_slack_alert

if __name__ == "__main__":
    webhook = os.environ.get("GIMBR_SLACK_WEBHOOK")
    model_path = "models/production/model.joblib"
    if os.path.exists(model_path):
        msg = f"✅ New model deployed: {model_path}"
        send_slack_alert(webhook, msg)
        print("Deployment notification sent.")
    else:
        print("No deployed model found for notification.")