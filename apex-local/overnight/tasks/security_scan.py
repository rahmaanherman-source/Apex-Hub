"""Deterministic local security checks; never print secret values."""
import re
import socket
import subprocess
from pathlib import Path
from .base import Task

ROOT = Path(__file__).resolve().parents[2]
SKIP = {".git", "node_modules", "venv", ".venv", "__pycache__", "logs"}
PATTERNS = [
    re.compile(r"sk_(?:live|test)_[A-Za-z0-9]{16,}"),
    re.compile(r"shpat_[A-Za-z0-9]{16,}"),
    re.compile(r"shpca_[A-Za-z0-9]{16,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{30,}"),
]


class SecurityScan(Task):
    name = "security_scan"
    timeout_s = 120

    def _powershell(self, command):
        try:
            r = subprocess.run(["powershell", "-NoProfile", "-Command", command], capture_output=True, text=True, timeout=15)
            return (r.stdout or "").strip()[:500]
        except OSError:
            return "unavailable"

    def run(self):
        secret_hits = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or any(part in SKIP for part in path.parts):
                continue
            if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".ico", ".exe", ".dll", ".zip"}:
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for pattern in PATTERNS:
                if pattern.search(text):
                    secret_hits.append(str(path.relative_to(ROOT)))
                    break
        local_ports = []
        for port in (7777, 7778, 11434):
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=0.3):
                    local_ports.append(port)
            except OSError:
                pass
        env_files = [str(p.relative_to(ROOT)) for p in ROOT.rglob(".env*") if p.is_file() and p.name != ".env.example"]
        return {
            "possible_secret_files": secret_hits,
            "dotenv_files_present": env_files,
            "local_services_reachable": local_ports,
            "firewall": self._powershell("Get-NetFirewallProfile | Select Name,Enabled | ConvertTo-Json -Compress"),
            "smbv1": self._powershell("(Get-SmbServerConfiguration).EnableSMB1Protocol"),
        }
