from __future__ import annotations
from .base import BaseProvider, GenerateRequest, GenerateResponse


class EchoProvider(BaseProvider):
    """Offline provider. Never calls the network."""
    name = "echo"

    def available(self) -> bool:
        return True

    def generate(self, req: GenerateRequest) -> GenerateResponse:
        last = req.messages[-1].content if req.messages else ""
        return GenerateResponse(text=f"[echo] {last}", provider=self.name, model="echo")
