"""Evidence-only Antigravity discovery. Presence never implies capability."""
import os
import shutil
import subprocess
from pathlib import Path
from .base import Task

ROOT = Path(__file__).resolve().parents[2]


def _expand(path: str) -> Path:
    return Path(os.path.expandvars(path)).expanduser()


def classify_presence(paths: list[Path], binary: str, configs: list[Path]) -> dict:
    found = [str(p) for p in paths if p.exists()]
    return {
        "install_paths_found": found,
        "binary_found": binary or "",
        "config_files_found": [str(p) for p in configs if p.exists()],
        "version": "",
        "local_capable": False,
        "classification": "PRESENT — CAPABILITY UNVERIFIED" if (found or binary) else "NOT INSTALLED",
    }


class AntigravityDiscovery(Task):
    name = "antigravity_discovery"
    timeout_s = 90

    def run(self):
        import yaml
        config_path = ROOT / "config" / "phone.yaml"
        cfg = yaml.safe_load(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
        ag = cfg.get("antigravity", {}) or {}
        if not ag.get("enabled", False):
            return {"enabled": False, "classification": "DISABLED", "local_capable": False}

        paths = [_expand(p) for p in ag.get("possible_paths", [])]
        configs = [_expand(p) for p in ag.get("possible_configs", [])]
        binary = ""
        for name in ag.get("possible_binaries", []):
            binary = shutil.which(name) or ""
            if binary:
                break
        result = classify_presence(paths, binary, configs)
        if binary:
            try:
                probe = subprocess.run([binary, "--version"], capture_output=True, text=True, timeout=10)
                if probe.returncode == 0:
                    result["version"] = (probe.stdout or probe.stderr).strip()[:100]
            except Exception as exc:
                result["version_probe"] = "FAILED"
        if result["classification"] != "NOT INSTALLED":
            result["notes"] = ["Presence detected; inference capability remains unverified until a real supported capability check succeeds."]
        return result
