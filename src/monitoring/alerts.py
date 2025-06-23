from src.notification.slack import send_slack_alert

def send_model_drift_alert(webhook, drifted_features):
    msg = f"🚨 Model drift detected in features: {', '.join(drifted_features)}"
    send_slack_alert(webhook, msg)