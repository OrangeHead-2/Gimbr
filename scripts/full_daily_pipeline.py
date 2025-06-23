import subprocess

if __name__ == "__main__":
    steps = [
        ["python", "scripts/fetch_data_incremental.py"],
        ["python", "scripts/preprocess_data.py"],
        ["python", "scripts/feature_engineering.py"],
        ["python", "scripts/retrain_model.py"],
        ["python", "scripts/generate_dashboard_data.py"],
        ["python", "scripts/send_batch_alerts.py"],
        ["python", "scripts/prune_old_models.py"],
        ["python", "scripts/delete_old_data_files.py"],
        ["python", "scripts/cleanup_old_logs.py"],
        ["python", "scripts/backup_to_s3.py"]
    ]
    for step in steps:
        print(f"Running: {' '.join(step)}")
        subprocess.run(step, check=True)
    print("Full daily pipeline completed successfully.")