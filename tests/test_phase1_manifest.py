import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "canonical" / "PHASE1_GROUND_TRUTH_MANIFEST.json"


def test_phase1_manifest_defines_required_services_and_checks():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert data["phase"] == "PHASE_1_GROUND_TRUTH"
    assert data["status"] == "RUNTIME_VERIFICATION_REQUIRED"
    assert data["required_services"] == ["api", "frontend", "postgres", "redis"]
    assert "api_health" in data["verification_checks"]
    assert "database_connectivity" in data["verification_checks"]
    assert "redis_connectivity" in data["verification_checks"]
    assert "no_fake_green" in data["verification_checks"]
