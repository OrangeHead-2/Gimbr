import pytest
from starlette.testclient import TestClient
from src.serve.ray_app import app

client = TestClient(app)

def test_ray_predict_endpoint(monkeypatch):
    dummy_response = [0.23, 0.52]
    monkeypatch.setattr("src.serve.ray_app.model_predict", lambda x: dummy_response)
    payload = [{"f1": 1, "f2": 3}, {"f1": 2, "f2": 4}]
    resp = client.post("/predict", json=payload)
    assert resp.status_code == 200
    assert resp.json() == dummy_response

def test_ray_healthcheck():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"