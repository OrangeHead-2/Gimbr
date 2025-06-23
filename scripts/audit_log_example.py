from src.audit.audit_log import AuditLogger

audit_logger = AuditLogger()
audit_logger.log_action(user="admin", action="model_train", details="training started")
# On failure
audit_logger.log_failure(user="admin", action="model_train", details="out of memory")