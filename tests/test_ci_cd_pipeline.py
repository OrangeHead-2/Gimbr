import pytest
from src.ci_cd.github_actions import run_pipeline_step

def test_run_pipeline_step_success(monkeypatch):
    monkeypatch.setattr("subprocess.run", lambda *a, **kw: None)
    assert run_pipeline_step("echo 'hello'") is True

def test_run_pipeline_step_fail(monkeypatch):
    class DummyErr(Exception): pass
    def fail(*a, **kw): raise DummyErr()
    monkeypatch.setattr("subprocess.run", fail)
    assert run_pipeline_step("fail", raise_on_error=False) is False