from google.cloud import storage

def upload_to_gcs(local_path, bucket, gcs_key):
    client = storage.Client()
    b = client.bucket(bucket)
    blob = b.blob(gcs_key)
    blob.upload_from_filename(local_path)

def download_from_gcs(bucket, gcs_key, local_path):
    client = storage.Client()
    b = client.bucket(bucket)
    blob = b.blob(gcs_key)
    blob.download_to_filename(local_path)