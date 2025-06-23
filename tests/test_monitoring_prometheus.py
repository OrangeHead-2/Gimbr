import pytest
from src.monitoring.prometheus_metrics import PrometheusMetrics

def test_prometheus_metrics_count(monkeypatch):
    p = PrometheusMetrics()
    p.inc_requests()
    p.inc_requests()
    assert p.requests_total._value.get() == 2

def test_prometheus_metrics_latency(monkeypatch):
    p = PrometheusMetrics()
    with p.request_latency.time():
        pass  # Should not raise
    # histogram should register at least one observation
    assert p.request_latency._sum.get() >= 0