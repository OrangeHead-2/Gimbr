import pytest
from src.registry.sync import RegistrySync

def test_registry_sync_push_and_pull(monkeypatch):
    # Dummy registry, just track calls
    calls = []
    class DummyRegistry:
        def push(self, model_path):
            calls.append(("push", model_path))
        def pull(self, model_name):
            calls.append(("pull", model_name))
            return "dummy_model_path"
    reg = DummyRegistry()
    sync = RegistrySync(registry=reg)
    sync.push("model.joblib")
    sync.pull("bridge_model")
    assert ("push", "model.joblib") in calls
    assert ("pull", "bridge_model") in calls