from __future__ import annotations
import json
import time
from pathlib import Path
from typing import Any


class Log:
    LEVELS = {"DEBUG": 10, "INFO": 20, "WARN": 30, "ERROR": 40}

    def __init__(self, path: Path, level: str = "INFO"):
        self.path = path
        self.level = self.LEVELS.get(level.upper(), 20)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _write(self, lvl: str, msg: str, **extra: Any) -> None:
        if self.LEVELS[lvl] < self.level:
            return
        entry = {"ts": time.time(), "level": lvl, "msg": msg, **extra}
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")

    def debug(self, msg: str, **e): self._write("DEBUG", msg, **e)
    def info(self, msg: str, **e):  self._write("INFO", msg, **e)
    def warn(self, msg: str, **e):  self._write("WARN", msg, **e)
    def error(self, msg: str, **e): self._write("ERROR", msg, **e)

    def tail(self, n: int = 50) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        lines = self.path.read_text(encoding="utf-8").strip().splitlines()
        return [json.loads(l) for l in lines[-n:]]
