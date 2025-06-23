from celery.result import AsyncResult
from src.tasks.celery_worker import celery_app

if __name__ == "__main__":
    # This script checks if celery is up and can accept jobs
    result = celery_app.send_task("src.tasks.celery_worker.retrain_model_task")
    print(f"Submitted retrain task: {result.id}")
    result = AsyncResult(result.id)
    print("Waiting for task status...")
    result.wait(timeout=10)
    print(f"Task status: {result.status}")