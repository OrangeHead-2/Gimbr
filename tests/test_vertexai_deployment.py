import pytest
from src.deployment.vertexai import deploy_model_vertexai

class DummyModel:
    def save(self, path): pass

def test_deploy_model_vertexai(monkeypatch):
    calls = {}
    def fake_deploy(*args, **kwargs):
        calls['deployed'] = True
        return "vertexai-endpoint"
    monkeypatch.setattr("src.deployment.vertexai.deploy_vertexai_model", fake_deploy)
    model = DummyModel()
    endpoint = deploy_model_vertexai(model, "vertex-bridge", machine_type="n1-standard-2")
    assert calls.get('deployed') is True
    assert endpoint == "vertexai-endpoint"