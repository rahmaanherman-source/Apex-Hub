"""Real local process adapter with captured stdout/stderr evidence."""
from __future__ import annotations
import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

class EcosystemAdapter:
    def __init__(self, working_dir: Path, evidence_root: Path = Path("EVIDENCE/RUNTIME_CAPTURES")):
        self.working_dir = working_dir
        self.evidence_root = evidence_root

    def run_command(self, command: list[str], timeout: int = 15) -> dict[str, Any]:
        started = datetime.now(timezone.utc)
        raw_input = "\0".join(command)
        input_fp = "sha256:" + hashlib.sha256(raw_input.encode()).hexdigest()
        self.evidence_root.mkdir(parents=True, exist_ok=True)
        try:
            result = subprocess.run(command, cwd=self.working_dir, capture_output=True, text=True, timeout=timeout, check=False)
            raw = f"STDOUT\n{result.stdout}\nSTDERR\n{result.stderr}"
            status = "CONNECTED" if result.returncode == 0 else "FAILED"
            error = None
        except (OSError, subprocess.SubprocessError, TimeoutError) as exc:
            result = None
            raw = f"{type(exc).__name__}: {exc}\n"
            status = "FAILED"
            error = str(exc)
        capture = self.evidence_root / f"cli_exec_{int(datetime.now(timezone.utc).timestamp() * 1000)}.log"
        capture.write_text(raw, encoding="utf-8")
        output_fp = "sha256:" + hashlib.sha256(raw.encode()).hexdigest()
        response: dict[str, Any] = {"operational_status": status, "input_fingerprint": input_fp, "output_fingerprint": output_fp, "evidence_file": str(capture), "timestamp": started.isoformat()}
        if result is not None:
            response["exit_code"] = result.returncode
        if error:
            response["error"] = error
        return response
