import requests
import time

def check_latency(url, runs=10):
    latencies = []
    for i in range(runs):
        start = time.time()
        try:
            requests.get(url, timeout=10)
        except Exception:
            pass
        elapsed = time.time() - start
        latencies.append(elapsed)
    avg = sum(latencies) / runs
    print(f"Average latency for {url}: {avg:.3f}s over {runs} runs")

if __name__ == "__main__":
    check_latency("http://localhost:8080/docs")
    check_latency("http://localhost:8050/")