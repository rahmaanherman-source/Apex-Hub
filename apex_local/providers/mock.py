from __future__ import annotations
import re
from .base import BaseProvider, GenerateRequest, GenerateResponse


class MockProvider(BaseProvider):
    name = "mock"

    def available(self) -> bool:
        return True

    def generate(self, req: GenerateRequest) -> GenerateResponse:
        last = req.messages[-1].content.strip().lower() if req.messages else ""
        if last.startswith("read "):
            return self._tool("read_file", {"path": last[5:].strip()})
        if last.startswith("list"):
            return self._tool("list_dir", {"path": "."})
        if last.startswith("write "):
            m = re.match(r"write\s+(\S+)\s*::\s*(.*)", last, re.DOTALL)
            if m:
                return self._tool("write_file", {"path": m.group(1), "content": m.group(2)})
        if last.startswith("run "):
            return self._tool("run_shell", {"cmd": last[4:]})
        return GenerateResponse(text=f"[mock] {last}", provider=self.name, model="mock")

    def _tool(self, name: str, args: dict) -> GenerateResponse:
        return GenerateResponse(provider=self.name, model="mock", tool_calls=[{"name": name, "args": args, "id": f"call_{name}"}])
