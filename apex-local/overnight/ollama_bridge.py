"""Bounded Ollama CLI bridge. Prompts never contain credentials."""
import subprocess
import time


def is_running() -> bool:
    try:
        return subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=5).returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def ensure_running() -> bool:
    if is_running():
        return True
    try:
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=0x00000008)
        time.sleep(3)
        return is_running()
    except OSError:
        return False


def list_models() -> list[str]:
    try:
        r = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=10)
        if r.returncode != 0:
            return []
        lines = [line for line in r.stdout.splitlines() if line.strip()]
        if not lines:
            return []
        return [line.split()[0] for line in lines[1:] if line.split()]
    except (OSError, subprocess.SubprocessError):
        return []


def health_check(model: str, timeout: int = 90) -> dict:
    started = time.monotonic()
    try:
        r = subprocess.run(["ollama", "run", model, "Reply with exactly: OK"], capture_output=True, text=True, timeout=timeout)
        elapsed = round(time.monotonic() - started, 2)
        return {"ok": r.returncode == 0, "latency_s": elapsed, "response_len": len((r.stdout or "").strip()), "error": "" if r.returncode == 0 else "model call failed"}
    except subprocess.TimeoutExpired:
        return {"ok": False, "latency_s": timeout, "response_len": 0, "error": "timeout"}
    except OSError as exc:
        return {"ok": False, "latency_s": round(time.monotonic() - started, 2), "response_len": 0, "error": f"runtime unavailable: {type(exc).__name__}"}
