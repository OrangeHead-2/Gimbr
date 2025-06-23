from celery import Celery

celery_app = Celery(
    "gimbr_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1"
)

@celery_app.task
def retrain_model_task():
    import subprocess
    subprocess.run(["python", "scripts/train_model.py"])

@celery_app.task
def notify_maintenance_alert(structure_id: str, risk: float):
    from src.notification.slack import send_slack_alert
    webhook = "https://hooks.slack.com/services/..."
    message = f"ALERT: Structure {structure_id} at risk {risk:.2f}"
    send_slack_alert(webhook, message)