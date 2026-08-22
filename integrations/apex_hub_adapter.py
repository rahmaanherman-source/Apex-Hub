"""Real HTTP adapter for APEX Hub probes; no synthetic responses."""
from __future__ import annotations
import hashlib
import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

class ApexHubAdapter:
    def __init__(self, endpoint: str, timeout_sec: int = 5, evidence_root: Path = Path("EVIDENCE/RUNTIME_CAPTURES")):
        self.endpoint = endpoint.rstrip("/")
        self.timeout_sec = timeout_sec
        self.evidence_root = evidence_root

    def execute_live_probe(self, path: str = "/api/health") -> dict[str, Any]:
        target = f"{self.endpoint}{path}"
        request = urllib.request.Request(target, headers={"User-Agent": "APEX-TruthGate-Engine/4.2", "Accept": "application/json"})
        timestamp = datetime.now(timezone.utc).isoformat()
        input_fp = "sha256:" + hashlib.sha256(target.encode()).hexdigest()
        self.evidence_root.mkdir(parents=True, exist_ok=True)
        capture = self.evidence_root / f"hub_probe_{int(datetime.now(timezone.utc).timestamp() * 1000)}.json"
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_sec) as response:
                raw = response.read()
                status = response.getcode()
                output_fp = "sha256:" + hashlib.sha256(raw).hexdigest()
                try:
                    body = json.loads(raw.decode("utf-8")) if raw else {}
                except (UnicodeDecodeError, json.JSONDecodeError):
                    body = {"raw_body_sha256": output_fp}
                evidence = {"url": target, "status_code": status, "headers": dict(response.info()), "body": body, "timestamp": timestamp}
                capture.write_text(json.dumps(evidence, indent=2), encoding="utf-8")
                return {"operational_status": "CONNECTED" if 200 <= status < 400 else "FAILED", "status_code": status, "input_fingerprint": input_fp, "output_fingerprint": output_fp, "evidence_file": str(capture), "timestamp": timestamp}
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as exc:
            raw = f"{type(exc).__name__}: {exc}\n"
            capture.write_text(raw, encoding="utf-8")
            return {"operational_status": "FAILED", "error": str(exc), "input_fingerprint": input_fp, "output_fingerprint": "sha256:" + hashlib.sha256(raw.encode()).hexdigest(), "evidence_file": str(capture), "timestamp": timestamp}
