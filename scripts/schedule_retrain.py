import time
import subprocess

def retrain_once():
    subprocess.run(["python", "scripts/retrain_model.py"], check=True)

def main():
    # Run retraining daily at 2AM server time (simple sleep loop, replace with Airflow for prod)
    import datetime
    while True:
        now = datetime.datetime.now()
        next_run = (now + datetime.timedelta(days=1)).replace(hour=2, minute=0, second=0, microsecond=0)
        wait_seconds = (next_run - now).total_seconds()
        print(f"Next retrain scheduled at {next_run}. Sleeping for {wait_seconds // 3600}h {(wait_seconds % 3600) // 60}m")
        time.sleep(wait_seconds)
        retrain_once()

if __name__ == "__main__":
    main()