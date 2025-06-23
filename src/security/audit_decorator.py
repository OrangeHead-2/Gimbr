from src.audit.audit_log import AuditLogger
from functools import wraps

def audited(action):
    logger = AuditLogger()
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                result = fn(*args, **kwargs)
                logger.log_action("api_user", action, status="success")
                return result
            except Exception as e:
                logger.log_failure("api_user", action, str(e))
                raise
        return wrapper
    return decorator