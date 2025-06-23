import requests
import jwt

def get_jwt():
    return jwt.encode({"user": "test"}, "YOUR_SECRET", algorithm="HS256")

def test_predict_endpoint():
    url = "http://localhost:8080/predict"
    headers = {"Authorization": f"Bearer {get_jwt()}"}
    data = [{
        "structure_id": "X123",
        "avg_daily_traffic": 15000,
        "bridge_condition": "Fair",
        "last_maintenance_date": "2023-01-01",
        "inspection_date": "2024-01-01",
        "latitude": 42.1,
        "longitude": -71.2,
        "precipitation": 3.2,
        "avg_temp": 16.0,
        "corrosion_level": 0.1,
        "previous_failures": 1,
        "soil_type": "clay",
        "region_code": "NE"
    }]
    r = requests.post(url, json=data, headers=headers)
    assert r.status_code == 200
    assert "failure_probability" in r.json()[0]