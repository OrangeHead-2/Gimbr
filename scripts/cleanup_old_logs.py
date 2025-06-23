import os
import glob
import time

def prune_logs(log_dir="logs", pattern="*.log", keep_days=14):
    now = time.time()
    for log_file in glob.glob(os.path.join(log_dir, pattern)):
        mtime = os.path.getmtime(log_file)
        age_days = (now - mtime) / 86400
        if age_days > keep_days:
            print(f"Deleting old log file: {log_file} ({age_days:.1f} days old)")
            os.remove(log_file)

if __name__ == "__main__":
    prune_logs()