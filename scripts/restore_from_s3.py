import os
import boto3

def download_dir_from_s3(bucket, s3_prefix, local_dir):
    s3 = boto3.client("s3")
    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket, Prefix=s3_prefix):
        for obj in page.get('Contents', []):
            s3_key = obj['Key']
            rel_path = os.path.relpath(s3_key, s3_prefix)
            local_path = os.path.join(local_dir, rel_path)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            print(f"Downloading s3://{bucket}/{s3_key} to {local_path}")
            s3.download_file(bucket, s3_key, local_path)

if __name__ == "__main__":
    bucket = os.environ["GIMBR_S3_BUCKET"]
    download_dir_from_s3(bucket, "model-backups/", "models/trained")
    download_dir_from_s3(bucket, "metrics-backups/", "models/evaluation")