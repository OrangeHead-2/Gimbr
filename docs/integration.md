# Gimbr: Production Integrations

## Sentry Error Monitoring

- Add `SENTRY_DSN` to your environment.
- Sentry will automatically capture all unhandled exceptions in Python.
- See `src/monitoring/sentry_integration.py` and initialization in `dashboard/api.py`.
- Sentry dashboard shows error traces, context, and performance metrics.

## ECS Deployment

1. Build and push Docker image to ECR:

    ```
    docker build -t gimbr-app .
    docker tag gimbr-app:latest <account_id>.dkr.ecr.<region>.amazonaws.com/gimbr-app:latest
    docker push <account_id>.dkr.ecr.<region>.amazonaws.com/gimbr-app:latest
    ```

2. Register ECS Task Definition using `ecs/task-definition.json`.

3. Create an ECS Fargate service or run standalone tasks.

## Kubernetes Deployment

- Apply secrets:
    ```
    kubectl apply -f k8s/secret.yaml
    ```
- Deploy API and service:
    ```
    kubectl apply -f k8s/deployment.yaml
    ```
- Access via LoadBalancer or Ingress.

## Data Validation Integration

```python
from src.validation.data_validation import DataValidator
schema = {...}
validator = DataValidator(schema)
df = validator.validate(df)
```

## Audit Logging Integration

```python
from src.audit.audit_log import AuditLogger
audit = AuditLogger()
audit.log_action(user="admin", action="predict", details="Request from dashboard")
```

## API Rate Limiting Integration

- Enables in `dashboard/api.py` using `slowapi`.
- Decorate endpoints: `@limiter.limit("10/minute")`

## Distributed Task Queue Integration

- Run: `celery -A src.tasks.celery_worker.celery_app worker`
- Submit async jobs: `retrain_model_task.delay()`

## Advanced Logging

- Use `app_json_logger` for structured logs.
- Log files in `logs/app.json.log` for ingestion by ELK/Splunk/CloudWatch.

---

For more, see each module's Python docstrings and comments.