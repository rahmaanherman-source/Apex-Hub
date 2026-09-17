from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ChatMessage:
    role: str
    content: str
    name: str | None = None
    tool_call_id: str | None = None


@dataclass
class GenerateRequest:
    messages: list[ChatMessage]
    tools: list[dict[str, Any]] = field(default_factory=list)
    max_tokens: int = 2048
    temperature: float = 0.2


@dataclass
class GenerateResponse:
    text: str = ""
    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    provider: str = ""
    model: str = ""
    raw: Any = None


class BaseProvider(ABC):
    name: str = "base"

    @abstractmethod
    def available(self) -> bool: ...

    @abstractmethod
    def generate(self, req: GenerateRequest) -> GenerateResponse: ...

    def health(self) -> dict[str, Any]:
        return {"name": self.name, "ok": self.available()}
