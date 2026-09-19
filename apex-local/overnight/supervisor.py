"""Local-first APEX overnight supervisor.

The supervisor is intentionally deterministic: each task runs locally, failures are
recorded as failures, STOP halts the sequence, and post-repair verification is
mandatory before the report is generated.
"""
from pathlib import Path
from datetime import datetime, timezone
import uuid

from .evidence import EvidenceLog

ROOT = Path(__file__).resolve().parent.parent
STOP_FILE = ROOT / "logs" / "STOP"


def stop_requested() -> bool:
    return STOP_FILE.exists()


def _task(name: str, cls):
    return name, cls


SEQUENCE = [
    _task("01_system_snapshot", "overnight.tasks.system_snapshot.SystemSnapshot"),
    _task("02_local_ai_discovery", "overnight.tasks.local_ai_discovery.LocalAIDiscovery"),
    _task("03_antigravity_discovery", "overnight.tasks.antigravity.AntigravityDiscovery"),
    _task("04_mcp_audit", "overnight.tasks.mcp_audit.MCPAudit"),
    _task("05_connected_apps", "overnight.tasks.connected_apps.ConnectedApps"),
    _task("06_gatekeeper_audit", "overnight.tasks.gatekeeper_audit.GatekeeperAudit"),
    _task("07_security_scan", "overnight.tasks.security_scan.SecurityScan"),
    _task("08_safe_repair", "overnight.tasks.safe_repair.SafeRepair"),
    _task("09_reverify", "overnight.tasks.reverify.Reverify"),
    _task("10_revenue_readiness", "overnight.tasks.revenue_readiness.RevenueReadiness"),
    _task("11_phone_notify", "overnight.tasks.phone_notify.PhoneNotify"),
    _task("12_report", "overnight.tasks.report.Report"),
]


def _resolve(path: str):
    module_name, class_name = path.rsplit(".", 1)
    module = __import__(module_name, fromlist=[class_name])
    return getattr(module, class_name)


def run() -> dict:
    run_id = "overnight-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:6]
    log = EvidenceLog(run_id)
    results = []

    for name, path in SEQUENCE:
        if stop_requested():
            log.write("supervisor", "STOPPED", {"before": name, "reason": "STOP file present"})
            break
        cls = _resolve(path)
        task = cls(log)
        task.execute()
        results.append(name)

    return {"run_id": run_id, "completed_tasks": results, "stopped": stop_requested()}


if __name__ == "__main__":
    run()
