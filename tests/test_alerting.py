import pytest
import requests
from src.alerting.slack import send_slack_alert

def test_send_slack_alert(monkeypatch):
    called = {}
    def fake_post(url, json):
        called['url'] = url
        called['json'] = json
        class Resp:
            status_code = 200
        return Resp()
    monkeypatch.setattr(requests, "post", fake_post)
    status = send_slack_alert("Test message", "http://webhook")
    assert status == 200
    assert called['url'] == "http://webhook"
    assert "Test message" in called['json']['text']