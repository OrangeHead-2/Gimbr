import pytest
from src.deployment.azureml import deploy_model_azureml

class DummyModel:
    def save(self, path): pass

def test_deploy_model_azureml(monkeypatch):
    calls = {}
    def fake_deploy(*args, **kwargs):
        calls['deployed'] = True
        return "azureml-endpoint"
    monkeypatch.setattr("src.deployment.azureml.deploy_azureml_service", fake_deploy)
    model = DummyModel()
    endpoint = deploy_model_azureml(model, "bridge-failure", compute_type="ACI")
    assert calls.get('deployed') is True
    assert endpoint == "azureml-endpoint"