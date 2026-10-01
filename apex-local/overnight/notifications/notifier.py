"""ntfy notification adapter. Never sends credential values."""
from pathlib import Path
from urllib.parse import urljoin
import requests
import yaml
from ..redaction import redact

ROOT = Path(__file__).resolve().parents[2]


def load_config() -> dict:
    path = ROOT / "config" / "phone.yaml"
    if not path.exists():
        return {"backend": "disabled"}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data.get("notify", {})


def _action_url(base: str, action: dict) -> str:
    if action.get("url"):
        return action["url"]
    return urljoin(base.rstrip("/") + "/", action.get("path", "" ).lstrip("/"))


def send(title: str, message: str, priority: str = "default", tags: list | None = None, actions: list | None = None) -> dict:
    cfg = load_config()
    if cfg.get("backend", "ntfy") != "ntfy":
        return {"ok": False, "status": "DISABLED"}
    topic = cfg.get("topic", "")
    server = cfg.get("server", "https://ntfy.sh").rstrip("/")
    if not topic or "CHANGE-ME" in topic:
        return {"ok": False, "status": "NOT_CONFIGURED"}

    safe_message = redact(message)
    headers = {"Title": redact(title), "Priority": priority, "Tags": ",".join(tags or ["robot"])}
    gateway = (cfg.get("gateway") or {}).get("public_url", "")
    if actions and gateway:
        parts = []
        for action in actions:
            parts.append(f"view, {action['label']}, {_action_url(gateway, action)}, clear=true")
        headers["Actions"] = "; ".join(parts)

    try:
        response = requests.post(f"{server}/{topic}", data=safe_message.encode("utf-8"), headers=headers, timeout=8)
        return {"ok": response.status_code == 200, "status": response.status_code}
    except requests.RequestException as exc:
        return {"ok": False, "status": "ERROR", "error": redact(str(exc))}
