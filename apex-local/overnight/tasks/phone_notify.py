"""Create owner decisions and send sanitized phone notifications."""
from .base import Task
from ..approvals import queue
from ..notifications import notifier


def _actions(req):
    base = (notifier.load_config().get("gateway") or {}).get("public_url", "").rstrip("/")
    if not base:
        return []
    cap = req["capability"]
    action = req["action"]
    return [
        {"label": "Approve", "url": f"{base}/decision/approve/{cap}?action={action}"},
        {"label": "Deny", "url": f"{base}/decision/deny/{cap}?action={action}"},
        {"label": "Defer", "url": f"{base}/decision/defer/{cap}?action={action}"},
    ]


class PhoneNotify(Task):
    name = "phone_notify"
    timeout_s = 120

    def run(self):
        entries = self.log.read_all()
        sent = []
        security = next((e for e in entries if e["task"] == "security_scan" and e["status"] == "OK"), None)
        if security:
            payload = security.get("payload", {})
            issues = payload.get("possible_secret_files", []) or payload.get("dotenv_files_present", [])
            if issues:
                req = queue.new_request("SECURITY_REVIEW", "HIGH", f"{len(issues)} security finding(s) require owner review", context={"count": len(issues)})
                result = notifier.send("APEX SECURITY", f"{len(issues)} finding(s). Values suppressed. Request: {req['request_id']}", priority="urgent", tags=["warning", "shield"], actions=_actions(req))
                sent.append({"type": "security", "request_id": req["request_id"], "notification": result})

        build = next((e for e in entries if e["task"] == "build_test" and e["status"] == "OK"), None)
        if build:
            failures = [k for k, v in build.get("payload", {}).items() if isinstance(v, dict) and v.get("ok") is False]
            if failures:
                req = queue.new_request("BUILD_FAILURE_REVIEW", "MEDIUM", f"Build/test failed: {', '.join(failures)}", context={"failures": failures})
                result = notifier.send("APEX BUILD", f"{len(failures)} failure(s). Request: {req['request_id']}", priority="default", tags=["warning"], actions=_actions(req))
                sent.append({"type": "build", "request_id": req["request_id"], "notification": result})

        if not sent:
            ok_count = sum(1 for e in entries if e.get("status") == "OK")
            result = notifier.send("APEX OVERNIGHT", f"{ok_count} checks completed. No human action required.", priority="min", tags=["white_check_mark"])
            sent.append({"type": "status", "silent": True, "notification": result})
        return {"notifications": sent}
