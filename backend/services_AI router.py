import os, httpx
from pydantic import BaseModel
from typing import Optional, List, Dict

BIFROST_URL = os.getenv("BIFROST_URL", "http://localhost:8002/v1/ai")

class AIRequest(BaseModel):
    capability: str
    messages: List[Dict[str, str]]
    model: Optional[str] = None
    stream: bool = False
    metadata: Optional[dict] = None

class AIRouter:
    def __init__(self):
        self.base_url = BIFROST_URL

    async def ask_by_capability(self, request: AIRequest) -> dict:
        async with httpx.AsyncClient(timeout=30.0) as client:
            payload = request.dict(exclude_none=True)
            resp = await client.post(f"{self.base_url}/completions", json=payload)
            resp.raise_for_status()
            return resp.json()

    async def health(self) -> bool:
        try:
            async with httpx.AsyncClient() as client:
                r = await client.get(f"{self.base_url}/../health")
                return r.status_code == 200
        except:
            return False

model_router = AIRouter()