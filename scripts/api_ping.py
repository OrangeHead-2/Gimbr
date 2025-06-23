import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080/"
    try:
        r = requests.get(url, timeout=10)
        print(f"Ping {url}: {r.status_code}")
    except Exception as e:
        print(f"Ping failed: {e}")