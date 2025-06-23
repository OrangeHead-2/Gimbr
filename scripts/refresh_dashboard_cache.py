import requests

if __name__ == "__main__":
    dashboard_url = "http://localhost:8050/_dash-update-component"
    # If your dashboard has a cache-refresh endpoint, call it here.
    try:
        r = requests.post(dashboard_url, json={"refresh": True})
        if r.status_code == 200:
            print("Dashboard cache refresh triggered.")
        else:
            print(f"Dashboard cache refresh failed: {r.status_code}")
    except Exception as e:
        print(f"Error contacting dashboard: {e}")