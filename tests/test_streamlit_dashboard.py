import pytest
import streamlit as st
from src.dashboard.streamlit_dashboard import make_dashboard

def test_make_dashboard_runs(monkeypatch):
    called = {}
    def fake_sidebar_selectbox(*args, **kwargs):
        called['sidebar'] = True
        return "Option1"
    monkeypatch.setattr(st.sidebar, "selectbox", fake_sidebar_selectbox)
    # Should not raise error
    make_dashboard()
    assert called.get('sidebar') is True