import pytest
import os
from src.data.dvc_integration import dvc_add, dvc_pull

def test_dvc_add(monkeypatch):
    called = {}
    def fake_run(cmd, *args, **kwargs):
        called["add"] = cmd
        return 0
    monkeypatch.setattr("os.system", fake_run)
    assert dvc_add("data/processed/features.csv") == 0
    assert "add" in called["add"]

def test_dvc_pull(monkeypatch):
    called = {}
    def fake_run(cmd, *args, **kwargs):
        called["pull"] = cmd
        return 0
    monkeypatch.setattr("os.system", fake_run)
    assert dvc_pull() == 0
    assert "pull" in called["pull"]