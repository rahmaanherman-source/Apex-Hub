"""Deterministic Golden World baseline locking and drift detection."""
from __future__ import annotations
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CANONICAL_INCLUSIONS = [
    "LAW/APEX_LAW.md",
    "CAPABILITY-REGISTRY/registry.schema.json",
    "CAPABILITY-REGISTRY/veo.schema.json",
    "runtime/verification_engine.py",
    "runtime/golden_world.py",
    "skills_validate.py",
]

class GoldenWorldEngine:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir

    def calculate_manifest(self) -> dict[str, Any]:
        entries = []
        tree = hashlib.sha256()
        for rel_path in sorted(CANONICAL_INCLUSIONS):
            target = self.root_dir / rel_path
            if not target.is_file():
                raise FileNotFoundError(f"Canonical file missing: {rel_path}")
            file_sha = hashlib.sha256(target.read_bytes()).hexdigest()
            tree.update(f"{rel_path}:{file_sha}\n".encode())
            entries.append({"path": rel_path, "sha256": file_sha, "size_bytes": target.stat().st_size})
        return {"locked_timestamp": datetime.now(timezone.utc).isoformat(), "manifest_version": "1.0.0", "tree_digest": "sha256:" + tree.hexdigest(), "files": entries}

    def write_manifest(self, destination: Path) -> dict[str, Any]:
        manifest = self.calculate_manifest()
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        return manifest

    def verify_drift(self, locked_manifest_path: Path) -> dict[str, Any]:
        if not locked_manifest_path.is_file():
            return {"status": "FAILED", "reason": "No locked manifest found."}
        manifest = json.loads(locked_manifest_path.read_text(encoding="utf-8"))
        drift = []
        for entry in manifest.get("files", []):
            target = self.root_dir / entry["path"]
            if not target.is_file():
                drift.append({"path": entry["path"], "error": "MISSING"})
                continue
            current = hashlib.sha256(target.read_bytes()).hexdigest()
            if current != entry["sha256"]:
                drift.append({"path": entry["path"], "expected": entry["sha256"], "current": current})
        return {"status": "MATCH" if not drift else "DRIFT", "drift_count": len(drift), "drifted_files": drift, "checked_at": datetime.now(timezone.utc).isoformat()}
