#!/usr/bin/env python3
"""APEX fail-closed verification engine.

This engine never upgrades a capability to VERIFIED merely because a registry
entry exists. Verification requires an executable check that returns success
and a persisted evidence record bound to the tested capability/version.
"""
from __future__ import annotations
import hashlib, json, subprocess, sys, time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "CAPABILITY-REGISTRY" / "registry.json"
EVIDENCE = ROOT / "EVIDENCE"
EVIDENCE.mkdir(exist_ok=True)

STATUSES = {"UNKNOWN", "CONFIGURED", "CONNECTED", "TESTED", "APPROVED", "VERIFIED", "FAILED", "REJECTED", "DEPRECATED"}

@dataclass
class Evidence:
    verification_id: str
    capability_id: str
    capability_version: str
    test_name: str
    started_at: float
    finished_at: float
    success: bool
    details: dict[str, Any]
    artifact_sha256: str

    @property
    def ref(self) -> str:
        return f"EVIDENCE/{self.verification_id}.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_registry() -> dict[str, Any]:
    if not REGISTRY.exists():
        return {"version": "1.0", "capabilities": []}
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def save_evidence(e: Evidence) -> str:
    payload = asdict(e)
    payload["evidence_ref"] = e.ref
    # Hash the canonical payload without its own hash field.
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    digest = sha256_bytes(raw)
    payload["artifact_sha256"] = digest
    path = EVIDENCE / f"{e.verification_id}.json"
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return str(path.relative_to(ROOT))


def verify(capability: dict[str, Any], test: Callable[[], tuple[bool, dict[str, Any]]]) -> Evidence:
    cid = capability["id"]
    version = str(capability.get("version", "unknown"))
    started = time.time()
    success = False
    details: dict[str, Any]
    try:
        success, details = test()
    except Exception as exc:  # fail closed; exceptions are evidence of failed execution
        details = {"error_type": type(exc).__name__, "error": str(exc)}
    finished = time.time()
    verification_id = f"verification-{cid.lower()}-{int(finished)}"
    evidence = Evidence(verification_id, cid, version, "registered-check", started, finished, bool(success), details, "")
    save_evidence(evidence)
    return evidence


def registry_update(capability_id: str, evidence: Evidence) -> None:
    registry = load_registry()
    for cap in registry.get("capabilities", []):
        if cap.get("id") != capability_id:
            continue
        cap.setdefault("evidence", []).append({
            "type": "runtime_verification",
            "ref": evidence.ref,
            "date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(evidence.finished_at)),
            "success": evidence.success,
        })
        cap["test_status"] = "VERIFIED" if evidence.success else "FAILED"
        # Governance status is never silently promoted by the runtime.
        if cap.get("apex_status") == "VERIFIED" and not evidence.success:
            cap["apex_status"] = "CONDITIONAL"
        cap["last_verified"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(evidence.finished_at))
        break
    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")


def command_check(command: list[str], cwd: Path = ROOT, timeout: int = 120) -> tuple[bool, dict[str, Any]]:
    """Execute a declared verification command; never fabricate success."""
    started = time.time()
    proc = subprocess.run(command, cwd=cwd, capture_output=True, text=True, timeout=timeout, check=False)
    return proc.returncode == 0, {
        "command": command,
        "returncode": proc.returncode,
        "stdout": proc.stdout[-12000:],
        "stderr": proc.stderr[-12000:],
        "duration_seconds": round(time.time() - started, 3),
    }


def main() -> int:
    registry = load_registry()
    failures = 0
    for cap in registry.get("capabilities", []):
        # Only capabilities with an explicitly declared executable check are tested.
        check = cap.get("verification_check")
        if not check:
            continue
        evidence = verify(cap, lambda c=check: command_check(c))
        registry_update(cap["id"], evidence)
        print(f"{cap['id']}: {'VERIFIED' if evidence.success else 'FAILED'} -> {evidence.ref}")
        failures += int(not evidence.success)
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
