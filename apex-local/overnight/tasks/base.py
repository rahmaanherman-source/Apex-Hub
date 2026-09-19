"""Task base class with bounded execution and evidence integration."""
import traceback
from datetime import datetime, timezone
from . import __name__ as _tasks_package
from ..redaction import safe_error, redact


class Task:
    name = "unnamed"
    timeout_s = 300

    def __init__(self, log):
        self.log = log

    def run(self) -> dict:
        raise NotImplementedError

    def execute(self) -> None:
        import threading
        box = {"value": None, "err": None, "trace": ""}
        done = threading.Event()

        def worker():
            try:
                box["value"] = self.run() or {}
            except Exception as exc:
                box["err"] = safe_error(exc)
                box["trace"] = redact(traceback.format_exc(limit=8))[-1200:]
            finally:
                done.set()

        started = datetime.now(timezone.utc).isoformat()
        threading.Thread(target=worker, daemon=True).start()
        if not done.wait(self.timeout_s):
            self.log.write(self.name, "FAIL", {"error": "timeout", "timeout_s": self.timeout_s, "started": started})
            return
        if box["err"]:
            self.log.write(self.name, "FAIL", {"error": box["err"], "trace": box["trace"], "started": started})
            return
        self.log.write(self.name, "OK", {"started": started, **box["value"]})
