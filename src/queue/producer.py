from celery import Celery
import os

celery_app = Celery("gimbr", broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0"))

def enqueue_job(name, args=None, kwargs=None):
    celery_app.send_task(name, args=args or [], kwargs=kwargs or {})