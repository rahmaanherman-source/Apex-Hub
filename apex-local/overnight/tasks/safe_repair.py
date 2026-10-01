"""Strictly non-destructive overnight repairs."""
import os
import shutil
from pathlib import Path
from .base import Task

ROOT = Path(__file__).resolve().parents[2]


class SafeRepair(Task):
    name = "safe_repair"
    timeout_s = 300

    def run(self):
        actions = []
        removed = 0
        for cache in ROOT.rglob("__pycache__"):
            if cache.is_dir() and ".git" not in cache.parts:
                try:
                    shutil.rmtree(cache)
                    removed += 1
                except OSError:
                    pass
        actions.append({"action": "remove_pycache", "count": removed})
        return {"actions": actions, "destructive_operations": False}
