import logging
import json
import os
from datetime import datetime

class AuditLogger:
    def __init__(self, log_file="logs/audit.log"):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        self.log_file = log_file

    def log_action(self, user, action, status="success", meta=None):
        self._log("ACTION", user, action, status, meta)

    def log_failure(self, user, action, error):
        self._log("FAILURE", user, action, "failure", {"error": error})

    def _log(self, event_type, user, action, status, meta=None):
        entry = {
            "ts": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "user": user,
            "action": action,
            "status": status,
            "meta": meta or {}
        }
        with open(self.log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")