import os
from src.cloud.storage import upload_to_gcs

if __name__ == "__main__":
    model_path = "models/trained/model.joblib"
    bucket = os.environ["GIMBR_GCS_BUCKET"]
    gcs_key = "prod/model.joblib"
    upload_to_gcs(model_path, bucket, gcs_key)
    print(f"Uploaded {model_path} to gs://{bucket}/{gcs_key}")