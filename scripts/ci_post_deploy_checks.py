import requests
import time
import sys

def health_check(url, retries=10, delay=10):
    for i in range(retries):
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"Health check passed for {url}")
                return True
            print(f"Attempt {i+1}/{retries} failed: Status {r.status_code}")
        except Exception as e:
            print(f"Attempt {i+1}/{retries} failed: {e}")
        time.sleep(delay)
    return False

if __name__ == "__main__":
    api_url = "http://localhost:8080/docs"
    dashboard_url = "http://localhost:8050/"
    all_ok = True
    if not health_check(api_url):
        print("API health check failed.", file=sys.stderr)
        all_ok = False
    if not health_check(dashboard_url):
        print("Dashboard health check failed.", file=sys.stderr)
        all_ok = False
    if not all_ok:
        sys.exit(1)
    print("All post-deployment checks passed.")