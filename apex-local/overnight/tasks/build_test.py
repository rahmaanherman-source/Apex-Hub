"""Deterministic local build/test checks."""
import json
import subprocess
from pathlib import Path
from .base import Task

ROOT = Path(__file__).resolve().parents[2]


def _run(command, cwd, timeout):
    try:
        r = subprocess.run(command, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return {"ok": r.returncode == 0, "code": r.returncode, "stdout_tail": (r.stdout or "")[-500:], "stderr_tail": (r.stderr or "")[-500:]}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "timeout"}
    except OSError as exc:
        return {"ok": False, "error": f"not available: {type(exc).__name__}"}


class BuildTest(Task):
    name = "build_test"
    timeout_s = 900

    def run(self):
        result = {"python_tests": _run(["python", "-m", "pytest", "-q"], ROOT, 600)}
        package = ROOT / "package.json"
        if package.exists():
            try:
                scripts = json.loads(package.read_text(encoding="utf-8")).get("scripts", {})
                if "typecheck" in scripts:
                    result["npm_typecheck"] = _run(["npm", "run", "typecheck"], ROOT, 300)
                if "test" in scripts:
                    result["npm_test"] = _run(["npm", "test", "--silent"], ROOT, 300)
                if "build" in scripts:
                    result["npm_build"] = _run(["npm", "run", "build"], ROOT, 300)
                if "lint" in scripts:
                    result["npm_lint"] = _run(["npm", "run", "lint"], ROOT, 300)
            except (OSError, ValueError) as exc:
                result["package_json"] = {"ok": False, "error": type(exc).__name__}
        return result
