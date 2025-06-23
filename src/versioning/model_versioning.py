import os
import joblib
import shutil
from datetime import datetime

def save_versioned_model(model, base_dir="models/versions"):
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    version_dir = os.path.join(base_dir, ts)
    os.makedirs(version_dir, exist_ok=True)
    model_path = os.path.join(version_dir, "model.joblib")
    joblib.dump(model, model_path)
    latest_path = os.path.join(base_dir, "latest")
    if os.path.islink(latest_path) or os.path.exists(latest_path):
        if os.path.islink(latest_path):
            os.unlink(latest_path)
        else:
            shutil.rmtree(latest_path)
    os.symlink(version_dir, latest_path)
    return model_path