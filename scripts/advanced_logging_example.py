from src.logging.advanced_logger import app_json_logger

app_json_logger.info("Batch inference started", extra={"user": "automation", "job_id": "20250623-001"})
try:
    # some code
    pass
except Exception as e:
    app_json_logger.error("Batch inference failed", extra={"err": str(e)})