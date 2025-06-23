import pytest
import gradio as gr
from src.serve.gradio_interface import build_interface

def test_build_interface_runs(monkeypatch):
    called = {}
    def fake_launch(*args, **kwargs):
        called['launched'] = True
    monkeypatch.setattr(gr.Interface, "launch", fake_launch)
    iface = build_interface()
    iface.launch()
    assert called.get('launched') is True