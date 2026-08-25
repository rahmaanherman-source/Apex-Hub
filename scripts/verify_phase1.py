#!/usr/bin/env python3
"""APEX Phase 1 verifier.

Read-only checks for the local runtime. This tool reports evidence; it never
promotes a component to VERIFIED by itself.
"""

from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "canonical" / "PHASE1_GROUND_TRUTH_MANIFEST.json"
API_URL = os.getenv("APEX_API_URL", "http://localhost:8000/health")
FRONTEND_URL = os.getenv("APEX_FRONTEND_URL", "http://localhost:3000")


def result(name: str, ok: bool, evidence: str) -> dict:
    return {"check": name, "status": "PASS" if ok else "FAIL", "evidence": evidence}


def check_command(name: str, command: list[str]) -> dict:
    if not shutil.which(command[0]):
        return result(name, False, f"missing executable: {command[0]}")
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=30)
    evidence = (proc.stdout + proc.stderr).strip()[-2000:]
    return result(name, proc.returncode == 0, evidence or f"exit={proc.returncode}")


def check_url(name: str, url: str) -> dict:
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            body = response.read(2000).decode("utf-8", errors="replace")
            return result(name, 200 <= response.status < 300, f"HTTP {response.status}: {body}")
    except Exception as exc:  # network/service failures are evidence, not crashes
        return result(name, False, f"{type(exc).__name__}: {exc}")


def check_port(name: str, host: str, port: int) -> dict:
    sock = socket.socket()
    sock.settimeout(2)
    try:
        sock.connect((host, port))
        return result(name, True, f"TCP {host}:{port} reachable")
    except OSError as exc:
        return result(name, False, f"TCP {host}:{port} unavailable: {exc}")
    finally:
        sock.close()


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    checks = [
        check_command("docker_available", ["docker", "--version"]),
        check_command("compose_config_valid", ["docker", "compose", "config", "--quiet"]),
        check_url("api_health", API_URL),
        check_url("frontend_reachable", FRONTEND_URL),
        check_port("database_connectivity", "127.0.0.1", 5432),
        check_port("redis_connectivity", "127.0.0.1", 6379),
    ]

    failures = [c for c in checks if c["status"] != "PASS"]
    payload = {
        "phase": manifest["phase"],
        "manifest_status": manifest["status"],
        "runtime_status": "OBSERVED_PASS" if not failures else "RUNTIME_BLOCKED",
        "checks": checks,
        "no_fake_green": "RUNTIME_STATUS_REQUIRES_OBSERVED_EVIDENCE"
    }
    print(json.dumps(payload, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
