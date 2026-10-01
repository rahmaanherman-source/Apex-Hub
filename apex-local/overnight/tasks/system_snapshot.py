"""Safe local system snapshot."""
import os
import platform
import shutil
import subprocess
from .base import Task


class SystemSnapshot(Task):
    name = "system_snapshot"
    timeout_s = 60

    def _version(self, command):
        try:
            r = subprocess.run(command, capture_output=True, text=True, timeout=10)
            return (r.stdout or r.stderr).strip()[:120] if r.returncode == 0 else "unavailable"
        except OSError:
            return "unavailable"

    def run(self):
        total, used, free = shutil.disk_usage(os.path.expanduser("~"))
        return {
            "os": f"{platform.system()} {platform.release()}",
            "python": platform.python_version(),
            "cpu_cores": os.cpu_count(),
            "disk_total_gb": round(total / 1e9, 1),
            "disk_free_gb": round(free / 1e9, 1),
            "disk_used_pct": round(used / total * 100, 1),
            "node": self._version(["node", "--version"]),
            "npm": self._version(["npm", "--version"]),
            "git": self._version(["git", "--version"]),
            "docker": self._version(["docker", "--version"]),
        }
