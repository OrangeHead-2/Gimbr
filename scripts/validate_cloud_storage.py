from src.cloud.storage import upload_to_gcs, download_from_gcs
import os

if __name__ == "__main__":
    model_path = "models/production/model.joblib"
    bucket = os.environ["GIMBR_GCS_BUCKET"]
    gcs_key = "test/model_validation.joblib"
    upload_to_gcs(model_path, bucket, gcs_key)
    print(f"Uploaded to gs://{bucket}/{gcs_key}")
    # Download to temp file for test
    download_path = "models/production/model_downloaded.joblib"
    download_from_gcs(bucket, gcs_key, download_path)
    print(f"Downloaded back to {download_path}")
    assert os.path.getsize(model_path) == os.path.getsize(download_path), "Mismatch in file sizes!"
    print("Cloud storage validation complete.")