from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import joblib
import pandas as pd
import os
import jwt

from src.features.engineering import feature_pipeline
from src.security.rate_limit import limiter, register_rate_limit
from src.audit.audit_log import AuditLogger
from src.monitoring.sentry_integration import init_sentry

app = FastAPI(title="Gimbr Predictive Maintenance API")
security = HTTPBearer()
model = joblib.load(os.getenv("MODEL_PATH", "models/trained/model.joblib"))
SECRET = os.getenv("SECRET", "YOUR_SECRET")
SENTRY_DSN = os.getenv("SENTRY_DSN", "")

# Initialize Sentry if DSN provided
if SENTRY_DSN:
    init_sentry(SENTRY_DSN)

# Register rate limiting
register_rate_limit(app)

audit_logger = AuditLogger()

def verify_jwt(token: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(token.credentials, SECRET, algorithms=["HS256"])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload

@app.post("/predict")
@limiter.limit("5/minute")
def predict(data: list, user=Depends(verify_jwt), request: Request = None):
    try:
        df = pd.DataFrame(data)
        df = feature_pipeline(df)
        features = [c for c in df.columns if c not in ['structure_id', 'failure_within_1yr']]
        preds = model.predict_proba(df[features])[:, 1]
        audit_logger.log_action(user.get("user", "unknown"), "predict", status="success")
        return [{"structure_id": sid, "failure_probability": float(p)} for sid, p in zip(df['structure_id'], preds)]
    except Exception as e:
        audit_logger.log_failure(user.get("user", "unknown"), "predict", str(e))
        raise HTTPException(status_code=500, detail=str(e))