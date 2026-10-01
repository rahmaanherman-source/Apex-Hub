import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def test_redaction_scrubs_nested_values_and_secret_patterns():
    from overnight.redaction import redact, contains_secret_like_value

    payload = {
        "api_key": "super-secret",
        "nested": {"message": "Authorization: Bearer abcdefghijklmnop"},
        "safe": "hello",
    }
    out = redact(payload)
    assert out["api_key"] == "[REDACTED]"
    assert out["nested"]["message"] == "[REDACTED]"
    assert out["safe"] == "hello"
    assert contains_secret_like_value("sk_live_abcdefghijklmnopqrstuv")


def test_approval_is_single_use_action_bound_and_expiring(tmp_path, monkeypatch):
    from overnight.approvals import queue

    monkeypatch.setattr(queue, "ROOT", tmp_path)
    queue.configure(tmp_path, expiry_minutes=30)
    req = queue.new_request("DEPLOY", "MEDIUM", "owner approval")
    assert req["status"] == "PENDING"
    assert req["capability"]
    raw_cap = req["capability"]
    stored = json.loads((tmp_path / "overnight" / "approvals" / "pending" / f"{req['request_id']}.json").read_text())
    assert "capability" not in stored
    assert queue.approve_with_capability(raw_cap, "WRONG") is False
    assert queue.approve_with_capability(raw_cap, "DEPLOY") is True
    assert queue.approve_with_capability(raw_cap, "DEPLOY") is False

    req2 = queue.new_request("DEPLOY", "MEDIUM", "owner approval")
    path = tmp_path / "overnight" / "approvals" / "pending" / f"{req2['request_id']}.json"
    data = json.loads(path.read_text())
    data["expires"] = (datetime.now(timezone.utc) - timedelta(minutes=1)).isoformat()
    path.write_text(json.dumps(data))
    assert queue.expire_stale() == 1
    assert queue.get_status(req2["request_id"]) == "EXPIRED"


def test_notifier_builds_sanitized_actions(monkeypatch):
    from overnight.notifications import notifier

    captured = {}

    def fake_post(url, data, headers, timeout):
        captured.update(url=url, data=data.decode(), headers=headers, timeout=timeout)
        class R:
            status_code = 200
        return R()

    monkeypatch.setattr(notifier.requests, "post", fake_post)
    monkeypatch.setattr(notifier, "load_config", lambda: {
        "backend": "ntfy", "topic": "private-topic", "server": "https://ntfy.sh",
        "gateway": {"public_url": "https://phone.example/approve"}
    })
    notifier.send("APEX", "credential_ref=STRIPE_PROD", actions=[{"label": "Approve", "url": "https://phone.example/approve/x"}])
    assert "secret" not in captured["data"].lower()
    assert captured["headers"]["Actions"].startswith("view, Approve")


def test_antigravity_presence_is_not_capability_verification(tmp_path, monkeypatch):
    from overnight.tasks.antigravity import classify_presence

    binary = tmp_path / "antigravity.exe"
    binary.write_text("stub")
    result = classify_presence([tmp_path], str(binary), [])
    assert result["classification"] == "PRESENT — CAPABILITY UNVERIFIED"
    assert result["local_capable"] is False


def test_local_only_policy_rejects_public_urls():
    from overnight.network_policy import assert_local_target

    assert_local_target("http://127.0.0.1:7777/health") is None
    assert_local_target("http://localhost:11434/api/tags") is None
    try:
        assert_local_target("https://example.com")
    except ValueError:
        pass
    else:
        raise AssertionError("public target must be rejected")


def test_ollama_discovery_checks_every_model(monkeypatch):
    from overnight.tasks.local_ai_discovery import discover_model_health

    models = [f"model-{i}" for i in range(7)]
    checked = []
    monkeypatch.setattr("overnight.tasks.local_ai_discovery.ob.list_models", lambda: models)
    monkeypatch.setattr("overnight.tasks.local_ai_discovery.ob.is_running", lambda: True)
    monkeypatch.setattr("overnight.tasks.local_ai_discovery.ob.health_check", lambda m, timeout=90: checked.append(m) or {"ok": True})
    result = discover_model_health()
    assert checked == models
    assert result["verified"] == models


def test_supervisor_sequence_has_reverify_after_repair():
    from overnight import supervisor
    names = [name for name, _ in supervisor.SEQUENCE]
    assert names.index("08_safe_repair") < names.index("09_reverify") < names.index("10_revenue_readiness") < names.index("12_report")


def test_stop_requested_uses_stop_file(tmp_path, monkeypatch):
    from overnight import supervisor
    stop = tmp_path / "STOP"
    monkeypatch.setattr(supervisor, "STOP_FILE", stop)
    assert supervisor.stop_requested() is False
    stop.write_text("STOP")
    assert supervisor.stop_requested() is True


def test_report_does_not_hardcode_checkout_verification():
    from overnight.tasks import report
    source = Path(report.__file__).read_text(encoding="utf-8")
    assert "live $1 test order" not in source
    assert "VERIFY SHOPIFY → STRIPE CHECKOUT" not in source
