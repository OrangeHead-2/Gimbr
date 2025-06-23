from src.tasks.celery_worker import retrain_model_task, notify_maintenance_alert

def launch_retrain_job():
    # This will execute asynchronously
    retrain_model_task.delay()

def send_critical_alert(structure_id, risk):
    notify_maintenance_alert.delay(structure_id, risk)