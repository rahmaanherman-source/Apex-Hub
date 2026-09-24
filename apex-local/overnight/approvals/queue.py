"""File-backed owner approval queue with one-time capabilities."""
import hashlib
import hmac
import json
import secrets
from datetime import datetime, timedelta, timezone
from pathlib import Path
from threading import Lock

ROOT = Path(__file__).resolve().parents[2]
CFG = {"default_expiry_minutes": 30, "auto_deny_on_expiry": True}
_LOCK = Lock()


def configure(root: Path | None = None, expiry_minutes: int = 30):
    global ROOT, CFG
    if root is not None:
        ROOT = Path(root)
    CFG = {"default_expiry_minutes": int(expiry_minutes), "auto_deny_on_expiry": True}
    for name in ("pending", "approved", "denied", "deferred"):
        (ROOT / "overnight" / "approvals" / name).mkdir(parents=True, exist_ok=True)


def _folder(name):
    p = ROOT / "overnight" / "approvals" / name
    p.mkdir(parents=True, exist_ok=True)
    return p


def _hash(capability: str) -> str:
    return hashlib.sha256(capability.encode("utf-8")).hexdigest()


def new_request(action: str, risk: str, reason: str, credential_ref: str = "", context: dict | None = None) -> dict:
    configure(ROOT, int(CFG.get("default_expiry_minutes", 30)))
    now = datetime.now(timezone.utc)
    rid = "OVN-" + now.strftime("%Y%m%d") + "-" + secrets.token_hex(4).upper()
    capability = secrets.token_urlsafe(32)
    req = {
        "request_id": rid,
        "action": action,
        "risk": risk,
        "reason": reason,
        "credential_ref": credential_ref,
        "created": now.isoformat(),
        "expires": (now + timedelta(minutes=CFG["default_expiry_minutes"])).isoformat(),
        "status": "PENDING",
        "capability_hash": _hash(capability),
        "context": context or {},
    }
    _folder("pending").joinpath(f"{rid}.json").write_text(json.dumps(req, indent=2), encoding="utf-8")
    return {**req, "capability": capability}


def _load(rid: str):
    for name in ("pending", "approved", "denied", "deferred"):
        path = _folder(name) / f"{rid}.json"
        if path.exists():
            return name, path, json.loads(path.read_text(encoding="utf-8"))
    return None, None, None


def _move_by_capability(capability: str, action: str, target: str, final_status: str) -> bool:
    if not capability or not action:
        return False
    with _LOCK:
        pending = _folder("pending")
        for path in pending.glob("OVN-*.json"):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            if data.get("action") != action or not hmac.compare_digest(data.get("capability_hash", ""), _hash(capability)):
                continue
            try:
                expires = datetime.fromisoformat(data["expires"])
            except Exception:
                return False
            if datetime.now(timezone.utc) >= expires:
                _move_path(path, "denied", "EXPIRED")
                return False
            data["status"] = final_status
            data["decided_at"] = datetime.now(timezone.utc).isoformat()
            _folder(target).joinpath(path.name).write_text(json.dumps(data, indent=2), encoding="utf-8")
            path.unlink()
            return True
    return False


def _move_path(path: Path, target: str, status: str):
    data = json.loads(path.read_text(encoding="utf-8"))
    data["status"] = status
    data["decided_at"] = datetime.now(timezone.utc).isoformat()
    _folder(target).joinpath(path.name).write_text(json.dumps(data, indent=2), encoding="utf-8")
    path.unlink()


def approve_with_capability(capability: str, action: str) -> bool:
    return _move_by_capability(capability, action, "approved", "APPROVED")


def deny_with_capability(capability: str, action: str) -> bool:
    return _move_by_capability(capability, action, "denied", "DENIED")


def defer_with_capability(capability: str, action: str) -> bool:
    return _move_by_capability(capability, action, "deferred", "DEFERRED")


def approve(rid: str) -> bool:
    return _move_id(rid, "approved", "APPROVED")


def deny(rid: str) -> bool:
    return _move_id(rid, "denied", "DENIED")


def defer(rid: str) -> bool:
    return _move_id(rid, "deferred", "DEFERRED")


def _move_id(rid, target, status):
    with _LOCK:
        name, path, _ = _load(rid)
        if name != "pending" or path is None:
            return False
        _move_path(path, target, status)
        return True


def get_status(rid: str) -> str:
    name, _, data = _load(rid)
    if not name:
        return "UNKNOWN"
    return data.get("status", name.upper())


def expire_stale() -> int:
    count = 0
    now = datetime.now(timezone.utc)
    for path in _folder("pending").glob("OVN-*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if now >= datetime.fromisoformat(data["expires"]):
                _move_path(path, "denied", "EXPIRED")
                count += 1
        except Exception:
            continue
    return count
