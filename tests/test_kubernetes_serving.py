import pytest
from src.deployment.kubernetes import deploy_model_kubernetes

def test_deploy_model_kubernetes(monkeypatch):
    calls = {}
    def fake_apply_yaml(yaml_path):
        calls['applied'] = yaml_path
        return True
    monkeypatch.setattr("src.deployment.kubernetes.apply_deployment_yaml", fake_apply_yaml)
    result = deploy_model_kubernetes("deploy.yaml")
    assert calls.get('applied') == "deploy.yaml"
    assert result is True