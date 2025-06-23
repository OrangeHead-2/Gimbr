import pytest
from fastapi.testclient import TestClient
from src.serve.app import app

client = TestClient(app)

def test_predict_endpoint_ok(monkeypatch):
    dummy_resp = [{"structure_id": "X", "failure_probability": 0.5}]
    monkeypatch.setattr("src.serve.app.predict_batch", lambda x: dummy_resp)
    payload = [{"f1": 1, "f2": 2}]
    resp = client.post("/predict", json=payload, headers={"Authorization": "Bearer DEMO_TOKEN"})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert "failure_probability" in resp.json()[0]

def test_healthcheck():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"