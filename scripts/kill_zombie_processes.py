import psutil
import os

def kill_zombies():
    zombies = []
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            if proc.info['status'] == psutil.STATUS_ZOMBIE:
                zombies.append(proc.info['pid'])
        except Exception:
            continue
    for pid in zombies:
        try:
            os.kill(pid, 9)
            print(f"Killed zombie process: {pid}")
        except Exception as e:
            print(f"Failed to kill {pid}: {e}")

if __name__ == "__main__":
    kill_zombies()