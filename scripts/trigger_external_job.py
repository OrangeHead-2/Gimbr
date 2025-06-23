import requests
import os

if __name__ == "__main__":
    job_url = os.environ.get("EXTERNAL_JOB_URL")
    api_token = os.environ.get("EXTERNAL_JOB_TOKEN")
    if not job_url or not api_token:
        print("Set EXTERNAL_JOB_URL and EXTERNAL_JOB_TOKEN environment variables.")
        exit(1)
    response = requests.post(job_url, headers={"Authorization": f"Bearer {api_token}"})
    print(f"Triggered external job: {response.status_code} {response.text}")