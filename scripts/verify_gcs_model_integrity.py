from src.cloud.storage import download_from_gcs
import os
import hashlib

def check_hash(local_path, expected_hash):
    h = hashlib.sha256()
    with open(local_path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest() == expected_hash

if __name__ == "__main__":
    bucket = os.environ["GIMBR_GCS_BUCKET"]
    gcs_key = "prod/model.joblib"
    local_path = "models/production/model_gcs_downloaded.joblib"
    expected_hash = os.environ.get("GIMBR_MODEL_SHA256")
    download_from_gcs(bucket, gcs_key, local_path)
    if expected_hash:
        if check_hash(local_path, expected_hash):
            print("GCS model integrity check: OK")
        else:
            print("WARNING: GCS model integrity check FAILED")
    else:
        print("No expected hash provided, download complete.")