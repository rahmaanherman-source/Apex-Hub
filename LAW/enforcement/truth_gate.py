#!/usr/bin/env python3
"""APEX Truth Gate: fail closed on unsupported VERIFIED claims."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "CAPABILITY-REGISTRY/registry.json"

class TruthGate:
    def __init__(self, registry_path: Path = REGISTRY):
        self.registry_path = registry_path
        self.registry = json.loads(registry_path.read_text(encoding="utf-8"))

    def capability(self, capability_id: str):
        return next((c for c in self.registry.get("capabilities", []) if c.get("id") == capability_id), None)

    def _sha256(self, path: Path) -> str:
        return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()

    def evidence_resolves(self, evidence: dict) -> bool:
        ref = str(evidence.get("ref", ""))
        path = ROOT / ref
        if not path.is_file() or path.stat().st_size == 0:
            return False
        expected = evidence.get("sha256")
        return not expected or expected == self._sha256(path)

    def veo_is_valid(self, evidence: dict, capability: dict) -> bool:
        if evidence.get("type") != "VEO" or not self.evidence_resolves(evidence):
            return False
        veo_path = ROOT / str(evidence["ref"])
        try:
            veo = json.loads(veo_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return False
        if veo.get("capability_id") != capability.get("id"):
            return False
        capture = ROOT / str(veo.get("evidence_file_path", ""))
        expected_capture = veo.get("evidence_file_sha256")
        return capture.is_file() and expected_capture == self._sha256(capture) and veo.get("governance_decision") in {"TESTED", "APPROVED", "VERIFIED"}

    def allow_verified(self, capability_id: str) -> bool:
        cap = self.capability(capability_id)
        if not cap or cap.get("apex_status") != "VERIFIED" or cap.get("test_status") != "VERIFIED":
            return False
        evidence = cap.get("evidence", [])
        return bool(evidence) and all(self.veo_is_valid(e, cap) for e in evidence)

    def enforce(self, capability_id: str) -> bool:
        if not self.allow_verified(capability_id):
            raise PermissionError(f"Truth Gate blocked {capability_id}: hash-validated VEO evidence is absent")
        return True
