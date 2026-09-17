"""Small loopback HTTP gateway for one-time phone decisions.

Bind to loopback by default. A private network overlay such as Tailscale may
route to this service; an unauthenticated public tunnel is not supported.
"""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
import json
from pathlib import Path
from ..approvals import queue

ROOT = Path(__file__).resolve().parents[2]
STOP_FILE = ROOT / "logs" / "STOP"


def _respond(handler, code, payload, content_type="application/json"):
    body = payload if isinstance(payload, bytes) else (json.dumps(payload) if content_type == "application/json" else payload).encode()
    handler.send_response(code)
    handler.send_header("Content-Type", content_type)
    handler.send_header("Cache-Control", "no-store")
    handler.end_headers()
    handler.wfile.write(body)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        return

    def do_GET(self):
        parsed = urlparse(self.path)
        parts = [p for p in parsed.path.split("/") if p]
        if parts == ["health"]:
            return _respond(self, 200, {"ok": True})
        if len(parts) == 3 and parts[0] == "decision":
            _, action, capability = parts
            if action not in {"approve", "deny", "defer", "stop"}:
                return _respond(self, 404, {"error": "unknown action"})
            if action == "stop":
                ok = queue.approve_with_capability(capability, "EMERGENCY_STOP")
                if ok:
                    STOP_FILE.parent.mkdir(parents=True, exist_ok=True)
                    STOP_FILE.write_text("PHONE STOP\n", encoding="utf-8")
                return _respond(self, 200 if ok else 403, {"status": "STOP_REQUESTED" if ok else "REJECTED"})
            action_name = {"approve": None, "deny": None, "defer": None}[action]
            query = parse_qs(parsed.query)
            bound_action = (query.get("action") or [""])[0]
            if not bound_action:
                return _respond(self, 400, {"error": "missing action binding"})
            fn = {"approve": queue.approve_with_capability, "deny": queue.deny_with_capability, "defer": queue.defer_with_capability}[action]
            ok = fn(capability, bound_action)
            return _respond(self, 200 if ok else 403, {"status": action.upper() if ok else "REJECTED"})
        if len(parts) == 2 and parts[0] == "status":
            return _respond(self, 200, {"request_id": parts[1], "status": queue.get_status(parts[1])})
        return _respond(self, 404, {"error": "not found"})


def run(host="127.0.0.1", port=7778):
    ThreadingHTTPServer((host, port), Handler).serve_forever()
