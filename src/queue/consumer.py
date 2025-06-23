from celery import Celery
import os

celery_app = Celery("gimbr", broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0"))

@celery_app.task
def process_inference_job(data):
    # Dummy: just echo back the data
    return data