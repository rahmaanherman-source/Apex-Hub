#!/usr/bin/env python3
"""Execution-grade APEX verification engine.

Real execution produces a runtime capture and a Verification Evidence Object
(VEO). Runtime can prove TESTED; it cannot grant governance approval.
"""
from __future__ import annotations
import hashlib, json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "CAPABILITY-REGISTRY" / "registry.json"
CAPTURE_DIR = ROOT / "EVIDENCE" / "RUNTIME_CAPTURES"
VEO_DIR = ROOT / "EVIDENCE" / "VEO"
CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
VEO_DIR.mkdir(parents=True, exist_ok=True)


def digest_bytes(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def digest_text(value: str) -> str:
    return digest_bytes(value.encode("utf-8"))


def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run_command(command: list[str], timeout: int = 120) -> tuple[str, str, int]:
    try:
        proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=timeout, check=False)
        return proc.stdout, proc.stderr, proc.returncode
    except Exception as exc:
        return "", f"{type(exc).__name__}: {exc}\n", 1


def emit_veo(cap: dict[str, Any], command: list[str]) -> dict[str, Any]:
    timestamp = iso_now()
    stdout, stderr, returncode = run_command(command)
    raw = f"STDOUT\n{stdout}\nSTDERR\n{stderr}"
    verification_id = (
        f"VEO-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}-"
        f"{hashlib.sha256((cap['id'] + timestamp + raw).encode()).hexdigest()[:8].upper()}"
    )
    capture = CAPTURE_DIR / f"{verification_id}.log"
    capture.write_text(raw, encoding="utf-8")
    operational = "CONNECTED" if returncode == 0 else "FAILED"
    governance = "TESTED" if returncode == 0 else "REJECTED"
    veo = {
        "verification_id": verification_id,
        "capability_id": cap["id"],
        "capability_version": str(cap.get("version", "unknown")),
        "timestamp": timestamp,
        "executor_id": "APEX_RUNTIME_ENGINE_V4",
        "environment": "local_sandbox",
        "operational_status": operational,
        "test_definition": {
            "probe_type": "CLI_EXEC",
            "target_uri": cap.get("source", "local"),
            "expected_condition": "EXIT_0",
            "command": command,
        },
        "raw_input_fingerprint": digest_text(json.dumps(command, separators=(",", ":"))),
        "raw_output_fingerprint": digest_text(raw),
        "evidence_file_path": str(capture.relative_to(ROOT)),
        "evidence_file_sha256": digest_bytes(capture.read_bytes()),
        "governance_decision": governance,
        "exit_code": returncode,
    }
    veo_path = VEO_DIR / f"{verification_id}.json"
    veo_path.write_text(json.dumps(veo, indent=2) + "\n", encoding="utf-8")
    veo["veo_path"] = str(veo_path.relative_to(ROOT))
    return veo


def main() -> int:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    failures = 0
    for cap in registry.get("capabilities", []):
        command = cap.get("verification_check")
        if not command:
            continue
        veo = emit_veo(cap, command)
        cap.setdefault("evidence", []).append({
            "type": "VEO",
            "ref": veo["veo_path"],
            "date": veo["timestamp"],
            "sha256": digest_bytes((ROOT / veo["veo_path"]).read_bytes()),
        })
        cap["operational_status"] = veo["operational_status"]
        cap["test_status"] = "TESTED" if veo["operational_status"] == "CONNECTED" else "FAILED"
        failures += int(veo["operational_status"] == "FAILED")
        print(f"{cap['id']}: {veo['operational_status']} | {veo['veo_path']}")
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
