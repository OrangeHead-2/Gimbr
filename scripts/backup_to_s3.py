import os
import boto3

def upload_dir_to_s3(local_dir, bucket, s3_prefix):
    s3 = boto3.client("s3")
    for root, _, files in os.walk(local_dir):
        for filename in files:
            local_path = os.path.join(root, filename)
            rel_path = os.path.relpath(local_path, local_dir)
            s3_key = os.path.join(s3_prefix, rel_path)
            print(f"Uploading {local_path} to s3://{bucket}/{s3_key}")
            s3.upload_file(local_path, bucket, s3_key)

if __name__ == "__main__":
    bucket = os.environ["GIMBR_S3_BUCKET"]
    upload_dir_to_s3("models/trained", bucket, "model-backups/")
    upload_dir_to_s3("models/evaluation", bucket, "metrics-backups/")