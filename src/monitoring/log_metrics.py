import json
from datetime import datetime
import os

def log_metric(metric_name, value, meta=None, log_file="logs/metrics.log"):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "metric": metric_name,
        "value": value,
        "meta": meta or {}
    }
    with open(log_file, "a") as f:
        f.write(json.dumps(record) + "\n")