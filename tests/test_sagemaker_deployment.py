import pytest
from src.deployment.sagemaker import deploy_model_sagemaker

class DummyModel:
    def save(self, path): pass

def test_deploy_model_sagemaker(monkeypatch):
    calls = {}
    def fake_deploy(*args, **kwargs):
        calls['deployed'] = True
        return "endpoint-123"
    monkeypatch.setattr("src.deployment.sagemaker.deploy_sagemaker_endpoint", fake_deploy)
    model = DummyModel()
    endpoint = deploy_model_sagemaker(model, "test-model", instance_type="ml.t2.medium")
    assert calls.get('deployed') is True
    assert endpoint == "endpoint-123"