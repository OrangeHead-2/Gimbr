import logging
import os
from pythonjsonlogger import jsonlogger

def setup_advanced_logger(name, log_file, level=logging.INFO):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logger = logging.getLogger(name)
    logHandler = logging.FileHandler(log_file)
    formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    logHandler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(logHandler)
    logger.setLevel(level)
    return logger

app_json_logger = setup_advanced_logger("gimbr_json", "logs/app.json.log")