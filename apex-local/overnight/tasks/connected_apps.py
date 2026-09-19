"""Offline connected-application inventory. No public network probes overnight."""
from pathlib import Path
import os
import yaml
from .base import Task

ROOT = Path(__file__).resolve().parents[2]


def inventory_connected_apps(root: Path | None = None) -> dict:
    root = Path(root or ROOT)
    result = {}
    models_path = root / "config" / "models.yaml"
    if models_path.exists():
        data = yaml.safe_load(models_path.read_text(encoding="utf-8")) or {}
        for provider, cfg in (data.get("cloud") or {}).items():
            result[provider] = {
                "configured": True,
                "mode": cfg.get("mode", "unknown"),
                "model": cfg.get("model", "unknown"),
                "credential_ref": cfg.get("key_env", ""),
                "status": "DAYTIME_CHECK_REQUIRED",
                "network_checked": False,
            }
    phone = root / "config" / "phone.yaml"
    if phone.exists():
        cfg = yaml.safe_load(phone.read_text(encoding="utf-8")) or {}
        notify = cfg.get("notify", {})
        if notify.get("backend"):
            result["phone_notify"] = {
                "configured": bool(notify.get("topic")),
                "mode": "notification-only",
                "status": "DAYTIME_CHECK_REQUIRED" if notify.get("backend") == "ntfy" else "UNVERIFIED",
                "network_checked": False,
            }
    return result


class ConnectedApps(Task):
    name = "connected_apps"
    timeout_s = 60

    def run(self):
        return {
            "apps": inventory_connected_apps(),
            "policy": "NO_PUBLIC_NETWORK_PROBES_OVERNIGHT",
            "note": "Authenticated/cloud health checks are deferred to daytime owner-authorized execution.",
        }
