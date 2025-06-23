import time
import subprocess

def schedule_retrain(cron_expr: str, retrain_script: str):
    import schedule
    def retrain_job():
        subprocess.run(["python", retrain_script])
    schedule.every().day.at(cron_expr).do(retrain_job)
    while True:
        schedule.run_pending()
        time.sleep(60)