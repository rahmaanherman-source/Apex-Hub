from __future__ import annotations
import subprocess
from ..sandbox import Sandbox


def run_shell(sandbox: Sandbox, cmd: str, timeout: int = 60) -> dict:
    import shlex
    try:
        argv = shlex.split(cmd, posix=True)
    except ValueError as e:
        return {"ok": False, "error": f"bad command: {e}"}
    if not argv: return {"ok": False, "error": "empty command"}
    try:
        proc = subprocess.run(argv, cwd=str(sandbox.root), capture_output=True, text=True, timeout=timeout)
        return {"ok": proc.returncode == 0, "code": proc.returncode, "stdout": proc.stdout[-20000:], "stderr": proc.stderr[-20000:]}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"timeout after {timeout}s"}
    except FileNotFoundError as e:
        return {"ok": False, "error": f"command not found: {e}"}
