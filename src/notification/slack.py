import requests

def send_slack_alert(webhook, message):
    if not webhook:
        raise RuntimeError("No Slack webhook URL provided")
    r = requests.post(webhook, json={"text": message})
    if r.status_code != 200:
        raise RuntimeError(f"Slack webhook failed: {r.status_code} {r.text}")