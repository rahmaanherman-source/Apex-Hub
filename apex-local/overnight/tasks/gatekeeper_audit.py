"""Metadata-only Gatekeeper audit. No credential values are requested."""
import json
import urllib.request
from .base import Task


class GatekeeperAudit(Task):
    name = "gatekeeper_audit"
    timeout_s = 60

    def _get(self, path):
        with urllib.request.urlopen(f"http://127.0.0.1:7777{path}", timeout=4) as response:
            return json.loads(response.read().decode("utf-8"))

    def run(self):
        result = {"broker_reachable": False, "credentials": [], "audit_entries": 0, "credential_values_requested": False}
        try:
            health = self._get("/health")
            result["broker_reachable"] = bool(health.get("ok"))
            registry = self._get("/registry")
            if isinstance(registry, list):
                result["credentials"] = [
                    {"provider": c.get("provider", ""), "fields": c.get("fields", []), "endpoint": c.get("endpoint", "")}
                    for c in registry
                ]
            audit = self._get("/audit")
            if isinstance(audit, list):
                result["audit_entries"] = len(audit)
        except Exception as exc:
            result["error"] = type(exc).__name__
        return result
