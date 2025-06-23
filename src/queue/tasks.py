from celery import Celery
import os

celery_app = Celery("gimbr", broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0"))

@celery_app.task
def retrain_model_task():
    import subprocess
    subprocess.run(["python", "scripts/retrain_model.py"], check=True)
    return "Retrain complete"