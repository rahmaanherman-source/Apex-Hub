#!/usr/bin/env python3
"""APEX Truth Gate: fail closed on unsupported VERIFIED claims."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
REGISTRY=ROOT/"CAPABILITY-REGISTRY/registry.json"

class TruthGate:
    def __init__(self, registry_path: Path=REGISTRY):
        self.registry_path=registry_path
        self.registry=json.loads(registry_path.read_text(encoding="utf-8"))

    def capability(self, capability_id: str):
        return next((c for c in self.registry.get("capabilities",[]) if c.get("id")==capability_id), None)

    def evidence_resolves(self, ref: str) -> bool:
        p=ROOT/ref
        return p.is_file() and p.stat().st_size > 0

    def allow_verified(self, capability_id: str) -> bool:
        cap=self.capability(capability_id)
        if not cap or cap.get("apex_status") != "VERIFIED" or cap.get("test_status") != "VERIFIED":
            return False
        evidence=cap.get("evidence",[])
        return bool(evidence) and all(self.evidence_resolves(str(e.get("ref",""))) for e in evidence)

    def enforce(self, capability_id: str):
        allowed=self.allow_verified(capability_id)
        if not allowed:
            raise PermissionError(f"Truth Gate blocked {capability_id}: reproducible VERIFIED evidence is absent")
        return True
