import os
from src.alerting.email_alert import send_email_alert

if __name__ == "__main__":
    metrics_file = "models/evaluation/metrics.json"
    to_emails = ["ops-team@example.com"]
    smtp_server = os.environ["SMTP_SERVER"]
    smtp_port = int(os.environ["SMTP_PORT"])
    smtp_user = os.environ["SMTP_USER"]
    smtp_password = os.environ["SMTP_PASSWORD"]

    with open(metrics_file) as f:
        body = f.read()

    subject = "Gimbr Model Metrics Report"
    send_email_alert(subject, body, to_emails, smtp_server, smtp_port, smtp_user, smtp_password)
    print("Email report sent.")