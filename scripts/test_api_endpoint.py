import requests
import jwt
import os

def get_jwt():
    return jwt.encode({"user": "integration"}, os.getenv("SECRET", "YOUR_SECRET"), algorithm="HS256")

if __name__ == "__main__":
    url = "http://localhost:8080/predict"
    headers = {"Authorization": f"Bearer {get_jwt()}"}
    data = [{
        "structure_id": "XTEST001",
        "avg_daily_traffic": 12000,
        "bridge_condition": "Fair",
        "last_maintenance_date": "2024-07-01",
        "inspection_date": "2025-06-01",
        "latitude": 40.7,
        "longitude": -74.0,
        "precipitation": 2.4,
        "avg_temp": 17.5,
        "corrosion_level": 0.05,
        "previous_failures": 0,
        "soil_type": "sandy",
        "region_code": "NY"
    }]
    r = requests.post(url, json=data, headers=headers)
    assert r.status_code == 200, f"Status {r.status_code}: {r.text}"
    print("API response:", r.json())
    print("API endpoint test passed.")