from __future__ import annotations
import json
import urllib.request
from .base import BaseProvider, GenerateRequest, GenerateResponse


class OllamaProvider(BaseProvider):
    name = "ollama"

    def __init__(self, endpoint: str = "http://localhost:11434", model: str = "qwen2.5-coder:7b"):
        self.endpoint = endpoint.rstrip("/")
        self.model = model

    def available(self) -> bool:
        try:
            req = urllib.request.Request(f"{self.endpoint}/api/tags", method="GET")
            with urllib.request.urlopen(req, timeout=2) as r:
                return r.status == 200
        except Exception:
            return False

    def generate(self, req: GenerateRequest) -> GenerateResponse:
        payload = {"model": self.model, "messages": [{"role": m.role, "content": m.content} for m in req.messages], "stream": False, "options": {"temperature": req.temperature, "num_predict": req.max_tokens}}
        data = json.dumps(payload).encode("utf-8")
        http_req = urllib.request.Request(f"{self.endpoint}/api/chat", data=data, headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(http_req, timeout=120) as r:
            body = json.loads(r.read().decode("utf-8"))
        return GenerateResponse(text=body.get("message", {}).get("content", ""), provider=self.name, model=self.model, raw=body)

    def health(self):
        return {"name": self.name, "ok": self.available(), "endpoint": self.endpoint, "model": self.model}
