import os
from src.alerting.email_alert import send_email_alert

if __name__ == "__main__":
    summary_file = "models/evaluation/metrics.md"
    to_emails = os.environ["SUMMARY_EMAILS"].split(",")
    smtp_server = os.environ["SMTP_SERVER"]
    smtp_port = int(os.environ["SMTP_PORT"])
    smtp_user = os.environ["SMTP_USER"]
    smtp_password = os.environ["SMTP_PASSWORD"]

    with open(summary_file) as f:
        body = f.read()

    subject = "Gimbr Daily Summary Report"
    send_email_alert(subject, body, to_emails, smtp_server, smtp_port, smtp_user, smtp_password)
    print("Daily summary email sent.")