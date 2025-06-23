import subprocess

if __name__ == "__main__":
    # Run through full pipeline for CI/CD smoke test, fail if any step fails
    steps = [
        ["python", "scripts/fetch_data.py"],
        ["python", "scripts/preprocess_data.py"],
        ["python", "scripts/feature_engineering.py"],
        ["python", "scripts/train_model.py"],
        ["python", "scripts/evaluate_model.py"],
        ["python", "scripts/generate_dashboard_data.py"]
    ]
    for step in steps:
        print(f"Running: {' '.join(step)}")
        subprocess.run(step, check=True)
    print("Smoke test pipeline completed with all steps successful.")